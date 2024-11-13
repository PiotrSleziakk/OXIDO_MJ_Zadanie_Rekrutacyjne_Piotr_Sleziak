import openai
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

openai.api_key = "org-Jv4rQ0GTKOUrEanjAoomRnxx"

# Funkcja przetwarzania artykułu
def process_article(file_path):
    # Odczyt artykułu z pliku
    with open(file_path, 'r', encoding='utf-8') as file:
        article_text = file.read()

    # Prompt do OpenAI (można modyfikować i ulepszać)
    prompt = f"Przetwórz ten artykuł na HTML. Struktura, placeholdery obrazów z podpisami w alt i tagach img: \n{article_text}"

    # Wysłanie do OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000  # Ustal odpowiednią ilość tokenów
    )

    # Pobranie wygenerowanego kodu HTML
    html_code = response.choices[0].text.strip()

    # Zapis do artykul.html
    with open("artykul.html", "w", encoding='utf-8') as file:
        file.write(html_code)
    print("Plik artykul.html został zapisany.")

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
