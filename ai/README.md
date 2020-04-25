# AI Project AVALAM

Samelson Nicolas - 17288  
Roquero Pedro - 17010

## Programming language used :

Python 3.7.5

## Libraries used :

* cherrypy
* json
* socket
* sys
* math 
* os
* msgpack
* Random 

## AI strategy:

Before playing, the AI will choose a depth of moves ahead of the current game 
depending on the advancement of the game. Starting by a depth of 3, going up to 4
and then when there isn't a lot of possibilities it will decrease.

After choosing it's depth it will choose the best move to do fo the AI to mark the best score.
For it to happen, we used minimax and alpha beta prunning:

1. At the deepest depth, or the leaves, it will check the state of the board and
calculate a score. For each pawn tower, it will add an amount of points,
if the height is between 1 and 4 and the score will be of 1 point, 
depending on the top pawn of the tower, +1 for the colour of the AI and -1
if it's the colour of the ennemy. If the height is 5, then it will add +5 or -5
depending on the top pawn of the tower

1. With the score of each possible move on the leaves, the algorythm Minimax will run and 
maximize the AI and minimize the player. Alpha Beta is implemented to prune some leaves and 
optimize a lot the process.

