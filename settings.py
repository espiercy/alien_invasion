class Settings:
    """A class to store all settings for alien invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.0

        # How difficult...
        self.difficulty_level = 'normal'

        # How quickly the alien point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that changed throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.set_speedup_scale()

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def set_speedup_scale(self):
        if self.difficulty_level == 'normal':
            self.speedup_scale = 1.1
        elif self.difficulty_level == 'hard':
            self.speedup_scale = 1.5
        elif self.difficulty_level == 'crazy':
            self.speedup_scale = 2.0

    def reset_speed(self):
        """have to reset speeds to original values on endgame"""
        self.difficulty_level = 'normal'
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0