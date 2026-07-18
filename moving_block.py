import pygame as game

game.init()

class Snake_design:
    def __init__(this):
        this.block = game.load("game-images/yellow_block.png")
        this.x = 100
        this.y = 100

    def right_key(this):
        this.x += 12

    def left_key(this):
        this.x -= 12

    def up_key(this):
        this.y -= 12

    def down_key(this):
        this.y += 12
        

class Game_design:
    def __init__ (this, window):
        this.screen = window
        this.window = game.display.set_mode((600, 600))
        this.window = game.image.load("game-images/grass.jpg")




    
        