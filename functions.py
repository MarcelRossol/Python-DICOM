import pydicom
import numpy as np
from PIL import Image


def get_metadata(path):
    dicom_file = pydicom.dcmread(path)
    patient_name = dicom_file.PatientName
    patient_id = dicom_file.PatientID
    print(dicom_file)


def pillow_show_img(path):

    # Reading DICOM file
    dicom_file = pydicom.dcmread(path)
    dicom_array = dicom_file.pixel_array

    # Converting to 8-bit
    float_dicom_array = dicom_array.astype(float)
    positive_dicom_array = np.maximum(float_dicom_array, 0)
    normalized_dicom_array = positive_dicom_array / positive_dicom_array.max()
    normalized_dicom_array *= 255.0
    uint8_image = np.uint8(normalized_dicom_array)

    # Showing image
    pillow_image = Image.fromarray(uint8_image)
    pillow_image.show()


def show_img(path):
    dicom_file = pydicom.dcmread(path)
    dicom_array = dicom_file.pixel_array

    # Changing the image contrast
    # hounsfield_min = np.min(dicom_array)
    # hounsfield_max = np.max(dicom_array)
    hounsfield_min = -200
    hounsfield_max = 200
    hounsfield_range = hounsfield_max - hounsfield_min

    # Normalizing image
    dicom_array[dicom_array < hounsfield_min] = hounsfield_min
    dicom_array[dicom_array > hounsfield_max] = hounsfield_max
    normalized_dicom_array = (dicom_array - hounsfield_min) / hounsfield_range

    normalized_dicom_array *= 255
    uint8_image = np.uint8(normalized_dicom_array)

    # Showing image
    pillow_image = Image.fromarray(uint8_image)
    pillow_image.show()


if __name__ == "__main__":
    file_path = "test.dcm"

    get_metadata(file_path)
    # pillow_show_img(file_path)
    #show_img(file_path)




