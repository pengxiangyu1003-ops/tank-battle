import pygame
import random
from player import Player
from bullet import Bullet
from character import Character
from scores_manager import load_scores, save_scores
from user_input import get_username  # 导入新的用户输入模块

def game_module(screen, mode="infinite", return_to_menu_callback=None):
    """
    Main game loop for the game module.

    Args:
        screen (pygame.Surface): The screen object to render the game.
        mode (str): The game mode (default is "infinite", or "time_limited").
        return_to_menu_callback (function, optional): A callback function to return to the main menu.

    This function manages the game loop, including:
    - Displaying a background
    - Handling user input (e.g., player movement and shooting)
    - Updating the score
    - Managing different game modes (infinite or time-limited)
    """
    # 获取用户名
    username = get_username(screen)  # Get the username for the game

    # Load background image and scale it
    background = pygame.image.load("assets/background.png")
    background = pygame.transform.scale(background, (900, 700))

    # Load shooting sound effect
    shoot_sound = pygame.mixer.Sound("assets/shoot.mp3")

    # Initialize player, bullets, characters, and score
    player = Player(400, 300)
    bullets = []
    characters = [Character(200, 200), Character(400, 200), Character(600, 200)]  # Create 3 characters
    score = 0  
    clock = pygame.time.Clock()

    # Initialize time tracking for time-limited mode
    start_time = pygame.time.get_ticks()
    time_limit = 60 * 1000  # 60 seconds for time-limited mode

    running = True
    while running:
        # Draw the background
        screen.blit(background, (0, 0))

        # Time-limited mode logic
        if mode == "time_limited":
            elapsed_time = pygame.time.get_ticks() - start_time
            remaining_time = max(0, (time_limit - elapsed_time) // 1000)
            font = pygame.font.Font(None, 36)
            time_text = font.render(f"Time Remaining: {remaining_time}s", True, (255, 255, 255))  
            screen.blit(time_text, (10, 10))  # Display remaining time
            if remaining_time <= 0:  # End game when time is up
                running = False  

        # Get keys pressed for player movement
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit game on quit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Shoot when space is pressed
                    bullets.append(Bullet(player.x + 25, player.y, "up"))  # Create a new bullet
                    shoot_sound.play()  # Play shoot sound

        # Move and draw bullets
        for bullet in bullets[:]:
            bullet.move()
            bullet.draw(screen)

            # Check for collisions between bullets and characters
            for character in characters[:]:
                if character.x <= bullet.x <= character.x + character.width and \
                   character.y <= bullet.y <= character.y + character.height:
                    score += 10  # Increase score on hit
                    bullets.remove(bullet)  # Remove the bullet
                    # Reposition the character randomly
                    character.x = random.randint(0, 700)
                    character.y = random.randint(0, 500)

        # Move and draw characters
        for character in characters:
            character.move()  # Update character's position
            character.draw(screen)  # Draw character on screen

        # Draw player on screen
        player.draw(screen)  

        # Display the score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))  
        screen.blit(score_text, (10, 50))

        # Update the screen and limit the frame rate
        pygame.display.update()
        clock.tick(60)  # Run at 60 frames per second

    # Load the scores and update the player's score
    scores = load_scores()
    scores[username] = max(scores.get(username, 0), score)  # Update score for the player
    save_scores(scores)  # Save the updated scores

    # Show score summary after the game ends
    score_summary(screen, score, return_to_menu_callback)


def score_summary(screen, score, return_to_menu_callback=None):
    """
    Displays the score summary screen after the game ends.

    Args:
        screen (pygame.Surface): The screen object to render the score summary.
        score (int): The final score of the player.
        return_to_menu_callback (function, optional): A callback function to return to the main menu.
    
    This function displays:
    - The final score
    - A "Back to menu" button
    """
    font = pygame.font.Font(None, 72)
    small_font = pygame.font.Font(None, 36)

    # Define the back button's properties
    back_button_radius = 50
    back_button_pos = (screen.get_width() - back_button_radius - 20, back_button_radius + 20)  

    running = True
    while running:
        screen.fill((255, 255, 255))  # Fill the screen with white
        title_text = font.render("Game Over!", True, (0, 0, 0))
        score_text = font.render(f"Your Score: {score}", True, (0, 0, 0))
        menu_text = small_font.render("Click the purple circle to go back to menu", True, (0, 0, 0))

        # Render the texts on screen
        screen.blit(title_text, (200, 200))
        screen.blit(score_text, (200, 300))  
        screen.blit(menu_text, (100, 400))

        # Draw the back button (purple circle)
        pygame.draw.circle(screen, (128, 0, 128), back_button_pos, back_button_radius) 
        back_button_text = small_font.render("Back", True, (255, 255, 255))  
        screen.blit(back_button_text, (back_button_pos[0] - back_button_text.get_width() // 2, back_button_pos[1] - back_button_text.get_height() // 2))

        pygame.display.update()

        # Handle events in the score summary screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                distance = ((mouse_x - back_button_pos[0]) ** 2 + (mouse_y - back_button_pos[1]) ** 2) ** 0.5
                if distance <= back_button_radius:  # Check if the back button is clicked
                    if return_to_menu_callback:  
                        return_to_menu_callback()  # Call the menu callback function

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Quit the game if 'Q' is pressed
                    pygame.quit()
                    exit()
