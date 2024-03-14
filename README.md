# Raw Pong - python

### Overview

As part of the small practice, I have prepared the Pong game.

I don't think I need to describe the history of the Pong game to anyone.
The first 'computer' game, as simple as building a flail.
I saw it for the first time about 34 years ago at my neighbors' house.
Back then, I didn't fully understand what a game console or computer was.
But I liked it!
Back to the topic. 

I didn't use the Pygame library.
My version of Pong uses the tkinter library as a window source and
the pillow library (PIL) to draw the game.
The game is controlled with the keyboard using the Keyboard library.
You can use the requirements.txt file to install dependencies.

My version of Pong will be used for further experiments with neural networks.
But more on that later.

### Game construction

The entire game constitutes one "Game" class.
I didn't see the point in splitting the player, ball, etc. into separate classes...
The Game class has several parameters, i.e. the x and y position of the ball,
the y position of both players, and the game parameters.
We have several methods in it to control players,
controlling the position of the ball, checking for collisions, drawing the playing field with players and the ball,
pausing the game.
The game loop works as follows:
* checking if the game is not paused,
* player movements,
* ball movement,
* collision test,
* drawing the field of game.

For more details please check the code.

### Licensing

There is no licensing. Everyone can use it as they want.

