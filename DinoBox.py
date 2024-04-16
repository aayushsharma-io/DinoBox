# Name: DinoBox
# Created by Aayush Sharma.
# Website: aayushsharma.remotikal.com 
# Github: https://github.com/aayushsharma-io/
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DinoBox by Aayush")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the game variables
player_width, player_height = 50, 50
player_x, player_y = 100, HEIGHT - player_height
player_vel = 10
jump_height = 100
jump_vel = 10
is_jumping = False

obstacle_width, obstacle_height = 30, 50
obstacle_vel = 5
obstacles = []

clock = pygame.time.Clock()

# Define functions
def draw_player():
    pygame.draw.rect(WIN, BLACK, (player_x, player_y, player_width, player_height))

def create_obstacle():
    obstacle_x = WIDTH
    obstacle_y = HEIGHT - obstacle_height
    obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

def move_obstacles():
    for obstacle in obstacles:
        obstacle.x -= obstacle_vel

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(WIN, BLACK, obstacle)

def check_collision():
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            return True
    return False

# Main game loop
run = True
while run:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
    if is_jumping:
        player_y -= jump_vel
        jump_height -= jump_vel
        if jump_height <= 0:
            is_jumping = False
            jump_height = 100
    if not is_jumping and player_y < HEIGHT - player_height:
        player_y += jump_vel

    # Create obstacles
    if random.randint(0, 100) < 5:
        create_obstacle()

    # Move and draw obstacles
    move_obstacles()

    # Check for collision
    player = pygame.Rect(player_x, player_y, player_width, player_height)
    if check_collision():
        run = False

    # Update the display
    WIN.fill(WHITE)
    draw_player()
    draw_obstacles()
    pygame.display.update()

    # Set the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
