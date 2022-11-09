from turtle import Turtle, Screen
from shape import Shape

turtle = Turtle()
# turtle.shape("turtle")
turtle.speed(10)
screen = Screen()
screen.colormode(255)
# screen.screensize(canvwidth=4000, canvheight=4000)

shape = Shape()
# max_sides = 5
# starting_sides = 3
# while starting_sides < (max_sides + 1):
#     shape.create_shape(turtle, starting_sides)
#     starting_sides += 1

# turtle.pensize(10)
# shape.random_walk(turtle, 25)

angle = 0
while angle < 360:
    turtle.setheading(angle)
    shape.circle(turtle, 100)
    angle += 45

screen.exitonclick()
