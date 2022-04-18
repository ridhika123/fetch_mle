#######################################################################################
# Calculating Coordinates: Fetch Rewards 
#######################################################################################

##### Pre-conditions #####
# User enters inputs for image dimension and corner points as defined below
# Image Dimension: 
#   The input for image dimensions must be a tuple (m,n) such that m and n are integers >= 2
#   m is the number of rows in the image and n is the number of columns in the image
# Corner Points:
#   The input for corner points must be a list of four two-element tuples
#   Each tuple must be (x,y), where x is the x-coordinate and y is the y-coordinate of any corner points of the image/rectangle
#   The coordinates mapped by the four tuples must form a rectangle parallel to the x and y axis
##### Post-conditions #####
# Returns m x n x 2 matrix, where m is the number of rows in the input image and n is the number of columns in the input image
# The matrix is ordered such that the each list 

from flask import Flask, request, render_template
import numpy as np 

app = Flask(__name__)
port = 5000

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/solution', methods = ["POST"])
def solution():
    if request.method == "POST":
        
        # Reading in the image dimensions and corner points
        image_dimensions_input = request.form['dimensions']
        corner_points_input = request.form['corner_points']

        # Converting image dimension string to tuple
        image_dimensions = tuple(map(int, image_dimensions_input[1:-1].split(", ")))
        # Converting corner points string to list of tuples
        corner_points_inter = corner_points_input[2:-2].split("), (")
        corner_points = []
        for point in corner_points_inter:
            corner_points.append(tuple(map(float, point.split(", "))))

        # Creating arrays of equally-spaced points on x-axis and y-axis
        lowest_point = min(corner_points)
        highest_point= max(corner_points)        
        x_points= np.linspace(lowest_point[0], highest_point[0], image_dimensions[1])
        y_points= np.linspace(lowest_point[1], highest_point[1], image_dimensions[0])

        # Populating solution_matrix in order from top left to bottom right
        solution_matrix = np.zeros([image_dimensions[0], image_dimensions[1], 2])
        for i in range(image_dimensions[0]): 
            for j in range(image_dimensions[1]): 
                solution_matrix[i, j, 0] = x_points[j]
                solution_matrix[i, j, 1] = y_points[-(i+1)]
        
        # Return error message if inputs don't meet pre-conditions
        if (image_dimensions[0] <= 1) or (image_dimensions[1] <= 1):
            return "Please enter valid values."
        else:
            return f"The solution matrix is: {solution_matrix}"
    else:
        return "error"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = port)