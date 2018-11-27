import Cars
import random
from time import sleep

#długość siatki
GRIDLEN = 150
#Czas symulacji
TIME = 500
#Liczba samochodów
CARNUM = 20

p = 0.2

def OrderCars (car):
    return car.position

class Model:
    def __init__(self):
        # generowanie samochodów
        self.traffic = [Cars.Car(GRIDLEN) for i in range(0, CARNUM)]
        # ułożenie samochodów na siatce rosnąco względem position
        self.traffic.sort(key=OrderCars)



    def UpdateCar(self,i,pred):
        dist = (pred.position - self.traffic[i].position) % GRIDLEN -1
        vtemp = min(self.traffic[i].currentVel +1, dist, self.traffic[i].maxVel)

        self.traffic[i].currentVel = max(vtemp-1, 0) if random.random()<p else vtemp

    def printGrid(self):
        grid = [0 for i in range(GRIDLEN)]
        for car in self.traffic:
            grid[car.position] = 1

        #retString = ""
        for el in grid:
            if el==0:
                print('_', end='')
                #retString = retString + "-"
            else:
                print('O', end='')
                #retString = retString + "O"

    def runSim(self):
        for iter in range(TIME):
            firstCar = self.traffic[0]
            for i in range(CARNUM - 1):
                self.UpdateCar(i, self.traffic[i+1])
            self.UpdateCar(-1, firstCar)

            for e in self.traffic:
                e.position = (e.position + e.currentVel) % GRIDLEN

            self.printGrid()
            sleep(0.1)
            print("")
            #print('\n' * 12)  # prints 80 line breaks
            #sleep(0.5)



model = Model()

model.runSim()


