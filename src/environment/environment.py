import pygame
import numpy as np
import copy

from .players import create_players, Lasers
from .helpers import plot_area, get_laser_measurements
from functionalities.trajectories import line

class Simulator:

    def __init__(self):
        self.backward = False
    
    def collect_data_from_traj(self, env, trajectory, p_trajectory, p_pos, e_pos, time, backward_option:bool = False, plot_lasers:bool = False):
        """
        Collect data from a trajectory
        Inputs:
            env: New world
            trajectory: Trajectory of the evasor
            p_trajectory: Trajectory of the pursuiter
            p_pos: Initial position of the pursuiter
            e_pos: Initial position of the evasor
            time: Time for the simulation
            backward_option: Flag to indicate if the trajectory is going backward or not
            plot_lasers: Flag to indicate if the lasers are going to be plotted or not
        """
               
        # Clock
        clock = pygame.time.Clock()

        # Create Pursuiter
        pursuiter = create_players("Pursuiter")()
        pursuiter.set_position(p_pos) # Set initial position
        
        # Lasers
        lasers = Lasers()

        # Create Evasor
        evasor = create_players("Evasor")()
        evasor.set_position(e_pos) # Set initial position
        evasor.set_color(color=(255,0,0)) # Set evasor color
        evasor.set_velocity(v=1.0) # Set evasor velocity

        # Wall limits (Restrictions for the players)
        wall_limits = (18,18,188,188)
        
        done = False # Done flag for the simulation (True when the simulation ends)
        t = 0 # Time counter
        traj_done = False # Trajectory done flag
        
        pygame.event.clear() # Clear events
        # Main loop
        while not done:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # If the user clicks the close button, the simulation ends
                    done = True

            ####### Drawing Zone ##########

            # Render the world objects (obstacles, background)
            env.render_objects()
            # Plot the target zone around the evasor 
            plot_area(surface=env.screen, color=(0, 255, 0), pos=evasor.position, r=40)
            # Plot the danger zone around the evasor
            plot_area(surface=env.screen, color=(108,59,170), pos=evasor.position, r=25)

            if plot_lasers:
                # Laser draw
                lasers.remove_lasers()
                lasers.draw(env.screen, pursuiter.position[0], pursuiter.position[1])   
            
            # Draw the trajectory
            evasor.position, pursuiter.position, t, traj_done = self.draw_trajectory(trajectory, p_trajectory, t, backward_option, cycles=1)
            
            evasor.spawn(surface=env.screen)
            pursuiter.spawn(surface=env.screen)

            ####### Ending Drawing Zone ########

            # Get laser measures
            #laser_measures = get_laser_measurements(evasor_pos=evasor.position.copy(), lasers=lasers.lasers, obstacles=env.obstacles.obstacles)       
            
            # Update screen
            env.update()
            clock.tick(60)

            time -= 1

            if time == 0 or traj_done:
                done = True
        
        return
    
    def draw_trajectory(self, trajectory, p_trajectory, t, backward_option, cycles:int=1):
        """
        Update the position of the player to follow a trajectory
        Inputs:
            trajectory: Trajectory of the evasor
            p_trajectory: Trajectory of the pursuiter
            t: Time counter
            backward_option: Flag to indicate if the trajectory is going backward or not
            cycles: Number of cycles for the trajectory (with backward option equal to True)
        """
        if backward_option:
            if (t < len(trajectory)) and (not self.backward):  
                t += 1
                return trajectory[t], p_trajectory[t], t, False                     
            else:                
                self.backward = True               
                t -=1
                e_position = trajectory[t]
                p_position = p_trajectory[t]                 
                if t == 0:
                    self.backward = False
                    cycles -= 1
                    if cycles == 0:
                        return e_position, p_position, t, True
                
                return e_position, p_position, t, False
        else:
            if t < (len(trajectory)-1):
                t += 1 
                return trajectory[t], p_trajectory[t], t, False
            else:
                return trajectory[-1], p_trajectory[-1], t, True

