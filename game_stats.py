class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize Statistics."""
        self.settings = ai_game.settings
        self.difficulty_modifier = .1
        self.reset_stats()

        # Start Alien Invasion in an active state
        self.game_active = False

    def reset_stats(self):
        """Initialize Statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.settings.speedup_scale = 1 + self.difficulty_modifier
        self.score = 0
