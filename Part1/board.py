class Board:
    def __init__(self, p1_position, p2_position, board_size):
        self.p1_position = p1_position
        self.p2_position = p2_position
        self.board_size = board_size

    def print_board(self, board_size):
        print("board")

    def execute_move(self, player, move):
        print("player has moved")
