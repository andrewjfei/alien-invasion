class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Make sure game is initially paused (e.g. not running).
        self.game_paused = False

        # Make sure help screen is initally not open.
        self.help_active = False

        # High score should never be reset.
        self.high_score = 0

        filename = 'high_score.txt'

        with open(filename, 'a+') as file:
            file.seek(0)
            high_score_str = file.read()
            if high_score_str:
                self.high_score = int(high_score_str)

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
        self._prep_wave()

    def show_stats(self):
        """Draws the users score for the game onto the screen."""
        