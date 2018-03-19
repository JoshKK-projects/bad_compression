from PIL import Image
from itertools import chain
from Tkinter import Tk
from tkFileDialog import askopenfilename

# Tk().withdraw()
# filename = askopenfilename()

# https://imgur.com/gallery/Sgg0j
im = Image.open("shrine_hd.jpg")
im = im.rotate(90)

im_width, im_height = im.size
slice_fractions = 1024
slice_width = (im_width / slice_fractions)
 
rows = []
pixels =  list(im.getdata())

for x in range(0,im_width*im_height,im_width):
	rows.append(pixels[x:x+im_width])
	
 # make rows


# if we want to slice other dirciont first just
slices = []

# slice it up
for x in range(0,im_width,slice_width):# | ### | ### |  ### | ###
	slices.append(rows[x:x+slice_width])
	# for y in range(x,x+slice_width):# | #, #, # |
odds = [x for index, x in enumerate(slices) if index%2==1]
evens = [x for index, x in enumerate(slices) if index%2==0]
compressed = odds+evens


squashed = list(chain(*list(chain(*compressed))))
im2 = Image.new("RGB",(im_width,im_height))
im2.putdata(squashed)
im2.save("shrine_hd.jpg")
