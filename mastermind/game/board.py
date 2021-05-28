import random
from game.player import Player

class Board:
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder

    Attributes:
        _piles (list): The number of piles of stones.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """

        self._items = {} 
        self._prepare()

    def apply(self, move):
        """Applies the given move to the playing surface. In this case, that 
        means removing a number of stones from a pile.
        
        Args:
            self (Board): an instance of Board.
            move (Move): The move to apply.
        """
        row = move.get_row()
        stones = move.get_stones()
        self._piles[pile] = max(0, self._piles[pile] - stones)
    
    def has_won(self, hint):
        """Determines if all the stones have been removed from the board.
        
        Args:
            self (Board): an instance of Board.

        Returns:
            boolean: True if the board has no stones on it; false if otherwise.
        """
        return hint == "xxxx"

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

    def _prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]