import pygame

class Bullet:
    """
    A class to represent a bullet in the game.

    Attributes:
        x (int): The x-coordinate of the bullet.
        y (int): The y-coordinate of the bullet.
        speed (int): The speed at which the bullet moves.
        direction (str): The direction in which the bullet moves (e.g., "up").
        bullet_img (pygame.Surface): The image representing the bullet.

    Methods:
        move(): Moves the bullet in the specified direction.
        draw(screen): Draws the bullet on the provided screen.
    """

    def __init__(self, x, y, direction):
        """
        Initializes a Bullet object.

        Args:
            x (int): The starting x-coordinate of the bullet.
            y (int): The starting y-coordinate of the bullet.
            direction (str): The direction in which the bullet will move (e.g., "up").
        """
        self.x = x
        self.y = y
        self.speed = 10  # Set the bullet's speed
        self.direction = direction  # Set the bullet's direction
        self.bullet_img = pygame.image.load("assets/bullet.png")  # Load the bullet image
        self.bullet_img = pygame.transform.scale(self.bullet_img, (25, 30))  # Scale the bullet image

    def move(self):
        """
        Moves the bullet in the specified direction.

        The bullet moves upwards based on the direction set at initialization.
        Additional directions can be added as needed (e.g., "down", "left", "right").
        """
        if self.direction == "up":
            self.y -= self.speed  # Move the bullet upwards

    def draw(self, screen):
        """
        Draws the bullet on the given screen.

        Args:
            screen (pygame.Surface): The screen where the bullet will be drawn.
        """
        screen.blit(self.bullet_img, (self.x, self.y))  # Draw the bullet at its current position
