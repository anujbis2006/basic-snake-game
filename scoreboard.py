from turtle import Turtle
ALIGNMENT = "center"
FONT  = ("Courier",24,"normal")





class Scoreboard(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("file.txt") as data:
            self.high_score = int(data.read())
        self.color ("white")
        self.penup()
        self.goto(0, 270)
        self.write(f" score : {self.score}",align = ALIGNMENT,font =FONT )
        self.hideturtle()
        self.update_Scoreboard()

    def update_Scoreboard(self):
        self.clear()
        self.write(f" score : {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("file.txt",mode = "w") as data:
                data.write(f"{self.high_score}")
            self.score = 0
            self.update_Scoreboard()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align = ALIGNMENT, font = FONT)
    def increase_Score(self):
        self.score +=1
        self.clear()
        self.write(f" score : {self.score}", align=ALIGNMENT, font=FONT)