import pygame as game

game.init()



class Snake_design:
    def __init__(this):

        try:
            this.block = game.image.load("game-images/yellow_block.png")
        except FileNotFoundError:
            print(f"Error: yellow_block.png not found")
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
        

class Game_design:
    def __init__ (this, window):
        this.screen = window
        this.window = game.display.set_mode((600, 600))
        try:
            this.window = game.image.load("game-images/grass.jpg")
        except FileNotFoundError:
            print(f"Error: grass.jpg not found")
            game.quit()
            exit()
        this.snake= Snake_design()

    def run(this):
        running = True
        
        while running:
            for event in game.event.get():
                if event.type == game.QUIT:
                     running = False

                if event.type == game.KEYDOWN:

                    if event.key == game.K_RIGHT:
                        this.snake.right_key()
                    
                    if event.key == game.K_LEFT:
                        this.snake.left_key()
                    
                    if event.key == game.K_UP:
                        this.snake.up_key()

                    if event.key == game.K_DOWN:
                        this.snake.down_key()
                        
