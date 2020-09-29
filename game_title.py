import pygame.font

from settings import Settings

class GameTitle:
    """Class used to render the game title: Alien Invasion."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.title = self.settings.title

        self.font = pygame.font.Font('assets/fonts/slkscre.ttf', 60)

        self.title_image = self.font.render(self.title, True, 
            self.settings.text_colour, self.settings.bg_colour)

        # Display the title at the top middle of the screen.
        self.title_rect = self.title_image.get_rect()
        self.title_rect.centerx = self.screen_rect.centerx
        self.title_rect.top = 200

    def draw_title(self):
        self.screen.blit(self.title_image, self.title_rect)
