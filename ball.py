from turtle import Turtle

class Ball(Turtle):
    SHAPE = "circle"
    WHITE = "#FFFFFF"
    BAT_HEIGHT, BAT_WIDTH = 1, 1
    x_move = 10
    y_move = 10
    speed = 0.03
    
    def __init__(self):
        super().__init__()
        self.shape(self.SHAPE)
        self.color(self.WHITE)
        self.shapesize(self.BAT_HEIGHT, self.BAT_WIDTH)
        self.penup()
        
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
        
    def bounce_x(self):
        self.x_move *= -1
        self.speed *= 0.96
        
    def bounce_y(self):
        self.y_move *= -1
        
    def reset(self):
        self.goto(0,0)
        self.bounce_x()
        # Speed of ball increases after the first point
        self.speed = 0.02