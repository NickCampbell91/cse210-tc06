class Move:
    """A maneuver in the game. The responsibility of Move is to keep track of the digits from the user and check if they are the given number.
    
    Stereotype: 
        Information Holder

    Attributes:
        _digits (integer): The digits to remove from.
    """
    def __init__(self, digits):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._digits = digits

    def get_digits(self):
        """Returns the digits to remove from.

        Args:
            self (Move): an instance of Move.
        """
        return self._digits

    