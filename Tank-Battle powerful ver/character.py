import pygame
import random

class Character:
    """
    A class to represent a character in the game.

    Attributes:
        x (int): The x-coordinate of the character.
        y (int): The y-coordinate of the character.
        character_img (pygame.Surface): The image representing the character.
        width (int): The width of the character image.
        height (int): The height of the character image.
        speed_x (int): The horizontal speed of the character.
        speed_y (int): The vertical speed of the character.

    Methods:
        move(): Moves the character within the screen boundaries, reversing direction when hitting edges.
        draw(screen): Draws the character on the provided screen.
    """

    def __init__(self, x, y):
        """
        Initializes a Character object with random movement speeds.

        Args:
            x (int): The starting x-coordinate of the character.
            y (int): The starting y-coordinate of the character.
        """
        self.x = x
        self.y = y
        self.character_img = pygame.image.load("assets/character.png")  # Load character image
        self.character_img = pygame.transform.scale(self.character_img, (100, 110))  # Scale character image
        self.width = 100  # Width of the character
        self.height = 110  # Height of the character
        self.speed_x = random.randint(1, 2)  # Random horizontal speed
        self.speed_y = random.randint(1, 2)  # Random vertical speed

    def move(self):
        """
        Moves the character within the screen boundaries.

        The character moves by its speed values. If it hits the edge of the screen, 
        its direction will reverse, and a new random speed will be assigned.

        This ensures the character bounces off the edges of the screen.
        """
        self.x += self.speed_x  # Move character horizontally
        self.y += self.speed_y  # Move character vertically
        
        # Reverse direction and randomly adjust speed if the character hits the screen edges
        if self.x <= 0 or self.x + self.width >= 800:  
            self.speed_x = random.choice([-1, 1]) * random.randint(1, 2)  # Randomize horizontal direction and speed

        if self.y <= 0 or self.y + self.height >= 600: 
            self.speed_y = random.choice([-1, 1]) * random.randint(1, 2)  # Randomize vertical direction and speed

    def draw(self, screen):
        """
        Draws the character on the given screen.

        Args:
            screen (pygame.Surface): The screen where the character will be drawn.
        """
        screen.blit(self.character_img, (self.x, self.y))  # Render character at its current position
