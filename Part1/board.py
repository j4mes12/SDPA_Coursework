from player import Player


class Board:
    def __init__(self, n):
        self.player1 = Player(init_body=[(0, 0)], init_direction="R")
        self.player2 = Player(init_body=[(n, n)], init_direction="L")
        self.n = n

    def make_board(self):

        board = [[0] * self.n for _ in range(self.n)]

        board[self.player1.head[0]][self.player1.head[1]] = "1"
        board[self.player2.head[0]][self.player2.head[1]] = "2"

        for p1, p2 in zip(self.player1.body[1:], self.player2.body[1:]):
            board[p1[0]][p1[1]] = "1"
            board[p2[0]][p2[1]] = "2"

        return board

    def print_board(self):

        board = self.make_board()

        print("#" * (2 * self.n + 3))

        for i in range(self.n):
            print("#|", end="")
            for j in range(self.n):
                if board[i][j] == 0:
                    out = " "
                else:
                    out = board[i][j]
                print(f"{out}|", end="")
            print("#")

        print("#" * (2 * self.n + 3))

    def next_position(self, position, step):
        return ((position[0] + step[0]), (position[1] + step[1]))
