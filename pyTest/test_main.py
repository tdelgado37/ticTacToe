import src.main as main
import src.player as player
import src.board as board


player = player.Player("X")
board = board.Board()

def test_play_Y():
    wantToPlay = main.play("Y")
    assert wantToPlay

def test_play_N():
    wantToPlay = main.play("N")
    assert not wantToPlay

#TODO: add in tests for the checkwinner function
def test_checkWinner_Win():
    player.take_turn(board, position="TopL")
    player.take_turn(board, position="TopM")
    player.take_turn(board, position="TopR")
    win, winner = main.checkForWinner(3, board)
    assert win

def test_checkWinner_noWin():
    board.clear()
    player.take_turn(board, position="TopL")
    player.take_turn(board, position="TopM")
    player.take_turn(board, position="BottomR")
    win, winner = main.checkForWinner(3, board)
    assert not win


