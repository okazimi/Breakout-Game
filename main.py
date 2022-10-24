import time
from screen import GameScreen
from paddle import Paddle
from ball import Ball
from brick import Bricks

# INITIALIZE PADDLE
paddle = Paddle()
# INITIALIZE GAME SCREEN
screen = GameScreen(paddle)
# INITIALIZE BALL
ball = Ball()
# INITIALIZE BRICKS
bricks = Bricks()


# SET BOOLEAN GAME STATUS
game_status = True
# WHILE LOOP
while game_status:
    # SCREEN SLEEP TO SLOW BALL MOVEMENT
    time.sleep(0.1)
    # UPDATE SCREEN
    screen.screen.update()
    # MOVE BALL
    ball.move(paddle, bricks)
    # CHECK USER LIVES
    # IF USER HAS NO LIVES LEFT, END GAME
    if not screen.check_lives(ball.user_lives):
        game_status = False
    # USER HAS LIVES LEFT, CONTINUE GAME
    else:
        game_status = True


# KEEP SCREEN OPEN
screen.screen.exitonclick()
