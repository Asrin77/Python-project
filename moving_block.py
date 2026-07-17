import pygame as game

game.init()

speed = game.time.Clock()

window = game.display.set_mode((600, 600))
background_image = game.image.load("grass.jpg")

running = True

while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    window.blit(background_image, (0,0))

    game.display.flip()

    speed.tick(60)
game.quit()