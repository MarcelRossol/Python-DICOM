# Opis plików DICOM
Pliki DICOM (Digital Imaging and Communications in Medicine) to standardowy format używany w medycynie do przechowywania i przesyłania obrazów medycznych oraz powiązanych danych. Łączą one obrazy diagnostyczne (CT, MRI, USG itp.) z metadanymi, takimi jak dane pacjenta i szczegóły techniczne badania. DICOM umożliwia łatwe zarządzanie, udostępnianie i analizę obrazów medycznych  w systemach PACS (Picture Archiving and Communication Systems). Dzięki temu pliki te są szeroko stosowane w różnych dziedzinach medycyny, zapewniając interoperacyjność między urządzeniami i systemami różnych producentów, co ułatwia diagnozowanie i leczenie pacjentów. Zestaw plików DICOM ze skanu trójwymiarowego (np. tomografia komputerowa) składa się z wielu pojedynczych plików, z których każdy reprezentuje osobny przekrój (warstwę) ciała pacjenta. Każdy plik DICOM w tym zestawie zawiera:
- Dane obrazowe
- Metadane – informacje o pacjencie (np. imię, nazwisko, wiek), dane techniczne dotyczące skanu (np. napięcie lampy rentgenowskiej, grubość warstwy) oraz dodatkowe informacje diagnostyczne.
- Szczegóły badania – informacje dotyczące parametrów skanu, takich jak data i czas wykonania badania, ustawienia aparatu, i inne szczegóły techniczne.
# Prezentacja aplikacji
Aplikacja pozwala na otwarcie zbioru plików DICOM przy użyciu przycisku „Open”. 
Po wciśnięciu przycisku pojawi się okno pozwalające na wybór folderu zawierającego pliki. Po wczytaniu zbioru zawierającego pliki DICOM zostanie wyświetlony komunikat potwierdzający (Rysunek 3). W przypadku wybory folderu bez plików DICOM, zostanie wyświetlony odpowiedni komunikat (Rysunek 4). Po wgraniu plików istnieje kilka możliwości interakcji ze zbiorem przy pomocy przycisków i suwaków:
- **Przycisk „Show info”** – pozwala na wyświetlenie informacji o pacjencie i procedurze.
- **Przycisk „Anonymize”** – pozwala zataić informacje o pacjencie i procedurze. Po wciśnięciu przycisku pojawi się okno pozwalające wybrać zbiór który ma być zatajony.
- **Przycisk „Save PNG”** – pozwala zapisać każdy z plików DICOM jako plik PNG. Po wciśnięciu przycisku pojawi się okno pozwalające wybrać folder do którego mają zostać  zapisane pliki PNG.
- **Przycisk „Filter”** – pozwala na wprowadzenie filtracji medianowej.
- **Przycisk „Segmentation”** – pozwala na przeprowadzenie segmentacji danej warstwy. Po wciśnięciu przycisku zostaje wyświetlone okno z suwakami pozwalającymi na dostosowanie minimalnej i maksymalnej wartości progowania. Zmiany są na bieżąco wyświetlane w głównym oknie.
- **Suwak „Slice”** – pozwala na zmianę warstwy, iterując przez zbiór danych DICOM.
- **Suwaki „Max” i „Min** – pozwalają na dostosowanie kontrastu obrazu. Po modyfikacji należy wcisnąć przycisk „Apply” w celu zastosowania zmian do wszystkich warstw (w innym przypadku przy zmianie warstwy, zmiany zostaną cofnięte. W przypadku potrzeby dalszej modyfikacji należy wcisnąć przycisk „Change”, który pozwoli na ponowną zmianę kontrastu. 
