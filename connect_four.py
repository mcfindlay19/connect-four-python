import sys
sys.stdout.reconfigure(encoding='utf-8')

class Board:
    white = '\U000026AA'
    blue = '\U0001F535'
    red = '\U0001F534'
    # This allows varaible set up of the height and width of the board, and creates a list of all c-oordinates. Each co-ordinate is then 'owned' by white, or no player
    #The co-ordinates of the board mimic the co-ordinates of a computer screen, not graph paper, i.e. top left is 0,0 and it increase left to right, top to bottom
    # The top left co-ordiante (0,0) is added first and is indexed at 0
    # Then the next top row (0, 1) is added and indexed at 1
    # Accessing individual indices is done by multiplying the row we want to find by the width of the board, and adding on the column
    # Example: We want the index of co-ordinate (3,4). We multiply 3 * 7 = 21 + 4 = 25
    # We can see this works by the following mapping of co-ordinates to indices in this standard connect four board:
    # (0,0) (0,1) (0,2) (0,3) (0,4) (0,5) (0,6)
    # (1,0) (1,1) (1,2) (1,3) (1,4) (1,5) (1,6)
    # (2,0) (2,1) (2,2) (2,3) (2,4) (2,5) (2,6)
    # (3,0) (3,1) (3,2) (3,3) (3,4) (3,5) (3,6)
    # (4,0) (4,1) (4,2) (4,3) (4,4) (4,5) (4,6)
    # (5,0) (5,1) (5,2) (5,3) (5,4) (5,5) (5,6)
    # ----------------------------------------- 
    # 0     1     2     3     4     5     6
    # 7     8     9     10    11    12    13
    # 14    15    16    17    18    19    20
    # 21    22    23    24    25    26    27
    # 28    29    30    31    32    33    34
    # 35    36    37    38    39    40    41
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
        if self.check_for_win(player) is True:
            print(player + " is a winner")
    
    def check_for_win(self, player):
        # Check horizontal win
        # Start at the top left of the board, and work across the row. If there is at least 4 in a row, that player wins
        # If no winner, move down a row, and start over.
        # Co-ordinate checking here needs to start at index 0, and increase by 1.
        # The algorithm is iterate through each row, then iterate through each column in that row, then increase the row we look at
        for i in range(self.height): # 0 to 5
            count = 0
            for j in range(self.width): # 0 to 6
                if self.coords[(i*self.width)+j][2] is player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
        #Check vertical win
        # Start at the top left of the board, and work down the column. If there is at least 4 in a row, that player wins
        # If no winner, move over a column, and start over
        # Co-ordinate checking here needs to start at index 0, then 7, 14, 21, 28, 35, and then wrap around to 1
        # The algorithm here is to iterate through each column, and then each row in that column, then increase the column we look at
        for i in range(self.width): # 0 to 6
            count = 0
            for j in range(self.height): # 0 to 5
                if self.coords[(j*self.width)+i][2] is player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
            


blue = '\U0001F535'
red = '\U0001F534'
board = Board()
board.print_board()
print()

board.play_move(0, red)
board.play_move(0, blue)
board.play_move(0, blue)
board.play_move(0, red)
board.play_move(0, red)
board.play_move(0, red)
board.play_move(1, blue)
board.play_move(1, blue)
board.play_move(1, blue)
board.play_move(1, red)
board.play_move(1, red)
board.play_move(1, red)
board.play_move(5, blue)
board.play_move(6, blue)
board.play_move(5, blue)
board.play_move(6, blue)
board.play_move(5, blue)
board.play_move(6, blue)
board.print_board()