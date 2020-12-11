class Board:
    def __init__(self):
        self.isCreated = True
        self.slots = {"TopL": " ", "TopM": " ", "TopR": " ",
            "MiddleL": " ", "MiddleM":" ", "MiddleR":" ",
            "BottomL": " ", "BottomM":" ", "BottomR": " "}

    def mark(self, slotKey, marking):
        newValue = {slotKey: marking}
        self.slots.update(newValue)
    
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
    
    