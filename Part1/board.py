class Board:
    def __init__(self, n):
        self.p1 = [(0, 0)]
        self.p2 = [(-1, -1)]
        self.n = n

    def make_board(self):

        board = [[0] * self.n for _ in range(self.n)]

        board[self.p1[-1][0]][self.p1[-1][0]] = "1"
        board[-1][-1] = "2"

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

    def execute_move(self, player, move):
        print("player has moved")
