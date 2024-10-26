import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Bird properties
bird_x = 50
bird_y = 300
bird_radius = 15
bird_y_velocity = 0
gravity = 0.5

# Pipe properties
pipe_width = 60
pipe_gap = 150  # Set a minimum gap between pipes
pipe_min_gap = 120  # Minimum gap size to ensure the bird can pass
pipe_velocity = 2
pipes = []

# Game state
game_active = False
score = 0
font = pygame.font.Font(None, 36)

# Function to create pipes with the minimum gap enforced
def create_pipe():
    pipe_height = random.randint(100, SCREEN_HEIGHT - 200)
    top_pipe = pygame.Rect(SCREEN_WIDTH, 0, pipe_width, pipe_height)
    bottom_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height + pipe_gap, pipe_width, SCREEN_HEIGHT - pipe_height - pipe_gap)
    pipes.append((top_pipe, bottom_pipe))

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_active:
                    # Reset the game on first space press
                    game_active = True
                    bird_y = 300
                    bird_y_velocity = 0
                    pipes.clear()
                    score = 0
                    create_pipe()
                else:
                    bird_y_velocity = -8  # Jump velocity

    screen.fill(BLACK)

    # Show start message
    if not game_active:
        start_text = font.render("Press SPACE to start", True, WHITE)
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
    else:
        # Update bird position
        bird_y_velocity += gravity
        bird_y += bird_y_velocity

        # Draw the bird
        pygame.draw.circle(screen, WHITE, (bird_x, int(bird_y)), bird_radius)

        # Update pipes
        for top_pipe, bottom_pipe in pipes:
            top_pipe.x -= pipe_velocity
            bottom_pipe.x -= pipe_velocity

        # Remove pipes that have gone off-screen
        pipes = [p for p in pipes if p[0].x + pipe_width > 0]

        # Add new pipes
        if len(pipes) == 0 or pipes[-1][0].x < SCREEN_WIDTH - 200:
            create_pipe()

        # Draw pipes
        for top_pipe, bottom_pipe in pipes:
            pygame.draw.rect(screen, WHITE, top_pipe)
            pygame.draw.rect(screen, WHITE, bottom_pipe)

        # Check for collisions
        for top_pipe, bottom_pipe in pipes:
            if top_pipe.colliderect((bird_x - bird_radius, bird_y - bird_radius, bird_radius * 2, bird_radius * 2)) or bottom_pipe.colliderect((bird_x - bird_radius, bird_y - bird_radius, bird_radius * 2, bird_radius * 2)):
                game_active = False

        # Check if the bird goes out of the screen
        if bird_y < 0 or bird_y > SCREEN_HEIGHT:
            game_active = False

        # Update score
        if pipes and bird_x > pipes[0][0].x + pipe_width:
            score += 1
            pipes.pop(0)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)
