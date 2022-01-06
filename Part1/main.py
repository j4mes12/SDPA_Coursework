# Import Packages
import random
from board import Board
from itertools import product


def main():
    """This is the main function that is run and controls the program. It contains
    the menu procedure, board size request and executes the game."""

    # This while loop requests user's menu choice and breaks once there is an acceptable entry
    while True:
        menu = input(
            """Welcome to the game. Please select which version you want to play:
            \t(1) Basic Game
            \t(2) Simultaneous Game
            \t(3) Versus Random Computer
            \t(4) Versus Smart Computer
            \t(Blank) Random! Just hit Enter...
            \t(q) Quit
            Choice: """
        )
        if menu == "q":  # Provides an option to quit the game
            return print("Game Ended.")
        if menu == "":  # Provides user a random option
            menu = random.sample("1234", 1)[0]
            print(f"Option {menu} Randomly Selected!")
            break
        elif menu in "1234":  # Checks for suitable options
            break
        else:
            print(f"Invalid Menu Choice. Input: {menu}")

    # This while loop asks the user to enter a suitable board size
    while True:
        board_size = input("Please enter board size (Blank for Random!): ")
        if board_size == "q":  # Provides an option to quit the game
            return print("Game Ended.")
        elif board_size == "":
            board_size = random.randint(2, 9)
            print(f"Random Board Size: {board_size}")
            break
        elif board_size.strip().isdigit():  # Makes sure input in digit
            board_size = int(board_size)
            break
        else:
            print(f"Invalid Board Size. Input: {board_size}")

    # Creates the game instance
    if menu in "34":  # If versus computer options are chosen, player2 is a Computer
        game = Board(board_size, computer=True)
    else:
        game = Board(board_size)

    # Display the initial board
    game.print_board()

    # The specific type of game is executed based on the menu choice
    if menu == "1":
        basic_game(game)
    elif menu == "2":
        simultaneous_game(game)
    elif menu == "3":
        computer_game(game)
    elif menu == "4":
        smart_computer_game(game)


def basic_game(game):
    """This function contains the method to run the basic game whereby players
    input their move alternately and the baord is displayed after each move.
    Response to Step 2.

    ---Parameters---
    game: Board instance
    instance of the Board class.

    ---Returns---
    print statement
    Prints the outcome of the game and the winner (if there is one).
    """

    # This loops through the game until a player has won
    while True:

        # Call get_input for player input to get player's move
        game.player1.get_input()

        # Checks if input is valid
        if game.player1.in_value == "q":
            return print("Game Ended.")
        elif game.check_legal_move(game.player1.in_value):
            game.player1.change_direction()
        else:
            return game.player2.display_winner()

        # Calculate player 1's next position
        game.player1.next_position = game.calculate_next_position(
            position=game.player1.head(), new_direction=game.player1.direction
        )

        # Check if new position is legal
        if game.check_legal_position(game.player1.next_position):
            game.player1.take_step()
        else:
            return game.player2.display_winner()

        # Display board
        game.print_board()

        # Call get_input for player input to get player's move
        game.player2.get_input()

        # Checks if input is valid
        if game.player2.in_value == "q":
            return print("Game Ended.")
        elif game.check_legal_move(game.player2.in_value):
            game.player2.change_direction()
        else:
            return game.player1.display_winner()

        # Calculate player 2's next position
        game.player2.next_position = game.calculate_next_position(
            position=game.player2.head(), new_direction=game.player2.direction
        )

        # Check if new position is legal
        if game.check_legal_position(game.player2.next_position):
            game.player2.take_step()
        else:
            return game.player1.display_winner()

        # Display board
        game.print_board()


