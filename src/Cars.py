import random

class Car:
    def __init__(self, gridSize, lane, carNum, MaxVel):
        self.posX = random.randint(0, gridSize)
        self.posY = lane
        self.maxVel = random.randint(2,MaxVel)
        self.currentVel = 0
        self.id = carNum

