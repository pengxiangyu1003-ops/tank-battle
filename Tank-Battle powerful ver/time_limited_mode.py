from game_module import game_module
import pygame

def time_limited_mode():
    """
    Initializes the game in Time-Limited Mode and starts the game module.
    
    This function initializes Pygame, sets up the display window, and launches the game in "time_limited" mode.
    The game will run until the player either wins or the time limit expires.

    :return: None
    """
    # Initialize Pygame to set up game environment
    pygame.init()

    # Set up the display screen with a resolution of 900x700 pixels
    screen = pygame.display.set_mode((900, 700))  # Set the screen size (width: 900, height: 700)
    
    # Set the title of the window for the Time-Limited Mode
    pygame.display.set_caption("Tank Battle - Time-Limited Mode")  # Window title for user

    # Start the game by calling the game module with the 'time_limited' mode
    # This will begin the game where players have a time limit to complete their mission
    game_module(screen, mode="time_limited")  # Pass the screen and the mode to the game module
