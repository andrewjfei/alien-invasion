import pygame.font
from pygame.sprite import Group

from small_spaceship import SmallSpaceship

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialise scorekepping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.finder = ai_game.finder
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.small_font = pygame.font.Font(self.finder.find_data_file(
            'silkscreen.ttf', 'fonts'), 16)
        self.medium_font = pygame.font.Font(self.finder.find_data_file(
            'silkscreen.ttf', 'fonts'), 24)
        self.large_font = pygame.font.Font(self.finder.find_data_file(
            'silkscreen.ttf', 'fonts'), 36)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_wave()
        self.prep_spaceships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.medium_font.render(score_str, True, 
            self.settings.text_colour, self.settings.bg_colour)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score_text = "High Score"
        self.high_score_text_image = self.small_font.render(high_score_text, True, 
            self.settings.text_colour, self.settings.bg_colour)

        # Center the high score at the top of the screen.
        self.high_score_text_rect = self.high_score_text_image.get_rect()
        self.high_score_text_rect.centerx = self.screen_rect.centerx
        self.high_score_text_rect.top = self.score_rect.top

        """Turn the high score into a rendered image."""
        high_score_str = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.large_font.render(high_score_str, True, 
            self.settings.text_colour, self.settings.bg_colour)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.high_score_text_rect.bottom + 6

    def prep_wave(self):
        """Turn the wave into a rendered image."""
        wave_str = "Wave " + str(self.stats.wave)
        self.wave_image = self.medium_font.render(wave_str, True, 
            self.settings.text_colour, self.settings.bg_colour)

        # Position the wave below the score.
        self.wave_rect = self.wave_image.get_rect()
        self.wave_rect.right = self.score_rect.right
        self.wave_rect.top = self.score_rect.bottom + 10

    def prep_spaceships(self):
        """Show how many ships are left."""
        self.spaceships = Group()
        for spaceship_number in range(self.stats.spaceships_left):
            spaceship = SmallSpaceship(self.ai_game)
            spaceship.rect.x = 20 + (spaceship_number * 
                spaceship.rect.width) + (spaceship_number * 10)
            spaceship.rect.y = 20
            self.spaceships.add(spaceship)

    def show_score(self):
        """Draw score and wave to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_text_image, self.high_score_text_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.wave_image, self.wave_rect)
        self.spaceships.draw(self.screen)

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            filename = 'high_score.txt'

            with open(filename, 'w') as file:
                file.write(str(self.stats.score))

            self.stats.high_score = self.stats.score
            self.prep_high_score()
