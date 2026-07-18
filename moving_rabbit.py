import pygame as game

game.init()
speed = game.time.Clock()

class Rabbit_design:
    def __init__(this, screen):
        this.screen = screen

        try:
            this.rb = game.image.load("game-images/rabbit.png")
        except FileNotFoundError:
            print(f"Error: rabbit.png not found")
            game.quit()
            exit()
 
        this.X = 236 # 600 -128 / 2
        this.Y = 236

    def right_key(this):
        if this.X < 580:
            this.X += 2

    def left_key(this):
        if this.X > 0:
            this.X -= 2

    def up_key(this):
        if this.Y > 0:
            this.Y -= 2

    def down_key(this):
        if this.Y < 580 :  
            this.Y += 2
    
    def display(this):
        this.screen.blit(this.rb, (this.X, this.Y))

        

class Game_design:
    def __init__ (this):
        this.screen = game.display.set_mode((600, 600))
        this.rabbit= Rabbit_design(this.screen)
         
        try:
            this.window = game.image.load("game-images/grass.jpg")
        except FileNotFoundError:
            print(f"Error: grass.jpg not found")
            game.quit()
            exit()
        

    def run(this):
        running = True

        key_actions = {
            game.K_RIGHT: this.rabbit.right_key,
            game.K_LEFT: this.rabbit.left_key,
            game.K_UP: this.rabbit.up_key,
            game.K_DOWN: this.rabbit.down_key
        }
        
        while running:
            for event in game.event.get():
                if event.type == game.QUIT:
                     running = False

                # if event.type == game.KEYDOWN:

                #     if event.key == game.K_RIGHT:
                #         this.rabbit.right_key()
                    
                #     if event.key == game.K_LEFT:
                #         this.rabbit.left_key()
                    
                #     if event.key == game.K_UP:
                #         this.rabbit.up_key()

                #     if event.key == game.K_DOWN:
                #         this.rabbit.down_key()
            keys = game.key.get_pressed()
            
            for k in key_actions:
                if keys[k]:
                    key_actions[k]()

                
            this.screen.blit(this.window, (0,0))
            this.rabbit.display()
            speed.tick(60)
            game.display.flip()
        game.quit()
        

rb = Game_design()
rb.run()
                        
