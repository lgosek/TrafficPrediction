import RoadModel
import matplotlib.pyplot as plt
import matplotlib.animation as animation

MODELNUM = 2
SPACING = 2

class Simulation:
    def __init__(self):

        self.models = [RoadModel.Model(0,0,150,20,2,5,1), RoadModel.Model(150,3.5,150,20,2,5,2)]

        self.fig, self.ax = plt.subplots()
        self.ani = animation.FuncAnimation(
            self.fig, self.animate,  interval=200, blit=False, save_count=50)

    def animate(self,i):
        self.ax.cla()
        plt.xlim((0, 150))
        plt.ylim((-0.5, 20))

        for mdl in self.models:
            mdl.runSim()

        for mdl in self.models:
            for lane in mdl.traffic:
                for car in lane:
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

