class Board:
    def __init__(self):
        self.isCreated = True
        self.slots = {"TopL": " ", "TopM": " ", "TopR": " ",
            "MiddleL": " ", "MiddleM":" ", "MiddleR":" ",
            "BottomL": " ", "BottomM":" ", "BottomR": " "}

    #TODO: add in logic to handle invalid positions on the board
    def mark(self, slotKey, marking):
        if(slotKey not in self.slots.keys()):
            print(slotKey + " invaild position...LOSE turn!")
        else:
            self.slots[slotKey] = marking
    
    def display(self) -> str:
        topLine = self.slots.get("TopL")+"|"+self.slots.get("TopM")+"|"+self.slots.get("TopR")
        midLine = self.slots.get("MiddleL")+"|"+self.slots.get("MiddleM")+"|"+self.slots.get("MiddleR")
        botLine = self.slots.get("BottomL")+"|"+self.slots.get("BottomM")+"|"+self.slots.get("BottomR")
        breakLine = "-----"
        return '{0}\n{3}\n{1}\n{3}\n{2}'.format(topLine, midLine, botLine, breakLine)

    def clear(self) -> str:
        for key in self.slots:
            self.slots[key] = " "
        return self.display()
    
    