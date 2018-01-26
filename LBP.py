import cv2
import numpy as np
from matplotlib import pyplot as plt

#to compare after
from skimage import feature

class LBP:
	def __init__(self, input):
		 # Read the image and convert to grayscale
		self.image = cv2.imread(input, 0)

		# a copy of the image to transform
		self.transformed_img = cv2.imread(input, 0)

		# get size informations		
		self.height = len(self.image)
		self.width = len(self.image[0])			

	def execute(self):				
		#Run a example of LBP
		#self.example()

		# We create a matrix with zeros that it will be replaced with 1 or 0.
		# We compare value of pixel[line,column] with values of its neighbours.
		# When neighbour >= center we replace with 1, otherwise 0.	
		# This procedure is done by _thresholded method
		img_lbp = np.zeros((self.height, self.width, 3), np.uint8)		
		
		# for each pixel we will find its LBP
		for line in range(self.height):			
			for column in range(self.width):				
		 		img_lbp[line, column] = self._calculateLBP(self.image, column, line)			
				
		self._histogram(self.image, self.transformed_img, "Result from algorithm developed")	
		self._displayImages(self.transformed_img, "Result from algorithm developed")	

	def example(self):
		'''
		Run a example how to calculate LBP
		'''
		# We have a matrix with pixels
		pixels = np.matrix([[6,5,2],[7,6,1],[9,3,7]])

		# We create a matrix with zeros that it will be replaced with 1 or 0.
		# We compare value of pixel[1,1] (center) with values of its neighbours.
		# When neighbour >= center we replace with 1, otherwise 0.	
		# This procedure is done by _thresholded method
		zero_matrix = np.zeros((3,3), np.uint8)
					
		# Get the values from matrixes
		line = 1
		column = 1
		center        = pixels[line,column]
			
		positions = self._get_positions(pixels, line, column)

		# We check each value and replace with 1 or 0		
		values = self._thresholded(center, positions)

		# Mask with the weights
		'''
	     1  | 2  | 4
	    ----------------
	     8  | 0  | 16
	    ----------------
	     32 | 64 | 128
	    ''' 	    
		weights = [1, 2, 4, 8, 16, 32, 64, 128]
		
		print("\nbit values")		
		for i in range(0, len(values)):
		 	print("For '{}' the bit value is '{}'".format(positions[i], values[i]))			

		print("\nValues for each pixel")
		lbp = 0
		for i in range(0, len(values)):
			lbp_temp = values[i]*weights[i]
			lbp+=lbp_temp
			print("For '{}' the LBP is '{}'".format(values[i], lbp_temp))						
	
		print("\nLBP={}".format(lbp))
								
	def _displayImages(self, transformed_img, title):		
		plt.figure()
		plt.axis("off")
		plt.title(title)
		plt.imshow(transformed_img, cmap='gray')
		plt.show()
		
	def _calculateLBP(self, pixel, column, line):		
	    # Now we want to get LBP for pixel[line,column].
		# we compare grey level value of pixel[line,column] with values of its neighbours
		# starting at the top-left pixel and moving clockwise
		values = self._thresholded(pixel[line,column], self._get_positions(pixel, column, line))

		# Mask with the weights
		weights = [1, 2, 4, 8, 16, 32, 64, 128]

		lbp = 0
		for i in range(0, len(values)):
			lbp += values[i]*weights[i]

		#Transform the image with the new value
		self.transformed_img.itemset((line,column), lbp)

		return lbp
	
	def _get_positions(self, pixels, column, line):
		top_left      = self._get_pixel_value(pixels,line-1, column-1)
		top_up        = self._get_pixel_value(pixels,line-1, column)
		top_right     = self._get_pixel_value(pixels,line-1, column+1)
		right         = self._get_pixel_value(pixels,line, column+1)
		left          = self._get_pixel_value(pixels,line, column-1)
		bottom_left   = self._get_pixel_value(pixels,line+1, column-1)
		bottom_down   = self._get_pixel_value(pixels,line+1, column)
		bottom_right  = self._get_pixel_value(pixels,line+1, column+1)

		positions = [top_left, top_up, top_right, left, right, bottom_left, bottom_down, bottom_right]

		return positions

	def _thresholded(self, center, neighbours):
		#we compare grey level value of pixel[x,y] (center) with values of its neighbours
	    result = []
	    for neighbour in neighbours:
	        if neighbour >= center:
	            result.append(1)
	        else:
	            result.append(0)
	    return result

	def _get_pixel_value(self, pixel, line, column, default=0):
		# if the index does not exist return 0 
		# Workaround to create a 'border'
		try:
			return pixel[line,column]
		except IndexError:					
			return default

	def _histogram(self, img, transformed_img, title):					
		hist,bins = np.histogram(img.flatten(),256,[0,256])

		#cumsum -> Return the cumulative sum of the elements along a given axis.
		#CDF: cumulative distribution function
		cdf = hist.cumsum()		
		cdf_normalized = cdf * hist.max()/ cdf.max()

		plt.plot(cdf_normalized, color = 'b')
		plt.hist(transformed_img.flatten(),256,[0,256], color = 'r')
		plt.xlim([0,256])
		plt.title(title)
		plt.legend(('Cumulative Distribution Function (CDF)','Histogram'), loc = 'upper left')
		plt.show()

		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def compare(self):
		# compute the Local Binary Pattern representation
		# of the image, and then use the LBP representation
		# to build the histogram of patterns
		numPoints = 8
		radius = 1
		lbp = feature.local_binary_pattern(self.image, numPoints, radius, method="default")		

		self._histogram(self.image, lbp, "Result from scikit-image")
self._displayImages(lbp, "Result from scikit-image")
