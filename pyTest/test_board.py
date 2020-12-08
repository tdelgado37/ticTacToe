import sys

sys.path.insert(1,'Users\tdelg\vsWorkBench\ticTacToe\board.py')

from board import Board

board = Board()

def test_board_created():
    
    assert board.isCreated

# def test_board_marked():

#     assert board.slots.topL is not None