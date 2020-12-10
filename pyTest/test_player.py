
import sys

sys.path.insert(1,'Users\tdelg\vsWorkBench\ticTacToe\player.py')

from player import Player

player1 = Player()


def test_player_created():

    assert player1.isCreated


