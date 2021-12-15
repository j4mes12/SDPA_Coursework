import random


class Player:
    def __init__(self, init_body, init_direction, id):
        self.body = init_body
        self.direction = init_direction
        self.id = id

    def head(self):
        return self.body[-1]

    def take_step(self, step):
        self.body.append(step)

    def change_direction(self, direction):
        self.direction = direction


class Computer(Player):

    computer_dict = {0: "l", 1: "r", 2: "u", 3: "d"}

    def __init__(self, init_body, init_direction, id):
        Player.__init__(self, init_body=init_body, init_direction=init_direction, id=id)

    def generate_move(self):
        rng = random.randint(0, 3)
        return self.computer_dict[rng]
