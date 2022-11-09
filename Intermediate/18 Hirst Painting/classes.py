import random
from colors import colors


class Shape:
    def random_color(self, turtle=None):
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        # return turtle.color(R, G, B)
        return (R, G, B)

    def dot_row(self, turtle):
        for _ in range(10):
            turtle.dot(20, random.choice(colors))
            turtle.forward(60)
