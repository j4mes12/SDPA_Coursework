"""
Name: James Stephenson
Section: Part 1
Description: This script contains the Player and Computer classes to house instance 
information for each player in the Tron Game. Player information is also harvested
within these classes using various methods. The computer class inherits from the
Player class.
"""

# Import required packages
import random
from itertools import product


class Player:
    """This class contains methods relating to the players. It also contains information
    on the past locations and current location of the players, player ids and the direction
    the player is facing"""

    # Define dictionaries to translate between vectors and letters.
    direction_dict = {"l": (0, -1), "r": (0, 1), "u": (-1, 0), "d": (1, 0)}

    def __init__(self, init_body, id, colour):
        """This init method initialises the body, id and colour that has been specified in
        the player instance. A dummy direction of None is assigned as a filler since there
        is no knowledge on where to move yet.

        ---Parameters---
        init_body: list
        list of 2 dimensional sets describing where the initial player body starts.

        init_direction: str
        string describing the initial direction the player starts.

        id: str, int
        integer or string denoting player id. This is preset to 1 and 2 for players
        1 and 2 respectively with the computer gettings assigned 'C'

        colour: str
        string that gives the display colour that the user has set"""

        # Initialse input parameters
        self.id = id
        self.body = init_body
        self.direction = None
        self.colour = colour

    def head(self):
        """Method that returns the current location of the player - the head of the snake so
        to speak.

        ---Returns---
        self.body[-1]: set
        2-d set on the current position of the player"""

        return self.body[-1]

    def calculate_next_position(self, temp_direction=None):
        """This method calculates the next position based on instance direction
        and position."""

        # Use direction dictionary to turn new_direction into a vector
        step = self.direction_dict[self.direction]

        # Calculate the next position using vector addition
        self.next_position = ((self.head()[0] + step[0]), (self.head()[1] + step[1]))

    def check_legal_move(self):
        """This method checks if the inputted move is one of L, R, U or D.

        ---Parameters---
        move: str
        player move

        ---Returns---
        lrud & single_character: bool
        boolean to describe if the move is one of l, r, u or d' and just one character"""

        # Checks if move is one of l, r, u or d
        lrud = self.in_value in "lrud"

        # Checks if move is one character
        single_character = len(self.in_value) == 1

        return lrud & single_character

    def check_legal_position(self, game, temp_position=None):
        """This method checks if the position is within the board and not a player's past move.

        ---Parameters---
        position: set
        set of length two that describes a position.

        ---Returns---
        no_cross & in_board_x & in_board_y: bool
        boolean that verifies position has not been previously used and is within the board in both x and y directions"""

        if temp_position == None:
            position = self.next_position
        else:
            position = temp_position

        # Checks if position has not been previously used by a player
        no_cross = position not in game.get_used_spaces()

        # Checks if position is in the board in x direction
        in_board_x = 0 <= position[0] <= game.n - 1

        # Checks if position is in board in y direction
        in_board_y = 0 <= position[1] <= game.n - 1

        return no_cross & in_board_x & in_board_y

    def take_step(self):
        """Method to add a new position to body of the snake for the player instance."""

        # Appends the player's next position to the end of the body
        self.body.append(self.next_position)

    def change_direction(self):
        """Method to assign a new direction to a player instance based on the get_input method"""

        self.direction = self.in_value

    def get_input(self):
        """Method to get the input (hidden) from a user for their move. This move is
        stored in the class variable in_value which is then used in the change_direction method"""

        self.in_value = input(f"Player {self.id} (Enter one of LRUD): ").lower()

    def display_winner(self):
        """This method displays the winning message when the game is over."""

        print(f"GAME OVER: Player {self.id} wins!")


class Computer(Player):
    """This class inherits from the Player class and contains methods that the computer uses
    to play the game."""

    def __init__(self, init_body, id, colour):
        """This method uses the inherited __init__ method from the Player class to initialise.

        ---Parameters---
        init_body: list
        list of 2 dimensional sets describing where the initial player body starts.

        init_direction: str
        string describing the initial direction the player starts.

        id: str, int
        integer or string denoting player id. This is preset to 1 and 2 for players
        1 and 2 respectively with the computer gettings assigned 'C'"""

        Player.__init__(self, init_body=init_body, id=id, colour=colour)

    def display_winner(self):
        """This method displays the winning message when the game is over. Since,
        in this case, the computer has won, we want to output a different string."""

        print("GAME OVER: Computer wins!")

    def calculate_temp_next_position(self, temp_direction):
        """This method calculates the next position based on a temporary direction
        and instance position.

        ---Parameters---
        temp_direction: str
        string that is one of 'l', 'r', 'u' or 'd'

        ---Returns---
        next_temp_position: tuple
        tuple of dimension two; a direction in vector form.
        """

        # Use direction dictionary to turn new_direction into a vector
        step = self.direction_dict[temp_direction]

        next_temp_position = ((self.head()[0] + step[0]), (self.head()[1] + step[1]))
        # If dealing with a temporary direction, we just want to return it
        return next_temp_position

    def gen_exe_computer_move(self, game, move_type):
        """This method generates a computer move based on the type of computer that
        is being used and then executes the generated move using the change_direction
        method."""

        # Check if computer is smart or random and generate move
        if move_type == "random":
            self.generate_random_move()
        elif move_type == "smart":
            self.generate_smart_move(game)

        # Execute move
        self.change_direction()
        print(f"Computer Move: {self.in_value}")

    def generate_random_move(self):
        """This method generates a random move for the random computer players. This uses the sample
        function from the random package to select one move from 'l', 'r', 'u' or 'd' as its random
        choice."""

        # Translate random number into direction and assign to in_value
        self.in_value = random.sample("lrud", 1)[0]

    def generate_smart_move(self, game):
        """This function generates the smart move for the computer using a search
        algorithm. It goes through all the viable directions and calculates the
        number of available spaces in the immediate 3x3 area in that direction. The
        direction that has the most available spaces is chosen. Since we are
        reviewing a 3x3 area, this in itself looks at future moves as well as effective/
        feasible next moves."""

        # Initialises a dictionary to store the search values
        search_dict = {i: 0 for i in "lrud"}

        # This loop runs through each direction and calculates the available spaces
        for i in "lrud":
            possible_position = game.player2.calculate_temp_next_position(
                temp_direction=i
            )

            # Check that possible position is legal and not currently taken
            if game.player2.check_legal_position(game, temp_position=possible_position):

                # This loop creates a grid of the surrounding area and counts available spaces
                for x, y in product(
                    range(2, -2, -1),
                    range(2, -2, -1),
                ):
                    # Calculate new position to search
                    search = (possible_position[0] + x, possible_position[1] + y)

                    # Makes sure search position is legal
                    if game.player2.check_legal_position(game, temp_position=search):
                        search_dict[i] += 1  # Increase count if space is available

        # Calculate the direction that has the greatest available spaces
        self.in_value = max(search_dict, key=search_dict.get)
