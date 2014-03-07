#! /usr/bin/env python
import sys
import pygame

pygame.init()
screen=pygame.disllay.set_mode((400,400),HWSURFACE|DOUBLEBUF|RESIZABLE)


green = pygame.image.load("images/green.jpg")
yellow = pygame.image.load("images/yellow.jpg")
red = pygame.image.load("images/red.jpg")
light = pygame.image.load("images/light.jpg")
down = pygame.image.load("start_button_down.jpg")
up = pygame.image.load("start_button_up.jpg")

