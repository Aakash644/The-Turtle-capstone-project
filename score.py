from turtle import Turtle
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1 
        self.penup()
        self.color("black") 
        self.goto(x=-280,y=230) 
        self.hideturtle()
        self.write(arg=f"Level:{self.level}",font="Algerian 15")

    def refresh(self):
        self.clear()
        self.level+=1 
        self.penup()
        self.color("black") 
        self.goto(x=-280,y=230)
        self.write(arg=f"Level:{self.level}",font="Algerian 15")
