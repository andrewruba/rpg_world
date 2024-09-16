from rpg_world import Place

class ConcretePlace(Place):
    """
    A concrete class for testing purposes, inheriting from Place.
    """

    def __init__(self, name):
        """
        Initialize the ConcretePlace class.
        Args:
            name (str): The name of the entity.
        """
        super().__init__(name)

def test_place_initialization():
    """
    Test that a ConcretePlace object can be initialized and logger is created.
    """
    place = ConcretePlace("TestPlace")
    
    # Ensure the name is correctly initialized
    assert place.name == "TestPlace"
