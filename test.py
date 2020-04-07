import BadEngine.main as be

#my varibles
input = be.Input()
window = be.Window(400, 400, 'demo for BadEngine')
testImg = be.Image.load('img/test.png')

#normal game varibles
px,py = 50,50

while True: #game loop

    input.update()

    #testing out all of my classes
    window.setBackground((146, 244, 255))

    #inputs
    if input.Key('leftArrow', 'keyd'):
        px -= 5

    if input.Key('rightArrow', 'keyd'):
        px += 5

    if input.Quit():
        be.sys.exit()
        be.pygame.quit()

    #basic things
    window.render(testImg, px, py)
    window.flip()
