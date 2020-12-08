import sys

sys.path.insert(1,'Users\tdelg\vsWorkBench\ticTacToe\main.py')

from main import play

def test_play_Y():
    wantToPlay = play("Y")
    assert wantToPlay

def test_play_N():
    wantToPlay = play("N")
    assert not wantToPlay

