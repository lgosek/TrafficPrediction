import RoadModel
import Cars
from random import choices


class Edge:
    def __init__(self, incoming_road, outgoing_road, probability):
        self.inRoad = incoming_road
        self.outRoad = outgoing_road
        self.probability = probability
        self.counter = 0

    # function generating new car with specified probability and adding that car to outgoing road
    def generateNewCar(self):
        isGenerated = choices([True, False], [self.probability, 1-self.probability])[0]

        if isGenerated:
            car = Cars.Car(self.outRoad.GRIDLEN, 0, 0, self.outRoad.MAXVEL)
            self.outRoad.addCar(car, True)
            self.counter = self.counter + 1
            self.outRoad.order()

        return isGenerated

    # function deleting cars leaving the simulation area
    def removeCarsOutsideGrid(self):
        removedCars = self.inRoad.removeCar()
        self.counter = self.counter + len(removedCars)
