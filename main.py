import time
from player import HumanPlayer, Player, SmartComputerPlayer
from tictactoe import TicTacToe


def play(game: TicTacToe, xPlayer: Player, oPlayer: Player, printGame=True) -> str:
    """
    Play game

    Return winning letter
    """

    if printGame:
        game.printBoardNums(game.size)

    letter = 'X'
    while game.emptySquares():
        if letter == 'O':
            square = oPlayer.getMove(game)
        else:
            square = xPlayer.getMove(game)

        if game.makeMove(square, letter):
            if printGame:
                print(f'{letter} makes a move to square {square}')
                game.printBoard()
                print()

            if game.currentWinner:
                if printGame:
                    print(f'{letter} wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(.8)

    if printGame:
        print('It\'s a tie!')


if __name__ == '__main__':
    game = TicTacToe(size=3, winLength=3)
    play(game, SmartComputerPlayer('X'), HumanPlayer('O'))
