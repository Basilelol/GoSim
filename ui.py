import tkinter as tk
from tkinter import messagebox
from board import GoBoard
from rules import GoRules

class GoUI:
    def __init__(self, size=19):
        self.size = size
        self.board = GoBoard(size)
        self.rules = GoRules(self.board, self)  # Passa l'oggetto GoUI alla classe GoRules
        self.current_player = 'black'

        # Variabili per il punteggio
        self.score_black = 0
        self.score_white = 0

        # Tkinter setup
        self.window = tk.Tk()
        self.window.title("Go Game")

        # Stile del canvas
        self.canvas = tk.Canvas(self.window, width=600, height=600, bg='#FAF3E0', highlightthickness=0)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)

        self.cell_size = 600 // self.size
        self.draw_board()

        # Etichetta di stato
        self.status_label = tk.Label(self.window, text="Turn: Black", font=("Helvetica", 16), bg='#333333', fg='#FFFFFF')
        self.status_label.pack(fill="x")

        # Etichette per visualizzare il punteggio
        score_frame = tk.Frame(self.window, bg='#333333')
        score_frame.pack(fill="x")

        self.score_label_black = tk.Label(score_frame, text=f"Black: {self.score_black}", font=("Helvetica", 14), bg='#333333', fg='#FFFFFF')
        self.score_label_black.pack(side="left", padx=20)

        self.score_label_white = tk.Label(score_frame, text=f"White: {self.score_white}", font=("Helvetica", 14), bg='#333333', fg='#FFFFFF')
        self.score_label_white.pack(side="right", padx=20)

    def draw_board(self):
        """Draw the Go board grid."""
        for i in range(self.size):
            x = i * self.cell_size + self.cell_size // 2
            self.canvas.create_line(x, self.cell_size // 2, x, 600 - self.cell_size // 2, fill="#8B5A2B")
            self.canvas.create_line(self.cell_size // 2, x, 600 - self.cell_size // 2, x, fill="#8B5A2B")

        # Disegna i punti hoshi (stelle di riferimento)
        if self.size >= 9:
            star_points = self._get_star_points()
            for (row, col) in star_points:
                x = col * self.cell_size + self.cell_size // 2
                y = row * self.cell_size + self.cell_size // 2
                self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="#8B5A2B", outline="")

    def _get_star_points(self):
        """Return the positions of hoshi points for the board size."""
        if self.size == 9:
            points = [2, 6]
        elif self.size == 13:
            points = [3, 9]
        else:  # Standard 19x19
            points = [3, 9, 15]
        return [(r, c) for r in points for c in points]

    def on_click(self, event):
        """Handle click events to place stones."""
        x, y = event.x, event.y
        row = int((y - self.cell_size // 2) // self.cell_size)
        col = int((x - self.cell_size // 2) // self.cell_size)

        if 0 <= row < self.size and 0 <= col < self.size:
            if self.board.place_stone(row, col, self.current_player):
                self.draw_stone(row, col)
                captured = self.rules.check_capture(row, col, self.current_player)
                if captured:
                    self.update_board()

                self.current_player = 'white' if self.current_player == 'black' else 'black'
                self.status_label.config(text=f"Turn: {'Black' if self.current_player == 'black' else 'White'}")
                self.update_score()

    def draw_stone(self, row, col, color=None):
        """Draw a stone on the board."""
        if color is None:
            color = 'black' if self.current_player == 'black' else 'white'

        x = col * self.cell_size + self.cell_size // 2
        y = row * self.cell_size + self.cell_size // 2

        # Effetto di ombra per maggiore profondità
        shadow_color = '#6E6E6E' if color == 'black' else '#D3D3D3'
        self.canvas.create_oval(x - 18, y - 18, x + 18, y + 18, fill=shadow_color, outline=shadow_color)

        # Pietra principale
        self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill=color, outline=color)

    def update_board(self):
        """Redraw the board to reflect the current state."""
        self.canvas.delete("all")
        self.draw_board()

        # Ridisegna tutte le pietre nel loro stato attuale
        for row in range(self.size):
            for col in range(self.size):
                if self.board.board[row][col] == 'black':
                    self.draw_stone(row, col, 'black')  # Disegna le pietre nere
                elif self.board.board[row][col] == 'white':
                    self.draw_stone(row, col, 'white')  # Disegna le pietre bianche

    def update_score(self):
        """Update the scores based on captured stones."""
        self.score_label_black.config(text=f"Black: {self.score_black}")
        self.score_label_white.config(text=f"White: {self.score_white}")

    def start(self):
        """Start the Tkinter main loop."""
        self.window.mainloop()

    def increment_score(self, player, captured_stones):
        """Increment the score for the player based on captured stones."""
        if player == 'black':
            self.score_black += len(captured_stones)
        elif player == 'white':
            self.score_white += len(captured_stones)