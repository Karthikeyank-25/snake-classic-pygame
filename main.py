# Importing Packages:
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# Creating Snake:
snake = Snake()
# Providing Food:
food = Food()
# Managing Scoreboard:
scoreboard = Scoreboard()
# Controlling Snake:
snake.control()
# Moving Snake:
snake.move(food,scoreboard)

# Making Screen On until click the Screen:
snake.snake_box.exitonclick()
# Creating a new file:
