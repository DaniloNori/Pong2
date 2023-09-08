import pygame
import random

pygame.init()

window_width = 1920
window_height = 1080
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong")

#Colors in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LINE_COLOR = (0, 255, 255)  # Color of futuristic lines
BALL_COLOR = (255, 0, 0)  # Color of the ball
NEON_GREEN = (0, 255, 0)  # Green color for neon objects

clock = pygame.time.Clock()

player_width = 15
player_height = 60
ball_size = 15

player1_pos = [50, (window_height - player_height) // 2]
player2_pos = [window_width - 50 - player_width, (window_height - player_height) // 2]
ball_pos = [(window_width - ball_size) // 2, (window_height - ball_size) // 2]

player_speed = 5
ball_speed = [5 * random.choice((-1, 1)), 5 * random.choice((-1, 1))]

#Function to draw neon objects
def draw_neon_object(x, y, width, height):
    neon_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(window, NEON_GREEN, neon_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_pos[1] -= player_speed
    if keys[pygame.K_s]:
        player1_pos[1] += player_speed
    if keys[pygame.K_UP]:
        player2_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player2_pos[1] += player_speed

    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    if ball_pos[1] <= 0 or ball_pos[1] >= window_height - ball_size:
        ball_speed[1] = -ball_speed[1]

    if (
        ball_pos[0] <= player1_pos[0] + player_width
        and ball_pos[1] + ball_size >= player1_pos[1]
        and ball_pos[1] <= player1_pos[1] + player_height
    ) or (
        ball_pos[0] + ball_size >= player2_pos[0]
        and ball_pos[1] + ball_size >= player2_pos[1]
        and ball_pos[1] <= player2_pos[1] + player_height
    ):
        ball_speed[0] = -ball_speed[0]

    if ball_pos[0] <= 0 or ball_pos[0] >= window_width - ball_size:
        ball_pos = [(window_width - ball_size) // 2, (window_height - ball_size) // 2]
        ball_speed = [5 * random.choice((-1, 1)), 5 * random.choice((-1, 1))]

    window.fill(BLACK)

#Draw futuristic lines in the center of the screen
    for y in range(0, window_height, 20):
        pygame.draw.line(window, LINE_COLOR, (window_width // 2, y), (window_width // 2, y + 10), 2)

#Draw neon green objects along the edges of the board
    draw_neon_object(0, 0, window_width, 10)
    draw_neon_object(0, window_height - 10, window_width, 10)
    draw_neon_object(0, 0, 10, window_height)
    draw_neon_object(window_width - 10, 0, 10, window_height)

    pygame.draw.rect(window, LINE_COLOR, (*player1_pos, player_width, player_height))
    pygame.draw.rect(window, LINE_COLOR, (*player2_pos, player_width, player_height))
    pygame.draw.ellipse(window, BALL_COLOR, (*ball_pos, ball_size, ball_size))

    pygame.display.update()
    clock.tick(60)