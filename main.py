import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_on = False

    if player.ycor() > player.finish:
        player.level_complete()
        car_manager.speed_up()
        scoreboard.level_up()

screen.exitonclick()
