from game.board import Board
from game.console import Console
from game.move import Move
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        board (Board): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        move (Move): An instance of the class of objects known as Move.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        self._move = None
        self._roster = Roster()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        num_players = int(input("Number of players: "))
        for n in range(num_players):
            name = self._console.read(f"Enter a name for player {n + 1}: ") # call the prepare function from board out to director - remove underscore from "_prepare" hence unprivatize
            player = Player(name)
            self._roster.add_player(player)
            self._board.prepare(player)
        self._roster.next_player()
    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        board = self._board.to_string()
        self._console.write(board)
        # get next player's move
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        digits = self._console.read_number("What is your guess? ")  # read user input
        move = Move(digits)
        player.set_move(move)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        move = player.get_move()
        self._board.apply(move, player)
        self._board._create_hint(move, player)
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if the hint = "xxxx".

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        if self._board.has_won(player):
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()