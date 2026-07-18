import pygame
from pygame.locals import *
import time
import random
import os

SIZE = 40
HIGHSCORE_FILE = "highscore.txt"

class Carrot:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/carrot.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = random.randint(0, 24) * SIZE
        self.y = random.randint(0, 19) * SIZE

class RottenCarrot:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/rotten_carrot.jpg").convert()
        self.x = -100
        self.y = -100

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = random.randint(0, 24) * SIZE
        self.y = random.randint(0, 19) * SIZE

class Rabbit:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/rabbit.jpg").convert()
        self.direction = 'down'
        self.length = length
        self.x = [40] * length
        self.y = [40] * length

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def hop(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
            
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

    def draw(self):
        self.parent_screen.fill((34, 139, 34)) 
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

    def increase_trail(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Rabbit & Carrot Chase")
        self.rabbit = Rabbit(self.surface, 2)
        self.carrot = Carrot(self.surface)
        self.rotten_carrot = RottenCarrot(self.surface)
        
        
        self.high_score = self.load_high_score()

    def load_high_score(self):
        """Reads high score from file. Creates file if missing."""
        if not os.path.exists(HIGHSCORE_FILE):
            with open(HIGHSCORE_FILE, "w") as f:
                f.write("0")
            return 0
        try:
            with open(HIGHSCORE_FILE, "r") as f:
                return int(f.read().strip())
        except ValueError:
            return 0 

    def save_high_score(self, current_score):
        """Saves new high score to file if broken."""
        if current_score > self.high_score:
            self.high_score = current_score
            with open(HIGHSCORE_FILE, "w") as f:
                f.write(str(self.high_score))

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        current_score = self.rabbit.length - 2
        
        
        score_txt = font.render(f"Carrots Eaten: {current_score}", True, (255, 255, 255))
        self.surface.blit(score_txt, (750, 10))
        
        
        hs_txt = font.render(f"High Score: {self.high_score}", True, (255, 215, 0)) # Gold color
        self.surface.blit(hs_txt, (10, 10))

    def show_game_over(self):
        current_score = self.rabbit.length - 2
        self.save_high_score(current_score) # Check and save high score to file
        
        self.surface.fill((34, 139, 34))
        font_large = pygame.font.SysFont('arial', 50)
        font_small = pygame.font.SysFont('arial', 30)
        
        line1 = font_large.render("Game Over!", True, (255, 0, 0))
        line2 = font_large.render("The Rabbit ate a rotten carrot!", True, (255, 255, 255))
        line3 = font_small.render(f"Your Score: {current_score}   |   All-Time High: {self.high_score}", True, (255, 215, 0))
        
        self.surface.blit(line1, (380, 250))
        self.surface.blit(line2, (220, 330))
        self.surface.blit(line3, (310, 430))
        
        pygame.display.flip()
        time.sleep(4) 

    def play(self):
        self.rabbit.hop()
        self.rabbit.draw()       
        self.carrot.draw()       
        self.rotten_carrot.draw() 
        self.display_score()    
        pygame.display.flip()   

        
        if self.is_collision(self.rabbit.x[0], self.rabbit.y[0], self.carrot.x, self.carrot.y):
            self.rabbit.increase_trail()
            self.carrot.move()
            self.rotten_carrot.move() 


        if self.is_collision(self.rabbit.x[0], self.rabbit.y[0], self.rotten_carrot.x, self.rotten_carrot.y):
            self.show_game_over()
            return False 
            
        return True

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.rabbit.move_left()
                    if event.key == K_RIGHT:
                        self.rabbit.move_right()
                    if event.key == K_UP:
                        self.rabbit.move_up()
                    if event.key == K_DOWN:
                        self.rabbit.move_down()
                elif event.type == QUIT:
                    running = False
            
            if not self.play():
                running = False
                
            time.sleep(0.15)

if __name__ == '__main__':
    game = Game()
    game.run()
