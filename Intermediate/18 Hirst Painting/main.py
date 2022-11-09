import random

# import colorgram
from colors import colors
from classes import Shape
from turtle import Turtle, Screen

# colors = colorgram.extract("Intermediate/18 Hirst Painting/image.jpg", 54)

# rgb_list = []
# for color in colors:
#     rgb = color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     color_tuple = (r, g, b)
#     rgb_list.append(color_tuple)

# print(rgb_list)

turtle = Turtle()
screen = Screen()
screen.colormode(255)
shape = Shape()

turtle.speed(10)
turtle.penup()
y = -300
turtle.setposition(-300, -300)

for _ in range(10):
    y += 60
    shape.dot_row(turtle)
    turtle.setposition(-300, y)


screen.exitonclick()
