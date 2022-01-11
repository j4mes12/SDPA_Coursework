"""
Name: James Stephenson
Section: Part 1
Description: This script houses the Board class which controls
the Tron game for Part1. It creates and houses the player
instances and contains methods to control the board.
"""

# Import classes from player
from player import Player, Computer


class Board:
    """This Class is responsible for controlling the game. It creates the instances
    for each player and contains methods regarding the board, calculating next
    positions and checking the legality of moves/positions.
    """

    def __init__(self, n, computer=False):
        """This method initialises the class and creates the players for the game.

        ---Parameters---
        n: int
        integer to define board size

        computer: bool
        flag if the user wants to play versus a computer
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

        # If versus a computer, player2 is a Computer instance
        if computer:
            print("---Computer---")

            # Get user personalisations and check for repeats
            comp_id, comp_body, comp_colour = self.get_second_user_information(
                "c"
            )
            self.player2 = Computer(
                id=comp_id, init_body=comp_body, colour=comp_colour
            )
        else:
            print("---Player 2---")

            # Get user personalisations and check for repeats
            p2_id, p2_body, p2_colour = self.get_second_user_information("p2")
            self.player2 = Player(
                id=p2_id, init_body=p2_body, colour=p2_colour
            )

        # Define dicitonary to translate to board display
        self.output_dict = {
            0: " ",
            1: bcolours.colour_text(self.player1.id, self.player1.colour),
            2: bcolours.colour_text(self.player2.id, self.player2.colour),
            "X": bcolours.colour_text("X", self.player1.colour),
            "O": bcolours.colour_text("O", self.player2.colour),
        }

    def get_user_id(self, player):
        """This method gets the user's chosen ID and makes sure it is suitable:
        check it is of length one, an alphanumeric character or the default.

        ---Parameters---
        player: str
        Player identifier. One of p1, p2 and c for player 1, player 2 and
        computer respectively.

        ---Returns---
        out: str
        a single character that is the user's chosen ID
        """

        # Loop to ask the user for their input and error check
        while True:
            # Get user input
            id_input = input(
                """Please Enter ID Character
                (Any number or letter - Blank for default): """
            )

            # Perform error checks
            if ((id_input.isalnum()) & len(id_input) == 1) | (id_input == ""):
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
        """This method gets the user's desired output colour and makes
        sure it's one of the menu options or the default value is requested.

        ---Returns---
        out: str
        string to identify what colour the user has chosen."""

        while True:

            # Display colour menu so user can see options
            self.display_colours()

            # Get user's colour selection
            colour_input = input(
                """Please Enter Player Colour
                (Any number or letter - Blank for default): """
            )

            # Make sure input is one of the colour options
            if (colour_input in "123456") | (colour_input == ""):
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
        """This method gets the user's desired initial position.
        It also makes sure the input type is in the correct format
        and that they are digits. This is so we can effectively
        read in the user's input. We also start by displaying the
        available locations in a grid.

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
                f"""Please Enter Start Location
                (format x,y with digits between 0 and {self.n - 1}): """
            )

            # Check for defaults
            if body_input == "":
                break

            body_split = body_input.split(",")

            # Check we have two coordinates
            if len(body_split) == 2:

                # Split input into x and y
                body_x = body_split[1]
                body_y = body_split[0]

                # Make sure coordinates are digits
                if body_x.isdigit() & body_y.isdigit():
                    body_x = int(body_x)
                    body_y = int(body_y)

                    # Check if coordinates are on board
                    if (0 <= body_x < self.n) & (0 <= body_y < self.n):
                        break
                    else:
                        print(
                            f"""Invalid Start Location.
                            Digits must be between 0 and {self.n - 1}"""
                        )
            else:
                print(
                    """Invalid Start Location Format.
                    Please enter two digits in the form x,y."""
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

        ---Parameters---
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

        # While loop to get the user's initial position and check for repeats
        while True:
            alternate_body = self.get_user_body(player)
            if self.player1.body == alternate_body:
                print("Starting Location already taken!")
                continue
            else:
                break

        # While loop to get the user's colour and check for repeats
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
        """This method displays a board so the user can decide
        where they want to start."""

        # Prints the column numbers with correct spacing
        print("   ", end="")
        for i in range(self.n):
            print(i, end=" ")
        print(" ")

        # Prints an empty board starting with the row number
        for i in range(self.n):
            if i < 10:  # Change spacing if row number has more than one digit
                print(f"{i} |", end="")
            else:
                print(f"{i}|", end="")

            # Print the empty grid row. Double spacing needed for two digits
            if self.n > 9:
                print(" |" * 10 + "  |" * (self.n - 10))
            else:
                print(" |" * self.n)

    def populate_board(self, board):
        """This method populates the board with the current body
        and head for each player.

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
        """This method displays the board aesthetically with pre-defined
        output symbols."""

        # Makes Board
        board = self.make_board()

        # Calls method to populate board
        self.populate_board(board)

        # Print initial border
        print("#" * (2 * self.n + 3))

        # Loops through the board and prints each position
        for i in range(self.n):
            print("#|", end="")
            for j in range(self.n):
                print(f"{self.output_dict[board[i][j]]}|", end="")
            print("#")

        # Print final border
        print("#" * (2 * self.n + 3))

    def get_used_spaces(self):
        """This method returns all the spaces that have already been
        taken on the board.

        ---Returns---
        used_spcaes: list
        list of tuples that contain the spaces that have been taken
        by previous moves.
        """

        used_spaces = self.player1.body + self.player2.body

        return used_spaces

    def calculate_next_positions_sim(self):
        """This method calculates the next position based on instance
        directions and head. The next position is assigned to the
        next_position instance variable."""

        # Calculate next position for player 1
        self.player1.calculate_next_position()

        # Calculate next position for player 2
        self.player2.calculate_next_position()

    def check_legal_moves_sim(self):
        """This method checks if the inputted move is one of lrud for
        both player instances.

        ---Returns---
        result: str
        string identifier that details the outcome of the legailty test.
        P0 = pass, T0 = tie, W1 = player 1 wins, W2 = player 2 wins"""

        result = "P0"

        # Checks if both moves are not legal - results in a tie
        if (not self.player1.check_legal_move()) & (
            not self.player2.check_legal_move()
        ):
            result = "T0"

        # Checks if player 2 is illegal and player 1 is legal - results in W1
        elif (self.player1.check_legal_move()) & (
            not self.player2.check_legal_move()
        ):
            result = "W1"

        # Checks if player 1 is illegal and player 2 is legal - results in W2
        elif (not self.player1.check_legal_move()) & (
            self.player2.check_legal_move()
        ):
            result = "W2"

        return result

    def check_legal_positions_sim(self, game):
        """This method checks if the positions are within the board and not
        a player's past move for both players simultaneously. Heavily uses
        the check_legal_position method.

        ---Returns---
        result: str
        string identifier that details the outcome of the legailty test.
        P0 = pass, T0 = tie, W1 = player 1 wins, W2 = player 2 wins"""

        # Initialse result to default on a pass
        result = "P0"

        # Checks if both positions are not legal - results in a tie
        if (not self.player1.check_legal_position(game)) & (
            not self.player2.check_legal_position(game)
        ) | (self.player1.next_position == self.player2.next_position):
            result = "T0"

        # Checks if player 2 is illegal and player 1 is legal - results in W1
        elif (self.player1.check_legal_position(game)) & (
            not self.player2.check_legal_position(game)
        ):
            result = "W1"

        # Checks if player 1 is illegal and player 2 is legal - results in W2
        elif (not self.player1.check_legal_position(game)) & (
            self.player2.check_legal_position(game)
        ):
            result = "W2"

        return result


class bcolours:
    """This class stores the colour information strings, a dictionary
    to print the colours aesthetically and a dictionary to store the
    available colours."""

    # End string
    global END
    END = "\033[0m"

    # Colour Strings
    WHITE = "\033[97m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[36m"
    MAGENTA = "\033[95m"

    # Function to apply colours
    def colour_text(string, colour):
        """This function applies the specified colour to the specified
        string and returns the coloured string.

        ---Parameters---
        string: str
        string to be coloured

        colour: str
        colour to be applied

        ---Returns---
        coloured_string: str
        string with colour prefixes and suffixes"""

        # Colour string based on arguments
        coloured_string = colour + string + END
        return coloured_string

    # Display dictionary
    display_dictionary = {
        "1": "WHITE",
        "2": colour_text("GREEN", GREEN),
        "3": colour_text("YELLOW", YELLOW),
        "4": colour_text("BLUE", BLUE),
        "5": colour_text("MAGENTA", MAGENTA),
        "6": colour_text("RED", RED),
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
