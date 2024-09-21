from .character import Character
from ..stats.character_stats import CharacterStats
from ..ability.spell import Spell

class Mage(Character):
    def __init__(self, name: str, health: float = 100, mana: float = 100, focus: float = 100, armor: float = 0, spells: list = None):
        """
        Initialize a Mage character with specific attributes, including health, mana, focus, armor, and spells.

        Args:
            name (str): The name of the mage character.
            health (float): The amount of health the mage has. Defaults to 100.
            mana (float): The amount of mana the mage has for casting spells. Defaults to 100.
            focus (float): The mage's focus, affecting casting speed and spell success. Defaults to 100.
            armor (float): The amount of armor the mage has, reducing incoming damage. Defaults to 0.
            spells (list, optional): A list of Spell objects that the mage knows at initialization. Defaults to None.
        """
        # Create CharacterStats instance with provided attributes
        stats = CharacterStats(health=health, mana=mana, focus=focus, armor=armor)
        
        # Initialize the Character with the name and stats
        super().__init__(name, stats=stats)

        # Initialize spells dictionary
        self.spells = {}

        # If spells are provided, teach them to the mage
        if spells:
            for spell in spells:
                self.learn_spell(spell)

    def learn_spell(self, spell: Spell):
        """
        Allow the mage to learn a new spell by adding it to their spell list.

        Args:
            spell (Spell): The spell object that the mage learns.
        """
        self.spells[spell.name] = spell
        self.logger.info(f"{self.name} learned the spell: {spell.name}.")

    def forget_spell(self, spell_name: str):
        """
        Allow the mage to forget a spell by removing it from their spell list.

        Args:
            spell_name (str): The name of the spell the mage wants to forget.
        """
        if spell_name in self.spells:
            del self.spells[spell_name]
            self.logger.info(f"{self.name} forgot the spell: {spell_name}.")
        else:
            self.logger.info(f"{self.name} doesn't know the spell: {spell_name}.")

    def cast_spell(self, spell_name: str, target, current_time: float):
        """
        Cast a spell if the mage knows the spell, has enough mana, and the spell is off cooldown.

        Args:
            spell_name (str): The name of the spell to cast.
            target (Character): The target of the spell (another character).
            current_time (float): The current time (as a timestamp) used to check for spell cooldowns.

        Returns:
            None
        """
        # Find the spell by name in the mage's spell list
        spell = self.spells.get(spell_name)
        if not spell:
            self.logger.info(f"{self.name} doesn't know the spell: {spell_name}.")
            return

        mana_cost = spell.mana_cost
        current_mana = self.mana
        if current_mana < mana_cost:
            self.logger.info(f"{self.name} doesn't have enough mana to cast {spell.name} (Required: {mana_cost}, Available: {current_mana}).")
            return

        # Cast the spell if enough mana and cooldown is valid
        spell_cast_success = spell.cast(self, target, current_time)
        if spell_cast_success:
            self.stats.modify('mana', -mana_cost)
            self.logger.info(f"{self.name} successfully cast {spell_name}. Mana remaining: {self.mana}")

    def __str__(self):
        """
        Provides a string representation of the mage's attributes and known spells.

        Returns:
            str: A string containing the mage's stats and the spells they have learned.
        """
        attrs = ', '.join(f"{key}: {value}" for key, value in self.stats.attributes.items())
        spells = ', '.join(spell for spell in self.spells.keys())
        return f"Mage {self.name}: {attrs}. Spells: [{spells}]"
