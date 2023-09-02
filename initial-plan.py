# Description: I am using two classes, Player and Othello. 
#              Below is my plan for each of the classes and methods in my project.

class Player:
    """
    A class to represent a player in the game with a name and color. Used by Othello class.
    """

    def __init__(self, name, color):
        """
        The constructor for Player class. Takes two parameters:
        name - player's name (string)
        color - piece color (string) either "black" or "white"

        Color is either "black" or "white." Initializes the required data members.

        All data members are private.
        """
        pass

    def get_player_name(self):
        """
        Returns private data member name. Used by Othello class to return winning player's name.
        """
        pass

    def get_color(self):
        """
        Returns private data member color.
        """
        pass


class Othello:
    """
    A class to represent Othello game, played by two players.

    Uses Player class to use data members for player's name and color and to create player objects.

    Player with black pieces starts first. Changes board if valid move, return error if invalid.
    """

    def __init__(self):
        """
        Constructor for Othello class. Takes no parameters. Data members are private.

        Initializes data member board to a list of lists that represent the game board, using *
        as an edge, X for a black piece, O for a white piece and . for an empty space. Initial
        board includes the four starting pieces (2 black, 2 white) in starting places.

        Initializes empty player list. Holds player objects.

        Initializes empty list for possible black positions.

        Initializes empty list for possible white positions.

        Initializes a black piece count and white piece count to 2 (for starting pieces).
        """
        pass

    def print_board(self):
        """
        Uses self._board to obtain the current board.
        Uses for loop to iterate through board list and print current board, including boundaries.
        """
        pass

    def create_player(self, player_name, color):
        """
        Takes two parameters:
        player_name
        color

        Creates a player object using Player class with the given name and color ("black" or
        "white"), such as Player(player_name, color).

        Appends player object to the self._player_list.
        """
        pass

    def return_winner(self):
        """
        When the game ends.

        If white pieces count > black pieces count:
            Returns "Winner is white player: player’s name"

        Else if black pieces count > white pieces count:
            Returns "Winner is black player: player’s name"

        Else:
        (if black and white player has the same number of pieces on the board)
            Returns "It's a tie"
        """
        pass

    def return_available_positions(self, color):
        """
        Takes one parameter:
        color - represents which player (black or white) to return available positions for

        Returns a list of possible positions initialized in init method for the player with
        the given color to move on the current board. For example,

        If color == "black":
            Return self._black_positions

        Also called if invalid move made.
        """
        pass

    def make_move(self, color, piece_position):
        """
        Takes two parameters:
        color - represents which player (black or white) is moving
        piece_position - tuple of coordinate where piece is being moved to

        Internal method called by play_game.

        Puts a piece of the specified color at the given position and updates the board
        accordingly.

        Once board is updated, finds new possible positions for each color and updates those
        lists. Finds specific color piece on board, look for horizontal, vertical, and diagonal
        possible positions to place adjacent to other color's piece. Appends position tuple to
        respective colors possible positions. Does this for both colors.

        Return the current board (as a 2d list).
        """
        pass

    def play_game(self, player_color, piece_position):
        """
        Takes two parameters:
        player_color - which player (black or white) is attempting to move
        piece_position - specified attempted position

        Attempts to make a move for the player with the given color at the specified position.

        To validate, check to see if piece_position in list of possible positions for that color.

        If the position the player wants to move is invalid:
            Does not make any move and return "Invalid move".
            Prints "Here are the valid moves:" followed by a list of possible positions obtained
            by calling return_available_positions method.

        If no valid moves exist:
            Returned list is empty.

        If the position is valid:
            Call make_move method.

        If the game is ended at that point:
            (If both lists, possible black positions and possible white positions, are empty)
            Print "Game is ended white piece: number black piece: number", gets count from black
            pieces and white pieces counts, and calls the return_winner method.
        """
        pass
