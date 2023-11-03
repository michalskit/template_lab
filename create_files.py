import os

def create_files():
    # Ustalamy bazowy katalog jako bieżący katalog roboczy
    base_dir = os.getcwd()

    # Definiujemy wzorce nazw plików
    file_patterns = ["lab4_{}.py", "test_lab4_{}.py"]

    for i in range(1, 12):
        # Dla każdego wzorca tworzymy plik
        for pattern in file_patterns:
            file_name = pattern.format(i)  # tworzymy nazwę pliku
            file_path = os.path.join(base_dir, file_name)  # tworzymy pełną ścieżkę do pliku

            # Tworzymy plik, jeśli nie istnieje
            if not os.path.exists(file_path):
                with open(file_path, "w") as file:
                    file.write("# Pusty plik Pythona o nazwie " + file_name)  # możesz tutaj wstawić dowolną zawartość

    print("Pliki zostały utworzone.")

# Wywołujemy funkcję
create_files()
