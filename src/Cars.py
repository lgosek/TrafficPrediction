import random

class Car:
    def __init__(self, gridSize):
        self.position = random.randint(0, gridSize)
        self.maxVel = 5 #random.randint(3,5)
        self.currentVel = 0

