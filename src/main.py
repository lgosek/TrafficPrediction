import RoadModel
import matplotlib.pyplot as plt
import matplotlib.animation as animation

MODELNUM = 2

class Simulation:
    def __init__(self):

        self.models = [RoadModel.Model((i+1)*20,(i+1)*15,150,20,2,5) for i in range(MODELNUM)]

        self.fig, self.ax = plt.subplots()
        self.ani = animation.FuncAnimation(
            self.fig, self.animate,  interval=300, blit=False, save_count=50)

    def animate(self,i):
        self.ax.cla()
        plt.xlim((0, 230))
        plt.ylim((-0.5, 50))

        for mdl in self.models:
            mdl.runSim()

        for mdl in self.models:
            for lane in mdl.traffic:
                for car in lane:
                    self.ax.plot([mdl.ModelX + car.posX], [mdl.ModelY + car.posY], marker='.', markersize=2, linestyle='', color='b')


    def start(self):
        plt.xlim((0, 230))
        plt.ylim((-0.5, 50))
        plt.show()



sim = Simulation()
sim.start()

