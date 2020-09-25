import sys

import pygame

from settings import Settings
from spaceship import Spaceship

class AlienInvasion:
    """Overall class used to manage game assets and behaviour."""

    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.spaceship = Spaceship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        # Repspond to keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the spaceship to the right.
                    self.spaceship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Move the spaceship to the left.
                    self.spaceship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.spaceship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.spaceship.moving_left = False


    def _update_screen(self):
        # Update images on the screen, and flip to the new screen.
        self.screen.fill(self.settings.bg_colour)
        self.spaceship.update()
        self.spaceship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()



if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

        