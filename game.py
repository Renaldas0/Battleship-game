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
