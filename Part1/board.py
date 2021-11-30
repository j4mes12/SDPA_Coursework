import numpy as np


class Board:
    def __init__(self, p1_position, p2_position, n):
        self.p1_position = p1_position
        self.p2_position = p2_position
        self.n = n

    def print_board(self, n):
        self.board = np.zeros(shape=(n, n)).astype(int)
        self.board[0, 0] = "1"
        self.board[-1, -1] = "2"

        for i in range(n):
            print("#|", end="")
            for j in range(n):
                if self.board[i, j] == 0:
                    out = " "
                else:
                    out = self.board[i, j]
                print(f"{out}|", end="")
            print("#")

    def execute_move(self, player, move):
        print("player has moved")
