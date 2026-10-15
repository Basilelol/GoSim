import tkinter as tk

class LanguageMenu:
    def __init__(self, back_to_menu_callback):
        """Crea il menu per la selezione della lingua.

        Args:
            back_to_menu_callback (callable): Funzione da richiamare per tornare al menu principale.
        """
        self.back_to_menu_callback = back_to_menu_callback

        self.window = tk.Tk()
        self.window.title("Change Language")
        self.window.geometry("400x300")  # Finestra più grande per un layout migliorato

        # Stile personalizzato per il background
        self.window.configure(bg="#F2E5D7")  # Colore beige chiaro simile alla tavola da Go

        # Titolo
        title_label = tk.Label(self.window, text="Select Language", font=("Arial", 18, "bold"), bg="#F2E5D7", fg="#5D3A00")
        title_label.pack(pady=20)

        # Pulsanti per cambiare lingua
        english_button = tk.Button(
            self.window, 
            text="English", 
            font=("Arial", 14), 
            bg="#8C593B", 
            fg="white", 
            activebackground="#A67853", 
            activeforeground="white", 
            command=lambda: self.set_language("English")
        )
        english_button.pack(pady=10, ipadx=20, ipady=5)

        italian_button = tk.Button(
            self.window, 
            text="Italiano", 
            font=("Arial", 14), 
            bg="#8C593B", 
            fg="white", 
            activebackground="#A67853", 
            activeforeground="white", 
            command=lambda: self.set_language("Italiano")
        )
        italian_button.pack(pady=10, ipadx=20, ipady=5)

        # Pulsante per tornare al menu principale
        back_button = tk.Button(
            self.window, 
            text="Back to Menu", 
            font=("Arial", 14), 
            bg="#5D3A00", 
            fg="white", 
            activebackground="#8C593B", 
            activeforeground="white", 
            command=self.back_to_menu
        )
        back_button.pack(pady=20, ipadx=20, ipady=5)

    def set_language(self, language):
        """Imposta la lingua selezionata (placeholder per funzionalità future)."""
        print(f"Language set to: {language}")  # Può essere sostituito con un sistema di traduzione

    def back_to_menu(self):
        self.window.destroy()
        self.back_to_menu_callback()  # Richiama il callback per tornare al menu principale

    def show(self):
        self.window.mainloop()

# Esempio di utilizzo, rimuovere o modificare per il contesto reale
if __name__ == "__main__":
    def back_to_menu():
        print("Back to main menu")

    menu = LanguageMenu(back_to_menu)
    menu.show()
