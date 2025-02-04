"""

This encoder track the eighth last movement of the current player

"""

from encoders.base import Encoder

class HistEncoder(Encoder):

    def __init__(self):
        self.pursuiter_hist = []
        self.evasor_hist = []

    def name(self):
        return "eighth_last_movement"
    
    def encode(self, current_player_plane, opponent_plane, current_player):
        """
            Encode the game state into numeric data.
            Args:
                current_player_plane: np.array, plane of the current player
                opponent_plane: np.array, plane of the opponent
                current_player: str, name of the current player
        """
        
        if current_player == "pursuiter":
            self.add_plane(current_player_plane, opponent_plane)
            return self.pursuiter_hist
        else:
            self.add_plane(opponent_plane, current_player_plane)
            return self.evasor_hist

    def add_plane(self, pursuiter_plane, evasor_plane):
        """
            Add the last movement of the pursuiter and evasor to the stack
        """
        if len(self.pursuiter_hist) == 0:
            for i in range(8):
                self.pursuiter_hist.append(pursuiter_plane)
                self.evasor_hist.append(evasor_plane)
            return
        
        self.pursuiter_hist.append(pursuiter_plane)
        self.evasor_hist.append(evasor_plane)

        if len(self.pursuiter_hist) > 8:
            self.pursuiter_hist.pop(0)
            self.evasor_hist.pop(0)

        