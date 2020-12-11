from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.lScore = 0
        self.rScore = 0

    def print_score(self):
        self.clear()
        self.write(f"{self.lScore} | {self.rScore}", align="center", font=("Arial", 20, "bold"))

    def increase_left(self):
        self.lScore += 1
        self.print_score()

    def increase_right(self):
        self.rScore += 1
        self.print_score()

    def print_final(self):
        self.clear()
        self.goto(0, 0)
        if self.lScore > self.rScore:
            self.write(f"Winner is Hidari-chan", align="center", font=("Arial", 30, "bold"))
        else:
            self.write(f"Winner is Migi-chan", align="center", font=("Arial", 30, "bold"))