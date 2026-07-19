import pygame
from pygame.locals import *
import time
import random

SIZE = 40
HS_FILE = "highscore.txt"  # File to store the high score

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("game-images/apple.png").convert_alpha()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE

class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("game-images/snake_block_yellow.png").convert_alpha()
        self.direction = 'down'
        self.length = length
        self.x = [40] * length
        self.y = [40] * length

    def move_left(self):
        if self.direction != 'right':  # Prevent instant reverse self-collision
            self.direction = 'left'

    def move_right(self):
        if self.direction != 'left':
            self.direction = 'right'

    def move_up(self):
        if self.direction != 'down':
            self.direction = 'up'

    def move_down(self):
        if self.direction != 'up':
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

    def draw(self):
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
        pygame.display.set_caption("Snake Game with Safe High Scores")
        self.snake = Snake(self.surface, 2)
        self.apple = Apple(self.surface)
        
        # Load high score safely on startup
        self.high_score = self.load_high_score()

    # === FILE AND ERROR HANDLING CODE ===
    def load_high_score(self):
        """Safely reads the high score from a file using specific exception handling."""
        try:
            with open(HS_FILE, 'r') as file:
                content = file.read().strip()
                return int(content) if content.isdigit() else 0
        except FileNotFoundError:
            print(f"Notice: '{HS_FILE}' not found. Creating a new one.")
            return 0
        except PermissionError as e:
            print(f"Error: {e}. No permission to read '{HS_FILE}'. Defaulting score to 0.")
            return 0
        except IOError as e:
            print(f"Error: {e}. System I/O issue while reading '{HS_FILE}'.")
            return 0
        except Exception as e:
            print(f"Unexpected error while loading high score: {e}")
            return 0

    def save_high_score(self):
        """Safely writes the high score to a file using specific exception handling."""
        try:
            with open(HS_FILE, 'w') as file:
                file.write(str(self.high_score))
                print(f"High score ({self.high_score}) successfully saved to '{HS_FILE}'.")
        except PermissionError as e:
            print(f"Error: {e}. No permission to write to '{HS_FILE}'. Score not saved.")
        except IOError as e:
            print(f"Error: {e}. System I/O issue while saving '{HS_FILE}'.")
        except Exception as e:
            print(f"Unexpected error while saving high score: {e}")
    # ====================================

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def display_ui(self):
        font = pygame.font.SysFont('arial', 26)
        
        # Current Score
        score_text = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score_text, (820, 10))
        
        # High Score
        hs_text = font.render(f"High Score: {self.high_score}", True, (255, 215, 0))
        self.surface.blit(hs_text, (820, 45))

    def play(self):
        self.surface.fill((110, 110, 5))  # Clear background once per frame
        
        self.snake.walk()
        self.snake.draw()
        self.apple.draw()
        
        # Check collision with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()
            
            # Check if current score beats high score
            if self.snake.length > self.high_score:
                self.high_score = self.snake.length
                self.save_high_score()  # Save instantly upon beating it

        self.display_ui()
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_LEFT:
                        self.snake.move_left()
                    elif event.key == K_RIGHT:
                        self.snake.move_right()
                    elif event.key == K_UP:
                        self.snake.move_up()
                    elif event.key == K_DOWN:
                        self.snake.move_down()
                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(.2)
            
        pygame.quit()
        print("Program ended")

if __name__ == '__main__':
    game = Game()
    game.run()
