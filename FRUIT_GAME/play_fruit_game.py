'''
Hello Mates!! 
This is a fruit game that you can enjoy and play. This game consists of a blue player (rectangle shape) which you would be controlling. 
There are fruits of black colour (square) which would be spawning randomly. The task is to make sure that the player can collect the fruits.
You have to use the right arrow key to move right and left arrow key to move left.
For every time you catch the fruit yyou get +2 points and everytime you miss the fruit you get-1 point.
The cummulative score will be printed on  your game window.
Hope you enjoy the game mates !!!
'''





import pygame
import numpy as np

# --- Game Environment ---
class Field:
    def __init__(self, height=10, width=5):
        self.width = width
        self.height = height
        self.clear_field()

    def clear_field(self):
        self.body = np.zeros(shape=(self.height, self.width))

    def update_field(self, fruits, player):
        self.clear_field()
        for fruit in fruits:
            if not fruit.out_of_field:
                for y in range(fruit.y, min(fruit.y + fruit.height, self.height)):
                    for x in range(fruit.x, min(fruit.x + fruit.width, self.width)):
                        self.body[y][x] = 1
        for i in range(player.width):
            self.body[player.y][player.x + i] = 2

class Fruit:
    def __init__(self, height=1, width=1, x=None, y=0, speed=1, field=None):
        self.field = field
        self.height = height
        self.width = width
        self.x = self.generate_x() if x is None else x
        self.y = y
        self.speed = speed
        self.out_of_field = False
        self.is_caught = 0

    def generate_x(self):
        return np.random.randint(0, self.field.width - self.width)

    def set_out_of_field(self):
        self.out_of_field = self.y > self.field.height - 1

    def move(self):
        self.y += self.speed
        self.set_out_of_field()

    def set_is_caught(self, player):
        if self.y != player.y:
            self.is_caught = 0
        else:
            if self.x + self.width > player.x and self.x < player.x + player.width:
                self.is_caught = 1
            else:
                self.is_caught = -1

class Player:
    def __init__(self, height=1, width=1, field=None):
        self.field = field
        self.height = height
        self.width = 5
        self.x = int(self.field.width / 2 - width / 2)
        self.last_x = self.x
        self.y = self.field.height - 1
        self.dir = 0
        self.colour = "blue"

    def move(self):
        self.last_x = self.x
        self.x += self.dir
        self.dir = 0
        self.constrain()

    def action(self, action):
        if action == 1:
            self.dir = -1
        elif action == 2:
            self.dir = 1
        else:
            self.dir = 0

    def constrain(self):
        if self.x < 0:
            self.x = self.field.width - self.width
        elif (self.x + self.width) > self.field.width:
            self.x = 0

