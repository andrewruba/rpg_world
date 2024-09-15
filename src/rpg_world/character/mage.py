from .base_character import BaseCharacter
from .character_stats import CharacterStats
from ..ability.spell import Spell

class Mage(BaseCharacter):
    def __init__(self, name: str, health: float = 100, mana: float = 100, focus: float = 100, armor: float = 0, spells: list = None):
        """
        Initialize a Mage character with specific attributes, including an optional list of spells.

        Args:
            name (str): The name of the mage.
            health (float): The amount of health the mage has.
            mana (float): The amount of mana the mage has for spellcasting.
            focus (float): The mage's focus, affecting casting speed and success.
            armor (float): The amount of armor the mage has to reduce incoming damage.
            spells (list): A list of Spell objects the mage knows at initialization (optional).
        """
        # Create CharacterStats instance with provided attributes
        stats = CharacterStats(health=health, mana=mana, focus=focus, armor=armor)
        
        # Initialize the BaseCharacter with the name and stats
        super().__init__(name, stats=stats)

        # Initialize spells dictionary
        self.spells = {}

        # If spells are provided, learn them
        if spells:
            for spell in spells:
                self.learn_spell(spell)

    def learn_spell(self, spell: Spell):
        """
        Allow the mage to learn a new spell.

        Args:
            spell (Spell): The spell the mage learns.
        """
        self.spells[spell.name] = spell
        self.logger.info(f"{self.name} learned the spell: {spell.name}.")

    def forget_spell(self, spell_name: str):
        """
        Allow the mage to forget a spell they've learned.

        Args:
            spell_name (str): The name of the spell to forget.
        """
        if spell_name in self.spells:
            del self.spells[spell_name]
            self.logger.info(f"{self.name} forgot the spell: {spell_name}.")
        else:
            self.logger.info(f"{self.name} doesn't know the spell: {spell_name}.")

    def cast_spell(self, spell_name: str, target, current_time: float):
        """
        Cast a spell if the mage has enough mana and the spell is off cooldown.

        Args:
            spell_name (str): The name of the spell to cast.
            target (BaseCharacter): The target of the spell.
            current_time (float): The current time for checking cooldowns.
        """
        # Find the spell by name in the mage's spells
        spell = self.spells.get(spell_name)
        if not spell:
            self.logger.info(f"{self.name} doesn't know the spell: {spell_name}.")
            return

        mana_cost = spell.mana_cost
        current_mana = self.mana
        if current_mana < mana_cost:
            self.logger.info(f"{self.name} doesn't have enough mana to cast {spell.name} (Required: {mana_cost}, Available: {current_mana}).")
            return

        spell_cast_success = spell.cast(self, target, current_time)
        if spell_cast_success:
            self.stats.modify('mana', -mana_cost)
            self.logger.info(f"{self.name} successfully cast {spell_name}. Mana remaining: {self.mana}")

    def __str__(self):
        """
        String representation of the mage's attributes and learned spells.
        """
        attrs = ', '.join(f"{key}: {value}" for key, value in self.stats.attributes.items())
        spells = ', '.join(spell for spell in self.spells.keys())
        return f"Mage {self.name}: {attrs}. Spells: [{spells}]"
