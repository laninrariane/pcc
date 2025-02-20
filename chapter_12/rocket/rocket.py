import pygame


class Rocket:
    """Class to manage rocket ship object"""

    def __init__(self, rs_game):
        """Initialize rocket and set starting position"""
        self.screen = rs_game.screen
        self.settings = rs_game.settings
        self.screen_rect = rs_game.screen.get_rect()

        # Load rocket image and get rect
        self.image = pygame.image.load("images/rocket.bmp")
        self.rect = self.image.get_rect()

        # Ship starts at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store float for horizontal and vertical positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update ship position based on flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.rocket_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)
