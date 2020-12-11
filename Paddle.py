from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed = 20
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x, y=y)

    def up(self):
        if self.ycor() < 250:
            self.goto(x=self.xcor(), y=self.ycor() + self.speed)

    def down(self):
        if self.ycor() > - 240:
            self.goto(x=self.xcor(), y=self.ycor() - self.speed)