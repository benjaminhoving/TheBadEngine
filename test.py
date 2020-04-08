
import pygame
import BadEngine.main as be
from BadEngine.main import (
    KeyCode, KeyFunction, Update, GameObject
)

#my varibles
input = be.Input()
window = be.Window(400, 400, 'demo for BadEngine')

#images
testImg = be.Image.load('img/test.png')

#GameObjects
player = GameObject(testImg, [50, 50], 50)

#testing colision
test_rect = pygame.Rect(100, 100, 100, 50)

while True: #game loop

    #inputs
    if input.Key(KeyCode.left, KeyFunction.keyDown):
        player.positionX -= 5

    if input.Key(KeyCode.right, KeyFunction.keyDown):
        player.positionX += 5

    if input.Quit():
        be.sys.exit()
        be.pygame.quit()

    #colisions
    if player.collision(test_rect):
        pygame.draw.rect(window.display, (255, 0, 0), test_rect)
    else:
        pygame.draw.rect(window.display, (0,0,0), test_rect)

    #testing out all of my classes
    player.falling(window.height)

    #update inputs
    input.update()

    #update window and graphics
    window.setBackground((146, 244, 255))
    window.render(player)
    window.flip()

    #update basics
    Update.setFps(60)
    Update()
