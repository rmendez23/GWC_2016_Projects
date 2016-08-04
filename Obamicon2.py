	#SAME AS OBAMICON.PY BUT WITH DIFFERENT COLORS
from PIL import Image
im = Image.open("Juan.jpg")

h = im.height
w = im.width

for x in range(w):
	for y in range(h):
		s=im.getpixel((x,y))
		intensity =  s[0] + s[1] +s[2]
		if intensity <= 182:
			im.putpixel((x,y), (149,50,230)) #Purple Hex: #9532e6
		elif intensity <= 364:
			im.putpixel((x,y), (201, 38, 174)) #Magenta Hex: #c926ae
		elif intensity <= 546:
			im.putpixel((x,y), (191, 230, 50)) #Lime Green Hex: #bfe632
		else:
			im.putpixel((x,y), (198, 232, 245)) #Light Baby Blue Hex: #c6e8f5
im.show()
#im.save("Juan.jpg", "jpeg")
			
	
		#do something w/ rgb colors.