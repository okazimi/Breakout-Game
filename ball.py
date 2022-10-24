from turtle import Turtle


class Ball(Turtle):

    # CONSTRUCTOR
    def __init__(self):
        super().__init__()
        # HIDE BALL
        self.hideturtle()
        # INITIALIZE BALL
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        # MOVE BALL TO STARTING POINT
        self.penup()
        self.goto(x=0, y=-240)
        # INITIALIZE BALL MOVEMENT VARIABLES
        self.x_move = 20
        self.y_move = 20
        # SHOW BALL
        self.showturtle()
        # INITIALIZE USER_LIVES VARIABLE
        self.user_lives = 3

    # BALL MOVEMENT FUNCTION
    def move(self, paddle, bricks):
        # DETECT COLLISION WITH PADDLE
        if self.distance(paddle) < 40 and self.ycor() < -240:
            # REVERSE BALLS Y DIRECTION
            self.y_move *= -1
        # DETECT BALL GOING OUT OF BOUNDS
        elif self.ycor() < -275:
            # SUBTRACT ONE FROM USER LIVES
            self.user_lives -= 1
            # RESET BALL POSITION
            # HIDE BALL
            self.hideturtle()
            # MOVE BALL TO STARTING POINT
            self.penup()
            self.goto(x=0, y=-240)
            # REVERSE Y DIRECTION
            self.y_move *= -1
            # SHOW BALL
            self.showturtle()
        # DETECT COLLISION WITH TOP OF SCREEN
        elif self.ycor() > 275:
            # CHANGE Y DIRECTION
            self.y_move *= -1
        # DETECT COLLISION WITH LEFT/RIGHT OF SCREEN
        elif self.xcor() > 375 or self.xcor() < -379.99:
            # CHANGE X DIRECTION
            self.x_move *= -1
        # DETECT COLLISION WITH BRICKS
        for brick in bricks.bricks:
            # IF BALL IS LESS THAN 40 FROM BRICK
            if self.distance(brick) < 35:
                # REVERSE Y DIRECTION OF BALL
                self.y_move *= -1
                # SUBTRACT ONE FROM BRICK QUANTITY
                brick.quantity -= 1
                # CHECK IF BRICK STILL EXISTS
                if brick.quantity == 0:
                    # REMOVE THE BRICK FROM SCREEN
                    brick.clear()
                    brick.hideturtle()
                    brick.goto(3000, 3000)
                    # REMOVE THE BRICK FROM THE LIST
                    bricks.bricks.remove(brick)

        # GENERATE NEW XCOR
        new_x = self.xcor() + self.x_move
        # GENERATE NEW YCOR
        new_y = self.ycor() + self.y_move
        # MOVE BALL
        self.goto(new_x, new_y)
