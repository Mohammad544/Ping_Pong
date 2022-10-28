import turtle, time
from bat import Bat
from ball import Ball
from score import Score

screen = turtle.Screen()

ORANGE = "#FF7F24"
screen.bgcolor(ORANGE)

SCREEN_WIDTH, SCREEN_HEIGHT = 960, 720
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

screen.title("Ping Pong")

screen.tracer(0)


left_bat = Bat(-440, 0)
right_bat = Bat(440, 0)

ball = Ball()

score = Score()

# Listen for screen/window inputs (such as clicking a key)
screen.listen()
# Binding the specific function to its corresponding (keyboard) key
screen.onkeypress(left_bat.up, "w")
screen.onkeypress(left_bat.down, "s")
screen.onkeypress(right_bat.up, "Up")
screen.onkeypress(right_bat.down, "Down")


def main():
    while True:
        time.sleep(ball.speed)
        screen.update()
        ball.move()
        
        # Bat and ball collisions
        if ball.distance(left_bat) < 50 and ball.xcor() < -320 or ball.distance(right_bat) < 50 and ball.xcor() > 320:
            ball.bounce_x()
            
        if ball.ycor() > 320 or ball.ycor() < -320:
            ball.bounce_y()
        
        # Player score
        if ball.xcor() > 520:
            score.left_score_increase()
            ball.reset()
            
        if ball.xcor() < -520:
            score.right_score_increase()
            ball.reset()
            
        #AI Player
        if right_bat.ycor() < ball.ycor() and abs(right_bat.ycor() - ball.ycor()) > 60:
            right_bat.up()
        elif right_bat.ycor() > ball.ycor() and abs(right_bat.ycor() - ball.ycor()) > 60:
            right_bat.down()
        

if __name__ == "__main__":
    main()