# Fetch Rewards Coding Assessment - Machine Learning Engineer

## Goal
The objective of this challenge is to write a program that calculates pixel coordinate values for an image that is to be displayed on a two dimensional surface given the dimensions of the image and the corner points of the image as it is to be displayed.

## File descriptions
* [app.py](app.py): Contains the python code for the flask application, includes pre and post conditions for the program
* [index.html](index.html): Contains html form that is used for POST request
* [Dockerfile](Dockerfile): Contains all the commands to be called on the command line to assemble the image
* [requirements.txt](requirements.txt): Contains the all the libraries, modules, and packages  used while developing this project
* [test.py](test.py): Contains tests for the functions and setup of the application

## Requirements 
* Install python and pip 
* To view/edit the files once downloaded, download visual studio code (or equivalent)

## How to Run the Flask App 

### Using Docker Build
* Create a folder on your desktop called "calculating_coordinates"
* Download and save [app.py](app.py), [Dockerfile](Dockerfile) and [requirements.txt](requirements.txt) into "calculating_coordinates" folder
* Create another folder called "templates" inside the "calculating_coordinates" folder
* Download and save [index.html](index.html) in "templates"
* Now, open a terminal window and change directory to be in the "calculating_coordinates" folder
* Next, run command ```docker build -t flask_calculating_coordinates .``` 
* Finally, run ```docker run -p 5000:5000 flask_calculating_coordinates``` 
* Ctrl+Click on the first link that pops up in terminal, this will open a web page, which is the Flask app

### Using Docker Pull
* Run the following command in terminal to pull image ```docker pull ridhika/flask_calculating_coordinates ```
* Next, run the following code which will display the images in directory ```docker images```
* Run the following command after replacing the <Image ID> with the Image ID associated with repository ridhika/flask_calculating_coordinates  ```docker run -p 5000:5000 <Image ID>```
* Ctrl+Click on the first link that pops up in terminal, this will open a web page, which is the Flask app
  
### How to Stop the Container
* In terminal, run ```docker ps``` and copy the Container ID corresponding to the relevant image
* Paste the Container ID in place of <Container ID> and run the command ```docker stop <Container ID>```
* Now, if you visit the link (http://127.0.0.1:5000/), it will display an error
  
## Testing
The unit tests are contained in file [test.py](test.py). 
The application passes all the tests:
![testing_output](https://user-images.githubusercontent.com/37682124/164016982-2b7b3619-fa9a-4209-b16e-adaf1b3ba754.png)

  
