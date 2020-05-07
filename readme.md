
Guide to Tic-Tac-Toe against a human/AI.
----------------------------------------

This repository contains three programs for playing the game Tic-Tac-Toe.

1) Tic-Tac-Toe.py - for two humans! Play with a friend.
2) Tic-Minimax.py - for one human! Play with an AI constructed using the Minimax algorithm.
3) Tic-Minimax-Alpha-Beta.py - for one human! Play with an AI constructed using the Minimax algorithm and optimised using alpha-beta pruning.

The Minimax algorithm allows the AI to choose an optimal move by generating the game tree for each state of the game. Assuming both players play optimally, it returns the index of the move that will minimise the maximum loss for the AI. The AI is the 'maximiser' and the player is the 'minimiser'. Minimax then explores all possibilities and returns the best move. 

Alpha-beta pruning is an optimisation technique that allows the AI to ignore certain branches of the game tree that do not need to be explored. If going down a particular branch doesn't give a better option for the algorithm, that branch is pruned (not considered).




