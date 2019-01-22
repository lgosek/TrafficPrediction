import random

class Car:
    def __init__(self, gridSize, lane, carNum, MaxVel, position = -1):
        # type of car - normal or traffic light (as trafiic lights are implemented as permanently stationary cars)
        self.id = carNum
        # posX - vertical position of car
        # maxVel - max available velocity for that car
        # curVel - cuurent velocity of the car
        # posY - number of lane on which the car is currently driving
        if carNum == 1:
            self.posX = gridSize
            self.maxVel = 0
        elif position != -1:
            self.posX = position
            self.maxVel = MaxVel
        else:
            self.posX = random.randint(0, gridSize)
            self.maxVel = random.randint(2, MaxVel)
        self.posY = lane
        self.currentVel = 0

