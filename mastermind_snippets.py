def prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]
        
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