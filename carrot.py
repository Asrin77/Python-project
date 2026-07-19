import pygame
import random
 
SIZE = 40
MAX_CARROTS = 18
 
 
class Carrot:
 
    def __init__(self, screen):
 
        self.screen = screen
 
        self.image = pygame.image.load(
            "game-images/carrot.png"
        ).convert_alpha()
 
        self.move()
 
        self.is_rotten = False
 
    def move(self):
 
        self.x = random.randint(0, 14) * SIZE
        self.y = random.randint(0, 14) * SIZE
 
    def display(self):
 
        self.screen.blit(self.image, (self.x, self.y))
 
 
class CarrotManager:
 
    def __init__(self, screen):
 
        self.screen = screen
 
        self.carrots = []
 
        self.spawn_carrot()
 
    def spawn_carrot(self):
 
        if len(self.carrots) >= MAX_CARROTS:
            return
 
        carrot = Carrot(self.screen)
 
        chance = random.randint(1, 5)
 
        if chance == 1:
            carrot.is_rotten = True
 
        self.carrots.append(carrot)
 
    def spawn_multiple(self, number):
 
        for i in range(number):
 
            if len(self.carrots) < MAX_CARROTS:
                self.spawn_carrot()
                def display_all(self):
 
        for carrot in self.carrots:
            carrot.display()
 
 
    def check_collision(self, rabbit_x, rabbit_y):
 
        for carrot in self.carrots:
 
            if (rabbit_x >= carrot.x and rabbit_x < carrot.x + SIZE and
                rabbit_y >= carrot.y and rabbit_y < carrot.y + SIZE):
 
                rotten = carrot.is_rotten
 
                self.carrots.remove(carrot)
 
                if len(self.carrots) < MAX_CARROTS:
 
                    new_carrots = random.randint(2, 3)
 
                    self.spawn_multiple(new_carrots)
 
                return rotten
 
        return None
 
 
    def carrot_count(self):
 
        return len(self.carrots)
 
 
    def game_over(self):
 
        if len(self.carrots) >= MAX_CARROTS:
            return True
 
        return False