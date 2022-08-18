from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()
        
    def update_score(self):
        self.write(f"{self.score_l}   : Score :   {self.score_r}", False, align="center", font=("Arial", 18, "normal"))
        
    def point_l(self):
        self.score_l += 1
        self.clear()
        self.update_score()
        
    def point_r(self):
        self.score_r += 1
        self.clear()
        self.update_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", False, align="center", font=("Arial", 18, "normal"))