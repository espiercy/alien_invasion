class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize Statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state
        self.game_active = False

        # High score should never be reset. We will get the inital high_score from a file in the same directory
        self._get_high_score()

    def reset_stats(self):
        """Initialize Statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.game_active = True

    def _get_high_score(self):
        with open('high_score.txt', 'r') as high_score_file:
            self.high_score = high_score_file.read()
            if not self.high_score:
                self.high_score = 0

            self.high_score = int(self.high_score)

    def update_high_score(self):
        with open('high_score.txt', 'r+') as high_score_file:
            old_score = high_score_file.read()
            if not old_score or self.score > old_score:
                high_score_file.write(str(self.score))