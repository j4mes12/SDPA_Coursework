class Player:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def head(self):
        return self.body[-1]

    def step(self, step):
        self.body.append(step)

    def change_direction(self, direction):
        self.direction = direction
