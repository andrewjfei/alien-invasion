import pygame.font

class Text:
    """Class used to display text on the screen."""

    def __init__(self, ai_game, text, size):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.finder = ai_game.finder

        self.font = pygame.font.Font(self.finder.find_data_file(
            'silkscreen.ttf', 'fonts'), size)

        self.text_image = self.font.render(text, True, 
            self.settings.text_colour, self.settings.bg_colour)

        # Display the text in the middle of the screen.
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.screen_rect.center

    def draw_text(self):
        self.screen.blit(self.text_image, self.text_rect)