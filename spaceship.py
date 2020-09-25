import pygame

class Spaceship:
    """A class to manage the spaceship in Alien Invasion."""

    def __init__(self, ai_game):
        """Initialise the spaceship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the spaceship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1

        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw the spaceship at its current location."""
        self.screen.blit(self.image, self.rect)
        