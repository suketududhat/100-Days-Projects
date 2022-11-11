from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


screen.listen()
screen.onkey(move_forward, "space")

screen.exitonclick()
