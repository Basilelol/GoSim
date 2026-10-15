class GoBoard:
    def __init__(self, size=19):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def place_stone(self, row, col, player):
        """Place a stone on the board if the cell is empty."""
        if self.board[row][col] is not None:
            return False  # Cell already occupied
        self.board[row][col] = player
        return True

    def get_board(self):
        """Return the current state of the board."""
        return self.board

    def remove_stones(self, stones):
        """Remove stones from the board (used for captures)."""
        for row, col in stones:
            self.board[row][col] = None

    def is_on_board(self, row, col):
        """Check if a position is within the board boundaries."""
        return 0 <= row < self.size and 0 <= col < self.size

    def get_hoshi_points(self):
        """Calculate and return hoshi points for the board size."""
        if self.size not in [9, 13, 19]:
            return []  # Hoshi points are standard for 9x9, 13x13, and 19x19 boards

        offset = 3 if self.size == 9 else 4
        positions = [offset - 1, self.size - offset, self.size // 2]
        hoshi_points = [(x, y) for x in positions for y in positions]

        # For 19x19, add center hoshi
        if self.size == 19:
            hoshi_points.append((self.size // 2, self.size // 2))

        return hoshi_points

    def draw_stone(self, canvas, row, col, color):
        """Draw a smaller, gradient-filled stone on the canvas."""
        cell_size = 600 // self.size
        x = col * cell_size + cell_size // 2
        y = row * cell_size + cell_size // 2
        radius = int(cell_size * 0.25)  # Further reduced stone size for better spacing

        if color == 'black':
            fill = "#111111"  # Darker black for a sleek appearance
        elif color == 'white':
            fill = "#f9f9f9"  # Softer white
        else:
            return

        canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius,
            fill=fill, outline=""
        )