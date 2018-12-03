import Cars
import random
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#długość siatki
GRIDLEN = 150
#Czas symulacji
TIME = 500
#Liczba samochodów
CARNUM = 40
#Liczba pasów ruchu
LANES = 2
#Maksymalna prędkość
MAXVEL = 5

#liczba wyroznionych samochodow
HIGHLIGHTED = 40;



p = 0.15
PCHANGE = 0.8

def OrderCars (car):
    return car.posX

class Model:
    def __init__(self):
        # generowanie samochodów
        #numRight = round(random.random()*CARNUM)
        # traffic[0] - prawy pas, traffic[1] - lewy pas
        #self.traffic = [[Cars.Car(GRIDLEN, 0) for i in range(0, numRight)], [Cars.Car(GRIDLEN, 1) for i in range(0, CARNUM-numRight)]]
        self.traffic = [ [Cars.Car(GRIDLEN, j, j*round(CARNUM/2)+i) for i in range(0, round(CARNUM/2))]  for j in range(LANES) ]
        #self.traffic = [Cars.Car(GRIDLEN, 0) for i in range(0, CARNUM)]
        # ułożenie samochodów na siatce rosnąco względem posX
        for i in range (LANES):
            self.traffic[i].sort(key=OrderCars)
        # self.traffic[0].sort(key=OrderCars)
        # self.traffic[1].sort(key=OrderCars)
        #self.traffic.sort(key=OrderCars)

        self.fig, self.ax = plt.subplots()
        self.x = np.arange(0, GRIDLEN, 1)

        self.highlightID = random.sample(range(0, CARNUM), HIGHLIGHTED)
        grd = self.printGrid()



        # self.line0 = self.ax.plot(self.x, grd[0], marker='.', linestyle='', color='b')[0]
        # self.line1 = self.ax.plot(self.x, grd[1], marker='.', linestyle='', color='b')[0]

        self.lines = [self.ax.plot(self.x, grd[i], marker='.', linestyle='', color='b')[0] for i in range(LANES)]
        self.lines.append(self.ax.plot(self.x, grd[2], marker='.', linestyle='', color='r')[0])


        self.ani = animation.FuncAnimation(
            self.fig, self.animate, init_func=self.init_plot,  interval=500, blit=False, save_count=50)



    def updateCarVel(self, car, pred):
        if car.posX == pred.posX:
            dist = 6
        else:
            dist = (pred.posX - car.posX) % GRIDLEN - 1
        vtemp = min(car.currentVel +1, dist, car.maxVel)

        car.currentVel = max(vtemp-1, 0) if random.random()<p else vtemp

    def printGrid(self):
        grid = [[None for i in range(0, GRIDLEN)] for j in range(LANES+1)]
        for j,lane in enumerate(self.traffic):
            for car in lane:
                if car.id in self.highlightID:
                    grid[2][car.posX - 1] = car.posY
                else:
                    grid[j][car.posX - 1] = car.posY
            # grid[0][car.posX - 1] = car.posY
            # grid[1][car.posX - 1] = car.posY+1
        #grid = [list(map(lambda x: None if x== HIGHLIGHT_ID else (0 if x is not None else None), grid[0])),
        #        list(map(lambda x: None if x == HIGHLIGHT_ID else (1 if x is not None else None), grid[1]))]
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
                car.posY = car.posY + change
                newTraffic[i+change].append(car)

        for i in range (LANES):
            newTraffic[i].sort(key=OrderCars)
        # newTraffic[0].sort(key=OrderCars)
        # newTraffic[1].sort(key=OrderCars)

        for i in range(LANES):
            for j in range(len(newTraffic[i])):
                self.updateCarVel(newTraffic[i][j], newTraffic[i][(j+1)%len(newTraffic[i])])

        # firstCar = self.traffic[0]
        # for i in range(CARNUM - 1):
        #     self.UpdateCarVel(i, self.traffic[i + 1])
        # self.UpdateCarVel(-1, firstCar)

        for lane in newTraffic:
            for e in lane:
                e.posX = (e.posX + e.currentVel) % GRIDLEN

        self.traffic = newTraffic

        return self.printGrid()


    def animate(self,i):
        ret = self.runSim()
        # self.line0.set_ydata(ret[0])  # update the data.
        # self.line1.set_ydata(ret[1])
        for i in range(LANES+1):
            self.lines[i].set_ydata(ret[i])
        return self.lines

    def init_plot(self):
        # self.line0.set_ydata([None for i in range(0, GRIDLEN)])
        # self.line1.set_ydata([None for i in range(0, GRIDLEN)])
        for i in range(LANES):
            self.lines[i].set_ydata([None for j in range(0, GRIDLEN)])
        return self.lines

    def start(self):
        plt.xlim((0, GRIDLEN))
        plt.ylim((-0.5,20))
        plt.show()



model = Model()

model.start()


