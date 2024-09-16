class GameState:
    def __init__(self):
        """
        Initialize the game state to track the current status of characters, world, quests, and more.
        """
        self.current_location = None
        self.characters = {}
        self.quests = []
        self.inventory = None
        self.time_of_day = None
        self.weather = None

    def update_location(self, location):
        """
        Update the current location in the game state.

        Args:
            location (Location): The new location to update.
        """
        self.current_location = location

    def add_character(self, character):
        """
        Add a character to the game state.

        Args:
            character (Character): The character to add.
        """
        self.characters[character.name] = character

    def update_quests(self, quest):
        """
        Update the current quests in the game state.

        Args:
            quest (Quest): The updated quest status.
        """
        self.quests.append(quest)

    def update_time_of_day(self, time_of_day):
        """
        Update the time of day in the game state.

        Args:
            time_of_day (TimeOfDay): The current time of day.
        """
        self.time_of_day = time_of_day

    def update_weather(self, weather):
        """
        Update the weather in the game state.

        Args:
            weather (Weather): The current weather.
        """
        self.weather = weather

    def get_game_snapshot(self):
        """
        Retrieve a snapshot of the current game state.
        """
        return {
            "location": self.current_location,
            "characters": self.characters,
            "quests": self.quests,
            "time_of_day": self.time_of_day,
            "weather": self.weather,
        }
