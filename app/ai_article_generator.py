import openai
import tkinter as tk
from tkinter import filedialog
import os

# Tworzenie instancji klienta OpenAI
client = openai.OpenAI(api_key="api.key")

# Funkcja przetwarzania artykułu
def process_article(file_path):
    # Odczyt artykułu z pliku
    with open(file_path, 'r', encoding='utf-8') as file:
        article_text = file.read()

    # Prompt do OpenAI (można modyfikować i ulepszać)
    prompt = f"Przeanalizuj i przekształć poniższy artykuł na kod HTML z użyciem odpowiednich nagłówków, akapitów i list. Wstaw miejsca na obrazy za pomocą tagu <img src='image_placeholder.jpg'> oraz użyj podpisów obrazów w tagach <figcaption>. Proszę o dodanie precyzyjnych opisów obrazów w atrybutach 'alt'. Nie dodawaj CSS ani JavaScript: \n{article_text}"

    # Wysłanie do OpenAI z modelem gpt-3.5-turbo
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Jesteś pomocnym asystentem."},
            {"role": "user", "content": prompt}
        ]
    )

    # Konwersja odpowiedzi na słownik
    response_dict = response.model_dump()

    # Pobranie wygenerowanego kodu HTML
    html_code = response_dict['choices'][0]['message']['content'].strip()

    # Ścieżka do folderu 'processed articles'
    folder_path = os.path.join(os.getcwd(), 'processed articles')

    # Ścieżka do pliku HTML
    file_path = os.path.join(folder_path, 'artykul.html')

    # Tworzenie folderu, jeśli nie istnieje
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Zapis do artykul.html
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(html_code)
    print(f"Plik artykul.html został zapisany w folderze: {folder_path}")

    # Zwrócenie ścieżki folderu w celu przekazania do obsługi przetwarzania
    return folder_path

# Funkcja do wyboru pliku i obsługi przetwarzania
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        # Zablokowanie przycisku i ustawienie informacji o trwającym przetwarzaniu
        select_button.config(state="disabled")
        status_label.config(text="Przetwarzanie pliku...")

        # Przetwarzanie artykułu i pobranie ścieżki folderu
        folder_path = process_article(file_path)

        # Zaktualizowanie informacji i odblokowanie przycisku
        status_label.config(text=f"Przetwarzanie zakończone! \nPlik artykul.html został zapisany w folderze: {folder_path}")
        select_button.config(state="normal")


# Tworzenie GUI
root = tk.Tk()
root.title("Generator Artykułów HTML")
window_width = 400
window_height = 200

# Pobranie rozmiaru ekranu
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Obliczanie pozycji x, y do wyśrodkowania okna
center_x = int((screen_width - window_width) / 2)
center_y = int((screen_height - window_height) / 2)

# Ustawienie rozmiaru okna i pozycji
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Informacja dla użytkownika
info_label = tk.Label(root, text="Aplikacja przetwarza artykuł tekstowy na HTML.\nWybierz plik tekstowy, aby rozpocząć.", justify="center")
info_label.pack(pady=(20, 10))

# Etykieta statusu przetwarzania
status_label = tk.Label(root, text="", fg="blue", justify="center", wraplength=380)
status_label.pack(pady=(0, 10))

# Przyciski
select_button = tk.Button(root, text="Wybierz Plik", command=select_file)
select_button.pack(pady=10)

# Uruchomienie GUI
root.mainloop()