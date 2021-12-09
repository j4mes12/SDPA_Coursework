from player import Player, Computer


class Board:

    direction_dict = {"l": (0, -1), "r": (0, 1), "u": (-1, 0), "d": (1, 0)}

    def __init__(self, n, computer=False):
        self.player1 = Player(init_body=[(0, 0)], init_direction="r")

        if computer:
            self.player2 = Computer(init_body=[(n - 1, n - 1)], init_direction="l")
        else:
            self.player2 = Player(init_body=[(n - 1, n - 1)], init_direction="l")
        self.n = n

        self.output_dict = {0: " ", 1: self.player1.id, 2: self.player2.id, "X": "X"}

    def make_board(self):

        board = [[0] * self.n for _ in range(self.n)]

        for body1 in self.player1.body:
            board[body1[0]][body1[1]] = "X"

        for body2 in self.player2.body:
            board[body2[0]][body2[1]] = "X"

        p1_head = self.player1.head()
        p2_head = self.player2.head()

        board[p1_head[0]][p1_head[1]] = 1
        board[p2_head[0]][p2_head[1]] = 2

        return board

    def print_board(self):

        board = self.make_board()

        print("#" * (2 * self.n + 3))

        for i in range(self.n):
            print("#|", end="")
            for j in range(self.n):
                print(f"{self.output_dict[board[i][j]]}|", end="")
            print("#")

        print("#" * (2 * self.n + 3))

    def next_position(self, position, new_direction):
        step = self.direction_dict[new_direction]
        return ((position[0] + step[0]), (position[1] + step[1]))

    def check_legal_move(self, move):
        return (move in "lrud") & (len(move) == 1)

    def check_legal_position(self, position):
        no_cross = position not in (self.player2.body + self.player1.body)
        in_board_x = 0 <= position[0] <= self.n - 1
        in_board_y = 0 <= position[1] <= self.n - 1
        return no_cross & in_board_x & in_board_y
