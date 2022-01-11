"""
Name: James Stephenson
Section: Part 1
Description: This script starts the Tron Game, makes the game run
and interact with the user. Different functions are used depending
on the user's initial menu choice.

"""

# Import Packages
import random
from board import Board


def main():
    """This is the main function that is run and controls the program. It contains
    the menu procedure, board size request and executes the game."""

    """ CHOOSE GAME TYPE
    This while loop requests the user's game-type choice and breaks once there
    is an acceptable entry"""

    while True:
        game_type = input(
            """Welcome to the game. Please select which version you want to play:
            \t(1) Basic Game
            \t(2) Simultaneous Game
            \t(Blank) Random! Just hit Enter...
            \t(q) Quit
            Choice: """
        )
        if game_type == "q":  # Provides an option to quit the game
            return print("Game Quitted.")
        if game_type == "":  # Provides user a random option
            game_type = random.sample("12", 1)[0]
            print(f"Option {game_type} Randomly Selected!")
            break
        elif game_type in "12":  # Checks for suitable options
            break
        else:
            print(f"Invalid Menu Choice. Input: {game_type}")

    # Translate user input into a string for code readability
    gt_dict = {"1": "basic", "2": "sim"}
    game_type = gt_dict[game_type]

    """ CHOOSE OPPONENT TYPE
    This while loop requests the user's opponent choice and breaks once there
    is an acceptable entry. opponent_type variable made global to be use in
    game functions."""
    global opponent_type
    while True:
        opponent_type = input(
            """Please select who you want to play against:
            \t(1) Human
            \t(2) Random Computer
            \t(3) Smart Computer
            \t(Blank) Random! Just hit Enter...
            \t(q) Quit
            Choice: """
        )
        if opponent_type == "q":  # Provides an option to quit the game
            return print("Game Quitted.")
        if opponent_type == "":  # Provides user a random option
            opponent_type = random.sample("123", 1)[0]
            print(f"Option {opponent_type} Randomly Selected!")
            break
        elif opponent_type in "123":  # Checks for suitable options
            break
        else:
            print(f"Invalid Menu Choice. Input: {opponent_type}")

    # Translate user input into a string for code readability
    opponent_dict = {"1": "Human", "2": "RComp", "3": "SComp"}
    opponent_type = opponent_dict[opponent_type]

    """ CHOOSE BOARD SIZE
    This while loop asks the user to enter a suitable board size"""
    while True:

        board_size = input(
            """Please enter board size
        (3 or higher, Blank for Random!): """
        )

        if board_size == "q":  # Provides an option to quit the game
            return print("Game Quitted.")
        elif board_size == "":  # Enact the random option
            board_size = random.randint(3, 20)
            print(f"Random Board Size: {board_size}")
            break
        elif board_size.strip().isdigit():  # Makes sure input in digit
            board_size = int(board_size)
            if board_size < 3:  # Checks the input is sufficiently big
                print(
                    f"""Invalid Board Size. Value must be strictly
                    greater than 3. Input: {board_size}"""
                )
            else:
                break
        else:
            print(f"Invalid Board Size. Input: {board_size}")

    # Creates global variable game so it can be used in game type functions
    global game

    # Creates the game instance
    # If versus computer options are chosen, player2 is a Computer
    if opponent_type[1:] == "Comp":
        game = Board(board_size, computer=True)
    else:
        game = Board(board_size)

    # Display the initial board
    game.print_board()

    # The specific type of game is executed based on the menu choice
    if game_type == "basic":
        basic_game()
    elif game_type == "sim":
        simultaneous_game()


def basic_game():
    """This function contains the method to run the basic game whereby
    moves are inputted alternately and the board is displayed after each
    move. Uses global variables game and opponent_type to take into account
    the user's choices.
    """

    # This loops through the game until a player has won
    while True:

        # Call get_input for player input to get player's move
        game.player1.get_input()

        # Checks if input is valid
        if game.player1.in_value == "q":
            return print("Game Quitted.")
        elif game.player1.check_legal_move():
            game.player1.change_direction()
        else:
            return game.player2.display_winner()

        # Calculate player 1's next position
        game.player1.calculate_next_position()

        # Check if new position is legal
        if game.player1.check_legal_position(game):
            game.player1.take_step()
        else:
            return game.player2.display_winner()

        # Display board
        game.print_board()

        # Check if we need to get second input
        if opponent_type == "Human":
            # Call get_input for player input to get player's move
            game.player2.get_input()

            # Checks if input is valid
            if game.player2.in_value == "q":
                return print("Game Quitted.")
            elif game.player2.check_legal_move():
                game.player2.change_direction()
            else:
                return game.player1.display_winner()

        else:
            # If computer chosen, check which type of computer and get move
            if opponent_type == "RComp":
                game.player2.gen_exe_computer_move(game, move_type="random")
            elif opponent_type == "SComp":
                game.player2.gen_exe_computer_move(game, move_type="smart")

        # Calculate player 2's next position
        game.player2.calculate_next_position()

        # Check if new position is legal
        if game.player2.check_legal_position(game):
            game.player2.take_step()
        else:
            return game.player1.display_winner()

        # Display board
        game.print_board()


def simultaneous_game():
    """This function contains the method to run the simultaneous game
    whereby moves are inputed simultaneously and the board is displayed
    after both moves have been executed. Uses global variables game and
    opponent_type to take into account the user's choices.
    """

    # This loops through the game until a player has won
    while True:
        # Get input for both players using the get_input method
        game.player1.get_input()

        # Check if input is to quit
        if game.player1.in_value == "q":
            return print("Game Quitted.")

        # Get input if opponent is human
        if opponent_type == "Human":
            game.player2.get_input()

            # Check if input is to quit
            if game.player2.in_value == "q":
                return print("Game Quitted.")

        else:
            # If a copmuter opponent is chosen, get moves accordingly
            if opponent_type == "RComp":
                game.player2.gen_exe_computer_move(game, move_type="random")
            elif opponent_type == "SComp":
                game.player2.gen_exe_computer_move(game, move_type="smart")

        # Check inputted moves are legal simultaneously
        lm_outcome = game.check_legal_moves_sim()

        # Make decisions based on lm_outcome return variable
        # Note: By definition, the computer's move will always be legal
        if lm_outcome == "T0":  # Tie
            return print("Shake hands: It's a tie")
        elif lm_outcome == "W1":  # Player 1 wins
            return game.player1.display_winner()
        elif lm_outcome == "W2":  # Player 2 wins
            return game.player2.display_winner()
        else:
            game.player1.change_direction()
            if opponent_type == "Human":
                game.player2.change_direction()

        # Calculate next positions for both players
        game.calculate_next_positions_sim()

        # Check inputted positions are legal simultaneously
        lp_outcome = game.check_legal_positions_sim(game)

        # Make decisions based on lp_outcome return variable
        if lp_outcome == "T0":  # Tie
            return print("Shake hands: It's a tie")
        elif lp_outcome == "W1":  # Player 1 wins
            return game.player1.display_winner()
        elif lp_outcome == "W2":  # Player 2 wins
            return game.player2.display_winner()
        else:
            game.player1.take_step()
            game.player2.take_step()

        # Display Board
        game.print_board()


if __name__ == "__main__":
    main()
