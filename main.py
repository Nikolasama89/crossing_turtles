import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
level = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move_player, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # CHECKING COLLISION BETWEEN OBJECTS. NUMBER 20 IS RESULT FROM HALF OF THE SIZE OF CAR OBJECT(20X40)

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            level.game_over()
            game_is_on = False

    # CHECKING IF PLAYER REACH TOP OF THE SCREEN
    if player.is_at_finish_line():
        player.go_to_start()
        level.level_update()
        car_manager.level_up()


screen.exitonclick()
