from .player_encoder import PlayerEncoder
from .world_encoder import WorldEncoder
from .hist_encoder import HistEncoder

class EncodeState:
    def __init__(self):
        self.world_encoder = WorldEncoder()
        self.player_encoder = PlayerEncoder()
        self.hist_encoder = HistEncoder()
        

    def encode(self, plane_dim, state, current_player):
        """
            Encode the game state into numeric data.
            Args:
                state: dict, game state (position of the players, list of obstacles)
        """
        print(state)
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
        
        sixth_plane = self.hist_encoder.encode(
                                               current_player_plane=first_plane,
                                               opponent_plane=second_plane,
                                               current_player=current_player
                                               )

        return first_plane, second_plane, third_plane, fourth_plane, twenty_first_plane