import RoadModel
import IntersectionModel
import EdgeModel
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

MODELNUM = 2
SPACING = 2


class Simulation:
    def __init__(self, showPlot):
        self.time = 0
        self.minutes = 0
        self.showPlot = showPlot

        self.outFile = open("output.txt", "w")
        # docelowo wersja poniżej, żeby nie nadpisywało danych, na razie zakomentowane żeby nie spamować plikami
        # filename = time.strftime("%d%b%H%M%S.txt")
        # self.outFile = open(filename, "w")

        self.models = [
            RoadModel.Model(X=5, Y=0, gridLen=92, carNum=0, lanes=1, maxVel=5, direction=1),   #0
            RoadModel.Model(X=97, Y=2, gridLen=92, carNum=0, lanes=1, maxVel=5, direction=2),  #1

            RoadModel.Model(X=102, Y=3, gridLen=52, carNum=0, lanes=2, maxVel=5, direction=3), #2
            RoadModel.Model(X=98, Y=55, gridLen=52, carNum=0, lanes=2, maxVel=5, direction=4), #3

            RoadModel.Model(X=4, Y=3, gridLen=52, carNum=0, lanes=2, maxVel=5, direction=3),   #4
            RoadModel.Model(X=0, Y=55, gridLen=52, carNum=0, lanes=2, maxVel=5, direction=4),  #5

            RoadModel.Model(X=5, Y=56, gridLen=92, carNum=0, lanes=1, maxVel=5, direction=1),  #6
            RoadModel.Model(X=97, Y=58, gridLen=92, carNum=0, lanes=1, maxVel=5, direction=2), #7

            RoadModel.Model(X=102, Y=59, gridLen=108, carNum=0, lanes=2, maxVel=5, direction=3), #8
            RoadModel.Model(X=98, Y=167, gridLen=108, carNum=0, lanes=2, maxVel=5, direction=4), #9

            RoadModel.Model(X=4, Y=59, gridLen=108, carNum=0, lanes=2, maxVel=5, direction=3),   #10
            RoadModel.Model(X=0, Y=167, gridLen=108, carNum=0, lanes=2, maxVel=5, direction=4),  #11

            RoadModel.Model(X=5, Y=168, gridLen=92, carNum=0, lanes=1, maxVel=5, direction=1),  # 12
            RoadModel.Model(X=97, Y=170, gridLen=92, carNum=0, lanes=1, maxVel=5, direction=2), # 13

            RoadModel.Model(X=102, Y=171, gridLen=52, carNum=0, lanes=2, maxVel=5, direction=3),  # 14
            RoadModel.Model(X=98, Y=223, gridLen=52, carNum=0, lanes=2, maxVel=5, direction=4),  # 15

            RoadModel.Model(X=4, Y=171, gridLen=52, carNum=0, lanes=2, maxVel=5, direction=3),    # 16
            RoadModel.Model(X=0, Y=223, gridLen=52, carNum=0, lanes=2, maxVel=5, direction=4),   # 17

            RoadModel.Model(X=5, Y=224, gridLen=92, carNum=0, lanes=1, maxVel=5, direction=1),  # 18
            RoadModel.Model(X=97, Y=226, gridLen=92, carNum=0, lanes=1, maxVel=5, direction=2)  # 19

        ]
        self.edgeRoads = [
            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 0
            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=2),  # 1

            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=3),  # 2
            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=4),  # 3

            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=3),  # 4
            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=4),  # 5

            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 6
            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 7

            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 8
            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 9

            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 10
            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 11

            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 12
            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 13

            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 14
            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 15

            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 16
            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 17

            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 18
            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 19

            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 20
            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 21

            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 22
            RoadModel.Model(X=0, Y=0, gridLen=15, carNum=0, lanes=1, maxVel=5, direction=1),  # 23
        ]
            #  przy definiowaniu skrzyżowania podajemy po kolei parami drogi które leżą na przeciwko siebie (zarówno wejściowe i wyjściowe)
            #  prawdopodobieństwa podajemy tak, że n-ta tablica oznacza prawdopodobieństwa wyboru drugi zjazdowej dla n-tej drogi wjazdowej
        self.intersections = [
            IntersectionModel.Intersection([self.models[1], self.edgeRoads[0], self.models[5], self.edgeRoads[2]],
                                           [self.models[0], self.edgeRoads[1], self.models[4], self.edgeRoads[3]],
                                           [[0, 0.6, 0.2, 0.2], [0.6, 0, 0.2, 0.2], [0.2, 0.2, 0, 0.6], [0.2, 0.2, 0.6, 0]]),  # 0

            IntersectionModel.Intersection([self.models[0], self.edgeRoads[6], self.models[3], self.edgeRoads[4]],
                                           [self.models[1], self.edgeRoads[7], self.models[2], self.edgeRoads[5]],
                                           [[0, 0.6, 0.2, 0.2], [0.6, 0, 0.2, 0.2], [0.2, 0.2, 0, 0.6], [0.2, 0.2, 0.6, 0]]),  # 1
            IntersectionModel.Intersection([self.models[4], self.models[11], self.models[7], self.edgeRoads[22]],
                                           [self.models[5], self.models[10], self.models[6], self.edgeRoads[23]],
                                           [[0, 0.6, 0.2, 0.2], [0.6, 0, 0.2, 0.2], [0.2, 0.2, 0, 0.6], [0.2, 0.2, 0.6, 0]]),  # 2
            IntersectionModel.Intersection([self.models[2], self.models[9], self.models[6], self.edgeRoads[8]],
                                           [self.models[3], self.models[8], self.models[7], self.edgeRoads[9]],
                                           [[0, 0.6, 0.2, 0.2], [0.6, 0, 0.2, 0.2], [0.2, 0.2, 0, 0.6], [0.2, 0.2, 0.6, 0]]),  # 3
            IntersectionModel.Intersection([self.models[10], self.models[17], self.models[13], self.edgeRoads[20]],
                                           [self.models[11], self.models[16], self.models[12], self.edgeRoads[21]],
                                           [[0, 0.6, 0.2, 0.2], [0.6, 0, 0.2, 0.2], [0.2, 0.2, 0, 0.6], [0.2, 0.2, 0.6, 0]]),  # 4
            IntersectionModel.Intersection([self.models[8], self.models[15], self.models[12], self.edgeRoads[10]],
                                           [self.models[9], self.models[14], self.models[13], self.edgeRoads[11]],
                                           [[0, 0.6, 0.2, 0.2], [0.6, 0, 0.2, 0.2], [0.2, 0.2, 0, 0.6], [0.2, 0.2, 0.6, 0]]),  # 5
            IntersectionModel.Intersection([self.models[16], self.edgeRoads[16], self.models[19], self.edgeRoads[18]],
                                           [self.models[17], self.edgeRoads[17], self.models[18], self.edgeRoads[19]],
                                           [[0, 0.7, 0, 0.3], [0.7, 0, 0, 0.3], [0.2, 0.2, 0, 0.6], [0.5, 0.5, 0, 0]]),  # 6
            IntersectionModel.Intersection([self.models[14], self.edgeRoads[14], self.models[18], self.edgeRoads[12]],
                                           [self.models[15], self.edgeRoads[15], self.models[19], self.edgeRoads[13]],
                                           [[0, 0.7, 0.3, 0], [0.7, 0, 0.3, 0], [0.5, 0.5, 0, 0], [0.2, 0.2, 0.6, 0]]),  # 7
        ]
        self.probabilities = [
            [0.003, 0.003, 0.003, 0.003, 0.003], #  0
            [0.06, 0.03, 0.029, 0.054, 0.037],  # 1
            [0.008, 0.046, 0.039, 0.023, 0.038],  # 2
            [0.003, 0, 0.007, 0.003, 0.007],  # 3
            [0.005, 0.005, 0.005, 0.005, 0.005],  # 4
            [0.007, 0.007, 0.008, 0.005, 0.005],  # 5
            [0.057, 0.05, 0.05, 0.077, 0.043],  # 6
            [0.037, 0.041, 0.039, 0.025, 0.047],  # 7
            [0.003, 0.017, 0.014, 0.011, 0.013],  # 8
            [0.021, 0.013, 0.009, 0.035, 0.017],  # 9
            [0.07, 0.01, 0.08, 0.07, 0.027],  # 10
            [0.01, 0.01, 0.01, 0.01, 0.01],  # 11
        ]
        self.expectedOutcome = [
            [24, 19, 24, 28, 17],  # 0
            [18, 26, 23, 13, 22],  # 1
            [0, 0, 0, 0, 0],  # 2
            [14, 16, 12, 7, 17],  # 3
            [58, 31, 62, 44, 24],  # 4
            [43, 30, 37, 31, 34],  # 5
            [7, 13, 13, 4, 12],  # 6
            [20, 25, 24, 35, 20],  # 7

        ]

        self.edges = [
            EdgeModel.Edge(self.edgeRoads[1], self.edgeRoads[0], self.probabilities[0][0]),  # 0
            EdgeModel.Edge(self.edgeRoads[3], self.edgeRoads[2], self.probabilities[1][0]),  # 1
            EdgeModel.Edge(self.edgeRoads[5], self.edgeRoads[4], self.probabilities[2][0]),  # 2
            EdgeModel.Edge(self.edgeRoads[7], self.edgeRoads[6], self.probabilities[3][0]),  # 3
            EdgeModel.Edge(self.edgeRoads[9], self.edgeRoads[8], self.probabilities[4][0]),  # 4
            EdgeModel.Edge(self.edgeRoads[11], self.edgeRoads[10], self.probabilities[5][0]),  # 5
            EdgeModel.Edge(self.edgeRoads[13], self.edgeRoads[12], self.probabilities[6][0]),  # 6
            EdgeModel.Edge(self.edgeRoads[15], self.edgeRoads[14], self.probabilities[7][0]),  # 7
            EdgeModel.Edge(self.edgeRoads[17], self.edgeRoads[16], self.probabilities[8][0]),  # 8
            EdgeModel.Edge(self.edgeRoads[19], self.edgeRoads[18], self.probabilities[9][0]),  # 9
            EdgeModel.Edge(self.edgeRoads[21], self.edgeRoads[20], self.probabilities[10][0]),  # 10
            EdgeModel.Edge(self.edgeRoads[23], self.edgeRoads[22], self.probabilities[11][0]),  # 11
        ]

        self.background = plt.imread("background.png")
        self.fig, self.ax = plt.subplots()
        # bindowanie funkcji wywoływanej przy zamknięciu okna (do zamykania plików etc
        self.fig.canvas.mpl_connect('close_event', self.handle_close)
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=200, blit=False, save_count=50)

    # def plotBorders(self):
    #     self.ax.plot([X], [Y], marker='.', markersize=2, linestyle='', color='b')

    # funkcja wywoływana przy zamykaniu okna
    def handle_close(self, evt):
        # print('Closed Figure!')
        self.outFile.close()

    def animate(self,i):
        if self.time % 300 == 0 and self.time > 0:

            print("log file update")
            self.outFile.write(str(self.minutes) + "\n")
            for num, inter in enumerate(self.intersections):

                self.outFile.write(str(num) + ": " + str(inter.counter) + "   " + str(self.expectedOutcome[num][self.minutes])+"\n")
                inter.counter = 0
            self.outFile.write("--------------\n")
            self.minutes = self.minutes + 1
            if self.minutes < 5:
                for edge in range(0,11):
                    (self.edges[edge]).probability = self.probabilities[edge][self.minutes]

        # print("\t\t"+str(self.time))
        if self.showPlot:
            self.ax.cla()
            plt.xlim((-5, 108))
            plt.ylim((-5, 230))
            plt.gca().set_aspect('equal', adjustable='box')
            self.ax.imshow(self.background, extent=[-5, 108, -5, 230])
            plt.axis('off')
        for edge in self.edges:
            edge.removeCarsOutsideGrid()
            edge.generateNewCar()
            #print(edge.counter)

        for inter in self.intersections:
            inter.changeRoad()

        for mdl in self.models + self.edgeRoads:
            mdl.runSim(self.time)

        if self.time % 30 == 0 and self.time > 0:
            for inter in self.intersections:
                inter.toggleLights()

        self.time = self.time + 1

        # self.plotBorders()

        for mdl in self.models:
            for lane in mdl.traffic:
                for car in lane:
                    if car.id == 1:
                        continue
                    if car.posX > mdl.GRIDLEN:
                        continue
                    X=Y=-1
                    if mdl.direction == 1:
                        Y = mdl.ModelY + car.posY
                        X = mdl.ModelX + car.posX
                    elif mdl.direction == 2:
                        Y = mdl.ModelY - car.posY
                        X = mdl.ModelX - car.posX
                    elif mdl.direction == 3:
                        Y = mdl.ModelY + car.posX
                        X = mdl.ModelX - car.posY
                    elif mdl.direction == 4:
                        Y = mdl.ModelY - car.posX
                        X = mdl.ModelX + car.posY
                    if self.showPlot:
                        self.ax.plot([X], [Y], marker='.', markersize=2, linestyle='', color='r')

    def start(self):
        # plt.xlim((0, 230))
        # plt.ylim((-0.5, 230))
        if self.showPlot:
            plt.show()
        else:
            while self.minutes < 5:
                self.animate(1)
            self.outFile.close()


sim = Simulation(False)
sim.start()

