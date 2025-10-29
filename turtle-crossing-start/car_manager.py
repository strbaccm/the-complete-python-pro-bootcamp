from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = 300
HEADING = 180


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.moving_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto((STARTING_POSITION, random_y))
            self.all_cars.append(new_car)


    def mov_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


    def level_up(self):
        self.moving_speed += MOVE_INCREMENT