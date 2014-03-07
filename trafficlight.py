#! /usr/bin/env python
import os, sys
import pygame
from pygame.locals import *
import time 

pygame.init()
screen=pygame.display.set_mode((600,900),HWSURFACE|DOUBLEBUF|RESIZABLE)



down = pygame.image.load("images/start_button_down.jpg")
#up = pygame.image.load("images/start_button_up.jpg")

def load_image(name):
	fullname = os.path.join("images", name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'Unable to load image:', fullname
		raise SystemExit, message		
	image = image.convert()
	return image, image.get_rect()
def lightcycle(background, red):
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
	screen.blit(background, (0,0))
	screen.blit(red, (0,11))
	pygame.display.flip()
	return True

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
		
def main():
	background = pygame.image.load("images/light.jpg")
	red = pygame.image.load("images/red.jpg")
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
					done = lightcycle(background, red)
	
if __name__ == '__main__': main()