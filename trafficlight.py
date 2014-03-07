#! /usr/bin/env python

###############################################################################
# Traffic light, v0.1                                                         #
# Written by Matthew Dinep                                                    #
# March, 7th, 2014                                                            #
# Code could definitely benefit from refactoring and efficiency improvements  #
###############################################################################


import os
import sys
import pygame
from pygame.locals import (MOUSEBUTTONDOWN, HWSURFACE, DOUBLEBUF, RESIZABLE,
                           QUIT)
import time

# Initialize pygame and set screen
pygame.init()
screen = pygame.display.set_mode((600, 900), HWSURFACE | DOUBLEBUF | RESIZABLE)


# Function to act as an image loader
# Eliminates need to call each image by fully qualified path
def load_image(name):
    image = pygame.image.load(os.path.join("images", name))
    image = image.convert()
    return image, image.get_rect()


# Function controlling light cycle
# Uses system time to determine length of each light
# Mouse events disabled at beginning of cycle and reenabled at end
def lightcycle(background, red):
    pygame.event.set_blocked(MOUSEBUTTONDOWN)
    buttondown, rect = load_image("start_button_down.jpg")
    buttondown = pygame.transform.scale(buttondown, (145, 160))
    screen.blit(buttondown, (380, 270))
    green = pygame.image.load("images/green.jpg")
    yellow = pygame.image.load("images/yellow.jpg")

    screen.blit(background, (0, 0))
    screen.blit(green, (0, 589))
    pygame.display.flip()
    time.sleep(10)

    screen.blit(background, (0, 0))
    screen.blit(yellow, (0, 303))
    pygame.display.flip()
    time.sleep(2)

    button, rect = load_image("start_button_up.jpg")
    button = pygame.transform.scale(button, (400, 300))
    screen.blit(button, (200, 200))
    screen.blit(background, (0, 0))
    screen.blit(red, (0, 11))
    pygame.display.flip()
    pygame.event.set_allowed(MOUSEBUTTONDOWN)


# Generic class for button object creation
class Button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("start_button_up.jpg")

    def setCords(self, x, y):
        self.rect.topleft = x, y

    def pressed(self, mouse):
        if self.rect.collidepoint(mouse):
            return True


# Main function.
# Renders initial screen, button, and executes light cycle on event
def main():
    background, rect = load_image("light.jpg")
    red, rect = load_image("red.jpg")
    button, rect = load_image("start_button_up.jpg")
    button = pygame.transform.scale(button, (400, 300))
    screen.blit(button, (200, 200))
    screen.blit(background, (0, 0))
    screen.blit(red, (0, 11))
    button = Button()
    button.setCords(200, 200)
    pygame.display.flip()
    while 1:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if button.pressed(pygame.mouse.get_pos()):
                    lightcycle(background, red)
            elif event.type == QUIT:
                pygame.quit()
                sys.exit(0)


if __name__ == '__main__':
    main()
