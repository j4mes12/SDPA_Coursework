import random
from getpass import getpass
from itertools import product


class Player:
    def __init__(self, init_body, init_direction, id):
        self.body = init_body
        self.direction = init_direction
        self.id = id

    def head(self):
        return self.body[-1]

    def take_step(self, step):
        self.body.append(step)

    def change_direction(self):
        self.direction = self.in_value

    def get_input(self):
        self.in_value = getpass(prompt=f"Player {self.id} (LRUD): ").lower()

    def display_winner(self):
        if self.id == "C":
            print("GAME OVER: Computer wins!")
        else:
            print(f"GAME OVER: Player {self.id} wins!")


class Computer(Player):

    computer_dict = {0: "l", 1: "r", 2: "u", 3: "d"}

    def __init__(self, init_body, init_direction, id):
        Player.__init__(self, init_body=init_body, init_direction=init_direction, id=id)

    def generate_move(self):
        rng = random.randint(0, 3)
        self.in_value = self.computer_dict[rng]

    def generate_smart_move(self):
        return self.generate_move()
