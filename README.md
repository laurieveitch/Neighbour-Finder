# Neighbour-Finder
*Simple Python project for finding neighbours of a point in a 2D array.*

### Description
This project is a simple exercise in some coding techniques such as a Object Oriented Programming, plotting, importing and slightly complex conditional statements. I initially completed a similar project in a Comp Science Masters course but decided to come back to it to add some extra features and refine its implementation a bit.

The program creates a set of 100 random points for use as its data set. I've restricted them to be within 1-100 on both the x axis and y axis. The **point_generator** uses an imported **Point** class to give the points there x and y characteristics as well as some additional methods, like distance finder between points and a string output to print a given points coordinates.

Once the point set is created the **neighbour_finder** function takes an origin point and goes through each point on the list- if a point is within the maxiumum specified distance then that point is added to the **neighbours_list** of the origin point. This list is then printed in the out programme output along with the total number of neighbours for the given origin point.

<img width="564" alt="neighbour_finder_output" src="https://github.com/user-attachments/assets/256c8e68-185e-423d-a718-3e7b7b27cceb" />

In my implementation I chose to use a random point from the random point 2D Array as the origin point. This gives a new starting point each time the program is run. If you're trying out this program it may be useful to set a ficed origin point until you've got the program running as expected, so that you can have verifiable and repeatable results. Also, my implementation takes a user input for the **max_distance** of neighbours, but you may want to set a fixed distance. 

Once the neighbours have been found a scatter plot is created using some features of **matplotlib**. I've adapted the standard outputs of the graph so that non-neighbours, neighbours and the origin are distinct and added a dotted circle to show the maximum distance boundary.

<img width="742" alt="neighbour_finder_plot" src="https://github.com/user-attachments/assets/ca6e373e-ab91-46a7-b446-3b468e7f175f" />


The **main** function contains the implementation of the programme including the user input section with some error handling to avoid crashing and to aid the user with functionality.

### Dependencies
* math
* random
* matplotlib

### Author

laurenceveitch@gmail.com
