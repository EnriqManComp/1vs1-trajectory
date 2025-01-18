from encoders.base import Encoder
import numpy as np
import matplotlib.pyplot as plt

class RewardPlane(Encoder):
    
    def __init__(self):
        self.reward_plane = []

    def name(self):
        return "reward_plane"
    
    def encode(self, plane_dim, current_player, zones):
        
        self.reward_plane = np.zeros(plane_dim)

        if current_player == "pursuiter":
            self.pursuiter_reward(plane_dim=plane_dim, zones=zones)
            return self.reward_plane
        else:
            self.evasor_reward(plane_dim=plane_dim, zones=zones)
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

        matrix_255 = self.reward_plane * 255

        # Visualize with Matplotlib
        plt.imshow(matrix_255)
        plt.colorbar(label='Pixel Intensity')
        plt.title('Boolean Matrix Visualization')
        plt.show()


        