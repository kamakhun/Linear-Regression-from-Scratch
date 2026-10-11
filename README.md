# Linear-Regression-from-Scratch
machine learning project implementing linear regression with gradient descent using pure Python.

Overview

The goal of this project is to understand the fundamentals of linear regression and gradient descent by implementing the algorithm from scratch rather than relying on ready-made machine learning libraries.

The model learns a linear relationship between input values and target values by iteratively updating its parameters.

Model

The prediction function is:

[
\hat{y} = wx + b
]

Where:

(x) — input feature

(\hat{y}) — predicted value

(w) — weight (slope)

(b) — bias (intercept)

Loss Function

Model performance is evaluated using Mean Squared Error (MSE):

[
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
]

The objective is to minimize MSE by updating the model parameters with gradient descent.

Gradient Descent

At each iteration, the gradients of the loss function with respect to the weight and bias are calculated. The parameters are then updated using the learning rate.

The learning rate controls the size of each update and affects how quickly the model converges.

Experiments

This project explores how different learning rates affect the training process.

Planned experiments:

Compare different learning rates.

Observe how MSE changes over training epochs.

Investigate convergence and divergence.

Compare the learned parameters with an analytical solution.

Technologies

Python

Basic calculus and linear algebra

Current Status

The basic linear regression model and gradient descent algorithm have been implemented.

The project is currently focused on understanding optimization and experimenting with learning rates.

Future Improvements

Plot MSE over training epochs.

Compare learning rates systematically.

Test the model on different datasets.

Compare gradient descent with an analytical solution.

Improve code organization and documentation.

What I Am Learning

This project is part of my journey into machine learning, with a focus on understanding the mathematics behind ML algorithms and implementing them from first principles.
