# Description: Contains a Player class with specified name and piece color. 
#              Contains an Othello class with methods to play the Othello game with two players and to manipulate Othello game board.

class Player:
    """Represents a player in the game with a name and color."""
    def __init__(self, name, color):
        self._name = name
        self._color = color

    def get_name(self):
        """Returns player's name."""
        return self._name

    def set_name(self, new_name):
        """Updates player's name."""
        self._name = new_name

    def get_color(self):
        """Returns player's color."""
        return self._color

    def set_color(self, new_color):
        """Updates player's color."""
        self._color = new_color


class Othello:
    """Represents Othello game, played by two players."""
    def __init__(self):
        self._board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', 'X', 'O', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self._player_list = []
        self._possible_black_positions = [(3, 4), (4, 3), (5, 6), (6, 5)]
        self._possible_white_positions = [(3, 5), (4, 6), (5, 3), (6, 4)]
        self._current_black_positions = [(4, 5), (5, 4)]
        self._current_white_positions = [(4, 4), (5, 5)]

    def print_board(self):
        """Prints current board, including boundaries."""
        for row in self._board:
            print(*row)

    def create_player(self, player_name, color):
        """Creates a player object with the given name and color and adds it to player list."""
        new_player = Player(player_name, color)
        self._player_list.append(new_player)

    def return_winner(self):
        """Returns who is winner of the game or if there is a tie."""
        for player in self._player_list:
            if player.get_color() == "white":
                white_player = player.get_name()
            else:
                black_player = player.get_name()

        if len(self._current_black_positions) > len(self._current_white_positions):
            print(f"Winner is black player: {black_player}")
        elif len(self._current_white_positions) > len(self._current_black_positions):
            print(f"Winner is white player: {white_player}")
        else:
            print("It's a tie")

    def return_available_positions(self, color):
        """Returns list of possible positions for player with given color to move on current board."""
        if color == "black":
            self._possible_black_positions.sort()
            return self._possible_black_positions
        else:
            self._possible_white_positions.sort()
            return self._possible_white_positions

    def make_move(self, color, piece_position):
        """
        Puts a piece of the specified color at the given position.
        Calls methods to flip captured pieces and update available positions.
        Returns the current board (as a 2d list).
        """
        row, col = piece_position
        # places piece at location and clears possible position lists to be updated
        if color == "black":
            self._board[row][col] = "X"
            self._current_black_positions.append(piece_position)
            self._possible_black_positions = []
            self._possible_white_positions = []
            opposite_color = "white"
        else:
            self._board[row][col] = "O"
            self._current_white_positions.append(piece_position)
            self._possible_white_positions = []
            self._possible_black_positions = []
            opposite_color = "black"

        self.flip_colors(color, piece_position)
        self.update_available_positions(color)
        self.update_available_positions(opposite_color)
        return self._board

    def flip_colors(self, color, piece_position):
        """Checks all directions and converts chains of captured opponent pieces to current player's color."""
        flip_these = []
        if color == "black":
            current_piece = "X"
            opponent_piece = "O"
            current_list = self._current_black_positions
            opponent_list = self._current_white_positions
        else:
            current_piece = "O"
            opponent_piece = "X"
            current_list = self._current_white_positions
            opponent_list = self._current_black_positions

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for direction in directions:
            new_position = (piece_position[0] + direction[0], piece_position[1] + direction[1])
            row, col = new_position
            if 0 < row < 9 and 0 < col < 9:
                # if opponent piece encountered in certain direction
                if self._board[row][col] == opponent_piece:
                    while self._board[row][col] == opponent_piece:
                        if 0 < row < 9 and 0 < col < 9:
                            # add prospective pieces to be flipped to list
                            flip_these.append(new_position)
                            new_position = (new_position[0] + direction[0], new_position[1] + direction[1])
                            row, col = new_position
                    # if opponent pieces are in between two current player pieces, flips pieces in list
                    if self._board[row][col] == current_piece:
                        for position in flip_these:
                            row, col = position
                            self._board[row][col] = current_piece
                            opponent_list.remove(position)
                            current_list.append(position)
                    flip_these = []

    def update_available_positions(self, color):
        """Updates available positions for input color."""
        if color == "black":
            positions = self._current_black_positions
            updated_list = self._possible_black_positions
            opponent_piece = "O"
        else:
            positions = self._current_white_positions
            updated_list = self._possible_white_positions
            opponent_piece = "X"
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        # checks in all directions from each current color positions
        for position in positions:
            for direction in directions:
                new_position = (position[0] + direction[0], position[1] + direction[1])
                row, col = new_position
                if 0 < row < 9 and 0 < col < 9:
                    # if opponent piece encountered in certain direction
                    if self._board[row][col] == opponent_piece:
                        while self._board[row][col] == opponent_piece:
                            if 0 < row < 9 and 0 < col < 9:
                                new_position = (new_position[0] + direction[0], new_position[1] + direction[1])
                                row, col = new_position
                        # if empty spot encountered, add as a possible position to list
                        if self._board[row][col] == ".":
                            if 0 < row < 9 and 0 < col < 9 and new_position not in updated_list:
                                updated_list.append(new_position)

    def play_game(self, player_color, piece_position):
        """Attempts to make a move for the player with given color at specified position."""
        if player_color == "black":
            if not self._possible_black_positions:   # if no possible positions, "skips turn"
                return
            if piece_position not in self._possible_black_positions:   # if input position invalid
                print("Here are the valid moves: " + str(self.return_available_positions("black")))
                return "Invalid move"
            else:
                self.make_move(player_color, piece_position)   # makes move if input position valid
        else:
            if not self._possible_white_positions:
                return
            if piece_position not in self._possible_white_positions:
                print("Here are the valid moves: " + str(self.return_available_positions("white")))
                return "Invalid move"
            else:
                self.make_move(player_color, piece_position)

        # checks possible positions, game ends if none for either player and returns winner
        if self._possible_black_positions == [] and self._possible_white_positions == []:
            black_count = len(self._current_black_positions)
            white_count = len(self._current_white_positions)
            print(f"Game is ended.\nWhite pieces: {white_count}\nBlack pieces: {black_count}")
            self.return_winner()
          
