from player import Player, Computer


class Board:
    """This Class is responsible for controlling the game. It creates the instances
    for each player and contains methods regarding the board, calculating next
    positions and checking legality of moves/positions.
    """

    # Define dictionaries related to directions to translate between vectors and letters.
    direction_dict = {"l": (0, -1), "r": (0, 1), "u": (-1, 0), "d": (1, 0)}
    opposite_direction = {"l": "r", "r": "l", "u": "d", "d": "u"}

    def __init__(self, n, computer=False):
        """This method initialises the class and creates the players for the game.

        ---Paramters---
        n: int
        integer to define board size

        computer: bool
        flag if user wants to play versus a computer
        """

        # Make n a class variable
        self.n = n

        # Create player instances
        self.player1 = Player(init_body=[(0, 0)], init_direction="r", id=1)

        if computer:
            self.player2 = Computer(
                init_body=[(n - 1, n - 1)], init_direction="l", id="C"
            )
        else:
            self.player2 = Player(init_body=[(n - 1, n - 1)], init_direction="l", id=2)

        # Define dicitonary to translate between output and board storing symbols.
        self.output_dict = {
            0: " ",
            1: self.player1.id,
            2: self.player2.id,
            "X": "X",
            "O": "O",
        }

    def populate_board(self, board):
        """This method populates the board with the current body and head for each player.

        ---Parameters---
        board: list
        square list of zeros"""

        # Fill board with past locations for each player
        for body1 in self.player1.body:
            board[body1[0]][body1[1]] = "X"

        for body2 in self.player2.body:
            board[body2[0]][body2[1]] = "O"

        # Fill board with current location for each player
        p1_head = self.player1.head()
        p2_head = self.player2.head()

        board[p1_head[0]][p1_head[1]] = 1
        board[p2_head[0]][p2_head[1]] = 2

    def make_board(self):
        """This method creates an empty square list using self.n and populates it using variables
        in each player instance.

        ---Returns---
        board: list
        square list filled in for each player"""

        # Creates empty, square list
        board = [[0] * self.n for _ in range(self.n)]

        # Calls method to populate board
        self.populate_board(board)

        return board

    def print_board(self):
        """This method displays the board aesthetically with pre-defined output symbols."""

        # Makes Board
        board = self.make_board()

        # Print initial border
        print("#" * (2 * self.n + 3))

        # Loops through the board and prints each point with symbols to break the board up
        for i in range(self.n):
            print("#|", end="")
            for j in range(self.n):
                print(f"{self.output_dict[board[i][j]]}|", end="")
            print("#")

        # Print final border
        print("#" * (2 * self.n + 3))

    def calculate_next_position(self, position, new_direction):
        """This method calculates the next position based on the entered direction and current position.

        ---Paramters---
        position: set
        set of length two that describes the current location
        new_direction: str
        string that describes in which direction a step is taking place

        ---Returns---
        next_position: set
        set of length two that describes next location"""

        # Use direction dictionary to turn new_direction into a vector
        step = self.direction_dict[new_direction]

        # Calculate the next position using vector addition
        next_position = ((position[0] + step[0]), (position[1] + step[1]))

        return next_position

    def check_legal_move(self, move):
        """This method checks if the inputted move is one of lrud.

        ---Paramters---
        move: str
        player move

        ---Returns---
        lrud & single_character: bool
        boolean to describe if move is one of l, r, u or d' and just one character"""

        # Checks if move is one of l, r, u or d
        lrud = move in "lrud"

        # Checks if move is one character
        single_character = len(move) == 1

        return lrud & single_character

    def check_legal_position(self, position):
        """This method checks if position is within the board and not a player's past move.

        ---Parameters---
        position: set
        set of length two that describes a position.

        ---Returns---
        no_cross & in_board_x & in_board_y: bool
        boolean that verifies position has not been previously used and is within the board in both x and y directions"""

        # Checks if position has not been previously used by a player
        no_cross = position not in (self.player2.body + self.player1.body)

        # Checks if position is in the board in x direction
        in_board_x = 0 <= position[0] <= self.n - 1

        # Checks if position is in board in y direction
        in_board_y = 0 <= position[1] <= self.n - 1

        return no_cross & in_board_x & in_board_y
