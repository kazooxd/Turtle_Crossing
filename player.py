from turtle import Turtle

STARTING_POS = (0, -280)
MOVE_DIST = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POS)
        self.setheading(90)
        self.finish = FINISH_LINE_Y

    def move_up(self):
        new_y = self.ycor() + MOVE_DIST
        self.goto(self.xcor(), new_y)

    def level_complete(self):
        self.goto(STARTING_POS)
