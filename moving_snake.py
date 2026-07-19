import pygame as game

game.init()
speed = game.time.Clock()

class Snake_design:
    def __init__(this, screen):
        this.screen = screen

        try:
            this.sk = game.image.load("game-images/yellow_snake.png")
        except FileNotFoundError:
            print(f"Error: yellow_snake.png not found")
            game.quit()
            exit()
 
        this.X = 100 
        this.Y = 100

    def right_key(this):
        if this.X < 600:
            this.X += 15

    def left_key(this):
        if this.X > 0:
            this.X -= 15

    def up_key(this):
        if this.Y > 0:
            this.Y -= 15

    def down_key(this):
        if this.Y < 600 :  
            this.Y += 15
    
    def display(this):
        this.screen.blit(this.sk, (this.X, this.Y))

        

class Game_design:
    def __init__ (this):
        this.screen = game.display.set_mode((600, 600))
        this.snake= Snake_design(this.screen)
         
        try:
            this.window = game.image.load("game-images/grass.jpg")
        except FileNotFoundError:
            print(f"Error: grass.jpg not found")
            game.quit()
            exit()
        

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
  
            this.screen.blit(this.window, (0,0))
            this.snake.display()
            speed.tick(60)
            game.display.flip()
        game.quit()
        

s = Game_design()
s.run()                
