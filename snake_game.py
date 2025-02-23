import pygame
import random

# Initialize Pygame
pygame.init()

# Game window settings
width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SHANMUKH'S SNAKE GAME")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game variables
snake_x, snake_y = width//2, height//2
change_x, change_y = 0, 0
food_x, food_y = random.randrange(0, width)//10*10, random.randrange(0, height)//10*10
snake_body = [(snake_x, snake_y)]
clock = pygame.time.Clock()
game_over = False
score = 0

# Fonts
font = pygame.font.SysFont(None, 40)
game_over_font = pygame.font.SysFont(None, 60)

def show_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    game_screen.blit(score_text, (10, 10))

def game_over_screen():
    game_screen.fill(BLACK)
    game_over_text = game_over_font.render("GAME OVER!", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    restart_text = font.render("Press C to Continue or Q to Quit", True, WHITE)
    
    game_screen.blit(game_over_text, (width//2 - 120, height//2 - 60))
    game_screen.blit(score_text, (width//2 - 80, height//2))
    game_screen.blit(restart_text, (width//2 - 180, height//2 + 60))
    pygame.display.update()

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_LEFT and change_x != 10:
                    change_x = -10
                    change_y = 0
                elif event.key == pygame.K_RIGHT and change_x != -10:
                    change_x = 10
                    change_y = 0
                elif event.key == pygame.K_UP and change_y != 10:
                    change_y = -10
                    change_x = 0
                elif event.key == pygame.K_DOWN and change_y != -10:
                    change_y = 10
                    change_x = 0
            else:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    # Reset game
                    snake_x, snake_y = width//2, height//2
                    change_x, change_y = 0, 0
                    snake_body = [(snake_x, snake_y)]
                    food_x, food_y = random.randrange(0, width)//10*10, random.randrange(0, height)//10*10
                    score = 0
                    game_over = False

    if not game_over:
        # Update snake position
        snake_x = (snake_x + change_x) % width
        snake_y = (snake_y + change_y) % height

        # Check self-collision
        if (snake_x, snake_y) in snake_body[1:]:
            game_over = True

        snake_body.append((snake_x, snake_y))

        # Food collision
        if snake_x == food_x and snake_y == food_y:
            food_x = random.randrange(0, width)//10*10
            food_y = random.randrange(0, height)//10*10
            score += 1
        else:
            del snake_body[0]

        # Draw elements
        game_screen.fill(BLACK)
        show_score()
        
        # Draw snake
        for segment in snake_body:
            pygame.draw.rect(game_screen, GREEN, (segment[0], segment[1], 10, 10))
        
        # Draw food
        pygame.draw.rect(game_screen, RED, (food_x, food_y, 10, 10))
        
        pygame.display.update()
        clock.tick(15)
    else:
        game_over_screen()

pygame.quit()