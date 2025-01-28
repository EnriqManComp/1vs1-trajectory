from .player_encoder import PlayerEncoder
from .world_encoder import WorldEncoder
from .hist_encoder import HistEncoder
from .reward_plane import RewardPlane
from .distance_plane import DistancePlane
from .utils import viz

class EncodeState:
    def __init__(self):
        self.world_encoder = WorldEncoder()
        self.player_encoder = PlayerEncoder()
        self.hist_encoder = HistEncoder()
        self.reward_plane = RewardPlane()
        self.distance_plane = DistancePlane()
        

    def encode(self, plane_dim, state, current_player, zones, visualize:bool=False):
        """
            Encode the game state into numeric data.
            Args:
                plane_dim: tuple, dimensions of the plane
                state: dict, game state (position of the players, list of obstacles)
                current_player: str, current player ("pursuiter" or "evasor")
                target_zone: pygame.Rect, target zone
                zones: dict, zones of interest (target zone, danger zone, etc.)
                visualize: bool, flag to indicate if the planes should be visualized
        """
        
        # Encode the player
        if current_player == "pursuiter":            
            current_player_position = state['players'][0]
            opponent_position = state['players'][1]
        else:
            current_player_position = state['players'][1]
            opponent_position = state['players'][0]

        first_plane, second_plane, twenty_first_plane = self.player_encoder.encode(plane_dim=plane_dim,
                                                                                                        current_player_position=current_player_position,
                                                                                                        opponent_position=opponent_position,
                                                                                                        player_dim=(8,8),
                                                                                                        current_player=current_player)
        # Encode the world
        third_plane, fourth_plane = self.world_encoder.encode(plane_dim=plane_dim,
                                                               first_plane=first_plane,
                                                               second_plane=second_plane,
                                                               obstacles=state['obstacles'])
        
        sixth_to_fourteen_plane = self.hist_encoder.encode(
                                               current_player_plane=first_plane,
                                               opponent_plane=second_plane,
                                               current_player=current_player
                                               )

        # Encode the reward plane
        reward_plane = self.reward_plane.encode(plane_dim=plane_dim,
                                                 current_player=current_player,
                                                 empty_plane=fourth_plane,
                                                 zones=zones)

        # Encode distance around the players
        distance_plane = self.distance_plane.encode(plane_dim=plane_dim,
                                                     current_player=current_player,
                                                     player_plane=first_plane,
                                                     empty_plane=fourth_plane,
                                                     player_position=current_player_position,
                                                     player_dim=(8,8))
        if visualize:
            viz(first_plane)
            viz(second_plane)
            viz(third_plane)
            viz(fourth_plane)
            viz(sixth_to_fourteen_plane)
            viz(reward_plane)
            viz(distance_plane)
            viz(twenty_first_plane)

        return first_plane, second_plane, third_plane, \
            fourth_plane, sixth_to_fourteen_plane, reward_plane, \
            distance_plane, twenty_first_plane