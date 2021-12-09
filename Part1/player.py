import random


class Player:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction
        self.id = self.get_id()

    def get_id(self):
        while True:
            id_input = input(f"Please Enter ID Character: ")
            valid_symbols = "!@#$%^&*_-+=<>€£:;[]{}()"
            if ((id_input.isalnum()) | (id_input in valid_symbols)) & len(
                id_input
            ) == 1:
                break
            else:
                print("Invalid ID. Please enter a single character.")
        print("ID Accepted.")
        return id_input

    def head(self):
        return self.body[-1]

    def take_step(self, step):
        self.body.append(step)

    def change_direction(self, direction):
        self.direction = direction


class Computer(Player):

    computer_dict = {0: "l", 1: "r", 2: "u", 3: "d"}

    def __init__(self, init_body, init_direction):
        Player.__init__()
