	#ORIGINAL OBAMICON
from PIL import Image
im = Image.open("Juan.jpg")

'''
im.rotate(45).show()
im.rotate(45).save("coconut.jpg", "jpeg")
myPixel = im.getpixel((3,4))
print("Pixel Color")
print(myPixel)
'''

h = im.height
w = im.width

for x in range(w):
	for y in range(h):
		s=im.getpixel((x,y))
		intensity =  s[0] + s[1] +s[2]
		if intensity <= 182:
			im.putpixel((x,y), (0,51,76))	#BLUE
		elif intensity <= 364:
			im.putpixel((x,y), (217, 26, 33))	#RED
		elif intensity <= 546:
			im.putpixel((x,y), (112, 150, 158))		#LIGHT BLUE
		else:
			im.putpixel((x,y), (252, 227, 166))		#YELLOW
im.show()
#im.save("Juan.jpg", "jpeg")
			
	
		#do something w/ rgb colors.