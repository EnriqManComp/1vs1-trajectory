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

    def encode(self, plane_dim, current_player_position, opponent_position, player_dim, current_player):
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
        for i in range(player_dim[0]//2):
            for j in range(player_dim[1]//2):
                first_plane[current_player_position[0] + i, current_player_position[1] + j] = 1
                first_plane[current_player_position[0] - i, current_player_position[1] - j] = 1

                second_plane[opponent_position[0] + i, opponent_position[1] + j] = 1
                second_plane[opponent_position[0] - i, opponent_position[1] - j] = 1

        twenty_first_plane, twenty_second_plane = self.current_player(plane_dim, current_player)

        return np.array(first_plane).astype(bool), np.array(second_plane).astype(bool), twenty_first_plane, twenty_second_plane

    def current_player(self, plane_dim, player:str):
        """
            Return two planes where the first plane has 1s when the current player is the pursuiter
            and the second plane has 1s when the current player is the evader.
            Args:
                plane_dim: tuple, dimensions of the planes
                player: str, name of the current player
        """

        if player == "pursuiter":
            twenty_first_plane = np.ones(plane_dim).astype(bool)
            twenty_second_plane = np.zeros(plane_dim).astype(bool)
        else:
            twenty_first_plane = np.zeros(plane_dim).astype(bool)
            twenty_second_plane = np.ones(plane_dim).astype(bool)

        return twenty_first_plane, twenty_second_plane