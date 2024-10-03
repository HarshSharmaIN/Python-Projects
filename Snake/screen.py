from turtle import Screen
import time


class SnakeScreen:
    def __init__(self, snake):
        self.screen = Screen()
        self.snake = snake
        self.initialize()

    def initialize(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.title('Snake Game')
        self.screen.tracer(0)

    def refresh(self):
        self.screen.update()
        time.sleep(0.1)

    def listen_key(self):
        self.screen.listen()
        self.screen.onkey(self.snake.up, 'Up')
        self.screen.onkey(self.snake.down, 'Down')
        self.screen.onkey(self.snake.left, 'Left')
        self.screen.onkey(self.snake.right, 'Right')

    def exit(self):
        self.screen.exitonclick()
