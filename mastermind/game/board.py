import random
from game.player import Player
from game.move import Move

class Board:
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder

    Attributes:
        _items (dictionary of lists): The code, guess, and hint
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """

        self._items = {} 

    def apply(self, move, player):
        """Applies the given move to the playing surface. In this case, that 
        means updating the current guess of a player.
        
        Args:
            self (Board): an instance of Board.
            move (Move): The move to apply.
            player (Player): The player who made the guess.
        """
        name = player.get_name()
        guess = move.get_digits()
        self._items[name][1] = str(guess)
    
    def has_won(self, player):
        """Determines if the guess equals the code.
        
        Args:
            self (Board): an instance of Board.
            player (Player): The player who made the guess.

        Returns:
            boolean: True if the hint has all xs.
        """
        name = player.get_name()
        return self._items[name][2] == "xxxx"

    def to_string(self):
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """ 
        text =  "\n--------------------"
        for x, y in self._items.items():
            text += (f"\nPlayer " + x + ": " + y[1] + ", " + y[2])
        text += "\n--------------------"
        return text

    def prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
            player (Player): The player who made the guess.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]
        #print()

    def _create_hint(self, move, player):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            player (Player): The player who made the guess.
            move (Move): The current guess.

        """ 
        name = player.get_name()
        guess = str(move.get_digits())
        code = self._items[name][0]
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        
        self._items[name][2] = hint