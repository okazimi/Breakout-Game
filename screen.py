from turtle import Screen, Turtle


class GameScreen:

    # CONSTRUCTOR
    def __init__(self, paddle):
        # INITIALIZE SCREEN
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.title("Breakout Game")
        # LISTEN FOR KEYBOARD INPUTS
        self.screen.listen()
        self.screen.onkey(paddle.go_left, "Left")
        self.screen.onkey(paddle.go_right, "Right")
        # CREATE "LIVES" TEXT BOX
        self.lives = Turtle()
        self.lives.color("white")
        self.lives.hideturtle()
        self.lives.penup()
        self.lives.goto(0, 275)

    # CHECK USER LIVES
    def check_lives(self, user_lives):
        # IF USER HAS NO LIVES LEFT
        if user_lives == 0:
            # UPDATE USER LIVES
            self.lives.undo()
            self.lives.penup()
            self.lives.goto(0, 275)
            self.lives.write(f"Lives: {user_lives}", font=("Arial", 15, "normal"))
            # RETURN FALSE
            return False
        # IF USER HAS LIVES LEFT
        else:
            # UPDATE USER LIVES
            self.lives.undo()
            self.lives.penup()
            self.lives.goto(0, 275)
            self.lives.write(f"Lives: {user_lives}", font=("Arial", 15, "normal"))
            # RETURN TRUE
            return True