class Environment:
    F_HEIGHT = 12
    F_WIDTH = 12
    PLAYER_WIDTH = 2
    FRUIT_WIDTH = 1

    ENVIRONMENT_SHAPE = (F_HEIGHT, F_WIDTH, 1)
    ACTION_SPACE = [0, 1, 2]
    ACTION_SPACE_SIZE = len(ACTION_SPACE)
    ACTION_SHAPE = (ACTION_SPACE_SIZE,)
    PUNISHMENT = -1  # Penalty for missing fruit
    REWARD = 2       # Reward for catching fruit
    score = 0
    MAX_VAL = 2

    LOSS_SCORE = -5
    WIN_SCORE = 5

    DRAW_MUL = 30
    WINDOW_HEIGHT = F_HEIGHT * DRAW_MUL
    WINDOW_WIDTH = F_WIDTH * DRAW_MUL

    game_tick = 0
    FPS = 12
    MOVE_FRUIT_EVERY = 1
    MOVE_PLAYER_EVERY = 1
    MAX_FRUIT = 1
    INCREASE_MAX_FRUIT_EVERY = 100
    SPAWN_FRUIT_EVERY_MIN = 60
    SPAWN_FRUIT_EVERY_MAX = 61
    next_spawn_tick = 0

    FRUIT_COLOURS = {-1: "red", 0: "black", 1: "green"}

    def __init__(self):
        self.reset()

    def get_state(self):
        return self.field.body / self.MAX_VAL

    def reset(self):
        self.game_tick = 0
        self.game_over = False
        self.game_won = False
        self.field = Field(height=self.F_HEIGHT, width=self.F_WIDTH)
        self.player = Player(field=self.field, width=self.PLAYER_WIDTH)
        self.score = 0
        self.fruits = []
        self.spawn_fruit()
        self.field.update_field(self.fruits, self.player)
        return self.get_state()

    def spawn_fruit(self):
        if len(self.fruits) < self.MAX_FRUIT:
            self.fruits.append(Fruit(field=self.field, height=self.FRUIT_WIDTH, width=self.FRUIT_WIDTH))
            self.set_next_spawn_tick()

    def set_next_spawn_tick(self):
        self.next_spawn_tick = self.game_tick + np.random.randint(self.SPAWN_FRUIT_EVERY_MIN, self.SPAWN_FRUIT_EVERY_MAX)

    def step(self, action=None):
        self.game_tick += 1
        if self.game_tick % self.INCREASE_MAX_FRUIT_EVERY == 0:
            self.MAX_FRUIT += 1
        if self.game_tick >= self.next_spawn_tick or len(self.fruits) == 0:
            self.spawn_fruit()
        if action is not None:
            self.player.action(action)
        self.player.move()

        reward = 0
        if self.game_tick % self.MOVE_FRUIT_EVERY == 0:
            in_field_fruits = []
            for fruit in self.fruits:
                fruit.move()
                fruit.set_is_caught(self.player)
                if fruit.is_caught == 1:
                    self.update_score(self.REWARD)
                    reward = self.REWARD
                elif fruit.is_caught == -1:
                    self.update_score(self.PUNISHMENT)
                    reward = self.PUNISHMENT
                if not fruit.out_of_field:
                    in_field_fruits.append(fruit)
            self.fruits = in_field_fruits

        self.field.update_field(fruits=self.fruits, player=self.player)

        if self.score <= self.LOSS_SCORE:
            self.game_over = True
        if self.score >= self.WIN_SCORE:
            self.game_won = True 

        return self.get_state(), reward, self.game_over or self.game_won, self.score
    
    def update_score(self, delta):
        self.score += delta

    def render(self, screen, cumulative_score, solo=True, x_offset=0, y_offset=0):
        if solo:
            screen.fill((255, 255, 255))  # White background
            pygame.display.set_caption(f"Score: {self.score}")

        # Draw player
        pygame.draw.rect(
            screen,
            pygame.Color(self.player.colour),
            pygame.Rect(self.player.x * self.DRAW_MUL + x_offset, self.player.y * self.DRAW_MUL + y_offset, self.player.width * self.DRAW_MUL, self.player.height * self.DRAW_MUL)
        )

        # Draw fruits
        for fruit in self.fruits:
            pygame.draw.rect(
                screen, 
                pygame.Color(self.FRUIT_COLOURS[fruit.is_caught]), 
                pygame.Rect(fruit.x * self.DRAW_MUL + x_offset, fruit.y * self.DRAW_MUL + y_offset, fruit.width * self.DRAW_MUL, fruit.height * self.DRAW_MUL)
            )

        # Display cumulative score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Cumulative Score: {cumulative_score}', True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

# --- Main Loop with Manual Play ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((Environment.WINDOW_WIDTH, Environment.WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    env = Environment()

    cumulative_score = 0  # Initialize cumulative score tracker
    running = True
    episode = 0

    while running:
        state = env.reset()
        done = False
        episode_score = 0  # Track score for each episode

        while not done:
            action = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        action = 1  # Move left
                    elif event.key == pygame.K_RIGHT:
                        action = 2  # Move right
                elif event.type == pygame.KEYUP:
                    action = 0  # Stop moving when key is released

            next_state, reward, done, score = env.step(action)
            episode_score += reward  # Update episode score
            
            # Update cumulative score after each step
            cumulative_score += reward

            env.render(screen, cumulative_score)

            clock.tick(env.FPS)

        # Print scores
        episode += 1
        print(f"\nEpisode {episode} Finished. Episode Score: {episode_score}. Cumulative Score: {cumulative_score}")

    pygame.quit()

if __name__ == "__main__":
    main()
