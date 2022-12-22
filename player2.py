from turtle import Turtle
class playermanager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup() 
        self.shape("turtle")  
        self.color("purple")
        self.setheading(90)
        self.goto(0,-230)
        
        
    def starting(self):
        self.shape("turtle")
        self.color("purple")
        self.penup() 
        self.setheading(90)   
        self.goto(0,-230) 
        
        
    def up(self):
        self.forward(20) 
    def down(self):
        self.backward(20)
