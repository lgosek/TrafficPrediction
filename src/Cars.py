import random

class Car:
    def __init__(self, gridSize, lane):
        self.posX = random.randint(0, gridSize)
        self.posY = lane
        self.maxVel = random.randint(2,5)
        self.currentVel = 0

