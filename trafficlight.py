#! /usr/bin/env python

#################################################################################
#Traffic light, v0.1															#
#Written by Matthew Dinep														#
#March, 7th, 2014																#
#Code could definitely benefit from refactoring and efficiency improvements		#
#################################################################################


import os, sys
import pygame
from pygame.locals import *
import time 

#initialize pygame and set screen
pygame.init()
screen=pygame.display.set_mode((600,900),HWSURFACE|DOUBLEBUF|RESIZABLE)

#function to act as an image loader
#eliminates need to call each image by fully qualified path
def load_image(name):
	fullname = os.path.join("images", name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'Unable to load image:', fullname
		raise SystemExit, message		
	image = image.convert()
	return image, image.get_rect()
	
#Function controlling light cycle
#Uses system time to determine length of each light
#mouse events disabled at beginning of cycle nad reenabled at end	
def lightcycle(background, red):
	try:
		pygame.event.set_blocked(MOUSEBUTTONDOWN)
		buttondown, rect = load_image("start_button_down.jpg")
		buttondown = pygame.transform.scale(buttondown, (145,160))
		screen.blit(buttondown, (380,270))
		green = pygame.image.load("images/green.jpg")
		yellow = pygame.image.load("images/yellow.jpg")
		now = time.time()
		endgreen = now + 10
		endyellow = endgreen + 2
		while time.time() < endgreen:
			screen.blit(background, (0,0))
			screen.blit(green, (0,589))
			pygame.display.flip()
		while endgreen <= time.time() < endyellow:
			screen.blit(background, (0,0))
			screen.blit(yellow, (0,303))
			pygame.display.flip()
		button, rect = load_image("start_button_up.jpg")
		button = pygame.transform.scale(button, (400,300))
		screen.blit(button, (200,200))
		screen.blit(background, (0,0))
		screen.blit(red, (0,11))
		pygame.display.flip()
		pygame.event.set_allowed(MOUSEBUTTONDOWN)
	except pygame.error, message:
		print 'Unable to execute light cycle'
		raise SystemExit, message

#Generic class for button object creation 
class Button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("start_button_up.jpg")
    def setCords(self,x,y):
        self.rect.topleft = x,y
    def pressed(self,mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False

#Main function. Renders initial screen, button, and executes light cycle on event
def main():
	background, rect = load_image("light.jpg")
	red, rect = load_image("red.jpg")
	button, rect = load_image("start_button_up.jpg")
	button = pygame.transform.scale(button, (400,300))
	screen.blit(button, (200,200))
	screen.blit(background, (0,0))
	screen.blit(red, (0,11))
	button = Button()
	button.setCords(200,200)
	pygame.display.flip()
	while 1:
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				mouse = pygame.mouse.get_pos()
				if button.pressed(mouse):
					lightcycle(background, red)
	
if __name__ == '__main__': 
	main()