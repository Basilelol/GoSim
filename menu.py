import tkinter as tk
from ui import GoUI
from credits import show_credits
from language_menu import LanguageMenu

class MainMenu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Go Game - Main Menu")

        # Configura il colore di sfondo
        self.window.configure(bg="#f0e5d6")

        # Titolo
        title_label = tk.Label(
            self.window,
            text="Go Game",
            font=("Arial", 36, "bold"),
            fg="#333333",
            bg="#f0e5d6"
        )
        title_label.pack(pady=30)

        # Stile pulsanti
        button_style = {
            "font": ("Arial", 14),
            "bg": "#333333",
            "fg": "#ffffff",
            "activebackground": "#555555",
            "activeforeground": "#ffffff",
            "relief": "groove",
            "bd": 2,
        }

        # Pulsante per iniziare la partita
        play_button = tk.Button(
            self.window,
            text="Start Game",
            command=self.start_game,
            **button_style
        )
        play_button.pack(pady=10)

        # Pulsante per il menu lingue
        language_button = tk.Button(
            self.window,
            text="Change Language",
            command=self.change_language,
            **button_style
        )
        language_button.pack(pady=10)

        # Pulsante per i credits
        credits_button = tk.Button(
            self.window,
            text="Credits",
            command=self.show_credits,
            **button_style
        )
        credits_button.pack(pady=10)

        # Pulsante per uscire
        exit_button = tk.Button(
            self.window,
            text="Exit",
            command=self.window.quit,
            **button_style
        )
        exit_button.pack(pady=20)

        # Animazioni hover per i pulsanti
        for button in [play_button, language_button, credits_button, exit_button]:
            button.bind("<Enter>", lambda e, b=button: b.config(bg="#555555"))
            button.bind("<Leave>", lambda e, b=button: b.config(bg="#333333"))

    def start_game(self):
        self.window.destroy()
        game_ui = GoUI()
        game_ui.start()

    def change_language(self):
        self.window.destroy()
        lang_menu = LanguageMenu(self.show)
        lang_menu.show()

    def show_credits(self):
        self.window.destroy()
        show_credits()

    def show(self):
        self.window.mainloop()

if __name__ == "__main__":
    menu = MainMenu()
    menu.show()
