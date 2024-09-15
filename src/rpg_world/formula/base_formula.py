from abc import ABC, abstractmethod

class BaseFormula(ABC):
    """
    Abstract base class for all formulas that calculate effect values.
    """

    @abstractmethod
    def calculate(self, **kwargs):
        """
        Abstract method to calculate the effect value.
        
        Args:
            **kwargs: Additional context variables.
        
        Returns:
            The result of the calculation.
        """
        pass
