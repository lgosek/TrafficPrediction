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
CARNUM = 5

p = 0.2

def OrderCars (car):
    return car.position

class Model:
    def __init__(self):
        # generowanie samochodów
        self.traffic = [Cars.Car(GRIDLEN) for i in range(0, CARNUM)]
        # ułożenie samochodów na siatce rosnąco względem position
        self.traffic.sort(key=OrderCars)

        self.fig, self.ax = plt.subplots()
        self.x = np.arange(0, GRIDLEN, 1)

        self.line, = self.ax.plot(self.x, self.printGrid(), marker='.')
        self.ani = animation.FuncAnimation(
            self.fig, self.animate, init_func=self.init_plot,  interval=500, blit=False, save_count=50)



    def UpdateCar(self,i,pred):
        dist = (pred.position - self.traffic[i].position) % GRIDLEN -1
        vtemp = min(self.traffic[i].currentVel +1, dist, self.traffic[i].maxVel)

        self.traffic[i].currentVel = max(vtemp-1, 0) if random.random()<p else vtemp

    def printGrid(self):
        grid = [None for i in range(0, GRIDLEN)]
        for car in self.traffic:
            grid[car.position-1] = 1


        return grid



    #RunSim wykonuje tylko jedną iterację i zwraca
    def runSim(self):

        firstCar = self.traffic[0]
        for i in range(CARNUM - 1):
            self.UpdateCar(i, self.traffic[i+1])
        self.UpdateCar(-1, firstCar)

        for e in self.traffic:
            e.position = (e.position + e.currentVel) % GRIDLEN


        return self.printGrid()


    def animate(self,i):
        self.line.set_ydata(self.runSim())  # update the data.
        return self.line,

    def init_plot(self):
        self.line.set_ydata([None for i in range(0, GRIDLEN)])
        return self.line,

    def start(self):
        plt.xlim((0, GRIDLEN))
        plt.show()



model = Model()

model.start()


