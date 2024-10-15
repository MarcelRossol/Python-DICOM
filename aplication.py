import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from tkinter import filedialog, Toplevel, IntVar
from tkinter.messagebox import showinfo
from glob import glob
import os
import numpy as np
import pydicom
from scipy.ndimage import median_filter  # Add this import
import app_functions

# Initialize the App
app = ttk.Window()
app.geometry("800x850")  # width and height of the window
app.style.theme_use('darkly')
app.title('DICOM Viewer')
width_height_viewer = 400

img = Image.open('utils/default_pic.png')
img = img.resize((width_height_viewer, width_height_viewer))
img_tk = ImageTk.PhotoImage(img)

app_title = ttk.Label(app, text='DICOM Viewer', font='poppins 30 bold')
app_title.pack()

# Functions
global dicom_files
global max_v
global min_v
global actual_slice_number
global on_off_click
global apply_filter
dicom_files = None
max_v = None
min_v = None
actual_slice_number = None
on_off_click = True
apply_filter = False


def open_dicoms():
    global dicom_files
    path_dicoms = filedialog.askdirectory()
    dicom_files = sorted(glob(os.path.join(path_dicoms, '*.dcm')))
    if dicom_files:
        visualize()
    else:
        notification_label.configure(text='Folder does not contain DICOM files')


def show(img):
    global tk_image
    normalized_slice = Image.fromarray(img)
    normalized_slice = normalized_slice.resize((width_height_viewer, width_height_viewer))
    tk_image = ImageTk.PhotoImage(normalized_slice)
    canvas_viewer.create_image(0, 0, anchor=NW, image=tk_image)


def prepare_dicoms(dcm_file, show=False, max_v=None, min_v=None, filter=False):
    dicom_file_data = pydicom.dcmread(dcm_file).pixel_array

    if max_v:
        HOUNSFIELD_MAX = int(float(max_v))
    else:
        HOUNSFIELD_MAX = np.max(dicom_file_data)
    if min_v:
        HOUNSFIELD_MIN = int(float(min_v))
    else:
        HOUNSFIELD_MIN = np.min(dicom_file_data)

    HOUNSFIELD_RANGE = HOUNSFIELD_MAX - HOUNSFIELD_MIN

    dicom_file_data[dicom_file_data < HOUNSFIELD_MIN] = HOUNSFIELD_MIN
    dicom_file_data[dicom_file_data > HOUNSFIELD_MAX] = HOUNSFIELD_MAX
    normalized_image = (dicom_file_data - HOUNSFIELD_MIN) / HOUNSFIELD_RANGE
    uint8_image = np.uint8(normalized_image * 255)

    if filter:
        uint8_image = median_filter(uint8_image, size=3)  # Apply median filter with a kernel size of 3

    return uint8_image


def return_min_max(dcm_file):
    array = pydicom.dcmread(dcm_file).pixel_array
    return np.min(array), np.max(array)


def visualize(slice_number=0):
    if dicom_files:
        global actual_slice_number, min_v, max_v, apply_filter
        actual_slice_number = slice_number
        slice_path = dicom_files[int(float(slice_number))]
        dcm_min_value, dcm_max_value = return_min_max(slice_path)
        slider_slices.configure(state='enabled', from_=0, to=len(dicom_files) - 1, value=actual_slice_number)
        slider_max.configure(state='enabled', value=dcm_max_value)
        slider_min.configure(state='enabled', value=dcm_min_value)
        apply_button.configure(state='enabled')
        change_button.configure(state='disabled')
        slider_slices_value.configure(text=int(float(actual_slice_number)))
        slider_max_value.configure(text=int(float(slider_max.get())))
        slider_min_value.configure(text=int(float(slider_min.get())))

        normalized_slice = prepare_dicoms(slice_path, filter=apply_filter)
        show(normalized_slice)
        max_v = dcm_max_value
        min_v = dcm_min_value

        notification_label.configure(text='DICOM files succesfuly loaded', bootstyle='info')


def scroll_slider(slice_number=0):
    if dicom_files:
        global max_v, min_v, on_off_click, actual_slice_number, apply_filter

        slice_path = dicom_files[int(float(slice_number))]
        dcm_min_value, dcm_max_value = return_min_max(slice_path)
        slider_slices.configure(state='enabled', from_=0, to=len(dicom_files) - 1)
        slider_slices_value.configure(text=int(float(slice_number)))

        if on_off_click:
            slider_max.configure(value=dcm_max_value)
            slider_min.configure(value=dcm_min_value)
            normalized_slice = prepare_dicoms(slice_path, max_v=dcm_max_value, min_v=dcm_min_value, filter=apply_filter)
        else:
            normalized_slice = prepare_dicoms(slice_path, max_v=max_v, min_v=min_v, filter=apply_filter)

        actual_slice_number = slice_number
        show(normalized_slice)


