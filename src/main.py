import Cars
import random
from tkinter import *
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#długość siatki
GRIDLEN = 150
#Czas symulacji
TIME = 500
#Liczba samochodów
CARNUM = 20
#Liczba pasów ruchu
LANES = 2
#Maksymalna prędkość
MAXVEL = 5

#liczba wyroznionych samochodow
HIGHLIGHTED = 10



p = 0.15
PCHANGE = 0.8

def OrderCars (car):
    return car.posX

class Model:
    def __init__(self, tk, canvas):
        self.tk = tk
        self.canvas = canvas

        # generowanie samochodów
        self.traffic = [ [Cars.Car(GRIDLEN, j, j*CARNUM+i,canvas) for i in range(0, CARNUM)]  for j in range(LANES) ]

        # ułożenie samochodów na siatce rosnąco względem posX
        for i in range (LANES):
            self.traffic[i].sort(key=OrderCars)

        #grd = self.printGrid()



    def updateCarVel(self, car, pred):
        if car.posX == pred.posX:
            dist = 6
        else:
            dist = (pred.posX - car.posX) % GRIDLEN - 1
        vtemp = min(car.currentVel +1, dist, car.maxVel)

        car.currentVel = max(vtemp-1, 0) if random.random()<p else vtemp

    def printGrid(self):
        grid = [[None for i in range(0, GRIDLEN)] for j in range(LANES)]
        for j,lane in enumerate(self.traffic):
            for car in lane:
                grid[j][car.posX - 1] = car.posY

        return grid

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
        if destLane < 0 or destLane > LANES-1:
            return 0

        gap = (pred.posX - car.posX) % GRIDLEN - 1

        print ("Car",car.posX,car.posY,sep=' ')

        back,front = self.findNearest(destLane,car.posX)
        if back==False and front == False:
            print("No neighbour")
            # if car.posY == 0:
            #     return 1
            # else:
            #     return -1
            gapo = MAXVEL +1
            gapob = MAXVEL +1
        else:
            if back.posX == car.posX or front.posX == car.posX:
                return 0

            print("Back",back.posX,"Front",front.posX,sep=' ')
            gapo = (front.posX - car.posX) %GRIDLEN -1
            gapob = (car.posX - back.posX) %GRIDLEN -1

        if dir == 1 and gap<car.currentVel+1 and gapo > car.currentVel+1 and gapob> MAXVEL and random.random()<PCHANGE:
            ret =  1
        elif dir == -1 and gapo > car.currentVel+1 and gapob> MAXVEL and random.random()<PCHANGE:
            ret =  -1
        else:
            ret =  0
        print("Returned ", ret)
        return ret

    #RunSim wykonuje tylko jedną iterację i zwraca
    def runSim(self):

        print("Iteration start")
        print("Traffic:")
        for lane in self.traffic:
            for car in lane:
                print(car.posX," ",car.posY)


        newTraffic = [[] for j in range(LANES)]
        #obsługa przejść między pasami
        for i in range(LANES):
            for j,car in enumerate(self.traffic[i]):
                change = self.switchLane(car, self.traffic[i][(j+1)%len(self.traffic[i])], -1)
                if change == 0:
                    change = self.switchLane(car, self.traffic[i][(j+1)%len(self.traffic[i])], 1)
                car.laneChange = change
                car.posY = car.posY + change
                newTraffic[i+change].append(car)

        for i in range (LANES):
            newTraffic[i].sort(key=OrderCars)

        for i in range(LANES):
            for j in range(len(newTraffic[i])):
                self.updateCarVel(newTraffic[i][j], newTraffic[i][(j+1)%len(newTraffic[i])])

        #przesuwanie samochodów
        for lane in newTraffic:
            for e in lane:
                e.posX = (e.posX + e.currentVel) % GRIDLEN
                e.updateMarker()


        self.traffic = newTraffic
        #return self.printGrid()


tk = Tk()
canvas = Canvas(tk, width = 1200, height = 400)
canvas.pack()


model = Model(tk,canvas)

while True:
    tk.update()
    model.runSim()
    sleep(0.5)


