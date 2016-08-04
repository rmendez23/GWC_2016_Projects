from turtle import *
import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((640,480))


# START WRITING YOUR CODE HERE
def square(size, color):
	pencolor(color)
	pendown()
	for i in range(4):
		right(90)
		forward(size)
        
def triangle(size, color):
	pencolor(color)
	pendown()
	for i in range(3):
		left(120)
		forward(size)


colorList = ["PaleVioletRed", "LightSteelBlue", "DarkGray"]
roofColors = ["MediumSlateBlue, CornflowerBlue"]
doorColors = ["IndianRed, BlueViolet"]
def house(size, color):
	#Recommended functions: fillcolor(...), triange(...), square(...), and door()
	fillcolor(randomColor)
	begin_fill()
	square(size, "Black" )
	end_fill()
	fillcolor(randomRoof)
	begin_fill()
	triangle(size, "BlueViolet")
	end_fill()
	penup()
	right(90)
	forward(size)
	right(90)
	forward(size*(3/4))
	pendown()
	fillcolor(randomDoor)
	begin_fill()
	door (size/2)
	end_fill()

def door(size):
	#remember you will have to adjust your pen because it just finished drawing 
	#your house
	#Recommended functions: penup(), color(...), forward(...), square(...)
	square(size,"Black")


#-----MAIN CODE HERE -----
#This code will run first!
houseXPos = 300
for i in range(20):
	randomColor = colorList[random.randint(0, (len(colorList)-1))]
	randomRoof = roofColors[random.randint(0, (len(roofColors)-1))]
	randomDoor = doorColors[random.randint(0, (len(doorColors)-1))]
	houseYPos = random.randint(-20,0)
	size = random.randint(50,80) #FEEL FREE TO CHANGE THIS AND SEE WHAT HAPPENS
	bgcolor("linen")
	penup()
	goto(houseXPos, houseYPos) #RANDOMIZES HOUSE Y POSITION
	fillcolor("BlueViolet")
	begin_fill()
	#circle(...)
	end_fill()
	#remember you have to move the pen to draw the next house!
	house(size, randomColor)
	#Move to new house position
	penup()
	forward(100)
	right(90)
	forward(50)
	right(90)
	houseXPos-=60
	
	
	


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








