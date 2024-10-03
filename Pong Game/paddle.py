from turtle import Turtle
STEP_DISTANCE = 20
SHAPE = 'square'
COLOR = 'white'


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.create_paddle(x_cor, y_cor)

    def create_paddle(self, x_cor, y_cor):
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(5, 1, None)
        self.penup()
        self.goto(x_cor, y_cor)

    def up(self):
        new_y = self.ycor() + STEP_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - STEP_DISTANCE
        self.goto(self.xcor(), new_y)
