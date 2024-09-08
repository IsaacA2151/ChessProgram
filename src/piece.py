# Player 0 = White 1 = Black

class Piece:

    def __init__(self,spriteFn,player,coord):
        self.sprite = spriteFn
        self.player = player
        self.coord = coord

    def checkMove(self, destination):
        pass