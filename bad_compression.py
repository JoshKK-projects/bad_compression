from PIL import Image
from itertools import chain
from Tkinter import Tk
from tkFileDialog import askopenfilename
import bad_compression
# https://imgur.com/gallery/Sgg0j
# rotate goes counter clockwise because of course
Tk().withdraw()
file_path = askopenfilename()
filename = file_path.split('/')[-1]
dir = file_path.split('/')[0:-1]

def image_work(filename):	
	# print "Choose an operation"
	output_file_name = raw_input("Output file name: ")

	quad_slice(filename,output_file_name)

def hort_slice(filename,output_name):
	im = Image.open(filename)
	im_width, im_height = im.size
	slice_fractions = 20
	slice_width = (im_width / slice_fractions)

	pixels =  list(im.getdata())

	rows = []

	for x in range(0,im_width*im_height,im_width):
		rows.append(pixels[x:x+im_width])
	
	slices = []
	# # slice it up
	for x in range(0,im_width,slice_width):# | ### | ### |  ### | ###
		slices.append(rows[x:x+slice_width])

	odds = [x for index, x in enumerate(slices) if index%2==1]
	evens = [x for index, x in enumerate(slices) if index%2==0]
	compressed = odds+evens

	squashed = list(chain(*list(chain(*compressed))))
	im2 = Image.new("RGB",(im_width,im_height))

	im2.putdata(squashed)
	im2.save(output_name)
	return output_name

def quad_slice(filename,output_file_name):
	hort_sliced = hort_slice(filename,'hort_sliced.jpg')
	hort_altered = Image.open(hort_sliced).rotate(90).save(hort_sliced)
	quad_sliced = hort_slice(hort_sliced,output_file_name + '.jpg')
	Image.open(quad_sliced).rotate(-90).save(quad_sliced)
	final = Image.open(quad_sliced)
	# final.show()

image_work(filename)