def simultaneous_game(game):
    """This function contains the method to run the simultaneous game whereby players
    input their move simultaneously and the baord is displayed after both moves have
    been executed. Response to Step 3A.

    ---Parameters---
    game: Board instance
    instance of the Board class.

    ---Returns---
    print statement
    Prints the outcome of the game and the winner (if there is one).
    """

    # This loops through the game until a player has won
    while True:
        # Get input for both players using the get_input method
        game.player1.get_input()
        game.player2.get_input()

        # Check if either inputs are to quit
        if game.player1.in_value == "q" or game.player2.in_value == "q":
            return print("Game Ended.")

        # Check inputted moves are legal simultaneously
        lm_outcome = game.check_legal_moves_sim()

        # Make decisions based on lm_outcome return variable
        if lm_outcome == "T0":
            return print("Shake hands: It's a tie")
        elif lm_outcome == "W1":
            return game.player1.display_winner()
        elif lm_outcome == "W2":
            return game.player2.display_winner()
        else:
            game.player1.change_direction()
            game.player2.change_direction()

        # Calculate next positions for both players
        game.calculate_next_positions_sim()

        # Check inputted positions are legal simultaneously
        lp_outcome = game.check_legal_positions_sim()

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


def computer_game(game):
    """This function contains the method to run the computer game whereby a player
    plays against a computer that generates moves randomly. Moves are executed
    simultaneously. Response to Step 3B.

    ---Parameters---
    game: Board instance
    instance of the Board class.

    ---Returns---
    print statement
    Prints the outcome of the game and the winner (if there is one).
    """

    # This loops through the game until a player has won
    while True:

        # Get player 1 input
        game.player1.get_input()

        # Generate random computer move and execute
        game.player2.generate_random_move()
        game.player2.change_direction()

        # Check for quit
        if game.player1.in_value == "q":
            return print("Game Ended.")

        # Checks if input is valid
        if game.check_legal_move(game.player1.in_value):
            game.player1.change_direction()
        else:
            return game.player2.display_winner()

        # Calculate both player's next positions
        game.calculate_next_positions_sim()

        # Check inputted positions are legal simultaneously
        lp_outcome = game.check_legal_positions_sim()

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


def smart_computer_game(game):
    """This function contains the method to run the smart computer game whereby a player
    plays against a smart computer that generates moves based on a search algorithm that
    searches using a 3x3 grid. Moves are executed simultaneously. Response to Step 3C.

    ---Parameters---
    game: Board instance
    instance of the Board class.

    ---Returns---
    print statement
    Prints the outcome of the game and the winner (if there is one).
    """

    def generate_smart_move():
        """This function generates the smart move for the computer using a search
        algorithm. It goes through all the viable directions and calculates the
        number of available spaces in the immediate 3x3 area in that direction. The
        direction that has the biggest available spaces is chosen.

        ---Returns---
        max_key: str
        string that is one of 'l', 'r', 'u' or 'd'"""

        # Initialises a dictionary to store the search values
        search_dict = {i: 0 for i in "lrud"}

        # This loop runs through each direction and calculates the available spaces
        for i in "lrud":
            possible_position = game.calculate_next_position(game.player2.head(), i)

            # Check that possible position is legal and not currently taken
            if game.check_legal_position(possible_position):
                # This loop creates a grid of the surrounding area and counts available spaces
                for x, y in product(
                    range(2, -2, -1),
                    range(2, -2, -1),
                ):
                    # Calculate new position to search
                    search = (possible_position[0] + x, possible_position[1] + y)

                    # Makes sure search position is legal
                    if game.check_legal_position(search):
                        search_dict[i] += 1  # Increase count if space is available

        # Calculate the direction that has the greatest available spaces
        max_key = max(search_dict, key=search_dict.get)

        return max_key

    # This loops through the game until a player has won
    while True:
        # Get player 1 input
        game.player1.get_input()

        # Check for quit
        if game.player1.in_value == "q":
            return print("Game Ended.")

        # Generate Computer's smart move and execute
        game.player2.in_value = generate_smart_move()
        game.player2.change_direction()

        # Checks if input is valid
        if game.check_legal_move(game.player1.in_value):
            game.player1.change_direction()
        else:
            return game.player2.display_winner()

        # Calculate both player's next positions
        game.calculate_next_positions_sim()

        # Check inputted positions are legal simultaneously
        lp_outcome = game.check_legal_positions_sim()

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
