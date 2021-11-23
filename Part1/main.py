import player as p
import board as b

board_size = input("Welcome to the game. Please enter board size: ")

b.print_board()

play = True
while play:
    p1_move = input("Enter move of player 1: ")
    p.update_position(p1_move)
    b.execute_move("p1", p1_move)

    p2_move = input("Enter move of player 2: ")
    b.execute_move("p2", p2_move)
    p.update_position(p2_move)