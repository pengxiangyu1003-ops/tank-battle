import pygame
import sys
from game_module import game_module  
from help_screen import show_help
from scores_manager import load_scores

def show_scores(screen):
    """
    Displays the high scores on the screen and allows the user to return to the main menu.

    This function loads the scores, displays them in a list format on the screen, 
    and provides a button to return to the main menu.
    """
    # Load scores from the scores manager
    scores = load_scores()
    font = pygame.font.Font(None, 36)

    # Fill the screen with black and display the title
    screen.fill((0, 0, 0))
    title_text = font.render("High Scores", True, (255, 255, 255))
    screen.blit(title_text, (300, 50))

    # Display each score in the list
    y_pos = 100
    for username, score in scores.items():
        score_text = font.render(f"{username}: {score}", True, (255, 255, 255))
        screen.blit(score_text, (300, y_pos))
        y_pos += 50

    # Update the display
    pygame.display.update()

    # Create a 'Back to Menu' button
    back_button = pygame.Rect(350, 500, 200, 50)
    pygame.draw.rect(screen, (200, 100, 100), back_button)
    back_text = font.render("Back to Menu", True, (255, 255, 255))
    screen.blit(back_text, (back_button.x + (back_button.width - back_text.get_width()) // 2, back_button.y + 10))

    pygame.display.update()

    # Event loop to allow user to navigate back to the main menu
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):  # Check if 'Back' button is clicked
                    running = False
        pygame.display.update()

def main_menu():
    """
    Displays the main menu of the game with options to play the game, view scores, 
    view help, or quit the game.
    
    This function initializes the Pygame window, loads background music, 
    and provides buttons for the user to interact with. The user can start the game, 
    view help instructions, or exit the game.
    """
    # Initialize Pygame and music mixer
    pygame.init()
    pygame.mixer.init()
    
    

    # Set up the screen dimensions and window title
    screen = pygame.display.set_mode((900, 700))
    pygame.display.set_caption("Tank Battle - Main Menu")

    # Load and scale the background image
    background = pygame.image.load("assets/images.jpg")
    background = pygame.transform.scale(background, (900, 700))

    # Initialize fonts for title and buttons
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)

    # Define button dimensions
    button_width = 200
    button_height = 50

    # Define button areas for different menu options
    play_infinite_button = pygame.Rect((screen.get_width() - button_width) // 2, 200, button_width, button_height)
    play_time_limited_button = pygame.Rect((screen.get_width() - button_width) // 2, 300, button_width, button_height)
    help_button = pygame.Rect((screen.get_width() - button_width) // 2, 400, button_width, button_height)
    quit_button = pygame.Rect((screen.get_width() - button_width) // 2, 500, button_width, button_height)
    scores_button = pygame.Rect((screen.get_width() - button_width) // 2, 600, button_width, button_height)

    # Main menu loop
    running = True
    while running:
        # Display the background image
        screen.blit(background, (0, 0))

        # Render and display the title text
        title_text = font.render("Tank Battle", True, (255, 255, 255))
        screen.blit(title_text, ((screen.get_width() - title_text.get_width()) // 2, 100))

        # Draw the buttons for various options
        pygame.draw.rect(screen, (100, 200, 100), play_infinite_button)
        pygame.draw.rect(screen, (100, 200, 100), play_time_limited_button)
        pygame.draw.rect(screen, (100, 100, 200), help_button)
        pygame.draw.rect(screen, (200, 100, 100), quit_button)
        pygame.draw.rect(screen, (200, 200, 100), scores_button)

        # Render the text for each button and position them
        infinite_text = small_font.render("Infinite Mode", True, (0, 0, 0))
        time_limited_text = small_font.render("Time-Limited Mode", True, (0, 0, 0))
        help_text = small_font.render("Help", True, (0, 0, 0))
        quit_text = small_font.render("Quit", True, (0, 0, 0))
        scores_text = small_font.render("View Scores", True, (0, 0, 0))

        screen.blit(infinite_text, (play_infinite_button.x + (button_width - infinite_text.get_width()) // 2, play_infinite_button.y + 10))
        screen.blit(time_limited_text, (play_time_limited_button.x + (button_width - time_limited_text.get_width()) // 2, play_time_limited_button.y + 10))
        screen.blit(help_text, (help_button.x + (button_width - help_text.get_width()) // 2, help_button.y + 10))
        screen.blit(quit_text, (quit_button.x + (button_width - quit_text.get_width()) // 2, quit_button.y + 10))
        screen.blit(scores_text, (scores_button.x + (button_width - scores_text.get_width()) // 2, scores_button.y + 10))

        # Event handling for button clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_infinite_button.collidepoint(event.pos):  # Start infinite mode
                    game_module(screen, mode="infinite", return_to_menu_callback=main_menu)
                elif play_time_limited_button.collidepoint(event.pos):  # Start time-limited mode
                    game_module(screen, mode="time_limited", return_to_menu_callback=main_menu)
                elif help_button.collidepoint(event.pos):  # Show help screen
                    show_help(screen)
                elif quit_button.collidepoint(event.pos):  # Quit the game
                    pygame.quit()
                    sys.exit()
                elif scores_button.collidepoint(event.pos):  # Show high scores
                    show_scores(screen)

        pygame.display.update()
