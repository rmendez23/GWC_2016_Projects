from turtle import *
import pygame
import sys
import math
pygame.init()
screen = pygame.display.set_mode((640,480))

# START WRITING YOUR CODE HERE
def square(size, color):
	pencolor(color)
	pendown()
	for i in range(4):
		forward(size)
		right(90)
        
def triangle(size, color):
	pencolor(color)
	pendown()
	for i in range(1):
		left(60)
		forward(size)
		right(120)
		forward(size)
		right(120)
		forward(size+10)

def house(houseWidth, roofHeight, color):
	#Recommended functions: fillcolor(...), triange(...), square(...), and door()
	pencolor(color)
	halfHouse = houseWidth / 2
	roofAngle = math.atan2(roofHeight,halfHouse)
	roofSide = math.sqrt(halfHouse**2 + roofHeight**2)
	roofTopAngle = 2 * math.atan2(halfHouse,roofHeight)
	degrees(roofAngle)
	degrees(roofTopAngle)
	square(houseWidth, color) #body of house
	left(roofAngle) #roof
	forward(roofSide)
	right(180-roofTopAngle)
	forward(roofSide)
	right(180-roofAngle)
	forward(houseWidth)
	

house(50, 30, "BlueViolet")
"""
def door(width, height, color):
	remember you will have to adjust your pen because it just finished drawing 
	your house
	Recommended functions: penup(), color(...), forward(...), square(...)
	for i in range(4)
		forward(width)
"""
#-----MAIN CODE HERE -----
#This code will run first!

"""
for i in range ...
	bgcolor("linen")
	penup()
	goto(..., 0) #REPLACE ... WITH A NUMBER YOU WANT
	size = 40 #FEEL FREE TO CHANGE THIS AND SEE WHAT HAPPENS

	fillcolor(...)
	begin_fill()
	circle(...)
	end_fill()
	remember you have to move the pen to draw the next house!
	house(..., ...)
"""

#this keeps the window open!
while True:
	#this allows for the window to remain open
	for event in pygame.event.get():
		# it listens for events or changes in the program
		if event.type == pygame.QUIT:
			'''if the change in the program is the user
			hitting the X button, then it will quit
			the game and exit the system.'''
			pygame.quit(); sys.exit();








