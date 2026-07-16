import pygame as game

game.init()

window = game.display.set_mode((1000, 400))
game.display.set_caption("Piko runs")
background_image = game.image.load("skybackground.png").convert()

speed = game.time.Clock()



running = True

while running:

    window.blit(background_image, (0,0))

    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    
    game.display.flip()

    speed.tick(60)   
game.quit()