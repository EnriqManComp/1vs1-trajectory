import pygame
from .obstacles import Limits

class Simple:
    def __init__(self):
        # Initialize game
        pygame.init()
        # Set main screen
        self.screen = pygame.display.set_mode((200,200))
        # FPS controller
        self.clock = pygame.time.Clock()

        ## Obstacles
        self.obstacles = Limits(self.screen)
    
    def render_objects(self):
        self.screen.fill((138,138,138))
        self.obstacles.render_walls()

    def update(self):
        pygame.display.update()

    def end_env(self):
        pygame.quit()
        