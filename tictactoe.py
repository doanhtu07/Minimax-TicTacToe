from typing import Dict, Tuple


class TicTacToe:
    def __init__(self) -> None:
        self.board = TicTacToe.makeBoard()
        self.boardNums = TicTacToe.getBoardNums()
        self.currentWinner = None

    @staticmethod
    def makeBoard():
        """
        Return empty board 3x3
        """

        board = [[' ' for _ in range(3)] for _ in range(3)]
        return board

    def printBoard(self):
        """
        Print current board
        """

        for r in range(3):
            print('| ', end='')
            for c in range(3):
                print(self.board[r][c], end=' | ')
            print()

    @staticmethod
    def getBoardNums() -> Dict[int, Tuple[int, int]]:
        """
        Return dictionary of (square -> (row, col))
        """

        square = 0
        boardNums = dict()

        for r in range(3):
            for c in range(3):
                boardNums[square] = (r, c)
                square += 1

        return boardNums

    @staticmethod
    def printBoardNums():
        """
        Print a map of each grid id
        """

        square = 0
        for r in range(3):
            print('| ', end='')
            for c in range(3):
                print(square, end=' | ')
                square += 1
            print()

    def makeMove(self, square: int, letter: str):
        """
        Return True if successfully make a move / False if error
        - square: Integer number of a board grid
        - letter: X or O
        """

        if self.board[self.boardNums[square]] == ' ':
            self.board[self.boardNums[square]] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True

        return False

    def winner(self, square: int, letter: str):
        """
        Return True if this new move makes a winner (thus this winner must be equal to letter)
        Else return False
        - square: Integer number of a board grid
        - letter: X or O
        """

        row, col = self.boardNums[square]

        # Check row
        if all([self.board[row][c] == letter for c in range(3)]):
            return True

        # Check col
        if all([self.board[r][col] == letter for r in range(3)]):
            return True

        # Check diagonals
        if square % 2 == 0:
            diag1 = [self.boardNums[square] for square in [0, 4, 8]]
            diag2 = [self.boardNums[square] for square in [2, 4, 6]]

            if all([self.board[r][c] == letter for r, c in diag1]):
                return True

            if all([self.board[r][c] == letter for r, c in diag2]):
                return True

        return False
