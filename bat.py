from turtle import Turtle

class Bat(Turtle):
    SHAPE = "square"
    BLACK = "#000000"
    BAT_HEIGHT, BAT_WIDTH = 7, 1.5
    Y_MOVE = 30
    
    def __init__(self, x , y):
        super().__init__()
        self.shape(self.SHAPE)
        self.color(self.BLACK)
        self.penup()
        self.shapesize(self.BAT_HEIGHT, self.BAT_WIDTH)
        self.goto(x,y)
        
    def up(self):
        y = self.ycor() + self.Y_MOVE
        self.goto(self.xcor(), y)
        
    def down(self):
        y = self.ycor() - self.Y_MOVE
        self.goto(self.xcor(), y)
        