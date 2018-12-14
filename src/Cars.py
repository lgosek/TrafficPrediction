import random

CARSIZE = 1
SPACING = 5

def convertY (Y):
    return 400-Y

class Car:
    def __init__(self, gridSize, lane, carNum, canvas):
        self.posX = random.randint(0, gridSize)
        self.posY = lane
        self.maxVel = random.randint(2,5)
        self.currentVel = 0
        self.id = carNum
        self.canvas = canvas
        self.laneChange = 0
        cx = (self.posX)
        cy = convertY(SPACING + self.posY*(CARSIZE+SPACING))-CARSIZE
        self.marker = canvas.create_rectangle(cx, cy, cx+CARSIZE, cy+CARSIZE, fill="red", tags=)

    def updateMarker(self):
        print(self.id)
        curPosX = self.canvas.coords(self.marker)[0]
        shiftX = self.posX - curPosX
        self.canvas.move(self.marker, shiftX, self.laneChange*(CARSIZE+SPACING))

