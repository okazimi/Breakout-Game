from turtle import Turtle


class Paddle(Turtle):

    # CONSTRUCTOR
    def __init__(self):
        super().__init__()
        # HIDE PADDLE
        self.hideturtle()
        # INITIALIZE PADDLE
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=0.75)
        # MOVE PADDLE TO STARTING POINT
        self.penup()
        self.goto(x=0, y=-275)
        # SHOW PADDLE
        self.showturtle()

    # GO LEFT
    def go_left(self):
        # IF XCOR EXCEEDS SCREEN WIDTH, PASS
        if self.xcor() <= -315:
            pass
        # IF XCOR DOES NOT EXCEED SCREEN WIDTH, MOVE LEFT
        else:
            new_x = self.xcor() - 23
            self.goto(new_x, self.ycor())

    # GO RIGHT
    def go_right(self):
        # IF XCOR EXCEEDS SCREEN WIDTH, PASS
        if self.xcor() >= 315:
            pass
        # IF XCOR DOES NOT EXCEED SCREEN WIDTH, MOVE RIGHT
        else:
            new_x = self.xcor() + 23
            self.goto(new_x, self.ycor())
