import sys
import copy
import math
import random

sys.stdout.reconfigure(encoding='utf-8')

class Board:
    white = '\U000026AA'
    blue = '\U0001F535'
    red = '\U0001F534'
    player1_name = ''
    player2_name = ''
    first_player = 0

    
    def __init__(self, rows = 6, columns = 7) -> None:
        self.columns = columns
        self.rows = rows
        self.number_of_moves = 0
        self.max_moves = self.columns * self.rows
        self.coords = []
        list_item = []
        
        for column in range(columns):
            list_item.append(self.white)
                
        for row in range(rows):
            copylist = copy.deepcopy(list_item)
            self.coords.append(copylist)
    
    def __repr__(self) -> str:
        return str(self.coords)
    
    def print_board(self):
        for r in range(self.rows):
            for c in range(self.columns):
                if c is (self.columns-1):
                    print(self.coords[r][c], end='')
                    print()
                else:
                    print(self.coords[r][c], end='')

    def get_valid_moves(self):
        valid_columns = []
        for column in range(self.columns):
            if self.coords[0][column] is self.white:
                valid_columns.append(column)
        return valid_columns
    
    def play_move(self, player, selection):
        for row in self.coords:
            if row[selection] is self.white:
                row_to_change = row
        row_to_change[selection] = player
        self.number_of_moves += 1
        
    def check_for_win(self, player):
        # Check horizontal for wins
        for c in range(self.columns - 3):
            for r in range(self.rows):
                if self.coords[r][c] == player and self.coords[r][c+1] == player and self.coords[r][c+2] == player and self.coords[r][c+3] == player:
                    return True
        
        # Check veritcal for wins
        for c in range(self.columns):
            for r in range(self.rows - 3):
                if self.coords[r][c] == player and self.coords[r+1][c] == player and self.coords[r+2][c] == player and self.coords[r+3][c] == player:
                    return True
        
        # Check for positively sloped wins
        for c in range(self.columns- 3 ):
            for r in range(self.rows - 3):
                if self.coords[r][c] == player and self.coords[r+1][c+1] == player and self.coords[r+2][c+2] == player and self.coords[r+3][c+3] == player:
                    return True
        
        # Check for negatively sloped wins
        for c in range(self.columns - 3):
            for r in range(self.rows):
                if self.coords[r][c] == player and self.coords[r-1][c+1] == player and self.coords[r-2][c+2] == player and self.coords[r-3][c+3] == player:
                    return True
    
    def check_for_tie(self):
        if self.number_of_moves == self.max_moves:
            return True
    
    def reset_board(self):
        self.number_of_moves = 0
        for r in range(self.rows):
            for c in range(self.columns):
                self.coords[r][c] = self.white


def main_screen(board):
    print("Welcome to Connect 4!")
    board.player1_name = input("Please enter your name: ")
    print("Please choose if you want to play against AI (1) or another person (2)")
    player = input("Enter selection: ")
    while (player != '1' and player != '2'):
        print("You did not enter in a valid selection. Please try again.")
        player = input("Enter selection: ")
    if player == '1':
        board.player2_name = "The AI"
    else:
        board.player2_name = input("Please enter the name of the second player: ")
        
    print("{name1} has chosen to play against {name2}!".format(name1 = board.player1_name, name2 = board.player2_name))
    board.first_player = input("Do you want to go first (1) or second (2): ")
    if board.first_player == '2':
        tmp = board.player2_name
        board.player2_name = board.player1_name
        board.player1_name = tmp
        
def game_play(board):
    first_player = board.red
    first_player_name = board.player1_name
    second_player = board.blue
    second_player_name = board.player2_name
    active_player = [first_player, first_player_name]
    
    
    game_over = False
    board.print_board()

    while not game_over:
        print("It is your move {current}".format(current = active_player[1]))
        print("Valid moves are {moves}".format(moves = board.get_valid_moves()))
        
        
        if active_player[1] == 'The AI':
            board.play_move(active_player[0], random_AI(board))
        
        else:    
            str_move = input("Please enter the column you wish to play: ")
            move = int(str_move)
            while move not in board.get_valid_moves():
                print("That is not a valid choice. Please choose again.")
                str_move = input("Please enter the column you wish to play: ")
                move = int(str_move)
            board.play_move(active_player[0], move)
            
        board.print_board()
        
        if board.check_for_win(active_player[0]):
            game_over = True
            print("CONGRATULATIONS {player}. YOU WON!".format(player = active_player[1]))

        if board.check_for_tie():
            game_over = True
            print("It's a tie!")
            
        if active_player == [first_player, first_player_name]:
            active_player = [second_player, second_player_name]

        else:
            active_player = [first_player, first_player_name]


def random_AI(board):
    return random.choice(board.get_valid_moves())
    
def score_position(board, player):
    pass


board = Board()
blue = '\U0001F535'
red = '\U0001F534'

main_screen(board)
game_play(board)