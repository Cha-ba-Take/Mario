# -*- coding: UTF-8 -*-

import pygame
from pygame.locals import *
import sys

import Map
import Player

pygame.init()
screen = pygame.display.set_mode((1024, 960))
pygame.display.set_caption("mario test")

keyEvent = 0
state = 0

map = Map.Map(screen, "course1-1.csv")
player = Player.Player(screen)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    keyPressed = pygame.key.get_pressed()
    previousKeyEvent = keyEvent
    keyEvent = 0
    keys = [K_RIGHT, K_LEFT, K_SPACE]
    for i in range(len(keys)):
        if keyPressed[keys[i]]:
            keyEvent += 2 ** i

    previousState = state
    if keyEvent == 0:
        if previousKeyEvent == 1:
            state = 0
        elif previousKeyEvent == 2:
            state = 1
        elif previousKeyEvent == 3:
            if previousState == 2:
                state = 0
            if previousState == 3:
                state = 1
        elif previousKeyEvent == 5:
            state = 0
        elif previousKeyEvent == 6:
            state = 1
    elif keyEvent == 1:
        state = 2
    elif keyEvent == 2:
        state = 3
    elif keyEvent == 3:
        if previousKeyEvent == 1:
            state = 3
        elif previousKeyEvent == 2:
            state = 2
        elif previousKeyEvent == 7:
            if previousState == 4:
                state = 2
            elif previousState == 5:
                state = 3
    elif keyEvent == 4:
        if previousState == 4:
            state = 0
        elif previousState == 5:
            state = 1
    elif keyEvent == 5:
        state = 4
    elif keyEvent == 6:
        state = 5
    elif keyEvent == 7:
        if previousKeyEvent == 3:
            if previousState == 2:
                state = 4
            elif previousState == 3:
                state = 5
        elif previousKeyEvent == 5:
            state = 5
        elif previousKeyEvent == 6:
            state = 4

    state = player.update(state)
    map.update(player.x, player.velocity)

    map.draw()
    player.draw()

    pygame.display.update()
    clock.tick(60)
