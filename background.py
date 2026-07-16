import pygame as game

game.init()

window = game.display.set_mode((1000, 400))

speed = game.time.Clock()

running = True

while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    window.fill("white")
    game.display.flip()

    speed.tick(60)   
game.quit()