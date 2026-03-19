import flet as ft
from deep_translator import GoogleTranslator

def main(page: ft.Page):
    # Configure the main application window and UI theme
    page.title = "Universal Text Translator"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 900
    page.window.height = 600
    page.padding = 30

    # Map display names to their corresponding API language codes
    languages = {
        "English": "en",
        "Greek": "el",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Italian": "it",
        "Japanese": "ja"
    }

    # Initialize the main header text
    title = ft.Text(
        "Text Translator 🌍", 
        size=32, 
        weight=ft.FontWeight.BOLD, 
        color=ft.Colors.BLUE_400
    )

    # Dropdowns for selecting source and target languages
    source_lang = ft.Dropdown(
        label="Translate From",
        options=[ft.dropdown.Option(key=val, text=key) for key, val in languages.items()],
        value="en",
        width=200
    )
    
    target_lang = ft.Dropdown(
        label="Translate To",
        options=[ft.dropdown.Option(key=val, text=key) for key, val in languages.items()],
        value="el",
        width=200
    )

    # Input area for the user's text
    input_text = ft.TextField(
        label="Type your text here...",
        multiline=True,
        min_lines=8,
        max_lines=8,
        expand=True,
        border_color=ft.Colors.BLUE_400
    )
    
    # Read-only output area for the translated result
    output_text = ft.TextField(
        label="Translation will appear here",
        multiline=True,
        min_lines=8,
        max_lines=8,
        read_only=True,
        expand=True,
        border_color=ft.Colors.GREEN_400
    )

    # Build a custom button using a Container to avoid Flet library deprecation issues
    btn_text = ft.Text("Translate", weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    translate_btn = ft.Container(
        content=ft.Row(
            controls=[ft.Icon(ft.Icons.TRANSLATE, color=ft.Colors.WHITE), btn_text],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        bgcolor=ft.Colors.BLUE_700,
        padding=15,
        border_radius=10,
        width=250,
        ink=True, # Enables the visual ripple effect on click
        alignment=ft.Alignment(0, 0)
    )

    # Handles the API call and UI updates when the button is clicked
    def translate_text(e):
        # Prevent empty submissions
        if not input_text.value:
            return
        
        # Temporarily disable the button and show a loading state
        btn_text.value = "Translating..."
        translate_btn.disabled = True
        page.update()

        try:
            # Fetch translation via deep-translator API values are explicitly cast to str() to satisfy Pylance strict typing rules
            translated = GoogleTranslator(
                source=str(source_lang.value), 
                target=str(target_lang.value)
            ).translate(str(input_text.value))
            
            output_text.value = translated
            
        except Exception as ex:
            # Provide user-friendly feedback if the network request fails
            output_text.value = f"⚠️Error: Could not connect to translation service.\nDetails: {ex}"
        
        # Restore the button to its original state
        btn_text.value = "Translate"
        translate_btn.disabled = False
        page.update()

    # Attach the logic to the custom button
    translate_btn.on_click = translate_text

    # Assemble the UI components sequentially on the page
    page.add(
        ft.Row([title], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(height=20, color="transparent"),
        
        # Language selectors with a directional arrow
        ft.Row(
            controls=[
                source_lang, 
                ft.Icon(ft.Icons.ARROW_FORWARD_ROUNDED, size=30, color=ft.Colors.GREY_500), 
                target_lang
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Divider(height=20, color="transparent"),
        
        # Text boxes placed side-by-side
        ft.Row(
            controls=[input_text, output_text], 
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            spacing=20
        ),
        ft.Divider(height=20, color="transparent"),
        
        # Centered action button
        ft.Row([translate_btn], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.run(main)