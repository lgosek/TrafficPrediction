import Cars
import random


p = 0.15
PCHANGE = 0.8

def OrderCars (car):
    return car.posX


class Model:
    def __init__(self, X, Y, gridLen, carNum, lanes, maxVel, direction):
        #constants
        self.ModelX = X
        self.ModelY = Y
        # grid length
        self.GRIDLEN = gridLen
        # number of cars generated
        self.CARNUM = carNum
        # number of traffic lanes
        self.LANES = lanes
        # maximum velocity
        self.MAXVEL = maxVel
        # road direction on the plot- 1 right, 2 - left, 3 - up, 4 - down
        self.direction = direction

        # generating cars
        self.traffic = [[Cars.Car(self.GRIDLEN, j, 0, self.MAXVEL) for i in range(0, self.CARNUM)] for j in range(self.LANES)]

        # placing cars on the grid in ascending order
        for i in range (self.LANES):
            self.traffic[i].sort(key=OrderCars)

        self.redLight = False

    # method handling cars' velocity changes
    def updateCarVel(self, car, pred):
        if car.posX == pred.posX:
            dist = self.MAXVEL+1
        else:
            dist = (pred.posX - car.posX) % self.GRIDLEN - 1
        vtemp = min(car.currentVel +1, dist, car.maxVel)

        car.currentVel = max(vtemp-1, 0) if random.random()<p else vtemp

    # method handling finding the nearest car on the grid
    def findNearest(self, destLane, posX):
        if not self.traffic[destLane]:
            return False, False
        for idx, car in enumerate(self.traffic[destLane]):
            if car.posX > posX:
                return self.traffic[destLane][idx-1], car
        return self.traffic[destLane][-1], self.traffic[destLane][0]

    # method handling traffic lane switching
    def switchLane(self, car, pred, dir):
        destLane = car.posY + dir
        if destLane < 0 or destLane > self.LANES-1:
            return 0

        gap = (pred.posX - car.posX) % self.GRIDLEN - 1
        back,front = self.findNearest(destLane,car.posX)
        if back==False and front == False:
            gapo = self.MAXVEL +1
            gapob = self.MAXVEL +1
        else:
            if back.posX == car.posX or front.posX == car.posX:
                return 0

            gapo = (front.posX - car.posX) %self.GRIDLEN -1
            gapob = (car.posX - back.posX) %self.GRIDLEN -1

        if dir == 1 and gap<car.currentVel+1 and gapo > car.currentVel+1 and gapob> self.MAXVEL and random.random()<PCHANGE:
            ret = 1
        elif dir == -1 and gapo > car.currentVel+1 and gapob> self.MAXVEL and random.random()<PCHANGE:
            ret = -1
        else:
            ret = 0

        return ret

    # method handling placing new car on the grid
    def addCar(self, car, changeDirection):
        if car.posY > self.LANES-1:
            car.posX = car.posY - self.LANES-1
            car.posY = self.LANES-1
        else:
            car.posX = 0
        if changeDirection:
            car.currentVel = 1
        self.traffic[car.posY].append(car)

    # method handling removing car from the grid
    def removeCar(self):
        carsOutsideGrid = []
        for lane in self.traffic:
            for car in lane:
                if car.posX > self.GRIDLEN:
                    carsOutsideGrid.append(car)
                    lane.remove(car)

        return carsOutsideGrid

    # method handling "traffic lights switching" by adding stationary car at the end of the road
    def toggleLights(self):
        if self.redLight:
            for i in range(self.LANES):
                self.traffic[i] = self.traffic[i][:-1]
        else:
            for i in range(self.LANES):
                self.traffic[i].append(Cars.Car(self.GRIDLEN, i, 1, 0))

        self.redLight = not self.redLight

    def order(self):
        for i in range(self.LANES):
            self.traffic[i].sort(key=OrderCars)

    # method performing one iteration of simulation for each car on the grid
    def runSim(self, time):

        newTraffic = [[] for j in range(self.LANES)]
        #handling transitions between traffic lanes
        if self.LANES > 1:
            for i in range(self.LANES):
                for j,car in enumerate(self.traffic[i]):
                    if car.id ==1:
                        newTraffic[i].append(car)
                        continue
                    change = self.switchLane(car, self.traffic[i][(j+1)%len(self.traffic[i])], -1)
                    if change == 0:
                        change = self.switchLane(car, self.traffic[i][(j+1)%len(self.traffic[i])], 1)
                    car.posY = car.posY + change
                    newTraffic[i+change].append(car)

            for i in range (self.LANES):
                newTraffic[i].sort(key=OrderCars)
        else:
            newTraffic = self.traffic

        for i in range(self.LANES):
            for j in range(len(newTraffic[i])):
                if newTraffic[i][j].id == 0:
                    self.updateCarVel(newTraffic[i][j], newTraffic[i][(j+1)%len(newTraffic[i])])

        for lane in newTraffic:
            for e in lane:
                if e.id == 0:
                    e.posX = (e.posX + e.currentVel)

        self.traffic = newTraffic