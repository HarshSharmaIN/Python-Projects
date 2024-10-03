from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('score.txt') as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 250)
        self.color('white')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score : {self.score} High Score : {self.high_score}', align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('score.txt', 'w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'Game Over.', align=ALIGNMENT, font=FONT)
