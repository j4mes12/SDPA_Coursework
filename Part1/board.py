# Import classes from player
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

        ---Parameters---
        n: int
        integer to define board size

        computer: bool
        flag if user wants to play versus a computer
        """

        # Make n a class variable
        self.n = n

        self.default_params = {
            "init_body": {
                "p1": [(0, 0)],
                "p2": [(n - 1, n - 1)],
                "c": [(n - 1, n - 1)],
            },
            "id": {"p1": "1", "p2": "2", "c": "C"},
            "colour": bcolours.WHITE,
        }

        # Create player instances
        print("---Player 1---")
        self.player1 = Player(
            id=self.get_user_id("p1"),
            init_body=self.get_user_body("p1"),
            colour=self.get_user_colour(),
        )

        # If game version is versus a computer, player2 is a Computer instance
        if computer:
            print("---Computer---")

            # Get user personalisations and check they haven't already been chosen
            comp_id, comp_body, comp_colour = self.get_second_user_information("c")
            self.player2 = Computer(id=comp_id, init_body=comp_body, colour=comp_colour)
        else:
            print("---Player 2---")

            # Get user personalisations and check they haven't already been chosen
            p2_id, p2_body, p2_colour = self.get_second_user_information("p2")
            self.player2 = Player(id=p2_id, init_body=p2_body, colour=p2_colour)

        # Define dicitonary to translate between output and board storing symbols.
        self.output_dict = {
            0: " ",
            1: self.player1.colour + self.player1.id + bcolours.END,
            2: self.player2.colour + self.player2.id + bcolours.END,
            "X": self.player1.colour + "X" + bcolours.END,
            "O": self.player2.colour + "0" + bcolours.END,
        }

    def get_user_id(self, player):
        """This method gets the user's chosen ID and makes sure it is suitable:
        check it's length of one, an alphanumeric character or the default.

        ---Parameters---
        player: str
        Player identifier. One of p1, p2 and c for player 1, player 2 and
        computer respectively.

        ---Returns---
        out: str
        single character that is user's chosen ID
        """

        # Loop to ask the user for their input and check it's of the correct type
        while True:
            # Get user input
            id_input = input(
                f"Please Enter ID Character (Any number or letter - Blank for default): "
            )

            # Perform error checks
            if ((id_input.isalnum()) & len(id_input) == 1) | (id_input == ""):
                print("ID Accepted.")
                break
            else:
                print("Invalid ID. Please enter a single character or digit.")

        # Define return value based on if user wants default value
        if id_input == "":
            out = self.default_params["id"][player]
        else:
            out = id_input

        return out

    def get_user_colour(self):
        """This method gets the user's desired output colour and makes sure it's one of the
        menu options or the default value is requested.

        ---Returns---
        out: str
        string to identify what colour the user has chosen."""

        while True:

            # Display colour menu so user can see options
            self.display_colours()

            # Get user's colour selection
            colour_input = input(
                f"Please Enter Player Colour (Any number or letter - Blank for default): "
            )

            # Make sure input is one of the colour options
            if (colour_input in "123456") | (colour_input == ""):
                print("Colour Accepted.")
                break
            else:
                print("Invalid Colour. Please enter a digit from the options.")

        # Define return value
        if colour_input == "":
            out = self.default_params["colour"]
        else:
            # Translate menu options into a colour
            out = bcolours.colour_dictionary[colour_input]

        return out

    def get_user_body(self, player):
        """This method gets the user's desired initial position. It also makes sure the input type
        is in the correct format and digits so we be effectively read in the user's input. We also
        start by displaying the available locations in a grid.

        ---Parameters---
        player: str
        Player identifier. One of p1, p2 and c for player 1, player 2 and
        computer respectively.

        ---Returns---
        out: list
        list of a single tuple of digit coordinates
        """

        while True:

            # Display board for user to choose locations
            self.display_location_board()

            # Get user input
            body_input = input(
                f"Please Enter Start Location (format x,y with digits between 0 and {self.n - 1}): "
            )

            # Check for defaults
            if body_input == "":
                print("Start Location Accepted.")
                break

            body_split = body_input.split(",")

            # Check we have two coordinates
            if len(body_split) == 2:

                # Split input into x and y.
                # Swapping due to difference in what the user would expect and matrix orders
                body_x = body_split[1]
                body_y = body_split[0]

                # Make sure coordinates are digits
                if body_x.isdigit() & body_y.isdigit():
                    body_x = int(body_x)
                    body_y = int(body_y)

                    # Check if coordinates are on board
                    if (0 <= body_x < self.n) & (0 <= body_y < self.n):
                        print("Start Location Accepted.")
                        break
                    else:
                        print(
                            f"Invalid Start Location. Digits must be between 0 and {self.n - 1}"
                        )
            else:
                print(
                    "Invalid Start Location Format. Please enter a two digits in the form x,y."
                )

        if body_input == "":
            out = self.default_params["init_body"][player]
        else:
            out = [(body_x, body_y)]

        return out

    def get_second_user_information(self, player):
        """This method gets the second user/computer's information (id,
        initial body and colour) from the user. We have put this in a method
        so we can check there are no repeated choices. If both users want
        the default colour (white) then that is acceptable.

        ---Paramters---
        player: str
        Player identifier. One of p1, p2 and c for player 1, player 2 and
        computer respectively.

        ---Returns---
        alternate_id: str
        User's desired player id

        alternate_body: str
        User's desired colour

        alternate_colour: str
        User's desired colour"""

        # While loop to get the user's id and check it's not already been taken
        while True:
            alternate_id = self.get_user_id(player)
            if self.player1.id == alternate_id:
                print("ID already taken!")
                continue
            else:
                break

        # While loop to get the user's initial position and check it's not already been taken
        while True:
            alternate_body = self.get_user_body(player)
            if self.player1.body == alternate_body:
                print("Starting Location already taken!")
                continue
            else:
                break

        # While loop to get the user's colour and check it's not already been taken
        while True:
            alternate_colour = self.get_user_colour()
            if alternate_colour != bcolours.WHITE:
                if self.player1.colour == alternate_colour:
                    print("Colour already taken!")
                    continue
            break

        return alternate_id, alternate_body, alternate_colour

    def display_colours(self):
        """This method displays the available colours for the user to decide
        before the game. We loop through the display dictionary printing the
        key and value pairs as a menu."""

        # Loop through dictionary and display colour menu
        print("Available Colours:")
        for k, v in bcolours.display_dictionary.items():
            print(f"\t({k}) {v}")

    def make_board(self):
        """This method creates an empty square list using self.n

        ---Returns---
        board: list
        empty square list, nxn"""

        # Creates empty, square list
        board = [[0] * self.n for _ in range(self.n)]

        return board

    def display_location_board(self):
        """This method displays a board so the user can decide where they want to start."""

        # Prints the column numbers with correct spacing
        print("  ", end="")
        for _ in range(self.n):
            print(_, end=" ")
        print(" ")

        # Prints an empty board starting with the row number
        for i in range(self.n):
            print(f"{i}|", end="")
            for j in range(self.n):
                print(f" |", end="")
            print("")

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

    def print_board(self):
        """This method displays the board aesthetically with pre-defined output symbols."""

        # Makes Board
        board = self.make_board()

        # Calls method to populate board
        self.populate_board(board)

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
        """This method checks if the inputted move is one of L, R, U or D.

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

    def calculate_next_positions_sim(self):
        """This method calculates the next position based on instance directions and head.
        The next position is assigned to the next_position instance variable."""

        # Calculate next position for player 1
        self.player1.next_position = self.calculate_next_position(
            position=self.player1.head(), new_direction=self.player1.direction
        )

        # Calculate next position for player 2
        self.player2.next_position = self.calculate_next_position(
            position=self.player2.head(), new_direction=self.player2.direction
        )

    def check_legal_moves_sim(self):
        """This method checks if the inputted move is one of lrud for both player instances.

        ---Returns---
        result: str
        string identifier that details the outcome of the legailty test. P0 = pass,
        T0 = tie, W1 = player 1 wins, W2 = player 2 wins"""

        result = "P0"

        # Checks if both moves are not legal - results in a tie
        if (not self.check_legal_move(self.player1.in_value)) & (
            not self.check_legal_move(self.player2.in_value)
        ):
            result = "T0"

        # Checks if player 2 is illegal and player 1 is legal - results in W1
        elif (self.check_legal_move(self.player1.in_value)) & (
            not self.check_legal_move(self.player2.in_value)
        ):
            result = "W1"

        # Checks if player 1 is illegal and player 2 is legal - results in W2
        elif (not self.check_legal_move(self.player1.in_value)) & (
            self.check_legal_move(self.player2.in_value)
        ):
            result = "W2"

        return result

    def check_legal_positions_sim(self):
        """This method checks if position is within the board and not a player's past
        move for both players simultaneously. Heavily uses the check_legal_position method.

        ---Returns---
        result: str
        string identifier that details the outcome of the legailty test. P0 = pass,
        T0 = tie, W1 = player 1 wins, W2 = player 2 wins"""

        # Initialse result to default on a pass
        result = "P0"

        # Checks if both positions are not legal - results in a tie
        if (not self.check_legal_position(self.player1.next_position)) & (
            not self.check_legal_position(self.player2.next_position)
        ) | (self.player1.next_position == self.player2.next_position):
            result = "T0"

        # Checks if player 2 is illegal and player 1 is legal - results in W1
        elif (self.check_legal_position(self.player1.next_position)) & (
            not self.check_legal_position(self.player2.next_position)
        ):
            result = "W1"

        # Checks if player 1 is illegal and player 2 is legal - results in W2
        elif (not self.check_legal_position(self.player1.next_position)) & (
            self.check_legal_position(self.player2.next_position)
        ):
            result = "W2"

        return result


class bcolours:
    """This class stores the colour information strings, a dictionary to print
    the colours aesthetically and a dictionary to store the available colours."""

    # End string
    END = "\033[0m"

    # Colour Strings
    WHITE = "\033[97m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[36m"
    MAGENTA = "\033[95m"

    # Display dictionary
    display_dictionary = {
        "1": "WHITE",
        "2": GREEN + "GREEN" + END,
        "3": YELLOW + "YELLOW" + END,
        "4": BLUE + "BLUE" + END,
        "5": MAGENTA + "MAGENTA" + END,
        "6": RED + "RED" + END,
    }

    # Colour dictionary
    colour_dictionary = {
        "1": WHITE,
        "2": GREEN,
        "3": YELLOW,
        "4": BLUE,
        "5": MAGENTA,
        "6": RED,
    }
