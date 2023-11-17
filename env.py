import math
import pygame
class buldingEnvironment:
    def __init__(self, MapDimension):
        pygame.init()
        self.pointCloud = []
        self.externalMap = pygame.image.load('map.png')
        self.maph, self.mapw = MapDimension
        self.MapWindowName = 'RRT path planning'
        self.map = pygame.display.set_mode((self.mapw,self.maph))
        self.map.blit(self.externalMap,(0,0))
        #Colors
        self.black = (0, 0, 0)
        self.grey = (70, 70 ,70)
        self.Blue = (0,0, 255)
        self.Green = (0, 255, 0)
        self.Reed = (255, 0, 0)
        self.White = (255, 255, 255)