def change_max(value):
    if dicom_files:
        global max_v, min_v, actual_slice_number, apply_filter
        max_v = value
        slider_max_value.configure(text=int(float(value)))
        slice_path = dicom_files[int(float(actual_slice_number))]
        normalized_slice = prepare_dicoms(slice_path, max_v=int(float(max_v)), min_v=int(float(min_v)), filter=apply_filter)
        show(normalized_slice)


def change_min(value):
    if dicom_files:
        global min_v, max_v, actual_slice_number, apply_filter
        min_v = value
        slider_min_value.configure(text=int(float(value)))
        slice_path = dicom_files[int(float(actual_slice_number))]
        normalized_slice = prepare_dicoms(slice_path, min_v=int(float(min_v)), max_v=int(float(max_v)), filter=apply_filter)
        show(normalized_slice)


def filter():
    global apply_filter, actual_slice_number
    apply_filter = not apply_filter  # Toggle filter state

    # Update the button's color and text
    if apply_filter:
        filter_button.configure(bootstyle='success', text='Filter: ON')
    else:
        filter_button.configure(bootstyle='danger', text='Filter: OFF')

    slice_path = dicom_files[int(float(actual_slice_number))]
    normalized_slice = prepare_dicoms(slice_path, max_v=int(float(max_v)), min_v=int(float(min_v)), filter=apply_filter)
    show(normalized_slice)


def apply():
    global min_v, max_v, on_off_click
    on_off_click = False
    slider_max.configure(state='disabled')
    slider_min.configure(state='disabled')
    apply_button.configure(state='disabled')
    change_button.configure(state='enabled')


def change():
    if dicom_files:
        global min_v, max_v, actual_slice_number, on_off_buttons
        on_off_click = True

        slider_max.configure(state='enabled', value=int(float(slider_max.get())))
        slider_min.configure(state='enabled', value=int(float(slider_min.get())))
        apply_button.configure(state='enabled')
        change_button.configure(state='disabled')


def show_info():
    if dicom_files:
        patient = pydicom.dcmread(dicom_files[0])
        infos_1, infos_2 = app_functions.return_information(patient)

        info_window = ttk.Toplevel(app)
        info_window.title('File Information')
        info_window.geometry('1000x600')

        info_title = ttk.Label(info_window, text='File Information', font='poppins 25 bold')
        info_title.pack()
        info_label_frame = ttk.Frame(info_window)
        info_label_frame.pack()
        info_label_1 = ttk.Label(info_label_frame, text=infos_1)
        info_label_1.grid(row=0, column=0, padx=(0, 30))
        info_label_2 = ttk.Label(info_label_frame, text=infos_2)
        info_label_2.grid(row=0, column=1)


def save_png():
    if dicom_files:
        path_to_save = filedialog.askdirectory()

        if path_to_save:
            for dicom_file in dicom_files:
                image_name = os.path.basename(dicom_file)[:-4]
                array = prepare_dicoms(dicom_file, max_v=max_v, min_v=min_v, filter=apply_filter)
                image = Image.fromarray(array)
                image.save(f'{path_to_save}/{image_name}.png')

            showinfo(message='The saving completed!')


def anonymize():
    if dicom_files:
        path_to_anonymize = filedialog.askdirectory()

        if path_to_anonymize:
            for dicom_file in dicom_files:
                image_name = os.path.basename(dicom_file)[:-4]
                anonymized_file = app_functions.anonymize_case(dicom_file)
                anonymized_file.save_as(f'{path_to_anonymize}/{image_name}.dcm')

            showinfo(message='The anonymizing completed!')


def open_segmentation_window():
    global threshold_min, threshold_max, seg_window
    seg_window = Toplevel(app)
    seg_window.title('Segmentation Window')
    seg_window.geometry('600x400')

    seg_label = ttk.Label(seg_window, text="Segmentation Tool", font='poppins 15 bold')
    seg_label.pack(pady=30)

    slider_threshold_min_label = ttk.Label(seg_window, text='Min Threshold', font='poppins 10')
    slider_threshold_min_label.pack(pady=(30, 0))
    threshold_min = ttk.Scale(seg_window, from_=-3000, to=3000, length=300, command=update_segmentation_preview)
    threshold_min.pack()

    slider_threshold_max_label = ttk.Label(seg_window, text='Max Threshold', font='poppins 10')
    slider_threshold_max_label.pack(pady=(30, 0))
    threshold_max = ttk.Scale(seg_window, from_=-3000, to=3000, length=300, command=update_segmentation_preview)
    threshold_max.pack()

    apply_segmentation_button = ttk.Button(seg_window, text="Apply Segmentation", bootstyle='success', command=apply_segmentation)
    apply_segmentation_button.pack(pady=30)


def update_segmentation_preview(event=None):
    if dicom_files:
        global actual_slice_number
        slice_path = dicom_files[int(float(actual_slice_number))]
        min_thresh = int(float(threshold_min.get()))
        max_thresh = int(float(threshold_max.get()))

        segmented_image = segment_slice(slice_path, min_thresh, max_thresh)
        show(segmented_image)


