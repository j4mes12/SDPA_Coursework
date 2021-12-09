from board import Board


def main():
    while True:
        board_size = input("Welcome to the game. Please enter board size: ")
        if board_size.strip().isdigit():
            board_size = int(board_size)
            break
        else:
            print(f"Invalid Board Size. Input: {board_size}")

    game = Board(board_size)

    game.print_board()

    while True:
        p1_input = input("Player1 (LRUD): ").lower()

        if game.check_legal_move(p1_input):
            game.player1.change_direction(p1_input)
        else:
            winner = 2
            break

        p1_next_position = game.next_position(
            position=game.player1.head(), new_direction=game.player1.direction
        )

        if game.check_legal_position(position=p1_next_position):
            game.player1.take_step(p1_next_position)
        else:
            winner = 2
            break

        game.print_board()

        p2_input = input("Player2 (LRUD): ").lower()

        if game.check_legal_move(p2_input):
            game.player2.change_direction(p2_input)
        else:
            winner = 1
            break

        p2_next_position = game.next_position(
            position=game.player2.head(), new_direction=game.player2.direction
        )

        if game.check_legal_position(p2_next_position):
            game.player2.take_step(p2_next_position)
        else:
            winner = 1
            break

        game.print_board()

    print(f"GAME OVER: Player {winner} wins!")


if __name__ == "__main__":
    main()
