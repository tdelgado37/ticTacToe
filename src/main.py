import player as player
import board as board

def play(input = "Y"):
    if(input is None):
        wantToPlay = input("Want to play a game: ")
    else:
        wantToPlay = input
    return wantToPlay == "Y"

def checkForWinner(turnsTaken,gameBoard):
    win = False
    winner = ""
    rowWins = [["BottomL", "BottomM","BottomR"], ["MiddleL", "MiddleM", "MiddleR"], ["TopL", "TopM", "TopR"]]
    vertWins = [["BottomL", "MiddleL", "TopL"],["BottomM", "MiddleM", "TopM"],["BottomR", "MiddleR", "TopR"]]
    diagonalWins = [["BottomL", "MiddleM", "TopR"], ["BottomR", "MiddleM", "TopL"]]

    if (turnsTaken >= 3):
        allWins =  [rowWins, vertWins, diagonalWins]
        for wayToWin in allWins:
            for combination in wayToWin:
                mark = gameBoard.slots[combination[0]]
                win, winner = checkWinningCombination(combination, mark,gameBoard)
                if win:
                    return win,winner

        
    return win, winner

def checkWinningCombination(combination, mark,gameBoard):
    win = False
    winner = ""
    if (mark == "X" or mark == "O"):
            for position in combination:
                if gameBoard.slots[position] == mark:
                    continue
                else:
                    break
            else:
                win = True
                if(mark == "X"):
                    winner = "player1"
                else:
                    winner = "player2"
    return win, winner

def main():

    print("Welcome to Tic Tac Toe")
    while play(input("Want to play a game? ")):

        gameBoard = board.Board()
        print("You have started a new game!\n" + gameBoard.display())
        player1 = player.Player("X")
        player2 = player.Player("O")
        turnsTaken = 0
        isWinner = False

        while not isWinner:
            turnsTaken += 1
            player1Move = input("Player1's move, please enter move: ")
            player1.take_turn(gameBoard, player1Move)
            print(gameBoard.display())
            isWinner, winner = checkForWinner(turnsTaken, gameBoard)
            if not isWinner:
                player2Move = input("Player2's move, please enter move: ")
                player2.take_turn(gameBoard, player2Move)
                print(gameBoard.display())
                isWinner, winner = checkForWinner(turnsTaken, gameBoard)
        print(winner + " has won the game!")

if __name__ == "__main__":
    main()