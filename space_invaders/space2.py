import pygame
import os
import time
import random

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 750, 750
WN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

RED_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
BLUE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
PLAYER_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
PLAYER_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

# Fonts
main_font = pygame.font.SysFont("comicsans", 40)

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not (0 <= self.y <= height)

    def collision(self, obj):
        return collide(self, obj)


class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cooldown_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers[:]:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cooldown_counter >= self.COOLDOWN:
            self.cooldown_counter = 0
        elif self.cooldown_counter > 0:
            self.cooldown_counter += 1

    def shoot(self):
        if self.cooldown_counter == 0:
            laser = Laser(self.x + self.width() // 2 - 15, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cooldown_counter = 1

    def width(self):
        return self.ship_img.get_width()

    def height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = PLAYER_SHIP
        self.laser_img = PLAYER_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs, score):
        self.cooldown()
        for laser in self.lasers[:]:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        score += 1
                        if laser in self.lasers:
                            self.lasers.remove(laser)
        return score

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.height() + 10, self.width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.height() + 10, self.width() * (self.health / self.max_health), 10))


class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SHIP, RED_LASER),
        "green": (GREEN_SHIP, GREEN_LASER),
        "blue": (BLUE_SHIP, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cooldown_counter == 0:
            laser = Laser(self.x - 20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cooldown_counter = 1


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    player_vel = 5
    laser_vel = 7
    enemy_vel = 1
    wave_length = 5
    score = 0

    player = Player(300, 650)
    enemies = []

    clock = pygame.time.Clock()

    def redraw_window():
        WN.blit(BG, (0, 0))

        # Draw text for lives and score
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        score_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))

        WN.blit(lives_label, (10, 10))
        WN.blit(score_label, (WIDTH - score_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WN)

        player.draw(WN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100), random.choice(["red", "green", "blue"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.height() < HEIGHT:  # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        score = player.move_lasers(-laser_vel, enemies, score)

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2 * FPS) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)

            elif enemy.y + enemy.height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        if lives <= 0 or player.health <= 0:
            run = False


main()
