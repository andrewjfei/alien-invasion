class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

        filename = 'high_score.txt'

        with open(filename, 'r+') as file:
            high_score_str = file.read()
            if high_score_str:
                self.high_score = int(high_score_str)

    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.spaceships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        