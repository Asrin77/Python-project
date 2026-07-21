import pygame
import random

SIZE = 40
WIDTH = 600
HEIGHT = 600

class Apple:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("game-images/apple.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (SIZE, SIZE))
        self.move()

    def move(self):
        self.x = random.randint(0, (WIDTH // SIZE) - 1) * SIZE
        self.y = random.randint(0, (HEIGHT // SIZE) - 1) * SIZE

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("game-images/block.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (SIZE, SIZE))

        self.length = 2
        self.x = [SIZE, 0]
        self.y = [0, 0]
        self.direction = "right"

    def draw(self):
        for i in range(self.length):
            self.screen.blit(self.image, (self.x[i], self.y[i]))

    def walk(self):
        
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        
        if self.direction == "right":
            self.x[0] += SIZE
        elif self.direction == "left":
            self.x[0] -= SIZE
        elif self.direction == "up":
            self.y[0] -= SIZE
        elif self.direction == "down":
            self.y[0] += SIZE

    def increase_length(self):
        self.length += 1
        self.x.append(self.x[-1])
        self.y.append(self.y[-1])

    def move_left(self):
        if self.direction != "right":
            self.direction = "left"

    def move_right(self):
        if self.direction != "left":
            self.direction = "right"

    def move_up(self):
        if self.direction != "down":
            self.direction = "up"

    def move_down(self):
        if self.direction != "up":
            self.direction = "down"



class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")

        self.background = pygame.image.load("game-images/grass.jpeg").convert()
        self.background = pygame.transform.scale(
            self.background, (WIDTH, HEIGHT))

        self.font = pygame.font.SysFont("Arial", 30)

        self.clock = pygame.time.Clock()

        
        self.eating_sound = pygame.mixer.Sound("sound/eating.mp3")
        self.eating_sound.set_volume(2.0)

        self.gameover_sound = pygame.mixer.Sound("sound/gameover.mp3")
        self.gameover_sound.set_volume(2.0)

        pygame.mixer.music.load("sound/background.mp3")
        pygame.mixer.music.set_volume(2.0)
        pygame.mixer.music.play(-1)

        
        self.speed = 4

        self.snake = Snake(self.screen)
        self.apple = Apple(self.screen)

    def collision(self):
        return self.snake.x[0] == self.apple.x and self.snake.y[0] == self.apple.y

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.apple.draw()
        self.snake.draw()

        score = self.font.render(
            f"Score: {self.snake.length - 2}", True, (255, 255, 255))
        self.screen.blit(score, (10, 10))

        pygame.display.update()

    def game_over(self):
        pygame.mixer.music.stop()
        self.gameover_sound.play()
        text = self.font.render(
            "GAME OVER!", True, (255, 0, 0))
        text2 = self.font.render(
            f"Final Score: {self.snake.length - 2}", True, (255, 255, 255))

        self.screen.blit(text, (300, 250))
        self.screen.blit(text2, (280, 300))

        pygame.display.update()

        pygame.time.wait(2500)

    def run(self):

        running = True

        while running:

            
            self.clock.tick(self.speed)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        running = False

                    elif event.key == pygame.K_LEFT:
                        self.snake.move_left()

                    elif event.key == pygame.K_RIGHT:
                        self.snake.move_right()

                    elif event.key == pygame.K_UP:
                        self.snake.move_up()

                    elif event.key == pygame.K_DOWN:
                        self.snake.move_down()

            self.snake.walk()

            
            if self.collision():
                self.eating_sound.play()
                self.snake.increase_length()
                self.apple.move()

                
                if self.speed < 12:
                    self.speed += 0.2

            
            if (self.snake.x[0] < 0 or
                self.snake.x[0] >= WIDTH or
                self.snake.y[0] < 0 or
                self.snake.y[0] >= HEIGHT):
                self.game_over()
                running = False

            self.draw()

        pygame.quit()

