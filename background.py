import pygame as game

game.init()

window = game.display.set_mode((1500, 600))

speed = game.time.Clock()

running = True

while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    speed.tick(60)
    window.fill("white")
game.quit()