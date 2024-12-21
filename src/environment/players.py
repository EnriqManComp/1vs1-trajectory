import pygame
import numpy as np

#

# Player disk factory class
def create_players(player:str) -> object:

    players = {
        "Pursuiter": Pursuiter,
        "Evasor": Evasor
    }

    return players[player]

class Players:
    def __init__(self):
        self.position = [0,0] # position in the environment
        self.color = (0,0,255) # color of the player
        # Object in pygame
        self.player = None
        # Velocity
        self.v = 1.5

    def spawn(self, surface):
        """
        Spawn the player in the given surface
        
        Input:
            surface: pygame.Surface object
        
        """

        self.player = pygame.draw.circle(surface, self.color, (self.position[0], self.position[1]), 8)
    
    def controls(self, limits:tuple, action:str="NO ACTION"):
        """
        Controls the player movement
        
        Input:
            limits: tuple, (left_limit, top_limit, right_limit, bottom_limit)
            action: str, action to take
        
        """

        if action == 'UP':
            if self.position[1] < limits[1]:
                self.position[1] = limits[1]                       
            else:
                self.position[1] -= self.v
        elif action == "DOWN":
            if self.position[1] > limits[3]:
                self.position[1] = limits[3]
            else:
                self.position[1] += self.v
        elif action == "RIGHT":
            if self.position[0] > limits[2]:
                self.position[0] = limits[2]
            else:
                self.position[0] += self.v
        elif action == "LEFT":
            if self.position[0] < limits[0]:
                self.position[0] = limits[0]
            else:
                self.position[0] -= self.v
        else:
            pass
        
        return
    
    def set_color(self, color:tuple):
        """
        Change the color of the player

        """
        self.color = color

    def set_velocity(self, v:int):
        """
        Change the velocity of the player

        """
        self.v = v

    def set_position(self, position:list):
        self.position = position
        
        
# Evasor class
class Evasor(Players):
    def __init__(self):
        super().__init__()

class Pursuiter(Players):
    def __init__(self):
        super().__init__()

class Lasers():
    def __init__(self):        

        
        self.lasers = []
        
    def remove_lasers(self):
        self.lasers = []
                      
    def draw(self, screen, pos_x, pos_y):  

        # Draw the lasers
        for i in range(0, 360, 2):
            angle = np.radians(i)
            
            x = pos_x + 200 * np.cos(angle)
            y = pos_y + 200 * np.sin(angle)

            #pygame.draw.line(screen, (0, 255, 0), (pos_x, pos_y), (x, y), 1)
            
            laser = ((pos_x,-pos_y),(x,-y), i) # i -> angle in degrees
            
            self.lasers.append(laser) # m, b, x, y