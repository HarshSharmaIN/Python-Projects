import pygame
from pygame import mixer
import random
import time
import os

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
DARK_GREEN = (102, 204, 0)
ORANGE = (204, 102, 0)
LIGHT_MAROON = (153, 0, 76)
BLUE = (0, 75, 255)
CYAN = (0, 255, 255)
MONOKAI = (46, 46, 46)
screen_width, screen_height = 800, 600

pygame.init()
mixer.init()
make_sound = mixer.Sound("eat_food.wav")

welcome_image = pygame.image.load("snake.png")
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SNAKES")
clock = pygame.time.Clock()
exit_game = False

pygame.display.update()

def text_on_screen(text, color, size, pos_x, pos_y, bold = False, italic = False):
    text_font = pygame.font.SysFont("timesnewroman", size, bold, italic,)
    text_on_screen = text_font.render(text, True, color)
    screen.blit(text_on_screen, [pos_x, pos_y])

def game_loop():
    game_over = False
    snake_size = 17
    food_x = random.randint(snake_size + 10, screen_width - snake_size)
    food_y = random.randint(50, screen_height - snake_size - 10)
    snake_x = 90
    snake_y = 90
    speed_x = 4
    speed_y = 4
    snake_length = 1
    eat_threshold = 7
    fps = 60
    flag = 0
    game_over = False
    score = 0
    snake_list = []
    global exit_game
    exit_game = False
    if os.path.exists(".high_score.txt"):
        with open (".high_score.txt", "r") as f:
            high_score = f.read()
    else:
        with open (".high_score.txt", "w") as f:
            high_score = f.write("0")
        with open (".high_score.txt", "r") as f:
            high_score = f.read()
    high_score = int(high_score)
    mixer.music.load("game_music.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()
    while not exit_game:
        if not game_over:
            screen.fill(MONOKAI)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP: flag = 1
                    if event.key == pygame.K_DOWN: flag = 2
                    if event.key == pygame.K_LEFT: flag = 3
                    if event.key == pygame.K_RIGHT: flag = 4
            if flag == 1: snake_y -= speed_y
            if flag == 2: snake_y += speed_y
            if flag == 3: snake_x -= speed_x
            if flag == 4: snake_x += speed_x
            # collision threshold
            if snake_x > screen_width - snake_size or snake_x < 0 or snake_y > screen_height - snake_size or snake_y < 0:
                mixer.music.fadeout(500)
                mixer.music.load("game_over_music.mp3")
                mixer.music.set_volume(0.2)
                mixer.music.play()
                game_over = True
            else:
                if abs(snake_x - food_x) < eat_threshold and abs(snake_y - food_y) < eat_threshold:
                    make_sound.set_volume(0.7)
                    make_sound.play()
                    food_x = random.randint(snake_size + 10, screen_width - snake_size)
                    food_y = random.randint(50, screen_height - snake_size - 10)
                    score += 5

                    # acceleration
                    speed_x += 0.1
                    speed_y += 0.1

                    # making the snake grow
                    snake_length += 2
                    
                head = [snake_x, snake_y]
                snake_list.append(head)
                if len(snake_list) > snake_length:
                    snake_list.pop(0)

                # if the snake collapses in on itself
                # if head in snake_list[:len(snake_list) - 1]:
                #     mixer.music.fadeout(500)
                #     mixer.music.load("game_over_music.mp3")
                #     mixer.music.set_volume(0.2)
                #     mixer.music.play()
                #     game_over = True
                pygame.draw.rect(screen, RED, pygame.Rect(food_x, food_y, snake_size, snake_size))
                for x,y in snake_list:
                    pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, snake_size, snake_size))

                text_on_screen(f"Score: {score}", GREEN, 30, 20, 20, True, True)
                text_on_screen(f"High Score: {high_score}", GREEN, 30, 200, 20, True, True)
            
        else:
            screen.fill(MONOKAI)
            text_on_screen("GAME OVER", RED, 40, screen_width/2 - 140, screen_height/2 - 120, True, False)
            text_on_screen(f"Final Score: {score}", GREEN, 30, screen_width/2 - 110, screen_height/2 - 60, True, False)
            text_on_screen(f"Hit Spacebar to continue", CYAN, 30, screen_width/2 - 190, screen_height/2 + 60, True, False)
            if score > high_score:
                text_on_screen(f"NEW HIGH SCORE!!!", YELLOW, 30, screen_width/2 - 170, screen_height/2, True, False)
                with open(".high_score.txt", "w") as f:
                    f.write(str(score))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        welcome_screen()
        pygame.display.update()
        clock.tick(fps)

def welcome_screen():
    mixer.music.load("intro_music.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()
    global exit_game
    while not exit_game:
        screen.blit(welcome_image, [0, 0])
        text_on_screen("Welcome to SNAKES!", ORANGE, 30, screen_width/2 - 350, screen_height/2 - 50, bold=True, italic=True)
        text_on_screen("Hit spacebar to play", LIGHT_MAROON, 30, screen_width/2 - 350, screen_height/2 - 0, bold=False, italic=True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    timer = 3
                    mixer.music.fadeout(500)
                    mixer.music.load("countdown_music.wav")
                    mixer.music.set_volume(0.3)
                    mixer.music.play()
                    while timer != 0:
                        screen.fill(MONOKAI)
                        text_on_screen("GET READY...", BLUE, 40, screen_width/2 - 160, screen_height/2 - 120, True, False)
                        text_on_screen(f"{timer}", RED, 35, screen_width/2 - 30, screen_height/2 - 40, True, False)
                        pygame.display.update()
                        time.sleep(1)
                        timer -= 1
                    mixer.music.fadeout(500)
                    game_loop()
        pygame.display.update()

welcome_screen()