class Player:
    
    def __init__(self, mark):
        self.isCreated = True
        self.isTurn = False
        self.marking = mark

    def take_turn(self, board, position=None):
        if self.isTurn and position is None:
            position = input("Please select position to mark: ")
        board.mark(position, self.marking)



    

    

