# Universal Text Translator

Hey! This is a desktop translation app I built using Python and Flet. I wanted a quick way to translate text without constantly opening a browser tab, so I used the `deep-translator` library to grab translations directly from the web without needing any complicated API keys.

## Key Features
* **Live API Integration:** Fetches accurate translations straight from the web using `deep-translator`.
* **Modern Dark Mode UI:** Built with Flet so it feels like a native, responsive desktop app.
* **Crash-Proof Error Handling:** I added `try/except` blocks, so if the internet drops, the app prints a friendly warning instead of just crashing.
* **Strict Type Safety:** I had to explicitly cast my variables using `str()` to get strict linters like Pylance to stop complaining about empty dropdowns.
* **Future-Proof Components:** Flet kept throwing deprecation warnings for `ElevatedButton`, so I built a completely custom interactive button from scratch to keep the terminal clean.

## Technologies Used
* **Python 3.x**
* **Flet** (for rendering the UI and window)
* **deep-translator** (for the backend translation)

## How to Run

Install the required dependencies from your terminal:
   pip install flet deep-translator
