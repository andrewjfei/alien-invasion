import pygame.font

class Button:
    """A button that can be used to start Alien Invasion."""

    def __init__(self, ai_game, button_img):
        """Initialise button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Load the play button image and set its rect attribute."""
        self.button_img = button_img
        self.rect = self.button_img.get_rect()
        self.rect.center = self.screen_rect.center

    def draw_button(self):
        # Draw button.
        self.screen.blit(self.button_img, self.rect)