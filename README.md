Deploying ML Model using Flask

This is a simple project to elaborate how to deploy a Machine Learning model using Flask API

Prerequisites

You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

Flask version: 0.12.2 conda install flask=0.12.2 (or) pip install Flask==0.12.2


Project Structure

This project has four major parts :

code.py - This contains code for our Machine Learning model to predict final score of the student.
app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
template - This folder contains the HTML template (index.html) to allow user to enter employee detail and displays the predicted employee salary.
static - This folder contains the css folder with style.css file which has the styling required for out index.html file.
Running the project

Ensure that you are in the project home directory. Create the machine learning model by running below command from command prompt -

python model.py

This would create a serialized version of our model into a file model.pkl

Run app.py using below command to start Flask API

python main.py

By default, flask will run on port 5000.

Navigate to URL http://127.0.0.1:5000/ (or) http://localhost:5000
You should be able to view the homepage.

Enter valid numerical values in all 5 input boxes and hit Predict.

If everything goes well, you should be able to see the predcited salary vaule on the HTML page! check the output here: http://127.0.0.1:5000/predict
