class Settings:
    """Store all settings for Rocket Ship"""

    def __init__(self):
        """Initialize game settings"""
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_coulor = (230, 230, 230)

        # Ship
        self.rocket_speed = 5