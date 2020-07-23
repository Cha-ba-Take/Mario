# -*- coding: UTF-8 -*-

import pygame

import Display
import Event

pygame.init()
event = Event.Event()
display = Display.Display(event)

frame = 0
clock = pygame.time.Clock()
while True:
    Event.quitEvent()
    event.keyEventGet()

    display.update()
    display.draw()

    clock.tick(60)
