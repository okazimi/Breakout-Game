import random
from turtle import Turtle

# GLOBAL VARIABLES
COLORS = ['light blue', 'royal blue',
          'light steel blue', 'steel blue',
          'light cyan', 'light sky blue',
          'violet', 'salmon', 'tomato',
          'sandy brown', 'purple', 'deep pink',
          'medium sea green', 'khaki']

WEIGHTS = [1, 3, 2, 1, 1, 2]


# CLASS TO CREATE A SINGLE BRICK
class Brick(Turtle):

    # CONSTRUCTOR
    def __init__(self, x_cor, y_cor):
        super().__init__()
        # HIDE BLOCK MOVEMENT
        self.hideturtle()
        self.penup()
        # SET SPEED
        self.speed("fastest")
        # SET SHAPE OF BRICK
        self.shape("square")
        # SET SIZE OF BRICK
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        # SET COLOR OF BRICK
        self.color(random.choice(COLORS))
        # MOVE BRICK
        self.goto(x_cor, y_cor)
        # SHOW BLOCK
        self.showturtle()
        # SET QUANTITY OF BRICKS (LAYERS)
        self.quantity = random.choice(WEIGHTS)
        # DEFINING BRICK BORDERS
        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.top_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15


# CLASS TO CREATE ALL BRICKS
class Bricks:

    # CONSTRUCTOR
    def __init__(self):
        # STARTING Y POSITION FOR BRICKS ON SCREEN
        self.y_start = 0
        # ENDING Y POSITION FOR BRICKS ON SCREEN
        self.y_end = 240
        # KEEP TRACK OF BRICKS
        self.bricks = []
        # CREATE ALL ROWS
        self.all_rows()

    # CREATE ROW OF BRICKS
    def row(self, y_cor):
        # LOOP THROUGH XCOR VALUES
        for x in range(-350, 350, 63):
            # CREATE BRICK
            brick = Brick(x, y_cor)
            # APPEND TO ALL BRICKS
            self.bricks.append(brick)

    # CREATE ALL ROWS OF BRICKS
    def all_rows(self):
        # LOOP THROUGH YCOR VALUES
        for y in range(self.y_start, self.y_end, 32):
            # CREATE ROW OF BRICKS
            self.row(y)

