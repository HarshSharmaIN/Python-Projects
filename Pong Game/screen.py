from turtle import Screen
TITLE = 'Ping-Pong Game'
COLOR = 'black'


class PongScreen:
    def __init__(self, l_paddle, r_paddle):
        self.screen = Screen()
        self.initializer()
        self.l_paddle = l_paddle
        self.r_paddle = r_paddle

    def initializer(self):
        self.screen.setup(800, 600)
        self.screen.bgcolor(COLOR)
        self.screen.title(TITLE)
        self.screen.tracer(0)

    def update(self):
        self.screen.update()

    def l_paddle_movement(self, up_key, down_key):
        self.screen.listen()
        self.screen.onkey(self.l_paddle.up, up_key)
        self.screen.onkey(self.l_paddle.down, down_key)

    def r_paddle_movement(self, up_key, down_key):
        self.screen.listen()
        self.screen.onkey(self.r_paddle.up, up_key)
        self.screen.onkey(self.r_paddle.down, down_key)

    def exit(self):
        self.screen.exitonclick()
