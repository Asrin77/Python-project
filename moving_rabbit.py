import pygame as game

game.init()


class Rabbit_design:
    def __init__(this, screen):
        this.screen = screen

        try:
            this.rb = game.image.load("game-images/rabbit.png")
        except FileNotFoundError:
            print(f"Error: rabbit.png not found")
            game.quit()
            exit()
 
        this.X = 100
        this.Y = 100

    def right_key(this):
        this.X += 12

    def left_key(this):
        this.X -= 12

    def up_key(this):
        this.Y -= 12

    def down_key(this):
        this.Y += 12
    
    def display(this):
        this.screen.blit(this.rb, (this.X, this.Y))

        

class Game_design:
    def __init__ (this):
        this.screen = game.display.set_mode((600, 600))
         
        try:
            this.window = game.image.load("game-images/grass.jpg")
        except FileNotFoundError:
            print(f"Error: grass.jpg not found")
            game.quit()
            exit()
        this.rabbit= Rabbit_design(this.screen)

    def run(this):
        running = True
        
        while running:
            for event in game.event.get():
                if event.type == game.QUIT:
                     running = False

                if event.type == game.KEYDOWN:

                    if event.key == game.K_RIGHT:
                        this.rabbit.right_key()
                    
                    if event.key == game.K_LEFT:
                        this.rabbit.left_key()
                    
                    if event.key == game.K_UP:
                        this.rabbit.up_key()

                    if event.key == game.K_DOWN:
                        this.rabbit.down_key()
                
            this.screen.blit(this.window, (0,0))
            this.rabbit.display()
            game.display.flip()
        game.quit()

rb = Game_design()
rb.run()
                        
