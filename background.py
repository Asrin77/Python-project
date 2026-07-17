import pygame as game

game.init()
speed = game.time.Clock()

window = game.display.set_mode((1000, 400))

background_image = game.image.load("skybackground.png")
b_width = background_image.get_width()
image_pos = (window.get_width()/b_width) + 2.5

scroll = 0

running = True

while running:

    window.blit(background_image, (0,0))
    
    for event in game.event.get():  #close button
        if event.type == game.QUIT:
            running = False
    
    
    for i in range(0,int(image_pos)):  #scrolling background
        window.blit(background_image, ((i*b_width+scroll , 0)))
    
    scroll -= 5

    if scroll <= -b_width:  #resetting
        scroll = 0
    
    game.display.flip()

    speed.tick(60)   
game.quit()