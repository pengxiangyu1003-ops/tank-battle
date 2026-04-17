import pygame

def get_username(screen):
    """
    Prompts the user to input their username.

    This function displays an input box on the screen, allowing the user to type in their username.
    The user can confirm the input by pressing the Enter key or clear the input using the Backspace key.
    The function will return the entered text (username) once the user presses Enter.

    :param screen: The Pygame screen object where the input box will be drawn.
    :return: The username entered by the user as a string.
    """
    
    # Set up the font for rendering text on the screen
    font = pygame.font.Font(None, 36)

    # Define the dimensions and position of the input box
    input_box = pygame.Rect(300, 300, 300, 40)

    # Colors for inactive and active states of the input box
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive  # Initially set the color to inactive

    # Initial state of the input box
    active = False  # Whether the input box is active or not
    text = ''  # Holds the user's input text
    done = False  # Whether the user has finished inputting their username

    # Main input loop
    while not done:
        # Fill the screen with a background color
        screen.fill((30, 30, 30))

        # Draw the input box with the appropriate color (active or inactive)
        pygame.draw.rect(screen, color, input_box, 2)

        # Render the current text in the input box
        txt_surface = font.render(text, True, pygame.Color('white'))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        # Adjust the width of the input box to fit the text
        input_box.w = max(300, txt_surface.get_width() + 10)

        # Handle events (keyboard, mouse, quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit the game if the window is closed
                exit()  # Exit the program

            # Handle mouse clicks for activating the input box
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):  # Check if the mouse click is within the input box
                    active = True
                    color = color_active  # Change the color to active
                else:
                    active = False
                    color = color_inactive  # Change the color to inactive

            # Handle keyboard events for text input
            if event.type == pygame.KEYDOWN:
                if active:  # Only accept input when the input box is active
                    if event.key == pygame.K_RETURN:  # User presses Enter to confirm input
                        done = True
                    elif event.key == pygame.K_BACKSPACE:  # User presses Backspace to delete last character
                        text = text[:-1]
                    else:
                        text += event.unicode  # Add the typed character to the text

        # Update the display and redraw the screen
        pygame.display.update()
        pygame.display.flip()  # Make the changes visible to the user

    # Return the entered text (username)
    return text
