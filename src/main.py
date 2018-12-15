import RoadModel
import matplotlib.pyplot as plt
import matplotlib.animation as animation

MODELNUM = 2
SPACING = 2

class Simulation:
    def __init__(self):
        self.time = 0
        self.models = [
            RoadModel.Model(X=5, Y=0, gridLen=92, carNum=10, lanes=1, maxVel=5, direction=1),   #0
            RoadModel.Model(X=97, Y=2, gridLen=92, carNum=10, lanes=1, maxVel=5, direction=2),  #1

            RoadModel.Model(X=102, Y=3, gridLen=52, carNum=5, lanes=2, maxVel=5, direction=3), #2
            RoadModel.Model(X=98, Y=55, gridLen=52, carNum=5, lanes=2, maxVel=5, direction=4), #3

            RoadModel.Model(X=4, Y=3, gridLen=52, carNum=5, lanes=2, maxVel=5, direction=3),   #4
            RoadModel.Model(X=0, Y=55, gridLen=52, carNum=5, lanes=2, maxVel=5, direction=4),  #5

            RoadModel.Model(X=5, Y=56, gridLen=92, carNum=10, lanes=1, maxVel=5, direction=1),  #6
            RoadModel.Model(X=97, Y=58, gridLen=92, carNum=10, lanes=1, maxVel=5, direction=2), #7

            RoadModel.Model(X=102, Y=59, gridLen=108, carNum=10, lanes=2, maxVel=5, direction=3), #8
            RoadModel.Model(X=98, Y=167, gridLen=108, carNum=10, lanes=2, maxVel=5, direction=4), #9

            RoadModel.Model(X=4, Y=59, gridLen=108, carNum=10, lanes=2, maxVel=5, direction=3),   #10
            RoadModel.Model(X=0, Y=167, gridLen=108, carNum=10, lanes=2, maxVel=5, direction=4),  #11

            RoadModel.Model(X=5, Y=168, gridLen=92, carNum=10, lanes=1, maxVel=5, direction=1),  # 12
            RoadModel.Model(X=97, Y=170, gridLen=92, carNum=10, lanes=1, maxVel=5, direction=2), # 13

            RoadModel.Model(X=102, Y=171, gridLen=52, carNum=5, lanes=2, maxVel=5, direction=3),  # 14
            RoadModel.Model(X=98, Y=223, gridLen=52, carNum=5, lanes=2, maxVel=5, direction=4),  # 15

            RoadModel.Model(X=4, Y=171, gridLen=52, carNum=5, lanes=2, maxVel=5, direction=3),    # 16
            RoadModel.Model(X=0, Y=223, gridLen=52, carNum=5, lanes=2, maxVel=5, direction=4),   # 17

            RoadModel.Model(X=5, Y=224, gridLen=92, carNum=10, lanes=1, maxVel=5, direction=1),  # 12
            RoadModel.Model(X=97, Y=226, gridLen=92, carNum=10, lanes=1, maxVel=5, direction=2)  # 13

        ]

        self.fig, self.ax = plt.subplots()
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=200, blit=False, save_count=50)

    # def plotBorders(self):
    #     self.ax.plot([X], [Y], marker='.', markersize=2, linestyle='', color='b')


    def animate(self,i):
        # print("\t\t"+str(self.time))
        self.ax.cla()
        plt.xlim((-5, 102))
        plt.ylim((-5, 230))

        for mdl in self.models:
            mdl.runSim(self.time)

        self.time = self.time + 1

        # self.plotBorders()

        for mdl in self.models:
            for lane in mdl.traffic:
                for car in lane:
                    if car.id == 1:
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
                    self.ax.plot([X], [Y], marker='.', markersize=2, linestyle='', color='b')


    def start(self):
        # plt.xlim((0, 230))
        # plt.ylim((-0.5, 230))
        plt.show()



sim = Simulation()
sim.start()

