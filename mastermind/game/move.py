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

    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint