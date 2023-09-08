# Pong2 Game Readme

## Overview

This is a simple implementation of the classic Pong game using the Pygame library in Python. In this game, two players control paddles and try to bounce a ball back and forth. The objective is to prevent the ball from reaching the edge of your side of the screen while trying to get the ball past your opponent's paddle.

## Prerequisites

Before running the code, you need to have Python and Pygame installed on your system. You can install Pygame using pip:

```bash
pip install pygame
```

## Getting Started

1. Clone or download the repository to your local machine.

2. Run the `pong.py` script using Python:

```bash
python pong.py
```

3. Use the following keys to control the paddles:
   - Player 1 (Left Paddle):
     - Move Up: W key
     - Move Down: S key

   - Player 2 (Right Paddle):
     - Move Up: Up Arrow key
     - Move Down: Down Arrow key

4. Enjoy the game! Try to score points by getting the ball past your opponent.

## Game Rules

- The game starts with the ball in the center of the screen, moving in a random direction.
- The ball bounces off the top and bottom edges of the screen.
- If the ball hits a paddle, it bounces off in the opposite direction.
- If the ball reaches the left or right edge of the screen (past a paddle), the opposing player scores a point.
- The game continues until you decide to exit by closing the game window.

## Customization

You can customize the game by modifying the following variables in the `pong.py` script:

- `window_width` and `window_height`: Set the dimensions of the game window.
- `player_speed`: Adjust the speed at which the paddles move.
- `ball_speed`: Change the initial speed and direction of the ball.
- `player_width` and `player_height`: Set the dimensions of the paddles.
- `ball_size`: Set the size of the ball.
- Customize the colors by changing the RGB values in the `BLACK`, `WHITE`, `LINE_COLOR`, `BALL_COLOR`, and `NEON_GREEN` variables.

## License

This project is licensed under the MIT License.
