import RoadModel
from random import choices

class Intersection:
    def __init__(self, incoming_roads, outgoing_roads, probability_matrix):
        self.inRoads = incoming_roads
        self.outRoads = outgoing_roads
        self.probabilities = probability_matrix
        self.posibilities = list(range(0, len(self.outRoads)))
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

                    self.outRoads[choices(self.posibilities, self.probabilities[road])[0]].addCar(car)

    def toggleLights(self):
        self.inRoads[self.greenLight].toggleLights()
        self.greenLight = (self.greenLight+1)%len(self.inRoads)
        self.inRoads[self.greenLight].toggleLights()
