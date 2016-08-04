#this imports all the libaries 
from turtle import *
import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((640,480))

# START WRITING YOUR CODE HERE

def drawSquare(length, color):
	for i in range(4):
		pencolor(color)
		forward(length)
		right(90)
		

drawSquare(50, "aquamarine1")

def drawTriangle(sideLength, color):
	for i in range(3):
		pencolor(color)
		forward(sideLength)
		right(120)
		
drawTriangle(50, "bisque2")

def starSquare(length, colorSquare, colorStar):
	for i in range(4):
		pencolor(colorSquare)
		forward(length)
		right(90)
	for i in range(3):
		pencolor(colorStar)
		forward(sideLength)
		right(120)
	penup()
	forward(length)
	pendown()
	for i in range(3):
		pencolor(colorStar)
		forward(sideLength)
		right(120)
		
		


while True:
	#this allows for the window to remain open
	for event in pygame.event.get():
		# it listens for events or changes in the program
		if event.type == pygame.QUIT:
			'''if the change in the program is the user
			hitting the X button, then it will quit
			the game and exit the system.'''
			pygame.quit(); sys.exit();