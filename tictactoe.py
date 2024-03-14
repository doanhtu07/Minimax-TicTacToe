from typing import List


class TicTacToe:
    Board = List[str]

    def __init__(self, size=3, winLength=3) -> None:
        self.size = size
        self.winLength = winLength

        self.board = TicTacToe.makeBoard(size)
        self.boardNums = TicTacToe.getBoardNums(size)
        self.currentWinner = None

    @staticmethod
    def makeBoard(size: int) -> Board:
        """
        Return empty square board size x size in 1D array for optimize access time
        """

        board = [' ' for _ in range(size * size)]
        return board

    def printBoard(self):
        """
        Print current board
        """

        for r in range(self.size):
            print('| ', end='')
            for c in range(self.size):
                print(self.board[r * self.size + c], end=' | ')
            print()

    @staticmethod
    def getBoardNums(size: int) -> dict[int, tuple[int, int]]:
        """
        Return dictionary of (square -> (row, col))
        """

        square = 0
        boardNums = dict()

        for r in range(size):
            for c in range(size):
                boardNums[square] = (r, c)
                square += 1

        return boardNums

    @staticmethod
    def printBoardNums(size: int):
        """
        Print a map of each grid id
        """

        square = 0
        for r in range(size):
            print('| ', end='')
            for c in range(size):
                print(square, end=' | ')
                square += 1
            print()

    def makeMove(self, square: int, letter: str) -> bool:
        """
        Return True if successfully make a move / False if error

        - square: Integer number of a board grid
        - letter: X or O
        """

        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True

        return False

    def winner(self, square: int, letter: str) -> bool:
        """
        Return True if this new move makes a winner (thus this winner must be equal to letter)

        Else return False

        - square: Integer number of a board grid
        - letter: X or O
        """

        row = square // self.size
        col = square % self.size

        if self.size < self.winLength:
            return False

        # Check row
        count = 1
        l, r = col-1, col+1

        while l >= 0:
            if self.board[row * self.size + l] == letter:
                count += 1
            else:
                break
            l -= 1

        while r < self.size:
            if self.board[row * self.size + r] == letter:
                count += 1
            else:
                break
            r += 1

        if count >= self.winLength:
            return True

        # Check col
        count = 1
        u, d = row-1, row+1

        while u >= 0:
            if self.board[u * self.size + col] == letter:
                count += 1
            else:
                break
            u -= 1

        while d < self.size:
            if self.board[d * self.size + col] == letter:
                count += 1
            else:
                break
            d += 1

        if count >= self.winLength:
            return True

        # Diag 1
        count = 1
        topRight = [row-1, col+1]
        botLeft = [row+1, col-1]

        while topRight[0] >= 0 and topRight[1] < self.size:
            r, c = topRight[0], topRight[1]
            if self.board[r * self.size + c] == letter:
                count += 1
            else:
                break
            topRight[0] -= 1
            topRight[1] += 1

        while botLeft[0] < self.size and botLeft[1] >= 0:
            r, c = botLeft[0], botLeft[1]
            if self.board[r * self.size + c] == letter:
                count += 1
            else:
                break
            botLeft[0] += 1
            botLeft[1] -= 1

        if count >= self.winLength:
            return True

        # Diag 2
        count = 1
        topLeft = [row-1, col-1]
        botRight = [row+1, col+1]

        while topLeft[0] >= 0 and topLeft[1] >= 0:
            r, c = topLeft[0], topLeft[1]
            if self.board[r * self.size + c] == letter:
                count += 1
            else:
                break
            topLeft[0] -= 1
            topLeft[1] -= 1

        while botRight[0] < self.size and botRight[1] < self.size:
            r, c = botRight[0], botRight[1]
            if self.board[r * self.size + c] == letter:
                count += 1
            else:
                break
            botRight[0] += 1
            botRight[1] += 1

        if count >= self.winLength:
            return True

        return False

    def emptySquares(self) -> bool:
        """
        Return True if there are any empty squares in the board

        Else return False
        """

        return any(self.board[square] == ' ' for square in range(9))

    def numEmptySquares(self) -> int:
        """
        Return number of empty squares in the board
        """

        return self.board.count(' ')

    def availableMoves(self) -> list[int]:
        """
        Return a list of available squares
        """

        return [i for i, val in enumerate(self.board) if val == ' ']
