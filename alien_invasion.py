import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

        # Create an instance to store game statistics, and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.spaceship = Spaceship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Make buttons.
        self.play_button = Button(self, 
            pygame.image.load('assets/images/play_button.bmp'))
        self.help_button = Button(self, 
            pygame.image.load('assets/images/help_button.bmp'))
        self.resume_button = Button(self, 
            pygame.image.load('assets/images/resume_button.bmp'))

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active and not self.stats.game_paused:
                self.spaceship.update()
                self._update_bullets()
                self._update_aliens()

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
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_resume_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if (button_clicked and not self.stats.game_active and 
            not self.stats.game_paused):
            # Reset the game settings.
            self.settings.initialise_dynamic_settings

            # Reset game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_spaceships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the spaceship.
            self._create_fleet()
            self.spaceship.center_spaceship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_resume_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.resume_button.rect.collidepoint(mouse_pos)
        if button_clicked and self.stats.game_active and self.stats.game_paused:
            self.stats.game_paused = False
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

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
        elif event.key == pygame.K_p:
            self.stats.game_paused = True
            # Show the mouse cursor.
            pygame.mouse.set_visible(True)

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
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens_x = available_space_x // (2 * alien_width)
        alien_spacing_x = (number_of_aliens_x * 
            alien_width) // (number_of_aliens_x - 1)

        # Determine the number of rows of aliens that fit on the screen.
        spaceship_height = self.spaceship.rect.height
        avialable_space_y = self.settings.screen_height - ((5 * alien_height) + spaceship_height)
        number_of_rows = avialable_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_of_rows):
            for alien_number in range(number_of_aliens_x):
                self._create_alien(alien_number, alien_spacing_x, row_number)
               

    def _create_alien(self, alien_number, alien_spacing_x, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + ((alien_width + alien_spacing_x) * 
            alien_number)
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 50 + (2 * alien_height * row_number)
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _spaceship_hit(self):
        """Respond to the spaceship being hit by an alien."""
        if self.stats.spaceships_left > 0:
            # Decrement spaceships_left, and update scoreboard.
            self.stats.spaceships_left -= 1
            self.sb.prep_spaceships()

            # Check to see if the has anymore spaceships left.
            if self.stats.spaceships_left <= 0:
                 self.stats.game_active = False
                 pygame.mouse.set_visible(True)
                 return

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the spaceship.
            self._create_fleet()
            self.spaceship.center_spaceship()

            # Pause to allow player to get ready.
            sleep(0.5)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom - 20:
                self._spaceship_hit()
                break

    def _update_aliens(self):
        """
        Check if the fleet is at an edge, then update the positions of all 
        aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.spaceship, self.aliens):
            self._spaceship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _update_screen(self):
        # Update images on the screen, and flip to the new screen.
        self.screen.fill(self.settings.bg_colour)
        self.spaceship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is invactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Draw the resume button if the game is paused.
        if self.stats.game_paused:
            self.resume_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

        