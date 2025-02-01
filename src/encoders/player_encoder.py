"""
    Player encoder module
    First plane: 1s where current player is
    Second plane: 1s where opponent is
    
"""
from encoders.base import Encoder
import numpy as np

class PlayerEncoder(Encoder):
    def name(self, player:str):
        return player

    def encode(self, plane_dim, restrictions, current_player_position, opponent_position, player_dim, current_player):
        """
            Encode the game state into numeric data.
            Args:
                plane_dim: tuple, dimensions of the plane
                current_player_position: tuple, center coordinate of the current player
                opponent_position: tuple, center coordinate of the opponent
                player_dim: tuple, dimensions of the players
                current_player: str, name of the current player
        """
        # First plane
        first_plane = np.zeros(plane_dim)
        # Central position of the current player
        first_plane[current_player_position[0], current_player_position[1]] = 1
        # Second plane
        second_plane = np.zeros(plane_dim)
        # Central position of the opponent
        second_plane[opponent_position[0], opponent_position[1]] = 1
        # Surrounding positions of the players
        for i in range(current_player_position[0] - player_dim[0], current_player_position[0] + player_dim[0]):
            for j in range(current_player_position[1] - player_dim[1], current_player_position[1] + player_dim[1]):
                if (i > restrictions[2]) or (j > restrictions[3]) or (i < restrictions[0]) or (j < restrictions[1]):
                    continue
                first_plane[i, j] = 1
        
        for i in range(opponent_position[0] - player_dim[0], opponent_position[0] + player_dim[0]):
            for j in range(opponent_position[1] - player_dim[1], opponent_position[1] + player_dim[1]):
                if (i > restrictions[2]) or (j > restrictions[3]) or (i < restrictions[0]) or (j < restrictions[1]):
                    continue
                second_plane[i, j] = 1

        twenty_first_plane = self.current_player_plane(plane_dim, current_player)

        return np.array(first_plane).astype(bool), np.array(second_plane).astype(bool), twenty_first_plane

    def current_player_plane(self, plane_dim, current_player:str):
        """
            Return two planes where the first plane has 1s when the current player is the pursuiter
            and the second plane has 1s when the current player is the evader.
            Args:
                plane_dim: tuple, dimensions of the planes
                player: str, name of the current player
        """

        if current_player == "pursuiter":
            twenty_first_plane = np.ones(plane_dim)
        else:
            twenty_first_plane = np.zeros(plane_dim)

        return twenty_first_plane