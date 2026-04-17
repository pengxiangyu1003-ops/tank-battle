import pygame

def show_help(screen):
    """
    Displays a help screen that explains the basic game controls.
    
    Args:
        screen (pygame.Surface): The surface on which the help screen will be displayed.
        
    This function creates a help screen with instructions on how to move, shoot, and quit the game.
    The user can press the ESC key to return to the previous screen or exit the game if needed.
    """
    running = True  # Flag to control the loop
    font = pygame.font.Font(None, 36)  # Create a font object for text rendering

    while running:
        screen.fill((200, 200, 200))  # Fill the screen with a gray color background
        
        # Render the help text with game instructions
        help_text = font.render("Use arrow keys to move. Space to shoot. ESC to go back.", True, (0, 0, 0))
        screen.blit(help_text, (50, 200))  # Display the help text on the screen

        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit pygame if the window is closed
                exit()  # Exit the program
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False  # Exit the help screen when ESC is pressed

        pygame.display.update()  # Update the screen to display the changes
