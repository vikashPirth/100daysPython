import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player  = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(key = "Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.cars:
        if car.distance(player)< 20:
            game_is_on = False
            score_board.game_over()

    if player.is_player_at_final():
        player.goto_start_position()
        car_manager.level_up()
        score_board.update_scoreboard()


screen.exitonclick()
