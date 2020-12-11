import src.player as player
import src.board as board

player1 = player.Player()
board = board.Board()


def test_player_created():

    assert player1.isCreated


def test_player_take_turn():
    player1.isTurn = True
    outputBeforeTurn = board.display()
    player1.take_turn(board, "TopL")
    outputAfterTurn = board.display()
    assert outputBeforeTurn != outputAfterTurn


