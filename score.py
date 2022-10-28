from turtle import Turtle

class Score(Turtle):
    WHITE = "#FFFFFF"
    left_score = 0
    right_score = 0
    
    
    def __init__(self):
        super().__init__()
        self.color(self.WHITE)
        self.penup()
        self.hideturtle()
        self.update()
        
    def update(self):
        self.goto(-100, 250)
        self.write(f"Player A: {self.left_score}      ", align="center", font=('Courier', 24, 'bold'))
        self.goto(100, 250)
        self.write(f"      Player B: {self.right_score}", align="center", font=('Courier', 24, 'bold'))

    def left_score_increase(self):
        self.left_score += 1
        self.clear()
        self.update()
        
    def right_score_increase(self):
        self.right_score += 1
        self.clear()
        self.update()