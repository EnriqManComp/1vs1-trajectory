from encoders.base import Encoder
import numpy as np
import matplotlib.pyplot as plt

class DistancePlane(Encoder):
    def __init__(self):
        self.distance_plane = []

    def name(self):
        return "distance_plane"
    
    def encode(self, plane_dim, current_player, player_plane, empty_plane, player_position, player_dim):
        """
            Encode the distance plane for the current player
            Args:
                plane_dim: tuple, dimensions of the plane
                current_player: str, current player ("pursuiter" or "evasor")
                empty_plane: np.array, empty plane
                player_position: tuple, position of the player
                player_dim: tuple, dimensions of the player
                
        """
        self.distance_plane = np.zeros(plane_dim)

        if current_player == "pursuiter":
            self.distance(player_plane=player_plane, player_position=player_position, player_dim=player_dim)
            # Adding the obstruction
            self.distance_plane = np.logical_and(self.distance_plane, empty_plane)

            return self.distance_plane
        else:
            self.distance(player_plane=player_plane, player_position=player_position, player_dim=player_dim)
            # Adding the obstruction
            self.distance_plane = np.logical_and(self.distance_plane, empty_plane)

            
            return self.distance_plane
        
    def distance(self, player_plane, player_position, player_dim):

        # Get the player position
        player_x, player_y = player_position
        player_width, player_height = player_dim

        self.distance_plane[player_x-player_width-8:player_x+player_width+8, player_y-player_height-8:player_y+player_height+8] = 1

        self.distance_plane = np.logical_and(self.distance_plane, np.logical_not(player_plane))

        
