from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

class Newtonian_Gravity():
    '''Simulation of newtonian gravity in 3 dimensions'''
    @staticmethod
    def create_initial_conditions():
        '''Create parameters for particles'''
        #particle positions and velocities (ith index is ith particle)
        x,y,z = [0,0,0],[0,10,1],[0,0,0]
        vx,vy,vz = [0,0,0],[0,0,0],[0,0,0]
        return [[x,y,z],[vx,vy,vz]]
        
    def __init__(self, pos, vel):
        '''Create plot for simulation'''
        #creates and shows the plot
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.fig.show()

        #store positions and velocities (x,y,z in ith index is to ith particle)
        self.part_pos = np.array(pos).T
        self.part_vel = np.array(vel).T

        self.initial_draw()
        return

    def initial_draw(self):
        '''Draw data onto plot from the initial conditions'''
        self.ax.scatter(*self.part_pos.T)
        return

    def start_simulation(self):
        '''Start animation'''
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=50)
        return

    def update(self, num):
        '''Animated function'''
        self.first_order()
        self.redraw()
        return

    def first_order(self):
        '''Calculate new parameters for particles with 1st order accuracy'''
        #calculate new positions via r = r_0 + v*dt
        #calculate force on ith particle due to j particles
            #don't forget the small parameter to avoid dividing by 0
        #obtain acceleration from a = F/m
        #calculate new velocities via v = v_0 + a_dt
        return

    def second_order(self):
        '''Calculate new parameters for particles with 2nd order accuracy'''
        return
    
    def third_order(self):
        '''Calculate new parameters for particles with 3rd order accuracy'''
        return
    
    def fourth_order(self):
        '''Calculate new parameters for particles with 4th order accuracy'''
        return
    
    def redraw(self):
        '''Redraw plot with new particle parameters'''
        self.ax.clear()
        self.ax.scatter(*self.part_pos.T)
        return



def main():
    '''Main function'''
    init_conditions = Newtonian_Gravity.create_initial_conditions()
    sim = Newtonian_Gravity(*init_conditions)
    sim.start_simulation()
    return

if __name__ == "__main__":
    main()
