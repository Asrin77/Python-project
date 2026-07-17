import pygame as game

game.init()
speed = game.time.Clock()

class Snake_game:
    window = game.display.set_mode((600, 600))

































try:
    background_image = game.image.load("game-images/grass.jpg")
except FileNotFoundError:
    print(f"Error: grass.jpg not found")
    game.quit()
    exit()


try:
    block = game.image.load("game-images/yellow_block.png")
except FileNotFoundError:
    print(f"Error: yellow_block.png not found")
    game.quit()
    exit()


X = 100
Y = 100
def block_design():
    window.blit(background_image, (0,0)) 
    window.blit(block, (X, Y))

running = True

while running:

    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        if event.type == game.KEYDOWN:
            if event.key == game.K_RIGHT:
                X+=6
    
            if event.key == game.K_LEFT:
                X -=6
                
            if event.key == game.K_UP:
                Y -= 6
                
            if event.key == game.K_DOWN:
                Y += 6
                
    block_design()

    game.display.flip()
    speed.tick(60)

game.quit()

    

    
        