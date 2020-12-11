from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10//2
        self.y_move = 10//2

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bouncing_wall(self):
        # self.setheading(360 - self.heading())
        self.y_move *= -1

    def bouncing_paddle(self):
        # self.setheading(self.heading()-90)
        self.x_move *= -1

    def refresh(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1