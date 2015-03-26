# Tic-Tac-Toe
A command line implementation of tic-tac-toe.

This is a project attempting to create a command line interactive game of tic-tac-toe.
It is an exercise in a combination of applied game theory and computer science. The division of
internal information is as follows:

The code containing the structure of the game, and the code that should be executed to initiate play is
in Game.py; however, there are few functions with any computational functionality located there.

Moves.py contains the code describing the majority of smaller tasks contained within the
overarching game, including showing the available moves, determining if a win condition has been
reached, and the process by which the computer selects its move

Board.py contains the implementation code for the game board itself, as well as the mechanism for
calculating what defines the win condition.

The code will only be functional vs the computer for a 3x3 tic tac toe game.
However, for multiplier play, any size board is available. The ultimate goal is to fully generalize the
