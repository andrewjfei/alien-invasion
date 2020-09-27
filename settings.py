class Settings:
    """A class used to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's static settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (30, 30, 30)

        # Spaceship settings.
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (255, 165, 0)
        self.bullets_allowed = 3

        # Alien settings.
        self.fleet_drop_speed = 10

        # How quickly the game speeds up.
        self.speedup_scale = 1.1

        # How quickly the alien point value increases.
        self.score_scale = 2

        self.initialise_dynamic_settings()


    def initialise_dynamic_settings(self):
        """Initialise settings that change throughout the game."""
        self.spaceship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.5

        # Fleet direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.spaceship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

        