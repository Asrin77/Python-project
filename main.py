import pygame
import random

size = 40
height = 40
width = 40

HS_FILE = "highscore.txt"

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen

        try:
            self.apple_image = pygame.image.load("game-images/apple.png").convert_alpha()
        except FileNotFoundError:
            print("Error: apple.png not found")
            pygame.quit()
            exit()
        
        self.x = 120
        self.y = 120

        def display_image(self):
            self.parent_screen.blit(self.apple_image, (self.x, self.y))

        def move(self):
            self.x = random.randint(1,24) * size
            self.y = random.randint(1,19) * size
            
