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

        self.in_value = input(f"Player {self.id} ( Enter one of LRUD): ").lower()

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
        feasible next moves.

        ---Returns---
        max_key: str
        string that is one of 'l', 'r', 'u' or 'd'"""

        # Initialises a dictionary to store the search values
        search_dict = {i: 0 for i in "lrud"}

        # This loop runs through each direction and calculates the available spaces
        for i in "lrud":
            possible_position = game.calculate_next_position(game.player2.head(), i)

            # Check that possible position is legal and not currently taken
            if game.check_legal_position(possible_position):
                # This loop creates a grid of the surrounding area and counts available spaces
                for x, y in product(
                    range(2, -2, -1),
                    range(2, -2, -1),
                ):
                    # Calculate new position to search
                    search = (possible_position[0] + x, possible_position[1] + y)

                    # Makes sure search position is legal
                    if game.check_legal_position(search):
                        search_dict[i] += 1  # Increase count if space is available

        # Calculate the direction that has the greatest available spaces
        max_key = max(search_dict, key=search_dict.get)

        return max_key
