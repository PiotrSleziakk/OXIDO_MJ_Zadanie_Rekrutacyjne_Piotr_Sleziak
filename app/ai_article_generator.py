import openai
import tkinter as tk
from tkinter import filedialog
import os

# Tworzenie instancji klienta OpenAI
client = openai.OpenAI(api_key="api.key")


# Funkcja generująca szablon HTML i zapisująca go do pliku
def generate_template():
    template_html = """<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Podgląd Artykułu</title>
    <style>
        html, body {
            height: 100%;  /* Ustalamy pełną wysokość okna */
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            flex-direction: column; /* Ustawiamy elementy w kolumnie */
        }
        .container {
            width: 80%;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            flex-grow: 1; /* Pozwala kontenerowi zająć całą dostępną przestrzeń */
        }
        h1, h2, h3 {
            color: #333;
        }
        p {
            font-size: 1.1em;
            line-height: 1.6;
            color: #555;
        }
        img {
            max-width: 100%;
            height: auto;
        }
        figcaption {
            text-align: center;
            font-size: 0.9em;
            color: #777;
        }
        footer {
            text-align: center;
            padding: 10px;
            background-color: #333;
            color: #fff;
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Artykuł będzie wklejony tutaj -->
    </div>
    <footer>
        <p>&copy; 2024 Generator Artykułów HTML</p>
    </footer>
</body>
</html>
"""

    # Zapis do szablon.html
    template_path = os.path.join(os.getcwd(), 'szablon.html')
    with open(template_path, 'w', encoding='utf-8') as file:
        file.write(template_html)


# Funkcja do generowania pełnego podglądu artykułu
def generate_preview(article_content):
    preview_html = f"""<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Podgląd Artykułu</title>
    <style>
        html, body {{
            height: 100%;  /* Ustalamy pełną wysokość okna */
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            flex-direction: column; /* Ustawiamy elementy w kolumnie */
        }}
        .container {{
            width: 80%;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            flex-grow: 1; /* Pozwala kontenerowi zająć całą dostępną przestrzeń */
        }}
        h1, h2, h3 {{
            color: #333;
        }}
        p {{
            font-size: 1.1em;
            line-height: 1.6;
            color: #555;
        }}
        img {{
            max-width: 100%;
            height: auto;
        }}
        figcaption {{
            text-align: center;
            font-size: 0.9em;
            color: #777;
        }}
        footer {{
            text-align: center;
            padding: 10px;
            background-color: #333;
            color: #fff;
            width: 100%;
        }}
    </style>
</head>
<body>
    <div class="container">
        {article_content}
    </div>
    <footer>
        <p>&copy; 2024 Generator Artykułów HTML</p>
    </footer>
</body>
</html>"""

    # Zapis do podglad.html
    preview_path = os.path.join(os.getcwd(), 'podglad.html')
    with open(preview_path, 'w', encoding='utf-8') as file:
        file.write(preview_html)

# Funkcja przetwarzania artykułu
def process_article(file_path):
    # Odczyt artykułu z pliku
    with open(file_path, 'r', encoding='utf-8') as file:
        article_text = file.read()

    # Prompt do OpenAI (można modyfikować i ulepszać)
    prompt = f"""Przeanalizuj poniższy artykuł i przekształć go na kod HTML, używając odpowiednich nagłówków, akapitów i list. 
    Wstaw miejsca na obrazy za pomocą tagu <img src='image_placeholder.jpg'> oraz użyj podpisów obrazów w tagach <figcaption>. 
    Proszę o dodanie precyzyjnych opisów obrazów w atrybutach 'alt'. 
    Nie dodawaj CSS, JavaScript, markdown ani żadnych dodatkowych znaczników HTML, takich jak kody źródłowe czy fragmenty z '```html'. 
    Bardzo ważne, aby cała zawartość artykułu została umieszczona **wyłącznie** pomiędzy tagami <body> i </body> bez dodatkowych znaków, niepotrzebnych elementów lub formatowania. 
    Proszę upewnić się, że wygenerowany HTML jest czysty, bez żadnych zbędnych tagów lub tekstów. 
    Poniżej znajduje się artykuł do przetworzenia:{article_text}"""

    # Wysłanie do OpenAI z modelem gpt-4o
    response = client.chat.completions.create(
        model="gpt-4o",
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

    # Generowanie szablonu HTML
    generate_template()

    # Generowanie podglądu artykułu
    generate_preview(html_code)

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

# Funkcja do zamknięcia aplikacji
def exit_application():
    root.quit()

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

# Ramka na przyciski
button_frame = tk.Frame(root)
button_frame.pack(pady=(0, 20))

# Przycisk do wyboru pliku
select_button = tk.Button(button_frame, text="Wybierz plik", command=select_file)
select_button.pack(side="left", padx=(0, 10))

# Przycisk wyjścia
exit_button = tk.Button(button_frame, text="Zakończ", command=exit_application)
exit_button.pack(side="left", padx=(10, 0))

# Uruchomienie GUI
root.mainloop()