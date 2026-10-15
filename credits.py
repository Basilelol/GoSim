# credits.py
import tkinter as tk

def show_credits():
    window = tk.Tk()
    window.title("Credits")

    # Titolo dei credits
    title_label = tk.Label(window, text="Game by", font=("Arial", 18))
    title_label.pack(pady=20)

    # Nome dell'autore
    name_label = tk.Label(window, text="Alessandro Basile", font=("Arial", 24, "bold"), justify="center")
    name_label.pack(pady=20)

    name_label = tk.Label(window, text="Quel coglione di ChatGPT", font=("Arial", 24, "bold"), justify="center")
    name_label.pack(pady=20)

    # Pulsante per tornare indietro
    back_button = tk.Button(window, text="Back to Menu", font=("Arial", 14), command=window.destroy)
    back_button.pack(pady=20)

    window.mainloop()
