import random


class Shape:
    def create_shape(self, turtle, sides):
        self.random_color(turtle)
        angle = 360 / sides
        for _ in range(sides):
            turtle.forward(50)
            turtle.right(angle)

    def random_color(self, turtle):
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        return turtle.color(R, G, B)

    def random_walk(self, turtle, steps):
        heading = [0, 90, 180, 270]
        for _ in range(steps):
            self.random_color(turtle)
            turtle.forward(50)
            turtle.setheading(random.choice(heading))

    def circle(self, turtle, radius):
        self.random_color(turtle)
        turtle.circle(radius)
