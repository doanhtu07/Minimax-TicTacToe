# Minimax-TicTacToe

Utility function = A * (1 + empty squares left)
- Assuming X is target winner, A = 1 if X wins / -1 if O wins / 0 if draw
- Empty squares left: Since we want to choose a state where we win as early as possible
- **1+** is for making utility value to be positive still when we win without any empty squares left