import sys
sys.stdout.reconfigure(encoding='utf-8')

class Board:
    white = '\U000026AA'
    blue = '\U0001F535'
    red = '\U0001F534'

    def  __init__(self, width = 7, height = 6):
        self.width = width
        self.height = height
        self.coords = []
        for row in range(self.height):
            for column in range(self.width):
                self.coords.append([row, column, self.white])
    def __repr__(self):
        return str(self.coords)

    def print_board(self):
        for coord in self.coords:
            if coord[1] is 6:
                print(coord[2], end= '')
                print()
            else:
                print(coord[2], end= '')


    def get_valid_moves(self):
        valid_columns = []
        for i in range(self.width):
            if self.coords[i][2] is self.white:
                valid_columns.append(i)
        return valid_columns
        
    def play_move(self, selection, player):
        if selection in self.get_valid_moves():
            coord_to_change = [selection]
            for i in range(selection, self.width*self.height, self.width):
                if self.coords[i][2] is self.white:
                    coord_to_change = self.coords[i]
            i = self.coords.index(coord_to_change)
            self.coords[i][2] = player
        else:
            print("Please choose a different column")

blue = '\U0001F535'
red = '\U0001F534'
board = Board()