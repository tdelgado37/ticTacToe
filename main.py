import board

def play(input = "Y"):
    if(input is None):
        wantToPlay = input("Want to play a game: ")
    else:
        wantToPlay = input
    return wantToPlay == "Y"
def main():
    play()
    Board()


if __name__ == "__main__":
    pass