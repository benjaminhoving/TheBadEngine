import sys

import pygame
from pygame import event
from pygame.locals import *

pygame.init()

class Window: #make the screen for the game

    def create(self, x, y, name): #to make the window

        pygame.display.set_caption(name)
        return pygame.display.set_mode((x, y), 0, 32)

    def render(self, window,image, x, y): #to render the select image onto the select window

        return window.blit(image, (x, y))
        print('image rendered')

    def setBackground (self, window, rgb):

        return window.fill(rgb)
        print('background color set')

class Input: #to check for input

    def Keys(self, Key): #to select a key

        if Key == 'quit':
            return QUIT

        if Key == 'leftArrow':
            return K_LEFT

        if Key == 'rightArrow':
            return K_RIGHT

        if Key == 'upArrow':
            return K_UP

        if Key == 'downArrow':
            return K_DOWN

        if Key == 'a':
            return K_a

        if Key == 'b':
            return K_b

        if Key == 'c':
            return K_c            

        if Key == 'd':
            return K_d

        if Key == 'e':
            return K_e

        if Key == 'f':
            return K_f

        if Key == 'g':
            return K_g

        if Key == 'h':
            return K_h

        if Key == 'i':
            return K_i

        if Key == 'j':
            return K_j

        if Key == 'k':
            return K_k

        if Key == 'l':
            return K_l

        if Key == 'm':
            return K_m

        if Key == 'n':
            return K_n

        if Key == 'o':
            return K_o

        if Key == 'p':
            return K_p

        if Key == 'q':
            return K_q

        if Key == 'r':
            return K_r

        if Key == 's':
            return K_s

        if Key == 't':
            return K_t

        if Key == 'u':
            return K_u

        if Key == 'v':
            return K_v

        if Key == 'w':
            return K_w

        if Key == 'x':
            return K_x

        if Key == 'y':
            return K_y

        if Key == 'z':
            return K_z

    def Key(self, KeyCode, KeyFunction): #making the input system easy

        for event in pygame.event.get():

            if KeyFunction == 'keyd': #seeing if the key is down or not
                if event.type == KEYDOWN:
                    if event.key == self.Keys(self, KeyCode):
                        return True

            if KeyFunction == 'keyu': #seeing if the key is up
                if event.type == KEYUP:
                    if event.key == self.Keys(self, KeyCode):
                        return True

    def Quit(self): #a qick preset event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

class KeyCode: #codes for key inputs

    left = 'leftArrow'
    right = 'rightArrow'
    up = 'upArrow'
    down = 'downArrow'
    quit = 'quit'
    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'
    E = 'e'
    F = 'f'
    G = 'g'
    H = 'h'
    I = 'i'
    J = 'j'
    K = 'k'
    L = 'l'
    M = 'm'
    N = 'n'
    O = 'o'
    P = 'p'
    Q = 'q'
    R = 'r'
    S = 's'
    T = 't'
    U = 'u'
    V = 'v'
    W = 'w'
    X = 'x'
    Y = 'y'
    Z = 'z'

class KeyFunction: #what am i checking the key for

    keyDown = 'keyd'
    keyUp = 'keyu'
    Quit = 'quit'

class Update: #update all the little things

    def __init__(self): #updating the screen
        pygame.display.update()

    def setFps(self, FramesPerSecond): #how many frames pass in a second

        if FramesPerSecond == None: #checking if it has been set or not
            FramesPerSecond = 60

        tic = pygame.time.Clock()
        tic.tick(FramesPerSecond)

class Image: #handling images

    def __init__(self):
        print('image initionalized')
        pass

    def load(self, path): #loading an image

        return pygame.image.load(path)
        print('The path of the image: ' + path)
