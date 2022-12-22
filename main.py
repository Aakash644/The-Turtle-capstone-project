from turtle import Turtle as t,Screen as s  
import time 
import player2
from carmanager import car
from score import scoreboard
screen=s()
screen.setup(width=600,height=500) 
screen.bgcolor("white")  
screen.tracer(0)             
car1=car()  
score=scoreboard()
player1=player2.playermanager() 
screen.listen()
screen.onkey(fun=player1.up,key="w")
screen.onkey(fun=player1.down,key="s")
gameison=True 
while(gameison):
    time.sleep(0.3)
    screen.update() 
    
    car1.createcar() 
    car1.move()  
    for car in car1.cars:
        if(car.distance(player1)<20):
            gameison=False 
            car1.gameover()
    if player1.ycor()>250: 
        player1.starting()
        score.refresh()
        car1.levelup()

screen.exitonclick()