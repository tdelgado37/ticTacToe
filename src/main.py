import src.player as player
import src.board as board

def play(input = "Y"):
    if(input is None):
        wantToPlay = input("Want to play a game: ")
    else:
        wantToPlay = input
    return wantToPlay == "Y"
def main():
    play()
    board.Board()


if __name__ == "__main__":
    pass