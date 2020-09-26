class Settings:
    """A class used to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (30, 30, 30)

        # Spaceship settings.
        self.spaceship_speed = 1.5

        # Bullet settings.
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (255, 165, 0)
        self.bullets_allowed = 3

        # Alien settings.
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
        