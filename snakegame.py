import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game Using Python")

# Snake initial position and movement
snake_x, snake_y = width // 2, height // 2
change_x, change_y = 0, 0
snake_body = [(snake_x, snake_y)]

# Food coordinates
food_x = random.randrange(0, width, 10)
food_y = random.randrange(0, height, 10)

# Clock to control FPS
clock = pygame.time.Clock()

# Font setup
font = pygame.font.SysFont(None, 50)

def show_game_over():
    game_screen.fill((0, 0, 0))
    game_over_text = font.render("GAME OVER!", True, (255, 0, 0))
    text_rect = game_over_text.get_rect(center=(width // 2, height // 2))
    game_screen.blit(game_over_text, text_rect)
    pygame.display.update()

def display_snake_and_food():
    global snake_x, snake_y, food_x, food_y, snake_body, game_over

    snake_x = (snake_x + change_x) % width
    snake_y = (snake_y + change_y) % height

    # Game Over check
    if (snake_x, snake_y) in snake_body[1:]:
        game_over = True
        return

    snake_body.append((snake_x, snake_y))

    if snake_x == food_x and snake_y == food_y:
        food_x = random.randrange(0, width, 10)
        food_y = random.randrange(0, height, 10)
    else:
        snake_body.pop(0)

    game_screen.fill((0, 0, 0))
    pygame.draw.rect(game_screen, (0, 255, 0), [food_x, food_y, 10, 10])
    for (x, y) in snake_body:
        pygame.draw.rect(game_screen, (255, 255, 255), [x, y, 10, 10])
    pygame.display.update()

# Game variables
current_direction = None
game_over = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_LEFT and current_direction != "RIGHT":
                change_x = -10
                change_y = 0
                current_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and current_direction != "LEFT":
                change_x = 10
                change_y = 0
                current_direction = "RIGHT"
            elif event.key == pygame.K_UP and current_direction != "DOWN":
                change_x = 0
                change_y = -10
                current_direction = "UP"
            elif event.key == pygame.K_DOWN and current_direction != "UP":
                change_x = 0
                change_y = 10
                current_direction = "DOWN"

    if not game_over:
        display_snake_and_food()
    else:
        show_game_over()

    clock.tick(10)
