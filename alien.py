import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the wave."""

    def __init__(self, ai_game):
        """Initialise the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.finder = ai_game.finder

        # Load the alien image and set its rect attribute."""
        self.image = pygame.image.load(self.finder.find_data_file(
            'alien.bmp', 'images'))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right or left."""
        self.x += (self.settings.alien_speed * self.settings.wave_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return Ture if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right - 20 or self.rect.left <= 20:
            return True

        
