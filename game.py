import random

class GameBoard:
    """
    The GameBoard class is used to create the playing board
    """

    def __init__(self, board):
        self.board = board

    def convert_letters_to_nums():
        letters_to_nums = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,"F": 5,}
        return letters_to_nums

    def print_board(self):
        print("  A B C D E F")
        print("  +-+-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

class Battleships():
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(4):
            self.x_row, self.y_column = random.randint(0, 5), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == 'X':  #while loop to check if there is something placed there
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def get_player_input(self):
        """ Function to validate user input, row must be a number
         between 0 and 5, column must be a letter between A and F according to 
         English Alphabetical order"""
        try:
            x_row = input("Guess the row of enemy ship: ")
            while x_row not in '12345':
                print('Please select a value between 0 and 5')
                x_row = input("Guess the row of enemy ship: ")

            y_column = input('Guess the column letter of enemy ship: ').upper()
            while y_column not in 'ABCDEF':
                print('Please select a value between A,B,C,D,E or F')
                y_column = input('Guess the column letter of enemy ship: ').upper()
            return int(x_row) - 1, GameBoard.convert_letters_to_nums()[y_column]
        except ValueError and KeyError:
            print('Not a valid input')
            return self.get_player_input()

    def count_sunk_ships(self):
        sunk_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    sunk_ships += 1
        return sunk_ships