'''
Program: Neighbours
Author: L_Veitch
Date: 25/03/25

Simple Python script which uses imported class to create a random 2D array and finds the
neighbouring points within a user defined distance of a random origin point and plots the
results in a scatter plot.
'''
import random
import points_class
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#creating data set of 100 random points within an x and y range of 100
def point_generator():
	points = [points_class.Points(random.randint(1, 100), random.randint(1, 100)) for i in range(100)]
	return points

#identifies neighbours of origin point based on a maximum distance from origin
def neighbour_finder(origin, max_distance, points):
	neighbours_list = []
	for point in points:
		distance = origin.distance(point)
		if 0 < distance <= max_distance: #excludes self and points outside max_distance
			neighbours_list.append(point)
			print(f"p1: {origin} p2: {point} distance: {distance}")
	print(f'Number of neighbours: {len(neighbours_list)}')
	return neighbours_list


#creation and visualistion of scatter plot
def plot(points, origin, neighbours, max_distance):
	#Extracting point coordinates
	x_all = [point.x for point in points]
	y_all = [point.y for point in points]
	#Extracting neighbour coordinates
	x_neighbour = [point.x for point in neighbours]
	y_neighbour = [point.y for point in neighbours]
	#Extracting origin coordinates
	x_origin = origin.x
	y_origin = origin.y

	#scaling plot and extracting subplots for adaptation
	fig, ax = plt.subplots(figsize=(8, 8))

	#setting grid lines
	ax.set_axisbelow(True)
	ax.grid(True, linestyle = '--')

	#plot title
	ax.set_title(f"Neighbours of Origin within distance of {max_distance}", fontsize=14)
	
	#setting x and y axis lines
	ax.set_aspect('equal')
	ax.axvline(0, color = (.6, .6, .6), linestyle = '--', zorder=1)
	ax.axhline(0, color = (.6, .6, .6), linestyle = '--', zorder=1)
	
	#plotting points, neighours and origin
	ax.scatter(x_all, y_all, label = 'All Points', color='None', edgecolor = 'lightseagreen')
	ax.scatter(x_neighbour, y_neighbour, label = 'Neighbours', color='lightseagreen', edgecolor = 'tomato')
	ax.scatter(x_origin, y_origin, s = 100, label = 'Origin', color='tomato',)

	#plotting a circle to show maximum distance boundary
	circle = patches.Circle((x_origin, y_origin), radius=max_distance, 
		edgecolor="tomato", facecolor="none", linestyle="--", label="Max Distance", zorder = 2)
	ax.add_patch(circle)

	#adding plot legend 
	ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=8)
	plt.subplots_adjust(right=0.8)
	
	#displaying plot
	plt.show()

#main script execution
def main():
	#generating data set
	points = point_generator()
	
	#selection of random origin point from point set
	origin = random.choice(points)
	
	#user input for maximum distance including error handling
	while True:
		try:
			neighbour_distance = int(input("Please enter a catchment radius for neighbouring points: "))
			if neighbour_distance <= 0:
				print("Please enter a positive number.")
			else:
				break
		except ValueError:
			print("Invalid input. Please enter a number.")
	
	#finding neighbours
	neighbours = neighbour_finder(origin, neighbour_distance, points)

	#plotting chart
	plot(points, origin, neighbours, neighbour_distance)

if __name__ == '__main__':
	main()

