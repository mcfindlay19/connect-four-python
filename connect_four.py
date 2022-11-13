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
        # Width and height have a default. Everything else is tied to the height and width of the board
        self.width = width
        self.height = height
        self.coords = []
        # Need a list of co-ords for easy checking. This is stored as a list of indices to quickly run through to find if a move is winning
        # left_to_right is a list of indices of the top row and left most column. This is needed for any diagonal where the x and y axis are positively linked
        # right_to_left is a list of indices of the top row and right most column. This is needed for any diagonal where the x and y axis are negatively linked
        self.indicies_to_check_left_to_right = []
        self.indicies_to_check_right_to_left = []
        for row in range(self.height):

            for column in range(self.width):
                list_item = [row, column, self.white]
                self.coords.append(list_item)

                # Get all indices of the top row and append them to both diagonal lists
                if row == 0:
                    self.indicies_to_check_left_to_right.append(self.coords.index(list_item))
                    self.indicies_to_check_right_to_left.append(self.coords.index(list_item))

                # Get all indices of the left most column, and if they aren't already addto the list, add them. This is only the case for (0, 0)
                if column == 0:

                    if self.coords.index(list_item) not in self.indicies_to_check_left_to_right:
                        self.indicies_to_check_left_to_right.append(self.coords.index(list_item))

                # Get all indices of the right most column, and if they aren't already addto the list, add them. This is only the case for (0, width - 1)
                if column == self.width-1:
                    
                    if self.coords.index(list_item) not in self.indicies_to_check_right_to_left:
                        self.indicies_to_check_right_to_left.append(self.coords.index(list_item))

    
    def __repr__(self):
        # Simplest way to visualize the class
        return str(self.coords)

    def print_board(self):
        # Runs through the list of coordinates. If the coordinate is the last column, print a new line as well
        for coord in self.coords:

            if coord[1] is (self.width-1):
                print(coord[2], end= '')
                print()

            else:
                print(coord[2], end= '')


    def get_valid_moves(self):
        # If the column has the top row available, then you must be able to place at least one toekn in that column
        valid_columns = []
        for i in range(self.width):

            if self.coords[i][2] is self.white:
                valid_columns.append(i)

        return valid_columns
        
    def play_move(self, selection, player):
        # Check to ensure the move is legal, and then find the lowest possible row it can belong, and change the owner of that tile from neutral to a colour
        if selection in self.get_valid_moves():
            coord_to_change = [selection]

            for i in range(selection, self.width*self.height, self.width):

                if self.coords[i][2] is self.white:
                    coord_to_change = self.coords[i]

            i = self.coords.index(coord_to_change)
            self.coords[i][2] = player

        # If that isn't a valid choice, let the player know
        else:
            print("Please choose a different column")
        
        # Check for a win after every move
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
                index = (i * self.width) + j

                if self.coords[index][2] is player:
                    count += 1

                    if count == 4:
                        return True

                else:
                    count = 0

        # Check vertical win
        # Start at the top left of the board, and work down the column. If there is at least 4 in a row, that player wins
        # If no winner, move over a column, and start over
        # Co-ordinate checking here needs to start at index 0, then 7, 14, 21, 28, 35, and then wrap around to 1
        # The algorithm here is to iterate through each column, and then each row in that column, then increase the column we look at
        for i in range(self.width): # 0 to 6
            count = 0

            for j in range(self.height): # 0 to 5
                index = (j * self.width) + i

                if self.coords[index][2] is player:
                    count += 1

                    if count == 4:
                        return True

                else:
                    count = 0

        # Check through all the possible diagonal start locations for going left to right.
        # Each check needs to increase index by 8 i.e. 1 more then board width
        # If we are checking the last column, or the bottom row, stop increasing index
        # Indices of the diagonals going left to right for reference of a standard connect four board:
        # 0  8  16 24 32 40
        # 1  9  17 25 33 41
        # 2  10 18 26 34
        # 3  11 19 27
        # 7  15 23 31 39
        # 14 22 30 38

        # Run through list of all possible diagonals starting indices
        for i in self.indicies_to_check_left_to_right:
            count = 0

            # Run through each diagonal up to height. This ensures we cover every diagonal, but this could end up in overflow, so we need to make sure the index is within bounds
            for j in range(self.height):
                index  = i + (j * (self.width + 1))

                # Ensure the index is in bounds
                if index <= len(self.coords)-1:

                    # Check to see if the coordinate we are checking is on the bottom row. If it is, check if there is a winner. If there is no winner, stop trying to look as there can't be anything below this row
                    if self.coords[index][0] is (self.height-1):

                        if self.coords[index][2] is player:
                            count +=1

                            if count == 4:
                                return True

                        else:
                            count = 0
                            break

                    # Check to see if the coordinate we are checking is on the right most column. If it is, check if there is a winner. If there is no winner, stop trying to look as there can't be anything to the right of this column
                    if self.coords[index][1] is (self.width-1):

                        if self.coords[index][2] is player:
                            count +=1

                            if count == 4:
                                return True

                        else:
                            count = 0
                            break

                    # If the coordinate is not the bottom row or right column, just continue checking like normal
                    else:
                        if self.coords[index][2] is player:
                            count +=1

                            if count == 4:
                                return True

                        else:
                            count = 0

        # Check through all the possible diagonal start locations for going right to left.
        # Each check needs to increase index by 6 i.e. 1 less then board width
        # If we are checking the first column, or the bottom row, stop increasing index
        # Indices of the diagonals going right to left for reference of a standard connect four board:
        # 3  9  15 21
        # 4  10 16 22 28
        # 5  11 17 23 29 35
        # 6  12 18 24 30 36
        # 13 19 25 31 37
        # 20 26 32 38

        # Run through list of all possible diagonals starting indices
        for i in self.indicies_to_check_right_to_left:
            count = 0

            # Run through each diagonal up to height. This ensures we cover every diagonal, but this could end up in overflow, so we need to make sure the index is within bounds
            for j in range(self.height):
                index  = i + (j*(self.width-1))

                # Ensure the index is in bounds
                if index <= len(self.coords)-1:

                    # Check to see if the coordinate we are checking is on the bottom row. If it is, check if there is a winner. If there is no winner, stop trying to look as there can't be anything below this row
                    if self.coords[index][0] is (self.height-1):

                        if self.coords[index][2] is player:
                            count +=1

                            if count == 4:
                                return True

                        else:
                            count = 0
                            break

                    # Check to see if the coordinate we are checking is on the left most column. If it is, check if there is a winner. If there is no winner, stop trying to look as there can't be anything to the left of this column
                    if self.coords[index][1] is (0):

                        if self.coords[index][2] is player:
                            count +=1

                            if count == 4:
                                return True

                        else:
                            count = 0
                            break

                    # If the coordinate is not the bottom row or right column, just continue checking like normal
                    else:
                        if self.coords[index][2] is player:
                            count +=1

                            if count == 4:
                                return True

                        else:
                            count = 0


blue = '\U0001F535'
red = '\U0001F534'
board = Board()
board.print_board()
