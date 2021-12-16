from board import Board


def main():
    while True:
        menu = input(
            """Welcome to the game. Please select which version you want to play:
            \t(1) Basic Game
            \t(2) Complex Game
            \t(3) Versus Random Computer
            \t(4) Versus Smart Computer
            \t(5) Basic Game on Hex Board
            Choice: """
        )
        if menu == "q":
            return print("Game Ended.")
        elif menu in "12345":
            break
        else:
            print(f"Invalid Menu Choice. Input: {menu}")

    while True:
        board_size = input("Please enter board size: ")
        if board_size == "q":
            return print("Game Ended.")
        elif board_size.strip().isdigit():
            board_size = int(board_size)
            break
        else:
            print(f"Invalid Board Size. Input: {board_size}")

    def basic_game():
        while True:
            game.player1.get_input()

            if game.player1.in_value == "q":
                return print("Game Ended.")
            elif game.check_legal_move(game.player1.in_value):
                game.player1.change_direction()
            else:
                game.player2.display_winner()
                break

            p1_next_position = game.calculate_next_position(
                position=game.player1.head(), new_direction=game.player1.direction
            )

            if game.check_legal_position(position=p1_next_position):
                game.player1.take_step(p1_next_position)
            else:
                game.player2.display_winner()
                break

            game.print_board()

            game.player2.get_input()

            if game.player2.in_value == "q":
                return print("Game Ended.")
            elif game.check_legal_move(game.player2.in_value):
                game.player2.change_direction()
            else:
                game.player1.display_winner()
                break

            p2_next_position = game.calculate_next_position(
                position=game.player2.head(), new_direction=game.player2.direction
            )

            if game.check_legal_position(p2_next_position):
                game.player2.take_step(p2_next_position)
            else:
                game.player1.display_winner()
                break

            game.print_board()

    def complex_game():
        while True:
            game.player1.get_input()
            game.player2.get_input()

            if game.player1.in_value == "q" or game.player2.in_value == "q":
                return print("Game Ended.")

            if game.check_legal_move(game.player1.in_value):
                game.player1.change_direction()
            else:
                game.player2.display_winner()
                break

            if game.check_legal_move(game.player2.in_value):
                game.player2.change_direction()
            else:
                game.player1.display_winner()
                break

            p1_next_position = game.calculate_next_position(
                position=game.player1.head(), new_direction=game.player1.direction
            )

            p2_next_position = game.calculate_next_position(
                position=game.player2.head(), new_direction=game.player2.direction
            )

            if p1_next_position == p2_next_position:
                return print("Shake hands: It's a tie")

            if game.check_legal_position(position=p1_next_position):
                game.player1.take_step(p1_next_position)
            else:
                game.player2.display_winner()
                break

            if game.check_legal_position(p2_next_position):
                game.player2.take_step(p2_next_position)
            else:
                game.player1.display_winner()
                break

            game.print_board()

    def computer_game():
        while True:
            game.player1.get_input()
            game.player2.generate_move()

            if game.player1.in_value == "q":
                return print("Game Ended.")

            if game.check_legal_move(game.player1.in_value):
                game.player1.change_direction()
            else:
                game.player2.display_winner()
                break

            game.player2.change_direction()

            p1_next_position = game.calculate_next_position(
                position=game.player1.head(), new_direction=game.player1.direction
            )

            p2_next_position = game.calculate_next_position(
                position=game.player2.head(), new_direction=game.player2.direction
            )

            if game.check_legal_position(position=p1_next_position):
                game.player1.take_step(p1_next_position)
            else:
                game.player2.display_winner()
                break

            if game.check_legal_position(position=p2_next_position):
                game.player1.take_step(p2_next_position)
            else:
                game.player1.display_winner()
                break

            game.print_board()

    def smart_computer_game():
        while True:
            game.player1.get_input()
            game.player2.generate_smart_move()

            if game.player1.in_value == "q":
                return print("Game Ended.")

            if game.check_legal_move(game.player1.in_value):
                game.player1.change_direction()
            else:
                game.player2.display_winner()
                break

            game.player2.change_direction()

            p1_next_position = game.calculate_next_position(
                position=game.player1.head(), new_direction=game.player1.direction
            )

            p2_next_position = game.calculate_next_position(
                position=game.player2.head(), new_direction=game.player2.direction
            )

            if game.check_legal_position(position=p1_next_position):
                game.player1.take_step(p1_next_position)
            else:
                game.player2.display_winner()
                break

            if game.check_legal_position(position=p2_next_position):
                game.player1.take_step(p2_next_position)
            else:
                game.player1.display_winner()
                break

            game.print_board()

    def basic_hex_game():
        print("not ready yet")

    if menu in "34":
        game = Board(board_size, computer=True)
    else:
        game = Board(board_size)

    game.print_board()

    if menu == "1":
        basic_game()
    elif menu == "2":
        complex_game()
    elif menu == "3":
        computer_game()
    elif menu == "4":
        smart_computer_game()
    elif menu == "5":
        basic_hex_game()


if __name__ == "__main__":
    main()
