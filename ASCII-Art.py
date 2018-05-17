##################################################
# Author  : Rebecca Louie
# Date	  : June 2017
# Function: Make ascii art from pictures
# Usage	  : python program.py image.jpg art.txt
##################################################
try:
    from PIL import Image
except ImportError:
    import Image

import Image, sys

img=Image.open(sys.argv[1],'r')
w,h=img.size #returns a tuple
w=int(120.0/h*w) #120 vertical lines for 2 point font in gedit
h=120
w=2*w #widen pic since most fonts are about twice as high as wide
img=img.resize((w,h), Image.BILINEAR) #or BICUBIC
img=img.convert('L') #greyscale
scale = ['@','#','A','%','S','<', '*','+', ':','.']

#Lines 24-26 generte the name of the ASCII art file
name=str(sys.argv[1])		#Converting sys.argv 1 into string
n=name.split(".")			#Spliting the string to exclude the file type
newname=n[0]+"-ASCII.png"	#Asigning a varible to be the original name with the additon of "ASCII.png"

f=open(newname,'w') #Opening new file with name defined on line 26
for y in range(h):
	for x in range(w):
		lum=img.getpixel((x,y)) #int from 0-255
		step=int(256/ (len(scale)-1)) #int(356/9)= 28
		index=lum//step
		f.write(scale[index])
	f.write('\n')

f.close()
