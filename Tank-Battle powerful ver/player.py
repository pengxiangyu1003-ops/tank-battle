import pygame
import cv2

class Player:
    def __init__(self, x, y, video_path="assets/jack.mp4", scale_width=100, scale_height=110):
        """
        Initialize the Player object with initial position, video settings, and speed.

        :param x: The initial x-coordinate of the player
        :param y: The initial y-coordinate of the player
        :param video_path: The path to the video file for the player's animation (default is "assets/jack.mp4")
        :param scale_width: The width to scale the video frames to (default is 100)
        :param scale_height: The height to scale the video frames to (default is 110)
        """
        self.x = x
        self.y = y
        self.speed = 5  # Speed at which the player moves
        self.scale_width = scale_width  # Width to scale each frame of the video
        self.scale_height = scale_height  # Height to scale each frame of the video

        self.video_path = video_path  # Path to the video used for the player's animation
        self.frames = self.load_video(video_path)  # Load the video frames into memory
        self.frame_index = 0  # Index to track the current frame
        self.frame_count = len(self.frames)  # Total number of frames in the video

    def load_video(self, video_path):
        """
        Load the video from the specified path and convert each frame into a Pygame Surface.

        :param video_path: Path to the video file to be loaded
        :return: A list of Pygame surfaces representing each frame of the video
        """
        cap = cv2.VideoCapture(video_path)  # Open the video file
        frames = []  # List to store frames as Pygame surfaces
        
        while cap.isOpened():
            ret, frame = cap.read()  # Read each frame from the video
            if not ret:
                break  # Stop if no more frames are available
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB color format
            frame = cv2.resize(frame, (self.scale_width, self.scale_height))  # Scale the frame to the desired size
            frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)  # Rotate the frame 90 degrees counterclockwise
            
            frame_surface = pygame.surfarray.make_surface(frame)  # Convert the frame to a Pygame surface
            frames.append(frame_surface)  # Add the surface to the list of frames
        
        cap.release()  # Release the video capture object after loading all frames
        return frames

    def move(self, keys):
        """
        Move the player based on keyboard input.

        :param keys: The state of all keyboard keys (typically returned by pygame.key.get_pressed())
        """
        if keys[pygame.K_LEFT]:  # Move player left
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:  # Move player right
            self.x += self.speed
        if keys[pygame.K_UP]:  # Move player up
            self.y -= self.speed
        if keys[pygame.K_DOWN]:  # Move player down
            self.y += self.speed

    def draw(self, screen):
        """
        Draw the current frame of the player's animation to the screen at the player's position.

        :param screen: The Pygame screen surface to draw the player to
        """
        if self.frame_count > 0:  # Ensure there are frames to display
            # Display the current frame at the player's current position
            screen.blit(self.frames[self.frame_index], (self.x, self.y))

            # Move to the next frame for the next call to this method
            self.frame_index += 1
            if self.frame_index >= self.frame_count:
                self.frame_index = 0  # Loop back to the first frame after the last frame
