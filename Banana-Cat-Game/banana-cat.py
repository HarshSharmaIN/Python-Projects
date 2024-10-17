import pygame
from sys import exit
from random import randint, choice
import os

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.rotozoom(pygame.image.load(os.path.join('Banana-Cat-Game', 'assets', 'images', 'cat.png')).convert_alpha(), 0, 3)
        self.rect = self.image.get_rect(midbottom = (100, 300))
        self.gravity = 0
        self.jump_strength = 16  
        self.mask = pygame.mask.from_surface(self.image)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -self.jump_strength
    
    def apply_gravity(self): 
        self.gravity += 0.8  
        self.rect.y += self.gravity
        if self.rect.bottom >= 330:
            self.rect.bottom = 330
    
    def update(self):
        self.player_input()
        self.apply_gravity()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'bird': 
            bird1 = pygame.transform.scale2x(pygame.image.load(os.path.join('Banana-Cat-Game', 'assets', 'images', 'bird1.png'))).convert_alpha()
            bird2 = pygame.transform.scale2x(pygame.image.load(os.path.join('Banana-Cat-Game', 'assets', 'images', 'bird2.png'))).convert_alpha()
            self.frames = [bird1, bird2]
            y_pos = 210
        else:
            banana = pygame.transform.scale2x(pygame.image.load(os.path.join('Banana-Cat-Game', 'assets', 'images', 'banana.png')).convert_alpha())
            self.frames = [banana]
            y_pos = 325

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(bottomright = (randint(820, 1000), y_pos))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5

    def animation(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation()
        self.rect.x -= self.speed
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

class Reward(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join('Banana-Cat-Game', 'assets', 'images', 'fish.png')).convert_alpha()
        self.rect = self.image.get_rect(midbottom = (randint(820, 1000), 320)) 
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5
    
    def update(self):
        self.rect.x -= self.speed
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f'Score: {current_time // 1000}', False, 'Black')
    score_rect = score_surf.get_rect(center = (200, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def collisions():
    if pygame.sprite.spritecollide(player.sprite, obstacle_grp, False, pygame.sprite.collide_mask):
        obstacle_grp.empty()
        return False
    return True

def reward_collide():
    for reward in reward_grp:
        if pygame.sprite.spritecollide(player.sprite, reward_grp, False, pygame.sprite.collide_mask):
            reward.kill()
            return 1
    return 0

def increase_difficulty():
    global obstacle_timer_duration, reward_timer_duration
    for obstacle in obstacle_grp:
        obstacle.speed += 0.75 
    for reward in reward_grp:
        reward.speed += 0.75 
    obstacle_timer_duration = max(250, obstacle_timer_duration - 100) 
    reward_timer_duration = max(800, reward_timer_duration - 150) 
    pygame.time.set_timer(obstacle_timer, obstacle_timer_duration)
    pygame.time.set_timer(reward_timer, reward_timer_duration)

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Banana Cat")

clock = pygame.time.Clock()
test_font = pygame.font.Font(os.path.join('Banana-Cat-Game', 'assets', 'font', 'Pixeltype.ttf'), 24)

game_active = False
start_time = 0
score = 0
reward_score = 0
high_score = 0
fps = 60

player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_grp = pygame.sprite.Group()
reward_grp = pygame.sprite.Group()

sky_surf = pygame.image.load(os.path.join('Banana-Cat-Game', 'assets', 'images', 'sky.png')).convert()
ground_surf = pygame.image.load(os.path.join('Banana-Cat-Game', 'assets', 'images', 'ground.png')).convert()

cat_surf = pygame.transform.rotozoom(pygame.image.load(os.path.join('Banana-Cat-Game', 'assets', 'images', 'cat.png')).convert_alpha(), 0, 6)
cat_gamescreen_rect = cat_surf.get_rect(center=(400, 200))

game_name = test_font.render('Banana Cat', False, 'Black')
game_name_rect = game_name.get_rect(center=(400, 100))

start_message = test_font.render('Press space to play', False, 'Black')
start_message_rect = start_message.get_rect(center=(400, 300))

game_message = test_font.render('Game Over! Press Space to restart', False, 'Black')
game_message_rect = game_message.get_rect(center=(400, 280))

obstacle_timer = pygame.USEREVENT + 1
obstacle_timer_duration = 900  
pygame.time.set_timer(obstacle_timer, obstacle_timer_duration)

reward_timer = pygame.USEREVENT + 2
reward_timer_duration = 1200  
pygame.time.set_timer(reward_timer, reward_timer_duration)

difficulty_timer = pygame.USEREVENT + 3
pygame.time.set_timer(difficulty_timer, 7500) 

last_spawn_time = 0
min_spawn_interval = 400

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not game_active:
                game_active = True
                start_time = pygame.time.get_ticks()
                obstacle_grp.empty()
                reward_grp.empty()
            else:
                if player.sprite.rect.bottom >= 300:
                    player.sprite.gravity = -player.sprite.jump_strength
                
        if game_active:
            current_time = pygame.time.get_ticks()
            if event.type == obstacle_timer and current_time - last_spawn_time >= min_spawn_interval:
                obstacle_grp.add(Obstacle(choice(['bird', 'banana'])))
                last_spawn_time = current_time

            if event.type == reward_timer and current_time - last_spawn_time >= min_spawn_interval:
                reward_grp.add(Reward())
                last_spawn_time = current_time

            if event.type == difficulty_timer:
                increase_difficulty()

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        score = display_score()

        player.draw(screen)
        player.update()

        obstacle_grp.draw(screen)
        obstacle_grp.update()

        reward_grp.draw(screen)
        reward_grp.update()

        reward_score += reward_collide()
        reward_surf = test_font.render(f'Fish: {reward_score}', False, 'Black')
        reward_rect = reward_surf.get_rect(center = (400, 50))
        screen.blit(reward_surf, reward_rect)

        high_score_surf = test_font.render(f'High Score: {high_score}', False, 'Black')
        high_score_rect = high_score_surf.get_rect(center = (600, 50))
        screen.blit(high_score_surf, high_score_rect)

        game_active = collisions()

        if not game_active:
            current_score = score // 1000
            if current_score > high_score:
                high_score = current_score

    else:
        screen.fill((94, 129, 162))
        screen.blit(cat_surf, cat_gamescreen_rect)
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(start_message, start_message_rect)
        else:
            screen.blit(game_message, game_message_rect)
            final_score = test_font.render(f'Your score: {score // 1000}', False, 'Black')
            final_score_rect = final_score.get_rect(center=(300, 330))
            screen.blit(final_score, final_score_rect)
            
            high_score_surf = test_font.render(f'High Score: {high_score}', False, 'Black')
            high_score_rect = high_score_surf.get_rect(center=(500, 330))
            screen.blit(high_score_surf, high_score_rect)

        reward_score = 0
        reward_grp.empty()
        obstacle_timer_duration = 900  
        reward_timer_duration = 1200  
        pygame.time.set_timer(obstacle_timer, obstacle_timer_duration)
        pygame.time.set_timer(reward_timer, reward_timer_duration)

    pygame.display.update()
    clock.tick(fps)
