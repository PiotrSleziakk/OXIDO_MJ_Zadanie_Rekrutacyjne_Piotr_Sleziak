## AI ARTICLE GENERATOR ##

Aplikacja jest narzędziem, które przetwarza plik tekstowy z artykułem na HTML. Umożliwia tworzenie struktury HTML artykułu, uwzględniając odpowiednie nagłówki, akapity, listy oraz miejsca na obrazy wraz z podpisami.

### Aplikacja generuje trzy pliki: ###
  - artykul.html - zawiera przetworzony artykuł w formacie HTML.
  - szablon.html - szablon HTML do podglądu artykułu z gotowym stylem CSS.
  - podglad.html - pełny podgląd artykułu z wbudowanym stylem.
  
### Wymagania ###
  - Python 3.x
  - Biblioteka OpenAI
  - Biblioteka Tkinter (standardowa biblioteka GUI dla Pythona)

## Instrukcja uruchomienia aplikacji (2 sposoby): ##
### 1. Uruchomienie aplikacji poprzez plik .exe: ###
	1.1. W folderze aplikacji przejść do /OXIDO_MJ_Zadanie_Rekrutacyjne_Piotr_Sleziak/app/dist , uruchomić plik ai_article_generator.exe.
	1.2. Po uruchomieniu należy wybrać plik tekstowy (.txt) zawierający artykuł do przetworzenia.
	1.3. Aplikacja wygeneruje plik artykul.html z zawartością artykułu w formacie HTML, a także pliki szablon.html i podglad.html do podglądu wynikowego artykułu.

### 2. W razie problemów z uruchomieniem aplikacji poprzez plik .exe, należy: ###
	2.1. Zainstalować python-a -> https://www.python.org/downloads/
	2.2. Następnie zainstalować biblioteke OpenAI, poprzez terminal wpisując komendę pip install openai
	2.3. Poprzez terminal przejść do folderu aplikacji /app i uruchomić skrypt ai_articles_generator.py
	2.4. Po uruchomieniu należy wybrać plik tekstowy (.txt) zawierający artykuł do przetworzenia.
	2.5. Aplikacja wygeneruje plik artykul.html z zawartością artykułu w formacie HTML, a także pliki szablon.html i podglad.html do podglądu wynikowego artykułu.

### DODATKOWE INFORMACJE: ###
- Przykład artykułu dołączonego do zadania znajduje się w folderze /app/dist/input.
- Plik wykonawczy aplikacji ai_article_generator.exe zawiera api_key co pozwala na przetestowanie aplikacji, natomiast uruchomienie poprzez terminal wymaga edytowania skryptu znajdującego się w folderze aplikacji /app (ai_articles_generator.py) i wpisania własnego klucza w miejscu "api.key" (7 linia kodu). 
Jest to spowodowane restrykcjami bezpieczeństwa GitHub-a, który nie zezwala na wprowadzenie do repozytorium widocznego klucza.
