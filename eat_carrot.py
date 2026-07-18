import pygame
from pygame.locals import *
import time
import random

SIZE = 40

class Carrot:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/carrot.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE

class RottenCarrot:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("game-images/poisonedcarrot.png").convert()
        self.x = 200
        self.y = 200

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE

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

    def walk(self):
        
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

        self.draw()

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.rabbit = Rabbit(self.surface, 2)
        self.rabbit.draw()
        self.carrot = Carrot(self.surface)
        self.carrot.draw()
        self.rotten_carrot = RottenCarrot(self.surface)
        self.rotten_carrot.draw()
        
        self.high_score = 0
        filename = 'highscore.txt'

        
        try:
            
            with open(filename, 'r') as file:
                content = file.read()
                self.high_score = int(content.strip())

        except FileNotFoundError as e:
            print(f"Error: {e}. The file '{filename}' does not exist.")
            
            with open(filename, 'w') as file:
                file.write("0")

        except IOError as e:
            print(f"Error: {e}. An I/O error occurred while handling the file '{filename}'.")

        except PermissionError as e:
            print(f"Error: {e}. You do not have permission to access the file '{filename}'.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.rabbit.length}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))
        
        hs_score = font.render(f"High Score: {self.high_score}", True, (200, 200, 200))
        self.surface.blit(hs_score, (10, 10))

    def play(self):
        self.rabbit.walk()
        self.carrot.draw()
        self.rotten_carrot.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.rabbit.x[0], self.rabbit.y[0], self.carrot.x, self.carrot.y):
            self.rabbit.increase_length()
            self.carrot.move()
            self.rotten_carrot.move()

        if self.is_collision(self.rabbit.x[0], self.rabbit.y[0], self.rotten_carrot.x, self.rotten_carrot.y):
            filename = 'highscore.txt'
            if self.rabbit.length > self.high_score:
                try:
                    with open(filename, 'w') as file:
                        file.write(str(self.rabbit.length))
                except Exception as e:
                    print(f"Could not save score: {e}")
            
            font = pygame.font.SysFont('arial', 50)
            game_over = font.render("Game Over! Rabbit ate rotten carrot.", True, (255, 0, 0))
            self.surface.blit(game_over, (200, 350))
            pygame.display.flip()
            time.sleep(2)
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
                
            time.sleep(.2)
        
        print("Program ended")

if __name__ == '__main__':
    game = Game()
    game.run()
