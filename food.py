from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

    def refresh(self, snake):
        while True:
            random_x = random.randint(-14,14) * 20
            random_y = random.randint(-14,13) * 20

            if all(segment.position()!= (random_x, random_y) for segment in snake.snakes):
                self.goto(random_x,random_y)
                break