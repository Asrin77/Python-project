import pygame
from pygame.locals import *
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
        self.x = random.randint(1,14) * size
        self.y = random.randint(1,14) * size

class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        try:
            self.snake_image = pygame.image.load("game-images/yellow_snake.png").convert_alpha()
        except FileNotFoundError:
            print("Error: yellow_snake.png not found")
            pygame.quit()
            exit()

        self.direction = "down" 
        self.length = length
        self.x = [40] * length
        self.y = [40] * length

    def move_right(self):
        if self.direction != "right":
            self.direction = "left"

    def move_left(self):
        if self.direction != "right":
            self.direction = "left"

    def move_up(self):
        if self.direction != "down":
            self.direction = "up"
    
    def move_down(self):
        if self.direction != "up":
            self.direction = "down"

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

            if self.direction == "right":
                self.x[0] += size

            if self.direction == "left":
                self.x[0] -= size
            
            if self.direction == "up":
                self.y[0] += size

            if self.direction == "down":
                self.y[0] -= size

    def display_image(self):
        for  i in range(self.length):
            self.parent_screen.blit(self.snake_image, (self.x[i], self.y[i]))

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
                                                 
