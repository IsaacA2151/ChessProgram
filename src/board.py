class Board:
    def __init__(self, size=8):
        self.size = size
        self.board = []

    def makeStandardBoard(self):
        self.board = [[[] for k in range(self.size)] for i in range(self.size)]


b = Board()
b.makeStandardBoard()

print(b.board)