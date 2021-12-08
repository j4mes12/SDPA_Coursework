from board import Board

board_size = input("Welcome to the game. Please enter board size: ")

game = Board(board_size)

game.print_board()

while True:
    p1_input = input("Player1 (LRUD): ").lower()

    if p1_input in "lrud":
        break

    p2_input = input("Player2 (LRUD): ").lower()

    if p2_input in "lrud":
        break
