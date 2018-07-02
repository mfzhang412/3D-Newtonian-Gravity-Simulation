#this branch will be used to fix the overflow bug in first_order

from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import math

class Newtonian_Gravity():
    '''Simulation of newtonian gravity in 3 dimensions'''
    #Gravitational constant
    G = 1
    #Mass of each particle
    m = 1
    #Euler timestep
    dt = .01
    
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

    @staticmethod
    def unit_vec(r1,r2):
        '''Return a unit vector in the r2-r1 direction'''
        r = r2-r1
        magn = np.dot(r,r)
        return r/math.sqrt(magn)

    @staticmethod
    def inverse_square(r1,r2):
        '''Return 1/r^2 where r=r2-r1'''
        r = r2-r1
        magn = np.dot(r,r)
        return 1/magn
    
    @staticmethod
    def weighted_vec(r1,r2):
        '''Return the vector 1/r^2 in the r direction where r=r2-r1'''
        r = Newtonian_Gravity.inverse_square(r1,r2)*Newtonian_Gravity.unit_vec(r1,r2)
        return r
    
    def first_order(self):
        '''Calculate new parameters for particles with 1st order accuracy'''
        G = Newtonian_Gravity.G
        m = Newtonian_Gravity.m
        dt = Newtonian_Gravity.dt
        
        #calculate new positions via r = r_0 + v*dt
        for i in range(len(self.part_pos)):
            self.part_pos[i] = self.part_pos[i] + self.part_vel[i]*dt
            
        #calculate force on ith particle due to j particles
            #don't forget the small parameter to avoid dividing by 0
        force = np.array([[0,0,0]]*len(self.part_pos))
        for i in range(len(self.part_pos)):
            for j in range(len(self.part_pos)):
                if (i != j):
                    #if force is instead repelling, change + to -
                    force[i] = force[i] + G*m*m*Newtonian_Gravity.weighted_vec(
                        self.part_pos[i],self.part_pos[j]
                        )
                    
        #calculate new velocities via v = v_0 + F/m*dt
        for i in range(len(self.part_pos)):
            self.part_vel[i] = self.part_vel[i] + force[i]/m*dt
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
