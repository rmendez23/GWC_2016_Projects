	#FOR TESTING WITH THE INTENSITY INEQUALITIES
from PIL import Image
im = Image.open("flowers.jpg")

h = im.height
w = im.width
'''
for x in range(w):
	for y in range(h):
		s=im.getpixel((x,y))
		intensity =  s[0] + s[1] +s[2]
		if intensity <= 150:
			im.putpixel((x,y), (97, 42, 119)) #Purple
		elif intensity <= 364:
			im.putpixel((x,y), (148, 48, 97)) #Magenta 
		elif intensity <= 580:
			im.putpixel((x,y), (123, 165, 54)) #Lime Green 
		else:
			im.putpixel((x,y), (171, 177, 58)) #Light Lime Green
im.show()
#im.save("Juan.jpg", "jpeg")
			
	
		#do something w/ rgb colors.

for x in range(w):
	for y in range(h):
		s=im.getpixel((x,y))
		intensity =  s[0] + s[1] +s[2]
		if intensity <= 150:
			im.putpixel((x,y), (57, 53, 125)) #Blue -- Jacket
		elif intensity <= 364:
			im.putpixel((x,y), (179, 150, 58)) #Mustard yellow -- face
		elif intensity <= 580:
			im.putpixel((x,y), (81, 46, 121)) #Lime Green -- face highlights
		else:
			im.putpixel((x,y), (179, 170, 58)) #Light Lime Green -- background
im.show()
#im.save("Juan.jpg", "jpeg")
			
	
		#do something w/ rgb colors.
'''
for x in range(w):
	for y in range(h):
		s=im.getpixel((x,y))
		intensity =  s[0] + s[1] +s[2]
		if intensity <= 150:
			im.putpixel((x,y), (97, 42, 119)) #Purple
		elif intensity <= 364:
			im.putpixel((x,y), (148, 48, 97)) #Magenta 
		elif intensity <= 580:
			im.putpixel((x,y), (123, 165, 54)) #Lime Green 
		else:
			im.putpixel((x,y), (171, 177, 58)) #Light Lime Green
im.show()
im.save("flowers2", "jpeg")
			
	
		#do something w/ rgb colors.