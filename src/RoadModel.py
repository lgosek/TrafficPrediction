import Cars
import random


p = 0.15
PCHANGE = 0.8

def OrderCars (car):
    return car.posX


class Model:
    def __init__(self, X, Y, gridLen, carNum, lanes, maxVel, direction):
        #stałe
        self.ModelX = X
        self.ModelY = Y
        # długość siatki
        self.GRIDLEN = gridLen
        # Liczba samochodów
        self.CARNUM = carNum
        # Liczba pasów ruchu
        self.LANES = lanes
        # Maksymalna prędkość
        self.MAXVEL = maxVel
        # Kierunek - 1 w prawo, 2 - w lewo, 3 - w górę, 4 - w dół
        self.direction = direction

        # generowanie samochodów
        self.traffic = [[Cars.Car(self.GRIDLEN, j, 0, self.MAXVEL) for i in range(0, self.CARNUM)] for j in range(self.LANES)]

        # ułożenie samochodów na siatce rosnąco względem posX
        for i in range (self.LANES):
            self.traffic[i].sort(key=OrderCars)

        self.redLight = False

    def updateCarVel(self, car, pred):
        if car.posX == pred.posX:
            dist = self.MAXVEL+1
        else:
            dist = (pred.posX - car.posX) % self.GRIDLEN - 1
        vtemp = min(car.currentVel +1, dist, car.maxVel)

        car.currentVel = max(vtemp-1, 0) if random.random()<p else vtemp

    def findNearest(self, destLane, posX):
        if not self.traffic[destLane]:
            return False, False
        for idx, car in enumerate(self.traffic[destLane]):
            if car.posX > posX:
                return self.traffic[destLane][idx-1], car
        return self.traffic[destLane][-1], self.traffic[destLane][0]

    #dir = 1 -> to the left, -1 -> to the right
    def switchLane(self, car, pred, dir):
        destLane = car.posY + dir
        if destLane < 0 or destLane > self.LANES-1:
            return 0

        gap = (pred.posX - car.posX) % self.GRIDLEN - 1

        # print ("Car",car.posX,car.posY,sep=' ')

        back,front = self.findNearest(destLane,car.posX)
        if back==False and front == False:
            # print("No neighbour")

            gapo = self.MAXVEL +1
            gapob = self.MAXVEL +1
        else:
            if back.posX == car.posX or front.posX == car.posX:
                return 0

            # print("Back",back.posX,"Front",front.posX,sep=' ')
            gapo = (front.posX - car.posX) %self.GRIDLEN -1
            gapob = (car.posX - back.posX) %self.GRIDLEN -1

        if dir == 1 and gap<car.currentVel+1 and gapo > car.currentVel+1 and gapob> self.MAXVEL and random.random()<PCHANGE:
            ret =  1
        elif dir == -1 and gapo > car.currentVel+1 and gapob> self.MAXVEL and random.random()<PCHANGE:
            ret =  -1
        else:
            ret =  0
        # print("Returned ", ret)
        return ret

    def addCar(self, car, changeDirection):
        if car.posY > self.LANES-1:
            car.posX = car.posY - self.LANES-1
            car.posY = self.LANES-1
        else:
            car.posX = 0;
        if changeDirection:
            car.currentVel = 1
        self.traffic[car.posY].append(car)

    def removeCar(self):
        carsOutsideGrid = []
        for lane in self.traffic:
            for car in lane:
                if car.posX > self.GRIDLEN:
                    carsOutsideGrid.append(car)
                    lane.remove(car)

        return carsOutsideGrid

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
    #RunSim wykonuje tylko jedną iterację i zwraca
    def runSim(self, time):

        # adding and deleting lights
        #if time%20 == 0 and time>0:
        #    if (time//25)%2 == 1 :
        #        for i in range(self.LANES):
        #           self.traffic[i].append(Cars.Car(self.GRIDLEN,i,1,0))
        #    else:
        #        for i in range(self.LANES):
        #            self.traffic[i] = self.traffic[i][:-1]




        # print("Iteration start")
        # print("Traffic:")
        # for lane in self.traffic:
        #     for car in lane:
        #         print(car.posX," ",car.posY)

        newTraffic = [[] for j in range(self.LANES)]
        #obsługa przejść między pasami
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