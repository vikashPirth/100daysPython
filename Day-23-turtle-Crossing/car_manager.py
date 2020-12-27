from turtle import Turtle
import  random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars= []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_choice = random.randrange(1,6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=0.5, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, y=random.randint(-260, 280))
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed +=MOVE_INCREMENT




