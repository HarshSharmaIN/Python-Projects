import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
GREEN = (0, 255, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids Shooting Game")

# Generate background with stars for a space vibe
def draw_space_background():
    screen.fill(BLACK)
    for _ in range(100):  # Randomly scatter 100 stars
        star_x = random.randint(0, WIDTH)
        star_y = random.randint(0, HEIGHT)
        pygame.draw.circle(screen, WHITE, (star_x, star_y), 1)

# Crosshair class
class Crosshair:
    def __init__(self):
        self.size = 15

    def draw(self):
        center_x, center_y = pygame.mouse.get_pos()
        pygame.draw.line(screen, GREEN, (center_x - self.size, center_y), (center_x + self.size, center_y), 2)
        pygame.draw.line(screen, GREEN, (center_x, center_y - self.size), (center_x, center_y + self.size), 2)

# Asteroid class
class Asteroid:
    def __init__(self):
        self.size = random.randint(25, 40)
        self.x = random.randint(self.size, WIDTH - self.size)
        self.y = random.randint(self.size, HEIGHT - self.size)
        self.speed_x = random.choice([-1, 1]) * random.uniform(1, 3)
        self.speed_y = random.choice([-1, 1]) * random.uniform(1, 3)

    def move(self, speed_multiplier=1):
        # Move and bounce off screen edges
        self.x += self.speed_x * speed_multiplier
        self.y += self.speed_y * speed_multiplier
        if self.x < self.size or self.x > WIDTH - self.size:
            self.speed_x *= -1
        if self.y < self.size or self.y > HEIGHT - self.size:
            self.speed_y *= -1

    def draw(self):
        points = []
        for i in range(8):
            angle = i * (math.pi / 4)
            radius = self.size + random.randint(-5, 5)
            point_x = int(self.x + math.cos(angle) * radius)
            point_y = int(self.y + math.sin(angle) * radius)
            points.append((point_x, point_y))
        pygame.draw.polygon(screen, BROWN, points)

    def is_hit(self, pos):
        # Check if click is within asteroid bounds
        return math.hypot(self.x - pos[0], self.y - pos[1]) < self.size

# Main game function
def game(target_score=30):
    clock = pygame.time.Clock()
    crosshair = Crosshair()
    asteroids = [Asteroid() for _ in range(5)]
    score = 0
    speed_multiplier = 1

    running = True
    while running:
        draw_space_background()  # Draw the background with stars
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for asteroid in asteroids[:]:
                    if asteroid.is_hit(event.pos):
                        asteroids.remove(asteroid)
                        score += 1
                        asteroids.append(Asteroid())

        # Increase speed when the score reaches 20
        if score >= 20:
            speed_multiplier = 1.5

        # Draw crosshair and asteroids
        crosshair.draw()
        for asteroid in asteroids:
            asteroid.move(speed_multiplier)
            asteroid.draw()

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Check if the player has won
        if score >= target_score:
            win_text = font.render("Victory!", True, WHITE)
            screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        pygame.display.flip()
        clock.tick(60)

# Run the game with the target score set to 30
game()
pygame.quit()
