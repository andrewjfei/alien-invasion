import pygame.font

class Button:
    """A button that can be used to start Alien Invasion."""

    def __init__(self, ai_game, msg):
        """Initialise button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Load the play button image and set its rect attribute."""
        self.play_button_image = pygame.image.load('images/play_button.bmp')
        self.rect = self.play_button_image.get_rect()
        self.rect.center = self.screen_rect.center

    def draw_button(self):
        # Draw button.
        self.screen.blit(self.play_button_image, self.rect)