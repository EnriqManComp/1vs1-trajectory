

class Encoder:
    def name(self):
        """
            Support logging or saving the name of
            the encoder your model is using.
        """
        raise NotImplementedError()
    
    def encode(self, game_state):
        """
            Encode the game state into numeric data.
        """
        raise NotImplementedError()
    
    
    