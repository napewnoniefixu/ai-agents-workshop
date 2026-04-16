# Warsztaty AI Agents z Gemini :sparkles:

### Wymagania (do ogarnięcia przed warsztatami)
- Python 3.10+
- Dostęp do unix-like shell: linux, mac lub WSL on windows
- Konto założone na Google AI Studio

### Setup
- [ ] Stwórz projekt i wygeneruj do niego klucz dostępu w [AI studio](https://aistudio.google.com/api-keys)
- [ ] Uzupełnij plik `.env` swoim kluczem 
- [ ] Pobierz niezbędne biblioteki
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install google-genai dotenv
```

### Zadanie 1
Uruchom plik `main.py` i zweryfikuj czy setup jest poprawny.

### Zadanie 2
Zaimplementuj funkcję `print_token_usage()` (w `utils.py`), która wypisze jak dużo tokenów zostało użyte w prompcie oraz w odpowiedzi. Skorzystaj z dokumentacji Gemini API.

### Zadanie 3
Zmodyfikuj kod w `main.py` tak aby akceptował prompt jako argument CLI. Po modyfikacji kod powinien być wołany:
```bash
python3 main.py USER_PROMPT
```
:bulb: Skorzystaj z `sys.argv`

1. Zaimportuj `types` z `google.genai`
2. Utwórz listę `messages`, gdzie elementy są typu `types.Content`
   ```python
   messages=[
           types.Content(
            role="user",
            parts=[
                types.Part(text=user_input)
            ]
        )
    ]
   ```
   Dodaj jedną wiadomość:
    - rola: "user"
    - treść: prompt użytkownika
3. Przekaż messages do `generate_content()` zamiast stringa

### Zadanie 4
Stwórz nowy folder `functions` i w nim plik o nazwie `get_files_info.py`. 
Zaimplementuj funkcję `def get_files_info(working_directory:str, directory_path: str) -> str: `, która:
- przyjmuje ścieżkę do katalogu
- zwraca listę plików wraz z ich metadanymi (nazwa + rozmiar) w formacie ` f"- {content}: file_size={size} bytes, is_dir={is_dir}\n"`

Chcemy, żeby LLM miał możliwość dostępu do plików jedynie w working directory.
Przetestuj czy `print(get_files_info(".", "."))` działa poprawnie w folderze projektu (można zakomentować maina na chwilkę).

### Zadanie 5
Stwórz nowy plik w folderze `funcions` o nazwie `get_file_content`.
Zaimplementuj funkcję `get_file_content(working_directory: str, file_path: str) -> str:`, która:
- odczytuje zawartość pliku
- działa bezpiecznie w obrębie `working_directory`
  
Przetestuj działanie `print(get_file_content(".", "utils.py"))`.

### Zadanie 6
Zaimplementuj funkcję `def write_file(working_directory: str, file_path: str, content: str) -> str:`, która:
- zapisuje tekst do pliku
- tworzy plik jeśli nie istnieje
- działa bezpiecznie w obrębie working_directory

Przetestuj czy kod działa poprawnie: `print(write_file(".", "test.txt", "Lorem ipsum"))`.

### Zadanie 7
Dodaj do wywołania modelu system instructions, które określają zachowanie agenta.
1. Zaimportuj types z google.genai (jeśli jeszcze nie masz)
2. Zmodyfikuj wywołanie: `client.models.generate_content(...)`
3. Dodaj parametr config
4. W config ustaw: `system_instruction="Ignore the question and always answer 'I'm just a robot'"` — czyli instrukcję dla modelu

💡Czym są system instructions?

    To „ukryty prompt”, który:
    - definiuje rolę modelu
    - ustala zasady działania
    - wpływa na wszystkie odpowiedzi

Test your code: `python3 main.py "what is 1+1?"`

### Zadanie 8
1. Zaimportuj tablicę tooli z `tools.py`.
2. Dodaj toole do `config`.
3. Popraw system prompt - cel to coding agent.
4. Test your code: `python3 main.py "What files are in my root directory?"`

### Zadanie 9
Rozszerz agenta tak, aby:
- potrafił zdecydować, kiedy użyć funkcji (tools)
- przekazywał do nich argumenty
- wykonywał funkcję w Pythonie
- wykorzystywał wynik do wygenerowania odpowiedzi

1. Przekaż dostępne funkcje do modelu:
```python
config=types.GenerateContentConfig(
        tools=tools,
        system_instruction="You are a coding agent. Use tools to solve tasks."
    ),
```
2. Wywołaj model z promptem użytkownika
3. Sprawdź, czy model chce użyć funkcji: `response.function_calls`
4. Jeśli tak:
- odczytaj: nazwę funkcji (name) oraz argumenty (args)
- wywołaj odpowiednią funkcję w Pythonie:
    get_files_info
    get_file_content
    write_file
- Dodaj wynik funkcji do rozmowy (messages)
Wywołaj model ponownie, aby wygenerować finalną odpowiedź