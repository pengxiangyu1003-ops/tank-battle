from game_module import game_module
import pygame

def infinite_mode():
    """
    Initializes and runs the game in infinite mode.
    
    This function sets up the game window, initializes the Pygame library, and starts the 
    game module in "infinite" mode, which means the game will run without a time limit.
    
    The game window has a resolution of 900x700 pixels and is titled "Tank Battle - Infinite Mode".
    """
    # Initialize the Pygame library
    pygame.init()

    # Create the game window with the specified dimensions
    screen = pygame.display.set_mode((900, 700))

    # Set the title of the game window
    pygame.display.set_caption("Tank Battle - Infinite Mode")

    # Call the game module with 'infinite' mode
    game_module(screen, mode="infinite")
