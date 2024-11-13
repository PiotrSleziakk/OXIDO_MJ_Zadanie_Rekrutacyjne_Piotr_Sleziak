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
    prompt = f"Przetwórz ten artykuł na HTML. Struktura, placeholdery obrazów z podpisami w alt i tagach img: \n{article_text}"

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

    # Ścieżka do folderu 'articles already processed'
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

# Funkcja do wyboru pliku
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        process_article(file_path)

# Tworzenie GUI
root = tk.Tk()
root.title("Generator Artykułów HTML")

# Przyciski
select_button = tk.Button(root, text="Wybierz Plik", command=select_file)
select_button.pack(pady=10)

# Uruchomienie GUI
root.mainloop()