import random
from getpass import getpass


class Player:
    """This class contains methods relating to the players. It also contains information
    on the past locations and current location of the players, player ids and the direction
    the player is facing"""

    def __init__(self, init_body, init_direction, id):
        """This init method initialises the body and direction of each instance alongside
        the id that has been specified.

        ---Parameters---
        init_body: list
        list of 2 dimentional sets describing where the inital player body starts.
        init_direction: str
        string describing initial direction player starts.
        id: str, int
        integer or string denoting player id. This is preset to 1 and 2 for players
        1 and 2 respecively with the computer gettings assigned 'C'"""

        # Initialse input paramters
        self.body = init_body
        self.direction = init_direction
        self.id = id

    def head(self):
        """Method that returns the current location of the player - the head of the snake so to speak

        ---Returns---
        self.body[-1]: set
        2-d set on the current position of the player"""

        return self.body[-1]

    def take_step(self, step):
        """Method to add a new position to body of the snake for the player instance."""

        # Appends the player's new position to the end of the body
        self.body.append(step)

    def change_direction(self):
        """Method to assign a new direction to a player instance based on the get_input method"""

        self.direction = self.in_value

    def get_input(self):
        """Method to get the input (hidden) from a user for their move. This move is
        stored in the class variable in_value which is then used in the change_direction method"""

        self.in_value = getpass(prompt=f"Player {self.id} (LRUD): ").lower()

    def display_winner(self):
        """This method displays the winning message when the game is over."""

        if self.id == "C":
            print("GAME OVER: Computer wins!")
        else:
            print(f"GAME OVER: Player {self.id} wins!")


class Computer(Player):
    """This class inherts from the Player class and contains methods that the computer uses to play the game."""

    # Dictionary to translate between random number and direction
    computer_dict = {0: "l", 1: "r", 2: "u", 3: "d"}

    def __init__(self, init_body, init_direction, id):
        """This method uses the inherited __init__ method from the Player class to initialise.

        ---Parameters---
        init_body: list
        list of 2 dimentional sets describing where the inital player body starts.
        init_direction: str
        string describing initial direction player starts.
        id: str, int
        integer or string denoting player id. This is preset to 1 and 2 for players
        1 and 2 respecively with the computer gettings assigned 'C'"""

        Player.__init__(self, init_body=init_body, init_direction=init_direction, id=id)

    def generate_random_move(self):
        """This method generates a random move for the random computer players. This uses the
        randint function to generate a random number and use the computer_dict to translate that
        into a direction to move in."""

        # Generate random number
        rng = random.randint(0, 3)

        # Translate random number into direction and assign to in_value
        self.in_value = self.computer_dict[rng]
