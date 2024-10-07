# Linear Regression
### Version 1.0
## Description
This project is an implementation of a linear regression model designed to predict the price of a car based on its mileage. The program uses gradient descent to train the model and supports several functionalities, including model training, accuracy evaluation, and graphical representation of the results.
## Features
- Linear Regression Model: Trains a model to predict car prices based on mileage using gradient descent.
- Accuracy Evaluation: Calculates the accuracy of the model after training.
- Graphical Visualization: Displays a graph of the linear regression model alongside the training data.
- Automatic Learning Rate Adjustment: Increases the learning rate to find the most precise model.
## Files and Functionalities
- learning.py: Trains the linear regression model using a dataset file.
- estimate.py: Asks for a mileage input and returns an estimated price based on the trained model.
- accuracy.py: Computes the accuracy of the model by outputting a value representing its precision.
- graph.py: Provides a visual representation of the model, plotting the training data and regression line.
- motherlord.py: Trains the model by incrementing the learning rate to optimize precision.
## Installation and Usage
### To Install:
Clone the repository:
```
git clone git@github.com:Maeltarh/Linear-Regression.git
```
Navigate to the project directory:
```
cd Linear-Regression
```
### Usage Example
To estimate a car price based on mileage, first run the learning program:
```
python3 learning.py
```
Then, to estimate a price:
```
python3 estimate.py
```
The program will prompt you for a mileage value and then output the estimated car price.
## Requirements
Recent version of python 3
### Libraries:
- json: For handling JSON data.
- pandas: For data manipulation and analysis.
- matplotlib: For data visualization.
- numpy: For numerical operations.
- subprocess: For managing system processes.
You can install these libraries using:
```
pip install json pandas matplotlib numpy subprocess
```
Or:
```
python3 -m pip install json pandas matplotlib numpy subprocess
```
