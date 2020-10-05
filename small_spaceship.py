import pygame
from pygame.sprite import Sprite

class SmallSpaceship(Sprite):
    """A class to used to show the number of spaceships left."""

    def __init__(self, ai_game):
        """Initialise the spaceship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.finder = ai_game.finder
        self.screen_rect = ai_game.screen.get_rect()

        # Load the small spaceship image and get its rect.
        self.image = pygame.image.load(self.finder.find_data_file(
            'small_spaceship.bmp', 'images'))
        self.rect = self.image.get_rect()