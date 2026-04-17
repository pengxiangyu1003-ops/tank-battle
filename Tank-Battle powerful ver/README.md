# README for team <yesyes>

You must add (at least) the following information:

  * team information
  * a list of all files required/included in your project, and a description of their contents
  * an explanation of how to run and interact with your project (similar to a user guide)

Team Information
*   This project was developed by: Yunxian Ding & Xiangyu Peng
    Since we both play the game Identity V ans we both appreciate the relationship between two of the characters in it,
    we decided to create this interactive and fun "tank battle" (Though it's technically not a tank...)game using Python and Pygame.
    We set the background as the "Red Church" from game Identity V.
    We used the image of "Jack the Dog" (adapted from the hunter Jack in game Identity V )as the tank.
    We used the image of "Naib the Edamame" (adapted from the survivor Naib in game Identity V) as the target charater to be shot at!

Files Included in the Project
* 1. main.py
    Purpose: The main entry point of the game. It initializes the menu, allowing players to choose game modes or view the help screen.
    Important Notes:
    Calls menu.py to display the main menu.
    Launches different game modes based on player choice.

* 2. menu.py
    Purpose: Handles the main menu functionality.
    Key Functions:
    Displays buttons for "Infinite Mode","Time-Limited Mode","Help","Quit", and "View Score"
    Listens for user input to transition to the selected mode.
    Notes: Updated menu text to say "Click on the top right corner X to exit."

* 3. game_module.py
    Purpose: Contains the main game loop logic shared between both game modes.
    Key Features:
    Loads and displays a background image.
    Handles player movement, shooting, and collision detection.
    Plays a sound effect (shoot.wav) when the player shoots.
    Includes a "Game Over" screen with the final score and options.
    Notes: The game automatically saves the highest score for the current player.

* 4. player.py
    Purpose: Defines the Player class to manage the "tank"'s behavior.
    Key Features:
    Handles tank movement using arrow keys.
    Draws the tank sprite on the screen.

* 5. bullet.py
    Purpose: Defines the Bullet class to manage bullet behavior.
    Key Features:
    Moves bullets upward after shooting.
    Detects collisions with the target.

* 6. character.py
    Purpose: Defines the Character class to manage the target.
    Key Features:
    Moves the target to random positions when hit.
    Draws the target on the screen.

* 7. scores_manager.py
    Purpose: Manages saving, loading, and updating player scores.
    Key Features:
    Reads from and writes to the scores.json file.
    Keeps track of the highest score for each player.

* 8. help_screen.py
    Purpose: Displays the help/instructions screen for players.
    Key Features:
    Explains controls and game rules.
    Provides options to return to the main menu.

* 9. infinite_mode.py
    Purpose: Starts the game in infinite mode.
    Notes: Relies on game_module.py for game logic.

* 10. time_limited_mode.py
    Purpose: Starts the game in time-limited mode.
    Key Features:
    Ends the game after 60 seconds.
    Displays the player's score on the "Game Over" screen.

* 11. user_input.py
    Purpose: Let the user input their name at the start

* 12. README.md
    Purpose: Provides detailed documentation about the project, including team information, file descriptions, and usage instructions.

* 13. scores.json
    Purpose: Stores player scores as a JSON object.

* 14. Assets Folder
    Purpose: Contains all assets required for the game, including images and sounds.
    tank.png: Jack the Dog
    character.png: Naib the Edamame
    background.png: Red Church
    shoot.wav: The sound effect for shooting bullets

How to Run and Play the Game
* Step 1: Prerequisites
    Install Python 3.8 or later.
    Open your Python terminal cmd using this command:
    windows+r
    Install Pygame using the command:
    pip install pygame

* Step 2: Downloading the Game
    Download the zip file "TankBattle" and save it to your desktop

* Step 3: Running the Game
    Open your Python terminal cmd using this command:
    windows+r
    Navigate to the project folder in your terminal using this command:
    cd Desktop\TankBattle
    Run the main script using this command:
    python main.py

* Step 4: Gameplay
    When you open the "TankBattle" game page you should see five buttons.
    The first two buttons are for Modes:
    Infinite Mode: Play without a time limit.
    Time-Limited Mode: Score as much as possible in 60 seconds.
    The third button is for help, which indicates the Controls:
    Arrow Keys: Move the tank
    Spacebar: Shoot bullets
    Esc: exit the help page
    The fourth button is to quit.
    The fifth button is to view your scores.

* Step 5: Exiting
    Click the "X" on the top right corner at any time to exit the game.


