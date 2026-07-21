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
