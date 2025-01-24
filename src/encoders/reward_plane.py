from encoders.base import Encoder
import numpy as np
import matplotlib.pyplot as plt

class RewardPlane(Encoder):
    
    def __init__(self):
        self.reward_plane = []

    def name(self):
        return "reward_plane"
    
    def encode(self, plane_dim, current_player, empty_plane, zones):
        
        self.reward_plane = np.zeros(plane_dim)

        if current_player == "pursuiter":
            self.pursuiter_reward(plane_dim=plane_dim, zones=zones)
            # Remove no valid zones
            self.reward_plane = np.logical_and(self.reward_plane, empty_plane)

            return self.reward_plane
        else:
            self.evasor_reward(zones=zones)
            # Remove no valid zones
            self.reward_plane = np.logical_and(self.reward_plane, empty_plane)
            return self.reward_plane
    
    def pursuiter_reward(self, plane_dim, zones):
        """
            Encode the reward plane for the pursuiter
        """

        # Create the target zone and the danger zone with the same dimensions as the plane
        target_point_0 = (zones["target_zone"][0], zones["target_zone"][1])
        target_point_1 = (target_point_0[0] + zones["target_zone"][2], target_point_0[1] + zones["target_zone"][3]) 

        target_zone = np.zeros(plane_dim)
        target_zone[target_point_0[0]:target_point_1[0], target_point_0[1]:target_point_1[1]] = 1

        danger_point_0 = (zones["danger_zone"][0], zones["danger_zone"][1])
        danger_point_1 = (danger_point_0[0] + zones["danger_zone"][2], danger_point_0[1] + zones["danger_zone"][3])

        danger_zone = np.zeros(plane_dim)
        danger_zone[danger_point_0[0]:danger_point_1[0], danger_point_0[1]:danger_point_1[1]] = 1
        
        self.reward_plane = np.logical_or(self.reward_plane, target_zone)
        self.reward_plane = np.logical_xor(self.reward_plane, danger_zone)

        """
        matrix_255 = self.reward_plane * 255

        # Visualize with Matplotlib
        plt.imshow(matrix_255)
        plt.colorbar(label='Pixel Intensity')
        plt.title('Boolean Matrix Visualization')
        plt.show()
        """

    def evasor_reward(self, zones):
        """
            Encode the reward plane for the evasor
        """

        x_p = zones["pursuiter_center"][0]
        y_p = zones["pursuiter_center"][1]
        x_e = zones["evasor_center"][0]
        y_e = zones["evasor_center"][1]

        # Pursuiter in the first quadrant
        if x_p < x_e and y_p < y_e:
            self.reward_plane[int(x_e):(int(x_e)+10), int(y_e)-10:(int(y_e)+10)] = 1
            self.reward_plane[int(x_e)-10:int(x_e), int(y_e):(int(y_e)+10)] = 1
        # Pursuiter in the second quadrant
        elif x_p > x_e and y_p < y_e:
            self.reward_plane[int(x_e)-10:(int(x_e)), int(y_e)-10:(int(y_e)+10)] = 1
            self.reward_plane[int(x_e):(int(x_e)+10), int(y_e):(int(y_e)+10)] = 1
        # Pursuiter in the third quadrant
        elif x_p > x_e and y_p > y_e:
            self.reward_plane[int(x_e)-10:(int(x_e)+10), int(y_e)-10:(int(y_e))] = 1
            self.reward_plane[int(x_e)-10:(int(x_e)), int(y_e):(int(y_e)+10)] = 1
        # Pursuiter in the fourth quadrant
        elif x_p < x_e and y_p > y_e:
            self.reward_plane[int(x_e)-10:(int(x_e)+10), int(y_e)-10:(int(y_e))] = 1
            self.reward_plane[int(x_e):int(x_e)+10, int(y_e):(int(y_e)+10)] = 1
        # Pursuiter in the same x-axis
        elif x_p == x_e and y_p < y_e:
            self.reward_plane[int(x_e)-10:(int(x_e)+10), int(y_e):(int(y_e)+10)] = 1
        elif x_p == x_e and y_p > y_e:
            self.reward_plane[int(x_e)-10:(int(x_e)+10), int(y_e)-10:(int(y_e))] = 1
        # Pursuiter in the same y-axis
        elif y_p == y_e and x_p < x_e:
            self.reward_plane[int(x_e):(int(x_e)+10), int(y_e)-10:(int(y_e)+10)] = 1
        elif y_p == y_e and x_p > x_e:
            self.reward_plane[int(x_e)-10:(int(x_e)), int(y_e)-10:(int(y_e)+10)] = 1
        
        """
        matrix_255 = self.reward_plane * 255

        # Visualize with Matplotlib
        plt.imshow(matrix_255)
        plt.colorbar(label='Pixel Intensity')
        plt.title('Boolean Matrix Visualization')
        plt.show()
        """

def midpoint(x1, y1, x2, y2):
  
    """Calculates the center point between two points.

        Args:
        x1: The x-coordinate of the first point.
        y1: The y-coordinate of the first point.
        x2: The x-coordinate of the second point.
        y2: The y-coordinate of the second point.

        Returns:
        A tuple containing the x and y coordinates of the center point.
    """
    x_mid = (x1 + x2) / 2
    y_mid = (y1 + y2) / 2
    return x_mid, y_mid

        