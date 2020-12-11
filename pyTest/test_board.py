import src.board as board

board = board.Board()

def test_board_created():
    
    assert board.isCreated

def test_board_TopL_notMarked():

    assert board.slots.get("TopL") == " "

def test_board_markingTopL():
    board.mark("TopL", "X")

    assert board.slots.get("TopL") == "X"

def test_board_display():
    output = board.display()
    assert output == 'X| | \n-----\n | | \n-----\n | | '

def test_board_clear():
    output = board.clear()

    assert output == ' | | \n-----\n | | \n-----\n | | '