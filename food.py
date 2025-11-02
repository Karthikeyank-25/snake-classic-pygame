from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
    def moving_food(self):
        new_x = random.randint(-279,280)
        new_y = random.randint(-280,279)
        self.goto((new_x,new_y))
