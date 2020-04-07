import sys

import pygame
from pygame import event
from pygame.locals import *

pygame.init()


class Input:
    KEY_MAP = {
        pygame.K_LEFT: 'leftArrow',
        pygame.K_RIGHT: 'rightArrow',
        pygame.K_UP: 'upArrow',
        pygame.K_DOWN: 'downArrow',
    }

    EVENT_TYPE_MAP = {
        pygame.QUIT: 'quit',
        pygame.KEYDOWN: 'keyd',
        pygame.KEYUP: 'keyu',
    }

    EVENT_TYPE_MAPPERS = {
        pygame.QUIT: lambda e: (Input.EVENT_TYPE_MAP.get(e.type, None),),
        pygame.KEYDOWN: lambda e: (Input.EVENT_TYPE_MAP.get(e.type, None), Input.KEY_MAP.get(e.key, None)),
        pygame.KEYUP: lambda e: (Input.EVENT_TYPE_MAP.get(e.type, None), Input.KEY_MAP.get(e.key, None)),
        pygame.MOUSEBUTTONDOWN: lambda e: (Input.EVENT_TYPE_MAP.get(e.type, None), e.button, e.pos),
        pygame.MOUSEBUTTONUP: lambda e: (Input.EVENT_TYPE_MAP.get(e.type, None), e.button, e.pos),
    }

    def __init__(self):
        self.events = set()

    def update(self):
        self.events = self._process_pygame_events(pygame.event.get())

    @classmethod
    def _process_pygame_events(cls, events):
        new_events = set()
        for event in events:
            new_event = cls._process_pygame_event(event)
            if new_event is not None:
                print(new_event)
                new_events.add(new_event)
        return new_events

    @classmethod
    def _process_pygame_event(cls, event):
        mapper = cls.EVENT_TYPE_MAPPERS.get(event.type, None)
        if mapper is not None:
            return mapper(event)

    def Quit(self):
        return ('quit', ) in self.events

    def Key(self, KeyCode, KeyFunction):
        # print(KeyFunction, KeyCode)
        # print(self.events)
        return (KeyFunction, KeyCode) in self.events


class Window: #make the screen for the game

    def __init__(self, x, y, name):
        self.display = pygame.display.set_mode((x, y), 0, 32)
        pygame.display.set_caption(name)

    def render(self, image, x, y): #to render the select image onto the select window
        # print('image rendered')
        return self.display.blit(image, (x, y))

    def setBackground(self, rgb):
        # print('background color set')
        return self.display.fill(rgb)

    def flip(self):
        pygame.display.flip()


class KeyCode: #codes for key inputs

    right = 'rightArrow'
    left = 'leftArrow'
    up = 'upArrow'
    down = 'downArrow'
    done = 'quit'
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


class KeyFunction:
    keyUp = 'keyu'
    keyDown = 'keyd'
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
    @staticmethod
    def load(path): #loading an image
        return pygame.image.load(path)
        # print('The path of the image: ' + path)
