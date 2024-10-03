from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.initializer()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def initializer(self):
        self.shape('circle')
        self.color('white')
        self.shapesize(1, 1)
        self.penup()

    def movement(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.y_move *= -1

    def ball_reset(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()
