import pygame
from pygame.locals import *
import random

pygame.init()
size = 40
height = 600
width = 600
clock = pygame.time.Clock()

HS_FILE = "highscore.txt"


class Apple:

    def __init__(self, screen):
        self.screen = screen

        try:
            self.apple_image = pygame.image.load("game-images/apple.png").convert_alpha()
        except FileNotFoundError:
            print("Error: apple.png not found")
            pygame.quit()
            exit()
        
        self.x = 400
        self.y = 400

    def display_image(self):
        self.screen.blit(self.apple_image, (self.x, self.y))

    def move(self):
        self.x = random.randint(1,14) * size
        self.y = random.randint(3,14) * size

class Snake:
    def __init__(self, screen, length):
        self.screen = screen
        try:
            self.snake_image = pygame.image.load("game-images/yellow_snake.png").convert_alpha()
        except FileNotFoundError:
            print("Error: yellow_snake.png not found")
            pygame.quit()
            exit()

        self.direction = "down" 
        self.length = length
        self.x = [120] * length
        self.y = [120] * length

    def move_right(self):
        if self.direction != "left":
            self.direction = "right"

    def move_left(self):
        if self.direction != "right":
            self.direction = "left"

    def move_up(self):
        if self.direction != "down":
            self.direction = "up"
    
    def move_down(self):
        if self.direction != "up":
            self.direction = "down"

    def move_snake(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "right":
            self.x[0] += size

        if self.direction == "left":
            self.x[0] -= size
        
        if self.direction == "up":
            self.y[0] -= size

        if self.direction == "down":
            self.y[0] += size

    def display_image(self):
        for  i in range(self.length):
            self.screen.blit(self.snake_image, (self.x[i], self.y[i]))

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:

    def __init__(self):

            self.surface = pygame.display.set_mode((width, height))
            pygame.display.set_caption("snake game")

            try:
                self.background = pygame.image.load("game-images/grass.jpg").convert()
            except FileNotFoundError:
                print("Error: grass.jpg not found")
                pygame.quit()
                exit()

            pygame.mixer.init()

            try:
                self.eating_sound = pygame.mixer.Sound("sound/eating.mp3")
                self.gameover_sound = pygame.mixer.Sound("sound/gameover.mp3")

                self.eating_sound.set_volume(1.0)
                self.gameover_sound.set_volume(1.0)

                pygame.mixer.music.load("sound/background.mp3")
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play(-1)

            except FileNotFoundError:
                print("Error: One or more sound files were not found.")
                pygame.quit()
                exit()

            self.snake = Snake(self.surface, 2)
            self.apple = Apple(self.surface)
            
            self.high_score = 0
            self.load_high_score()


    def load_high_score(self):
        try:
            with open(HS_FILE, "r") as file:
                 content = file.read()
                 
            if content.isdigit():
                self.high_score = int(content)
            else:
                self.high_score = 0

        except FileNotFoundError as e:
            print(f"error: {e}. the file '{HS_FILE}' does not exist")
            self.high_score = 0


    def save_high_score(self):
        try:
            with open(HS_FILE, "w") as file:
                file.write(str(self.high_score))

        except IOError as e:
            print(f"error: {e}. unable to save the high score")


    def check_collision(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return True
        return False


    def display_text(self):

        font = pygame.font.SysFont("arial", 26, bold = True)

        score_text = font.render(f"Score: {self.snake.length - 2}", True, (255, 192, 203))
        self.surface.blit(score_text, (20,20))

        hs_text = font.render(f"high score: {self.high_score}", True, (255, 215, 0))
        self.surface.blit(hs_text, (20,50))


    def game_over(self):
        pygame.mixer.music.stop()
        self.gameover_sound.play()

        self.surface.fill((0,0,0))

        font = pygame.font.SysFont("arial",40)

        text1 = font.render("GAME OVER", True, (255,0,0))
        text2 = font.render(f"Final Score : {self.snake.length - 2}", True, (255,255,255))

        self.surface.blit(text1,(180,220))
        self.surface.blit(text2,(180,280))

        pygame.display.flip()

        pygame.time.wait(3000)

        pygame.quit()
        exit()

    def play(self):
        try:
            self.surface.blit(self.background, (0, 0))

            self.snake.move_snake()
            self.snake.display_image()
            self.apple.display_image()

            if self.check_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
                self.eating_sound.play()
                self.snake.increase_length()
                self.apple.move()
                
                if self.snake.length - 2 > self.high_score:
                    self.high_score = self.snake.length - 2
                    self.save_high_score()

            if (self.snake.x[0] < 0 or
                self.snake.x[0] >= width  or
                self.snake.y[0] < 0 or
                self.snake.y[0] >= height):

                self.game_over()
            self.display_text()

            for i in range(1, self.snake.length):
                if (self.snake.x[0] == self.snake.x[i] and
                    self.snake.y[0] == self.snake.y[i]):

                    self.game_over()
                    self.display_text()
        except Exception as e:
            print(f"error in game play: {e}")
            pygame.quit()
            exit()

    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     running = False

                if event.type == KEYDOWN:

                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    
                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()
            
            self.play()
            clock.tick(3)
            pygame.display.flip()
        pygame.quit()
game = Game()
game.run()