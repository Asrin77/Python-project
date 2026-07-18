import pygame as game

game.init()

class Snake_design:
    def __init__(this):
        this.block = game.load.("game-images/yellow_block.png")
        this.x = 100
        this.y = 100
        

class Game_design:
    def __init__ (this, window):
        this.screen = window
        this.window = game.display.set_mode((600, 600))




    
        