import sys

import pygame

from settings import Settings
from spaceship import Spaceship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class used to manage game assets and behaviour."""

    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Uncomment code to run Alien Invasion in full screen mode.
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        # Comment line out when trying to run Alien Invasion in full screen
        # mode.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.spaceship = Spaceship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.spaceship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        # Repspond to keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # Move the spaceship to the right.
            self.spaceship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the spaceship to the left.
            self.spaceship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.spaceship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.spaceship.moving_left = False

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Determine equal spacing between all aliens in the row.
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens_x = available_space_x // (2 * alien_width)
        alien_spacing_x = (number_of_aliens_x * 
            alien_width) // (number_of_aliens_x - 1)

        # Create the first row of aliens.
        for alien_number in range(number_of_aliens_x):
            #Create an alien and place it in the row.
            alien = Alien(self)
            alien.x = alien_width + ((alien_width + alien_spacing_x) * 
                alien_number)
            alien.rect.x = alien.x
            self.aliens.add(alien)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positons.
        self.bullets.update()

         # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        # Update images on the screen, and flip to the new screen.
        self.screen.fill(self.settings.bg_colour)
        self.spaceship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()



if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

        