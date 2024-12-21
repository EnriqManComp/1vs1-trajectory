import pygame

class Limits:

    def __init__(self, main_screen):

        """
        Limits of the world environment
        
        """
        self.screen = main_screen
        # Attributes
        self.wall_color = (255,200,0) # Yellow

        self.obstacles = []
        self.obstacles.append([[5,-5],[195,-5], "up"]) # p1, p2, name
        self.obstacles.append([[5,-195],[195,-195], "down"]) 
        self.obstacles.append([[5,-5],[5,-195], "left"])
        self.obstacles.append([[195,-5],[195,-195], "right"])

        # Walls
        self.left_wall = None
        self.top_wall = None
        self.right_wall = None
        self.bottom_wall = None

        # PyGame Rectangle Object
        self.left_wall_obj = (0, 0, 10, self.screen.get_height())
        self.top_wall_obj = (0, 0, self.screen.get_width(), 10)
        self.right_wall_obj = (self.screen.get_width() - 10, 0, 10, self.screen.get_height())
        self.bottom_wall_obj = (0, self.screen.get_height() - 10, self.screen.get_width(), 10)

    def render_walls(self):
        """
        
        Update the limit walls for render purpose
                
        """

        self.left_wall = pygame.draw.rect(self.screen, self.wall_color, self.left_wall_obj)
        
        self.top_wall = pygame.draw.rect(self.screen, self.wall_color, self.top_wall_obj)
        
        self.right_wall = pygame.draw.rect(self.screen, self.wall_color, self.right_wall_obj)
        
        self.bottom_wall = pygame.draw.rect(self.screen, self.wall_color, self.bottom_wall_obj)
    
