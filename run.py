import random


class GameBoard:
    """
    The GameBoard class is used to create the playing board
    """
    def __init__(self, board):
        self.board = board

    def convert_letters_to_nums():
        """
        Function to convert letters to numbers for the columns
        """
        letters_to_nums = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return letters_to_nums

    def print_board(self):
        """
        Function creating the layout of the board, sets 1-5,A-E
        and the divider that also acts as a guide to columns.
        """
        print("  A B C D E")
        print("  +-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleships():
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        """
        Function that creates the ships on computers board and
        sets them to random locations between
        index 0 and 4.
        """
        for i in range(4):
            self.x_row, self.y_column = random.randint(0, 4), random.randint(0, 4)
            while self.board[self.x_row][self.y_column] == 'X':
                self.x_row, self.y_column = random.randint(0, 4), random.randint(0, 4)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def get_player_input(self):
        """ Function to validate user input, row must be a number
         between 1 and 5, column must be a letter between A and E according to
         English Alphabetical order"""
        try:
            x_row = input("Guess the row of enemy ship 1-5:\n")
            while x_row not in '12345':
                print('Please select a value between 1 and 5')
                x_row = input("Guess the row of enemy ship 1-5:\n ")

            y_column = input('Guess the column letter of enemy ship A-E:\n ').upper()
            while y_column not in 'ABCDE':
                print('Please select a value between A,B,C,D,E')
                y_column = input('Guess the column letter of enemy ship A-E:\n ').upper()
            return int(x_row) - 1, GameBoard.convert_letters_to_nums()[y_column]
        except ValueError and KeyError:
            print('Not a valid input')
            return self.get_player_input()

    def count_sunk_ships(self):
        """Track the number of ships that have been hit and sunk"""
        sunk_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    sunk_ships += 1
        return sunk_ships


def StartGame():
    """
    Main function that runs the game, controls turn countdown,
    checks if guess is valid or has already been guessed there and
    marks down where an area was guessed.
    """
    computers_board = GameBoard([[" "] * 5 for i in range(5)])
    players_board = GameBoard([[" "] * 5 for i in range(5)])
    Battleships.create_ships(computers_board)

    # start 10 guess counter
    turns = 10
    while turns > 0:
        GameBoard.print_board(players_board)
        # get player input
        player_x_row, player_y_column = Battleships.get_player_input(object)
        # check if value was already guessed
        while players_board.board[player_x_row][player_y_column] == "-" or players_board.board[player_x_row][player_y_column] == "X":
            print("You already guessed here")
            player_x_row, player_y_column = Battleships.get_player_input(object)
        # check if a ship is hit or missed
        if computers_board.board[player_x_row][player_y_column] == "X":
            print('You sunk and enemy battleship!\n')
            players_board.board[player_x_row][player_y_column] = "X"
        else:
            print('You missed my battleship!\n')
            players_board.board[player_x_row][player_y_column] = "-"
        # check if you have won or lost
        if Battleships.count_sunk_ships(players_board) == 4:
            print('Congradulations, You have destroyed all enemy battleships!')
            break
        else:
            turns -= 1
            print(f"You have {turns} turns remaining!")
            if turns == 0:
                print('You ran out of ammo to shoot')
                GameBoard.print_board(players_board)
                break

print('Welcome to Battleships!!')
print('-' * 25)
print('You have 10 guesses to destroy enemy ships')
print('Press enter twice to exit the game')
print('Row ranges from 1 - 5')
print('Column ranges from A to E')
print('-' * 25)


if __name__ == '__main__':
    StartGame()
