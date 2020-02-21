import pygame.font

class Button:

    def __init__(self, ai_game, button_color, width, height):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = width, height
        self.button_color = button_color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self, msg, bottom=None, left=None):
        # Draw blank button and then draw message.
        if not bottom:
            self.rect.center = self.screen_rect.center
        else:
            self.rect.bottom = bottom
            self.rect.left = left
        # The button message needs to be prepped only once.
        self._prep_msg(msg)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)