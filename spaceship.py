import pygame

class Spaceship:
    """A class to manage the spaceship in Alien Invasion."""

    def __init__(self, ai_game):
        """Initialise the spaceship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('assets/images/spaceship.bmp')
        self.rect = self.image.get_rect()

        self.center_spaceship()

        # Movement flag.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the spaceship's position based on the movement flag."""
        # Update ths spaceship;s x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.spaceship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.spaceship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the spaceship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_spaceship(self):
        """Center the ship on the screen."""
        # Start each new spaceship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Make sure spaceship is not touching the bottom of the screen.
        self.rect.y = self.rect.y - self.rect.height

        # Store a decimal value for the spaceship's horizontal postion.
        self.x = float(self.rect.x)
        