from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode="r") as hs:
            self.high_score = int(hs.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.outdated_score()
    def outdated_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score} | High Score : {self.high_score}", align="center", font=("Arial",18,"normal"))
    def updating_score(self,snake):
        self.score += 1
        self.outdated_score()
    def high_score_update(self):
        if self.score > self.high_score :
            self.high_score = self.score
        with open("high_score.txt", mode="w") as hs:
            hs.write(f"{self.high_score}")
        self.score = 0