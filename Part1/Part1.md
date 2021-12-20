
# "Part 1: Software Development (Snake Game)"

## Project Design

This project is a game where one or two players interact with a board and control
snakes with the L, R, U, D keys. The intention is to avoid colliding with both the snake
and the walls of the board.

Technically, this game uses three classes together to create the game and interact with the
user(s) which are in turn called upon and used to create instances in the main.py script.

The two classes are the Board class (in board.py) and the Player and Computer classes (in player.py)
with the Computer class inheriting from the Player class.

 A small note on the structure of the classes: the Board class is used to control anything related
 to the board and the Player/Computer classes are used to control everything related to the
 player/computer. Player instances are created *inside* the Board class's '_\_init__' method and
 so are only accessed through the Board instances.

Each game type is split up into its own function for ease of code review. The game, housed in a
while loop to play, uses methods as much as possible and succesfully does this. There are a
fwe exceptions were this was not possible such as generating the smart computer move. This
was the case because information from multiple instances of the Player/Computer classes as
well as the current instance of the Board classes were required thus we would have only been
able to turn it into a method within the Board class. However, this approach didn't seem like
it would be inituitive to have a Computer-based method housed in the Board class.

## Design Decisions

The game starts with a menu so the user can choose which type of game they wish to play. I
considered splitting the menu up and starting by asking the user if they wanted to player the basic
game or complex game to start with and then moving on to asking if they want to player a two player
or one player version (in place of a computer game option) etc.

I felt that the menu approach was preferable since it required the user to input less information
before playing the game. Instead the player has to choose between four options, set the board size
and then play the game. This allowed me to add personalisation features (such as initial location
and player id) without bombarding the user with questions before they play the game.

Also, a key design decision was regarding the computer's generated moves. There were many ways generate
random moves to start with, I initially used a dictionary and random integer generator to generate a random
number between 0 and 3 and translate that number into a move. The approach I settled on however it a lot cleaner
and is more readable.

## Files

There are three files in this project: main.py, board.py and player.py

- main.py contains the main script that is run to play the game
- board.py only contains the Board class
- player.py contains the Player class and the Computer class that inherits from the Player class.

## Classes

### Board Class

This Class is responsible for controlling the game. It creates the instances for each player and contains methods regarding the board, calculating next positions and checking legality of moves/positions.

#### \_\_init\_\_ (Board)

This method initialises the class and creates the Player instances for the game.

#### populate_board

This method populates the board with the current body and head for each player.

#### make_board

This method creates an empty square list using self.n and populates it using variables in each player instance.

#### print_board

This method displays the board aesthetically with pre-defined output symbols.

#### calculate_next_position

This method calculates the next position based on the entered direction and current position.

#### check_legal_move

This method checks if the inputted move is one of L, R, U or D.

#### check_legal_position

This method checks if position is within the board and not a player's past move.

#### calculate_next_positions_sim

This method calculates the next position based on instance directions and head. The next position is assigned to the next_position instance variable.

#### check_legal_moves_sim

This method checks if the inputted move is one of lrud for both player instances.

#### check_legal_positions_sims

This method checks if position is within the board and not a player's past move for both players simultaneously. Heavily uses the check_legal_position method.

### Player Class

This class contains methods relating to the players. It also contains information on the past locations and current location of the players, player ids and the direction the player is facing.

#### \_\_init\_\_ (Player)

The __init__ method for the Player class initialises the body and direction of each instance alongside the id that has been specified.

#### head

This method returns the current location of the player - the head of the snake so-to-speak.

#### take_step

This method adds a new position to body of the snake for the player instance.

#### change_direction

This method assigns a new direction to a player instance based on the get_input method.

#### get_input

This method gets the input (hidden) from a user for their move. This move is stored in the class variable in_value which is then used in the change_direction method.

#### display_winner (Player)

This method displays the winning message when the game is over.

### Computer Class

This class inherts from the Player class and contains methods that the computer uses to play the game.

#### \_\_init\_\_ (Computer)

This method uses the inherited __init__ method from the Player class to initialise.

The __init__ method for the Computer class calls the Player __init__ method to make use of the inhertiance.

#### display_winner (Computer)

This method displays the winning message when the game is over. Since, in this case, the computer has won, we want to output a different string.

#### generate_random_move

This method generates a random move for the random computer players. This uses the sample function from the random package to select one move from 'l', 'r', 'u' or 'd' as its random choice.

# other important details
