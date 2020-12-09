import sys
from sys import stderr

sys.path.insert(1,'Users\tdelg\vsWorkBench\ticTacToe\board.py')

from board import Board

board = Board()

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