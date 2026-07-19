import pygame
import random

SIZE = 40
MAX_CARROTS = 18
rabbit_size = 26

class Carrot:
    def __init__(self, screen):
        self.screen = screen
        try:
            self.image = pygame.image.load("game-images/carrot.png")
        except FileNotFoundError:
            print(f"Error: carrot.png not found")
            pygame.quit()
            exit()


        self.move()
        self.is_rotten = False

    def move(self):
        self.x = random.randint(0, 13) * SIZE
        self.y = random.randint(0, 13) * SIZE

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
            # Uncomment if you have a rotten carrot image:
            # carrot.image = pygame.image.load(
            #     "game-images/rotten_carrot.png"
            # ).convert_alpha()

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
            if (rabbit_x + rabbit_size > carrot.x and rabbit_x < carrot.x + SIZE and
                rabbit_y + rabbit_size > carrot.y and rabbit_y < carrot.y + SIZE):

                rotten = carrot.is_rotten
                self.carrots.remove(carrot)

                if len(self.carrots) < MAX_CARROTS:
                    self.spawn_multiple(random.randint(1,2))

                return rotten

        return None

    def carrot_count(self):
        return len(self.carrots)

    def game_over(self):
        return len(self.carrots) >= MAX_CARROTS
    
