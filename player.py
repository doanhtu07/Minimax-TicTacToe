import math
import random
from tictactoe import TicTacToe


class Player:
    def __init__(self, letter: str) -> None:
        self.letter = letter

    def getMove(self, game: TicTacToe) -> int:
        """
        Return the square that the player wants to move
        """
        pass


class HumanPlayer(Player):
    def __init__(self, letter: str) -> None:
        super().__init__(letter)

    def getMove(self, game: TicTacToe) -> int:
        validSquare = False
        inputSquare = None

        while not validSquare:
            try:
                inputSquare = int(
                    input(self.letter + '\'s turn. Input move (0-9): ')
                )

                if inputSquare not in game.availableMoves():
                    raise ValueError

                validSquare = True

            except ValueError:
                print('Invalid square. Try again.')

        return inputSquare


class RandomComputerPlayer(Player):
    def __init__(self, letter: str) -> None:
        super().__init__(letter)

    def getMove(self, game: TicTacToe) -> int:
        return random.choice(game.availableMoves())


class SmartComputerPlayer(Player):
    def __init__(self, letter: str) -> None:
        super().__init__(letter)

    def getMove(self, game: TicTacToe) -> int:
        square = None
        moves = game.availableMoves()

        if len(moves) == 9:
            square = random.choice(moves)
        else:
            square = self.minimax(game, self.letter)['position']

        return square

    def minimax(self, state: TicTacToe, player: str):
        """
        - state: An instance of TicTacToe game at a moment
        - player: Current considering player (will alternate when traversing down the state tree)

        Return {'position': Optimal move for requested player, 'score': score of this optimal move}
        """

        # state.printBoard()
        # print(state.currentWinner)
        # print(player)

        # Try to maximize for this player (yourself). In this case, yourself is a smart computer
        maxPlayer = self.letter

        # Opposite player of currently considering player
        otherPlayer = 'O' if player == 'X' else 'X'

        # If previous move is a winner
        if state.currentWinner == otherPlayer:
            return {
                'position': None,
                'score': 1 * (state.numEmptySquares() + 1) if otherPlayer == maxPlayer else -1 * (state.numEmptySquares() + 1)
            }
        # Draw
        elif not state.emptySquares():
            return {
                'position': None,
                'score': 0
            }

        if player == maxPlayer:
            best = {
                'position': None,
                'score': -math.inf  # Will try to beat this
            }
        else:
            best = {
                'position': None,
                'score': math.inf  # Will try to minimize this
            }

        for possibleMove in state.availableMoves():
            state.makeMove(possibleMove, player)

            # Simulate a game after above move
            simulated = self.minimax(state, otherPlayer)

            # Fill position with move of current player, so we can return the optimal move for requested player
            simulated['position'] = possibleMove

            # Undo move
            state.board[possibleMove] = ' '
            state.currentWinner = None

            if player == maxPlayer:
                if simulated['score'] > best['score']:
                    best = simulated
            else:
                if simulated['score'] < best['score']:
                    best = simulated

        return best
