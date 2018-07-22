from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import math
import random

class Newtonian_Gravity():
    '''Simulation of newtonian gravity in 3 dimensions'''
    #Gravitational constant
    G = 100
    #Mass of each particle
    m = 1
    #Euler timestep
    dt = .01
    
    @staticmethod
    def create_initial_conditions():
        '''Create parameters for particles'''
        #number of particles in the simulation
        numPart = 100
        
        #top and bottom bound for random distribution of positions and velocities
        botBound = -10
        topBound = 10
        
        #particle positions and velocities (ith index is ith particle)
        x,y,z = [0.0]*numPart,[0.0]*numPart,[0.0]*numPart
        vx,vy,vz = [0.0]*numPart,[0.0]*numPart,[0.0]*numPart
        
        #set limits of graph axis
        xlim,ylim,zlim = [botBound-5,topBound+5],[botBound-5,topBound+5],[botBound-5,topBound+5]

        #create random positions and velocities for particles
        for i in range(numPart):
            x[i] = random.uniform(botBound,topBound)
            y[i] = random.uniform(botBound,topBound)
            z[i] = random.uniform(botBound,topBound)
            vx[i] = random.uniform(botBound,topBound)
            vx[i] = random.uniform(botBound,topBound)
            vx[i] = random.uniform(botBound,topBound)
        return [[x,y,z],[vx,vy,vz],[xlim,ylim,zlim]]
        
    def __init__(self, pos, vel, lim):
        '''Create plot for simulation'''
        #sets the axis range
        self.xlim = lim[0]
        self.ylim = lim[1]
        self.zlim = lim[2]
        
        #creates and shows the plot
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.setPlotParams()
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
        #frame update interval in milliseconds
        upd = 1
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=upd)
        return

    def redraw(self):
        '''Redraw plot with new particle parameters'''
        self.ax.clear()
        self.setPlotParams()
        self.ax.scatter(*self.part_pos.T)
        return

    def setPlotParams(self):
        '''Set the title, range, and labels of the axis'''
        #set plot title
        plt.title('3D Newtonian Gravity Simulation')

        #set axis range
        self.ax.set_xlim(self.xlim)
        self.ax.set_ylim(self.ylim)
        self.ax.set_zlim(self.zlim)

        #set axis labels
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_zlabel('z')

    def update(self, num):
        '''Animated function'''
        self.first_order()
        self.redraw()
        return

    @staticmethod
    def unit_vec(r1,r2):
        '''Return a unit vector in the r2-r1 direction'''
        r = r2-r1
        vec = r/np.linalg.norm(r)
        return vec

    @staticmethod
    def inverse_square(r1,r2):
        '''Return 1/r^2 where r=r2-r1'''
        r = r2-r1
        magn = np.dot(r,r)
        val = 1/magn
        return val
    
    @staticmethod
    def weighted_vec(r1,r2):
        '''Return the vector 1/r^2 in the r direction where r=r2-r1'''
        #a small value parameter is needed to avoid divide by zero errors
            #and avoid slingshot effects when particles are too close to eachother
        small_val_param = 1
        r = r2-r1
        vec = r/((np.linalg.norm(r))**3 + small_val_param)
        return vec
    
    def first_order(self):
        '''Calculate new parameters for particles with 1st order accuracy'''
        G = Newtonian_Gravity.G
        m = Newtonian_Gravity.m
        dt = Newtonian_Gravity.dt
        #calculate new positions via r = r_0 + v*dt
        for i in range(len(self.part_pos)):
            self.part_pos[i] = self.part_pos[i] + self.part_vel[i]*dt
            
        #calculate force on ith particle due to j particles
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



def main():
    '''Main function'''
    init_conditions = Newtonian_Gravity.create_initial_conditions()
    sim = Newtonian_Gravity(*init_conditions)
    sim.start_simulation()
    return

if __name__ == "__main__":
    main()
