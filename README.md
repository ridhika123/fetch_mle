# Fetch Rewards Coding Assessment - Machine Learning Engineer

## Goal
The objective of this challenge is to write a program that calculates pixel coordinate values for an image that is to be displayed on a two dimensional surface given the dimensions of the image and the corner points of the image as it is to be displayed.

## File description
* [app.py](app.py): Contains the python code for the flask application, includes pre and post conditions for the program
* [index.html](index.html): Contains html form that is used for POST request
* [Dockerfile](Dockerfile): xx
* [requirements.txt](requirements.txt): xx

# Requirements 
* Install Docker desktop and make sure you are logged in  

## How to Run the Flask App 
### Using Docker Build
### Using Docker Pull
* Run the following command in terminal to pull image
```docker pull ridhika/flask_calculating_coordinates ```
* Next, run the following code which will display the images in directory
```docker images```
* Run the following command after replacing the <Image ID> with the Image ID associated with repository ridhika/flask_calculating_coordinates 
```docker run -p 5000:5000 <Image ID>```
* Ctrl+Click on the link that pops up in terminal, this will open a web page, which is the Flask app.
* 