def apply_segmentation():
    if dicom_files:
        global actual_slice_number
        slice_path = dicom_files[int(float(actual_slice_number))]
        min_thresh = int(float(threshold_min.get()))
        max_thresh = int(float(threshold_max.get()))

        segmented_image = segment_slice(slice_path, min_thresh, max_thresh)
        show(segmented_image)


def segment_slice(dcm_file, min_thresh, max_thresh):
    dicom_file_data = pydicom.dcmread(dcm_file).pixel_array
    segmented_image = np.where((dicom_file_data >= min_thresh) & (dicom_file_data <= max_thresh), dicom_file_data, 0)
    normalized_image = (segmented_image - min_thresh) / (max_thresh - min_thresh)
    uint8_image = np.uint8(normalized_image * 255)
    return uint8_image


# User Notifications
notification_label = ttk.Label(app, text='You need to open DICOM files', font='poppins 15 bold', bootstyle='info')
notification_label.pack()

# Frame Containers #
frame_buttons = ttk.Frame(app)
frame_buttons.pack()

frame_viewer = ttk.Frame(app)
frame_viewer.pack()  # Using pack instead of grid

canvas_viewer = ttk.Canvas(frame_viewer, width=width_height_viewer, height=width_height_viewer, bg="#FFFFFF")
canvas_viewer.pack()

canvas_viewer.create_image(0, 0, anchor=NW, image=img_tk)

# Buttons #
open_button = ttk.Button(frame_buttons, text='Open', bootstyle='light', width=17, command=open_dicoms)
open_button.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))

show_info_button = ttk.Button(frame_buttons, text='Show info', bootstyle='light', width=17, command=show_info)
show_info_button.grid(row=0, column=1, pady=(20, 20))

filter_button = ttk.Button(frame_buttons, text='Filter: OFF', bootstyle='danger', width=17, command=filter)
filter_button.grid(row=0, column=2, padx=(20, 20), pady=(20, 20))

anonymize_button = ttk.Button(frame_buttons, text='Anonymize', bootstyle='light', width=17, command=anonymize)
anonymize_button.grid(row=1, column=0, padx=(20, 20), pady=(0, 20))

save_png_button = ttk.Button(frame_buttons, text='Save PNG', bootstyle='light', width=17, command=save_png)
save_png_button.grid(row=1, column=1, padx=(20, 20), pady=(0, 20))

segmentation_button = ttk.Button(frame_buttons, text='Segmentation', bootstyle='light', width=17, command=open_segmentation_window)
segmentation_button.grid(row=1, column=2, padx=(20, 20), pady=(0, 20))

# Sliders #
contrast_field = ttk.Frame(app)
contrast_field.pack()

slider_slices_label = ttk.Label(contrast_field, text='Slice', font='poppins 10')
slider_slices_label.grid(pady=(30, 0), padx=(0, 20), row=0, column=0)

slider_slices = ttk.Scale(contrast_field, from_=0, to=1000, length=400, command=scroll_slider, state="disabled")
slider_slices.grid(pady=(30, 0), padx=(0, 20), row=0, column=1)

slider_slices_value = ttk.Label(contrast_field, text=int(float(slider_slices.get())))
slider_slices_value.grid(pady=(30, 0), row=0, column=2)

slider_max_label = ttk.Label(contrast_field, text='Max', font='poppins 10')
slider_max_label.grid(pady=(30, 0), padx=(0, 20), row=1, column=0)

slider_max = ttk.Scale(contrast_field, from_=-3000, to=3000, length=400, command=change_max, state="disabled")
slider_max.grid(pady=(30, 0), padx=(0, 20), row=1, column=1)

slider_max_value = ttk.Label(contrast_field, text=int(float(slider_max.get())))
slider_max_value.grid(pady=(30, 0), row=1, column=2)

slider_min_label = ttk.Label(contrast_field, text='Min', font='poppins 10')
slider_min_label.grid(pady=(30, 0), padx=(0, 20), row=2, column=0)

slider_min = ttk.Scale(contrast_field, from_=-3000, to=3000, length=400, command=change_min, state="disabled")
slider_min.grid(pady=(30, 0), padx=(0, 20), row=2, column=1)

slider_min_value = ttk.Label(contrast_field, text=int(float(slider_min.get())))
slider_min_value.grid(pady=(30, 0), row=2, column=2)

on_off_buttons = ttk.Frame(app)
on_off_buttons.pack()

apply_button = ttk.Button(on_off_buttons, text="Apply", bootstyle='success, outline', width=20, command=apply, state='disabled')
apply_button.grid(pady=(20, 0), padx=(0, 10), row=0, column=0)

change_button = ttk.Button(on_off_buttons, text="Change", bootstyle='warning, outline', width=20, command=change, state='disabled')
change_button.grid(pady=(20, 0), padx=(10, 0), row=0, column=1)

app.mainloop()
