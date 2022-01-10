
# Part 1: Software Development (Snake Game)

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
while loop to play, uses methods as much as possible and successfully does this.

As an extension, I have decided to add default values and random selections. It gives the user the
option to hit Enter with no input and get a random choice in the case of game type and board size.
In the case of player configurations, such as start position, id and colour, a blank input will
set these parameters to their pre-assigned default values. These default values are chosen as
specified in the handbook: player 1 has id = 1, player 2 has id = 2; starting locations are the
top left and bottom right corners, and both colours default to white.

## Design Decisions

The game starts with a menu so the user can choose which type of game they wish to play. I
considered splitting the menu up and starting by asking the user if they wanted to player the basic
game or complex game to start with and then moving on to asking if they want to play a two-player
or one-player version (in place of a computer game option) etc.

I felt that the menu approach was preferable since it required the user to input less information
before playing the game. Instead, the player has to choose between four options, set the board size,
configure personalisations and then play the game. This allowed me to add personalisation features
(such as initial location, player id and player colour) without bombarding the user with questions
before they play the game.

When the option to play against a computer was added, we countinued with simultaneous submission of
moves thus if a play and computer move into the same space, it will always end in a tie. This decision
was actively taken based on the wording of the game specification.

Also, a key  design decision was regarding the computer's generated moves. There were many ways to generate
random moves to start with, I initially used a dictionary and random integer generator to generate a random
number between 0 and 3 and translate that number into a move. The approach I settled on however it a lot cleaner
and is more readable. Regarding the computer's smart moves, the search approach I have taken creates an
effective smart computer - it will give the user a run for their money!

As previously mentioned, an extension I added to the project was adding personal configurations to be made
such as player id, start position and player colour for both players. I added new methods to achieve this and
felt that splitting these questions up was important for clarity as I considered lumping them together in one
line, but that approach was not as user friendly.

I also considered allowing the user to input the starting direction but concluded that no
initial direction was required as it had no impact on the game.

Further, it was hard to portray to the user how to input their intended location in a meaningful way due to
the coordinate-nature of the board. I settled on adding new functionality to display a blank board with
labelled columns and rows which I felt really helped in the user's understanding of inputting their start
location.

## Files

There are three files in this project: main.py, board.py and player.py

- main.py contains the main script that is run to play the game
- board.py contains the Board class and the bcolours class
- player.py contains the Player class and the Computer class that inherits from the Player class.

## Classes

### Board Class

This Class is responsible for controlling the game. It creates the instances for each player and contains methods regarding the board, calculating next positions and checking the legality of moves/positions.

#### \_\_init\_\_ (Board)

This method initialises the class and creates the Player instances for the game.

#### get_user_id

This method gets the user's chosen ID and makes sure it is suitable: check it is of length one, an alphanumeric character or the default.

#### get_user_colour

This method gets the user's desired output colour and makes sure it's one of the menu options or the default value is requested.

#### get_user_body

This method gets the user's desired initial position. It also makes sure the input type is in the correct format and that they are digits. This is so we can effectively read in the user's input. We also start by displaying the available locations in a grid.

#### get_second_user_information

This method gets the second user/computer's information (id, initial body and colour) from the user. We have put this in a method so we can check there are no repeated choices. If both users want the default colour (white) then that is acceptable.

#### display_colours

This method displays the available colours for the user to decide before the game. We loop through the display dictionary printing the key and value pairs as a menu.

#### make_board

This method creates an empty square list using self.n

#### display_location_board

This method displays a board so the user can decide where they want to start.

#### populate_board

This method populates the board with the current body and head for each player.

#### print_board

This method displays the board aesthetically with pre-defined output symbols.

#### get_used_spaces

This method returns all the spaces that have already been taken on the board.

#### calculate_next_position

This method calculates the next position based on the entered direction and current position.

#### check_legal_move

This method checks if the inputted move is one of L, R, U or D.

#### check_legal_position

This method checks if the position is within the board and not a player's past move.

#### calculate_next_positions_sim

This method calculates the next position based on instance directions and head. The next position is assigned to the next_position instance variable.

#### check_legal_moves_sim

This method checks if the inputted move is one of lrud for both player instances.

#### check_legal_positions_sims

This method checks if the positions are within the board and not a player's past move for both players simultaneously. Heavily uses the check_legal_position method.

### bcolours Class

This class stores the colour information strings, a dictionary to print the colours aesthetically and a dictionary to store the available colours. There a no methods in this class, it's just used to store colour information.

### Player Class

This class contains methods relating to the players. It also contains information on the past locations and current location of the players, player ids and the direction the player is facing.

#### \_\_init\_\_ (Player)

This init method initialises the body, id and colour that has been specified in the player instance. A dummy direction of None is assigned as a filler since there is no knowledge on where to move yet.

#### head

This method returns the current location of the player - the head of the snake so-to-speak.

#### take_step

This method adds a new position to body for the player instance.

#### change_direction

This method assigns a new direction to a player instance based on the get_input method.

#### get_input

This method gets the input from a user for their move. This move is stored in the class variable in_value which is then used in the change_direction method.

#### display_winner (Player)

This method displays the winning message when the game is over.

### Computer Class

This class inherits from the Player class and contains methods that the computer uses to play the game.

#### \_\_init\_\_ (Computer)

The __init__ method for the Computer class calls the Player __init__ method to make use of the inheritance.

#### display_winner (Computer)

This method displays the winning message when the game is over. Since, in this case, the computer has won, we want to output a different string.

#### generate_random_move

This method generates a random move for the random computer players. This uses the sample function from the random package to select one move from 'l', 'r', 'u' or 'd' as its random choice.

#### generate_smart_move

This function generates the smart move for the computer using a search algorithm. It goes through all the viable directions and calculates the number of available spaces in the immediate 3x3 area in that direction. The direction that has the most available spaces is chosen. Since we are reviewing a 3x3 area, this in itself looks at future moves as well as effective/feasible next moves.
