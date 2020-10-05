import pygame.font

class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialise statistics."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.finder = ai_game.finder
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Initially set get ready to false.
        self.get_ready = False

        # Counter used to for count down before the game starts.
        self.get_ready_counter = 3

        # Set incoming wave of aliens initially to false.
        self.incoming_wave = False

        # Make sure game is initially paused (e.g. not running).
        self.game_paused = False

        # Make sure help screen is initally not open.
        self.help_active = False

        # Initially set game over to false.
        self.game_over = False

        # High score should never be reset.
        self.high_score = 0

        filename = 'high_score.txt'

        with open(filename, 'a+') as file:
            file.seek(0)
            high_score_str = file.read()
            if high_score_str:
                self.high_score = int(high_score_str)

    def reset_counter(self):
        self.get_ready_counter = 3

    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.spaceships_left = self.settings.ship_limit
        self.score = 0
        self.wave = 1
        self.aliens_destroyed = 0
        self.bullets_fired = 0

    def _prep_stats(self):
        """Pepare stats text."""
        self._prep_game_over_text()
        self._prep_bullets_fired()
        self._prep_aliens_destroyed()
        self._prep_accuracy()
        self._prep_wave()
        self._prep_score()

    def _prep_game_over_text(self):
        """Show game over text."""
        game_over_title_str = 'Game Over!'
        self.game_over_title_image = self.large_font.render(
            game_over_title_str, True, self.settings.text_colour, 
            self.settings.bg_colour)

        # Display the title in the middle top of the screen.
        self.game_over_title_rect = self.game_over_title_image.get_rect()
        self.game_over_title_rect.centerx = self.screen_rect.centerx
        self.game_over_title_rect.top = 200

    def _prep_bullets_fired(self):
        """Show how many bullets the user fired during the game."""
        bullets_fired_str = f'Bullets Fired: {self.bullets_fired}'
        self.bullets_fired_image = self.small_font.render(
            bullets_fired_str, True, self.settings.text_colour, 
            self.settings.bg_colour)

        # Display the bullets fired under the title.
        self.bullets_fired_rect = self.bullets_fired_image.get_rect()
        self.bullets_fired_rect.centerx = self.screen_rect.centerx
        self.bullets_fired_rect.top = self.game_over_title_rect.bottom + 50

    def _prep_aliens_destroyed(self):
        """Show how many aliens the user destroyed during the game."""
        aliens_destroyed_str = f'Aliens Destroyed: {self.aliens_destroyed}'
        self.aliens_destroyed_image = self.small_font.render(
            aliens_destroyed_str, True, self.settings.text_colour, 
            self.settings.bg_colour)

        # Display the number aliens destroyed under the title.
        self.aliens_destroyed_rect = self.aliens_destroyed_image.get_rect()
        self.aliens_destroyed_rect.centerx = self.screen_rect.centerx
        self.aliens_destroyed_rect.top = self.bullets_fired_rect.bottom + 20

    def _prep_accuracy(self):
        """Show how many aliens the user destroyed during the game."""
        if self.bullets_fired != 0:
            accuracy = int((self.aliens_destroyed / self.bullets_fired) * 100)
        else:
            accuracy = 0
        accuracy_str = f'Accuracy: {accuracy}%'
        self.accuracy_image = self.small_font.render(
            accuracy_str, True, self.settings.text_colour, 
            self.settings.bg_colour)

        # Display the number aliens destroyed under the title.
        self.accuracy_rect = self.accuracy_image.get_rect()
        self.accuracy_rect.centerx = self.screen_rect.centerx
        self.accuracy_rect.top = self.aliens_destroyed_rect.bottom + 20

    def _prep_wave(self):
        """Show the wave the user got to before losing."""
        wave_str = f'Wave Reached: {self.wave}'
        self.wave_image = self.small_font.render(wave_str, True, 
            self.settings.text_colour, self.settings.bg_colour)

        # Display the wave reached under the title.
        self.wave_rect = self.wave_image.get_rect()
        self.wave_rect.centerx = self.screen_rect.centerx
        self.wave_rect.top = self.accuracy_rect.bottom + 20

    def _prep_score(self):
        """Show the user's total score for the game."""
        score_str = f'Score: {self.score}'
        self.score_image = self.small_font.render(score_str, True, 
            self.settings.text_colour, self.settings.bg_colour)

        # Display the wave reached under the title.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = self.wave_rect.bottom + 20

    def show_stats(self):
        """Draws the users score for the game onto the screen."""
        # Font settings for scoring information.
        self.small_font = pygame.font.Font(self.finder.find_data_file(
            'silkscreen.ttf', 'fonts'), 24)
        self.large_font = pygame.font.Font(self.finder.find_data_file(
            'silkscreen.ttf', 'fonts'), 48)

        # Prepare stats to draw onto screen.
        self._prep_stats()

        self.screen.blit(self.game_over_title_image, self.game_over_title_rect)
        self.screen.blit(self.bullets_fired_image, self.bullets_fired_rect)
        self.screen.blit(self.aliens_destroyed_image, 
            self.aliens_destroyed_rect)
        self.screen.blit(self.accuracy_image, self.accuracy_rect)
        self.screen.blit(self.wave_image, self.wave_rect)
        self.screen.blit(self.score_image, self.score_rect)
        