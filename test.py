import BadEngine.main as be

#my varibles
Input = be.Input
kf = be.KeyFunction
kc = be.KeyCode
update = be.Update
img = be.Image
window = be.Window

win = window.create(window, 400, 400 , 'demo for BadEngine')
testImg = img.load(img, 'img/test.png')

#normal game varibles
px,py = 50,50

while True: #game loop
    
    #testing out all of my classes
    window.setBackground(window, win, (146, 244, 255))

    #inputs
    if Input.Key(Input, kc.left, kf.keyDown):
        px -= 5

    if Input.Key(Input, kc.right, kf.keyDown):
        px += 5

    if Input.Key(Input, 'quit', 'quit'):
        be.sys.exit()
        be.pygame.quit()

    #basic things
    window.render(window, win, testImg, px, py)
    update()
    update.setFps(update, 60)