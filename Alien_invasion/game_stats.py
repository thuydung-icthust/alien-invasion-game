class GameStats():
        """ Track Statistics for Alien Invansion """
        def __init__(self, ai_settings):
                """Initialize statistics. """
                self.ai_settings = ai_settings
                self.reset_stats()
                # Start the game in inactive state.
                self.game_active = False

                # High score should never be reset
                
                
        def reset_stats(self):
                """Initialize statistics that can change during the game."""
                self.ships_left = self.ai_settings.ship_limit
                self.score = 0
                self.level = 1
                with open ('highscore.txt', 'r') as f:
                        saved_high_score = f.read()
                        if saved_high_score == '':
                                self.high_score = 0
                        else:  
                                self.high_score = int(saved_high_score)