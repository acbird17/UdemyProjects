from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()
            
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center", font=("Arial", 18, "normal"))
        
    def point(self):
        self.score += 1
        self.update_score()
        
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center", font=("Arial", 18, "normal"))
        self.score = 0
        self.update_score()