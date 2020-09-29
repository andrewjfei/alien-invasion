import pygame.font

from settings import Settings

class HowToPlay:
    """Class used to render how to play text as an image."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Font settings for scoring information.
        self.medium_font = pygame.font.Font('assets/fonts/slkscre.ttf', 20)
        self.large_font = pygame.font.Font('assets/fonts/slkscre.ttf', 36)

        # Prepare how to play text.
        self._prep_title()
        self._prep_text()

    def _prep_title(self):
        """Turn the title into a rendered image."""
        title_str = 'How To Play'
        self.title_image = self.large_font.render(title_str, True, 
        self.settings.text_colour, self.settings.bg_colour)

        # Display the title in the middle top of the screen.
        self.title_rect = self.title_image.get_rect()
        self.title_rect.centerx = self.screen_rect.centerx
        self.title_rect.top = 100

    def _prep_text(self):
        """Turn the help into a rendered image."""
        text = [
            '1. Use the left and right arrow keys to move the spaceship.',
            '2. Press the space key to fire a bullet.',
            '3. Only 3 bullets can be active at a time.',
            '4. If a bullet hits an alien, the alien is destroyed.',
            '5. When an entire fleet is destroyed, a more advanced fleet '
            'appears.',
            '6. If an alien reaches the spaceship the spaceship is destroyed.',
            '7. If an alien reaches the bottom of the screen the spaceship is ' 
            'destroyed',
            '8. After 3 spaceships have been destroyed the game is over.',
            '9. Destroy as many aliens as you possibly can. Good Luck!']

        self.text_images = []
        self.text_rects = []

        for line in text:
            self.text_images.append(self.medium_font.render(line, True, 
                self.settings.text_colour, self.settings.bg_colour))

        for index in range(len(self.text_images)):
            # Display the help text in the middle of the screen under the title.
            self.text_rects.append(self.text_images[index].get_rect())
            self.text_rects[index].centerx = self.title_rect.centerx
            self.text_rects[index].top = self.title_rect.bottom + 100 + (
                (self.text_rects[index].height + 20) * index)

    def show_help(self):
        """Draw the help text including the title onto the screen."""
        self.screen.blit(self.title_image, self.title_rect)

        for index in range(len(self.text_images)):
            self.screen.blit(self.text_images[index], self.text_rects[index])
