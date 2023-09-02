# Othello (Reversi) Game

Python backend for Othello, a two-player strategy board game.

## Objective:
The goal of Othello is to have the most discs of your color on the board when the game is over.

### Setup:
1. The game board is an 8x8 grid at the start.
2. Each player is assigned as black or white.

### Initial Position:
Four discs placed in the center of the board in a 2x2 pattern. The central squares will look like this:
```
WB
BW
```
### Gameplay:
1. Players take turns, starting with Black.
2. On your turn, you must place one of your discs on an empty square in such a way that it "sandwiches" one or more of your opponent's discs between your newly placed disc and your other discs already on the board.
  - "Sandwiching" means that you place your disc so that a straight line (vertical, horizontal, or diagonal) exists between your new disc and your other disc(s), and there are one or more of your opponent's discs in between.
3. When you sandwich your opponent's discs, you flip them to your color.
4. You must make a legal move if one is available. If you can't make a legal move, you turn is forfeited.
5. The game ends when the board is full, or neither player can make a legal move.
6. The player with the most discs of their color on the board wins.

### Winning:
The number of discs of each color on the board are counted. The player with the most discs of their color wins. A tie is possible if both players have an equal number of discs.
