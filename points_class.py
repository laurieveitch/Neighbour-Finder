'''
Program: points_class
Author: L_Veitch
Date: 25/03/25

Simple class data type used to create 2D points. Includes methods to calculate distance for one
point to another and to return the points own coordinates as a user readable string.
'''

import math

class Points:
	#initialising point with x and y coordinates
	def __init__(self, x, y):
		self.x = x
		self.y = y

	#calculates distance from self point to another
	def distance (self, point):
		dist = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
		return dist

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	#returns string of points x and y coordinates
	def __str__(self):
		return f'x: {self.x} y: {self.y}'
