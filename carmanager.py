from turtle import Turtle as t  
import random
color=["green","red","yellow","blue","purple","orange"]
dis_y=[]  
car=[]
for i in range(-210,220,20):
    dis_y.append(i)
class car(t):
    def __init__(self):
        super().__init__()  
        self.cars=[] 
        self.level=20
    def createcar(self):  
        rand=random.randint(1,6) 
        if(rand==1):
          car=t("square")
          car.color(random.choice(color))  
          car.shapesize(stretch_wid=1,stretch_len=2) 
          car.penup()
          car.goto(x=270,y=random.choice(dis_y))  
          self.cars.append(car)
    def move(self): 
        for car in self.cars:
            car.backward(self.level)
    
    def gameover(self):
         self.penup()
         self.goto(-50,0)
         self.write(arg="Game Over",font="Algerian 25")
    def levelup(self):  
        self.level+=10
        for car in self.cars:
            car.backward(self.level)
        




