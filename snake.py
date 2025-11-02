from turtle import Turtle,Screen
import time
SNAKE_POSITION = [(0,0),(-20,0),(-40,0)]
MOVING_POSITION = 20
class Snake:
    def __init__(self):
        self.snake_body = []
        for i in range(0, 3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(SNAKE_POSITION[i])
            self.snake_body.append(snake)
            self.snake_box = Screen()
            self.snake_box.tracer(0)
            self.snake_box.title(titlestring="My Snake Game")
            self.snake_box.bgcolor("black")
            self.snake_box.setup(width=600, height=600)
        self.head = self.snake_body[0]
    def add_segment(self):
        snake_2 = Turtle()
        snake_2.color("white")
        snake_2.shape("square")
        snake_2.penup()
        x, y = self.snake_body[-1].position()
        snake_2.goto(x, y)
        self.snake_body.append(snake_2)
    def restart(self):
        # Move all segments off-screen
        for segment in self.snake_body:
            segment.goto(1000, 1000)
        # Clear the snake_body list
        self.snake_body.clear()
        # Create a new snake at center
        for i in range(0, 3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto([(0, 0), (-20, 0), (-40, 0)][i])
            self.snake_body.append(segment)
        self.head = self.snake_body[0]
    def move(self,food,scoreboard):
        play_game = True
        while play_game:
            self.snake_box.update()
            time.sleep(0.1)
            for body_parts in range(len(self.snake_body) - 1, 0, -1):
                new_x = self.snake_body[body_parts - 1].xcor()
                new_y = self.snake_body[body_parts - 1].ycor()
                self.snake_body[body_parts].goto(new_x, new_y)
            self.snake_body[0].forward(MOVING_POSITION)
            if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290 :
                self.restart()
                scoreboard.high_score_update()
                scoreboard.outdated_score()
            if self.head.distance(food) < 20 :
                food.moving_food()
                self.add_segment()
                scoreboard.updating_score(self)
            for segment in self.snake_body[1:] :
                if self.head.distance(segment) < 10:
                    self.restart()
                    scoreboard.high_score_update()
                    scoreboard.outdated_score()
    def control(self):
        def front():
            if self.head.heading() != 270:
                self.head.setheading(90)
        def back():
            if self.head.heading() != 90:
                self.head.setheading(270)
        def left():
            if self.head.heading() != 0:
                self.head.setheading(180)
        def right():
            if self.head.heading() != 180:
                self.head.setheading(0)
        self.snake_box.listen()
        self.snake_box.onkey(front, "Up")
        self.snake_box.onkey(back, "Down")
        self.snake_box.onkey(left, "Left")
        self.snake_box.onkey(right, "Right")