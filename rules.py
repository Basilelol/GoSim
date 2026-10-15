class GoRules:
    def __init__(self, board, ui):
        self.board = board
        self.ui = ui  # Aggiungi il parametro ui per interagire con l'interfaccia

    def check_capture(self, row, col, player):
        """Check if placing a stone at (row, col) captures opponent stones."""
        opponent = 'black' if player == 'white' else 'white'
        captured_stones = []

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            group, liberties = self._get_group_and_liberties(row + dr, col + dc)
            if liberties == 0 and self.board.is_on_board(row + dr, col + dc):
                if group and self.board.board[group[0][0]][group[0][1]] == opponent:
                    captured_stones.extend(group)

        if captured_stones:
            self.board.remove_stones(captured_stones)
            self.ui.increment_score(player, captured_stones)  # Increments the score
        return captured_stones

    def _get_group_and_liberties(self, row, col):
        """Find a group of connected stones and count their liberties."""
        if not self.board.is_on_board(row, col) or self.board.board[row][col] is None:
            return [], 0

        visited = set()
        group = []
        liberties = 0
        color = self.board.board[row][col]

        def dfs(r, c):
            nonlocal liberties
            if (r, c) in visited:
                return
            if not self.board.is_on_board(r, c):
                return
            visited.add((r, c))

            if self.board.board[r][c] == color:
                group.append((r, c))
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dfs(r + dr, c + dc)
            elif self.board.board[r][c] is None:
                liberties += 1

        dfs(row, col)
        return group, liberties
