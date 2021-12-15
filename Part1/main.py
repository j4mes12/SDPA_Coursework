from board import Board


def main():
    while True:
        menu = input(
            "Welcome to the game. Please select which version you want to play:\n\t(1) Basic Game\n\t(2) Complex Game\n\t(3) Versus Computer\nChoice: "
        )
        if menu == "q":
            return print("Game Ended.")
        elif menu in ["1", "2", "3"]:
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
            p1_input = input(f"Player {game.player1.id} (LRUD): ").lower()

            if p1_input == "q":
                return print("Game Ended.")
            elif game.check_legal_move(p1_input):
                game.player1.change_direction(p1_input)
            else:
                winner = game.player2.id
                break

            p1_next_position = game.next_position(
                position=game.player1.head(), new_direction=game.player1.direction
            )

            if game.check_legal_position(position=p1_next_position):
                game.player1.take_step(p1_next_position)
            else:
                winner = game.player2.id
                break

            game.print_board()

            p2_input = input(f"Player {game.player2.id} (LRUD): ").lower()

            if p2_input == "q":
                return print("Game Ended.")
            elif game.check_legal_move(p2_input):
                game.player2.change_direction(p2_input)
            else:
                winner = game.player1.id
                break

            p2_next_position = game.next_position(
                position=game.player2.head(), new_direction=game.player2.direction
            )

            if game.check_legal_position(p2_next_position):
                game.player2.take_step(p2_next_position)
            else:
                winner = game.player1.id
                break

            game.print_board()

        print(f"GAME OVER: Player {winner} wins!")

    def complex_game():
        while True:
            p1_input = input(f"Player {game.player1.id} (LRUD): ").lower()
            p2_input = input(f"Player {game.player2.id} (LRUD): ").lower()

            if p1_input == "q" or p2_input == "q":
                return print("Game Ended.")

            if game.check_legal_move(p1_input):
                game.player1.change_direction(p1_input)
            else:
                winner = game.player2.id
                break

            if game.check_legal_move(p2_input):
                game.player2.change_direction(p2_input)
            else:
                winner = game.player1.id
                break

            p1_next_position = game.next_position(
                position=game.player1.head(), new_direction=game.player1.direction
            )

            p2_next_position = game.next_position(
                position=game.player2.head(), new_direction=game.player2.direction
            )

            if p1_next_position == p2_next_position:
                return print("Shake hands: It's a tie")

            if game.check_legal_position(position=p1_next_position):
                game.player1.take_step(p1_next_position)
            else:
                winner = game.player2.id
                break

            if game.check_legal_position(p2_next_position):
                game.player2.take_step(p2_next_position)
            else:
                winner = game.player1.id
                break

            game.print_board()

        print(f"GAME OVER: Player {winner} wins!")

    def computer_game():
        while True:
            p1_input = input(f"Player {game.player1.id} (LRUD): ").lower()
            p2_input = game.player2.generate_move()

            if p1_input == "q":
                return print("Game Ended.")

            if game.check_legal_move(p1_input):
                game.player1.change_direction(p1_input)
            else:
                winner = "COMPUTER"
                break

            game.player2.change_direction(p2_input)

            p1_next_position = game.next_position(
                position=game.player1.head(), new_direction=game.player1.direction
            )

            p2_next_position = game.next_position(
                position=game.player2.head(), new_direction=game.player2.direction
            )

            if game.check_legal_position(position=p1_next_position):
                game.player1.take_step(p1_next_position)
            else:
                winner = "COMPUTER"
                break

            if game.check_legal_position(position=p2_next_position):
                game.player1.take_step(p2_next_position)
            else:
                winner = game.player1.id
                break

            game.print_board()

        if not winner == "COMPUTER":
            winner += "Player "

        print(f"GAME OVER: {winner} wins!")

    if menu == "3":
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


if __name__ == "__main__":
    main()
