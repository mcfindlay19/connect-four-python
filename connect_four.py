import sys
sys.stdout.reconfigure(encoding='utf-8')

class Board:
    width = 8
    height = 4
    white_circle = '\U000026AA'
    blue_circle = '\U0001F535'
    red_circle = '\U0001F534'

    def print_board(self):
        for i in range(self.height):
            for i in range(self.width):
                print(self.white_circle, end='')
            print()


board = Board()
board.print_board()
