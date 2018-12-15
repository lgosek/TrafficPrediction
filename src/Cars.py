import random

class Car:
    def __init__(self, gridSize, lane, carNum, MaxVel):
        self.id = carNum    # 0 - normal car, 1 - traffic light
        if carNum == 1:
            self.posX = gridSize
            self.maxVel = 0
        else:
            self.posX = random.randint(0, gridSize)
            self.maxVel = random.randint(2, MaxVel)
        self.posY = lane
        self.currentVel = 0

