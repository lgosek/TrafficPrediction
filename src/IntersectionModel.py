import RoadModel
from random import choices

class Intersection:
    def __init__(self, incoming_roads, outgoing_roads, probability_matrix, lights=True):
        self.inRoads = incoming_roads
        self.outRoads = outgoing_roads
        self.probabilities = probability_matrix
        self.posibilities = list(range(0, len(self.outRoads)))
        self.counter = 0

        self.lights = lights;
        if self.lights:
            self.greenLight = 0
            for road in self.inRoads:
                road.toggleLights()
            self.inRoads[self.greenLight].toggleLights()

    def changeRoad(self):
        for road in range(len(self.inRoads)):
            cars = self.inRoads[road].removeCar()
            if not cars:
                continue
            else:
                for car in cars:
                    choice = choices(self.posibilities, self.probabilities[road])[0]
                    self.counter = self.counter + 1

                    if road%2 == 0:
                        if choice == road+1:
                            changeDirection = False
                        else:
                            changeDirection = True
                    else:
                        if choice == road-1:
                            changeDirection = False
                        else:
                            changeDirection = True

                    self.outRoads[choice].addCar(car, changeDirection)
                for oroad in self.outRoads:
                    oroad.order()

    def toggleLights(self):
        if self.lights:
            self.inRoads[self.greenLight].toggleLights()
            self.greenLight = (self.greenLight+1)%len(self.inRoads)
            self.inRoads[self.greenLight].toggleLights()
