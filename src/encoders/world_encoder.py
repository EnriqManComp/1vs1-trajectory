import numpy as np
from encoders.base import Encoder
import matplotlib.pyplot as plt

class WorldEncoder(Encoder):
    def __init__(self):
        pass        

    def encode(self, plane_dim, first_plane, second_plane, obstacles):
        """
            Encode the game state into numeric data.
            Args:
                plane_dim: tuple, dimensions of the plane
                first_plane: numpy array, first plane with current player position
                second_plane: numpy array, second plane with opponent position
        """
        # Obstacles positions
        third_plane = np.zeros(plane_dim)
        # Add the obstacles to the third plane
        third_plane = self.obstacles(third_plane, obstacles=obstacles)
        
        """
        matrix_255 = third_plane * 255

        # Visualize with Matplotlib
        plt.imshow(matrix_255)
        plt.colorbar(label='Pixel Intensity')
        plt.title('Boolean Matrix Visualization')
        plt.show()
        
        """
        first_plane = first_plane.astype(bool)
        second_plane = second_plane.astype(bool)
        third_plane = third_plane.astype(bool)
        
        # Empty spaces
        fourth_plane = np.zeros(plane_dim)
        # Add the first and second planes
        fourth_plane = np.logical_or(first_plane, second_plane)
        # Add the third plane
        fourth_plane = np.logical_or(fourth_plane, third_plane)
        
        # Inverse the values to get the empty spaces
        fourth_plane = np.logical_not(fourth_plane)
    
        """
        matrix_255 = fourth_plane * 255

        # Visualize with Matplotlib
        plt.imshow(matrix_255)
        plt.colorbar(label='Pixel Intensity')
        plt.title('Boolean Matrix Visualization')
        plt.show()
        
        """

        return third_plane, fourth_plane
    
    def name(self):
        return "WorldEncoder"
    
    def obstacles(self, plane, obstacles):
        """
            Return a binary plane where 1s represent obstacles in a world.
            Args:
                plane: numpy array, empty plane of given dimensions 
                obstacles: list of tuples, (left, top, width, height)
        """
        print(obstacles)
        for obstacle in obstacles:
            left, top, width, height = obstacle
            plane[left:left+width, top:top+height] = 1

        return plane