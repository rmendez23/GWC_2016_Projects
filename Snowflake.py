"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow")


class SnowFlake():
	'''
    This class will be used to create the SnowFlake Objects.
    It takes: 
        size - an integer that tells us how big we want the snowflake
        position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
        wind - a boolean that lets us know if there is any wind or not.  
	'''
	def __init__(self, size, position, wind=False):
		self.size = size
		self.position = position
		self.wind = wind
    
	def fall(self, speed):
		self.position[1] += speed
		
		
		if self.wind == True:
			self.position[0]+= speed
		'''
        Take in a int that represnts the speed at which the snowflake is falling in the y-direction.  
        A + int will have the snowflake falling down the screen. 
        A - int will have the snowflake falling up the screen. 
        
        If wind = True
            - the x direction of the snowflake changes
		'''
        
	def draw(self,size):
		pygame.draw.circle(screen,WHITE,(self.position[0],self.position[1]),size)			#circle(Surface, color, pos, radius, width=0)
		'''
        Uses pygame and the global screen variable to draw the snowflake on the screen
		'''
		
	# ---- end of class is here!	

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Speed
speed = 5


# Snow List - it's empty in the beginning! You must initialize
# snowflakes objects in the code below.
snow_list = []

# -------- Main Program Loop -----------
y=0
while not done:
    # --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Screen-clearing code goes here
	screen.fill(BLACK)
	# Begin Snow
	x = random.randrange(0,700)
	#y = random.randrange(0,500)
	
	snow_list.append(SnowFlake(4,[x,0],False))
	for i in snow_list:
		size = random.randrange(2,5)
		i.fall(speed)
		i.draw(size)
		
	#call or make the object place into a list
	#call the fall function on that object
	
	
    



    


	# End Snow
	# --- update screen
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
