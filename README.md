# Linear Regression from Scratch

<p align="center">
  <b>Understanding Machine Learning from First Principles</b>
  <br>
  A simple implementation of linear regression using gradient descent in pure Python.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/ML-From%20Scratch-orange" alt="Machine Learning">
  <img src="https://img.shields.io/badge/Status-Learning-success" alt="Project status">
</p>

---

## About the Project

This project is an exploration of the mathematical foundations of machine learning through code.

Instead of using ready-made ML libraries, I implemented the core components of linear regression myself to understand how a model learns from data.

**The main goals are:**
- Understand how linear regression makes predictions.
- Implement Mean Squared Error (MSE).
- Calculate gradients manually.
- Implement gradient descent.
- Investigate how the learning rate affects convergence.

## The Mathematics

### 1. The Model

Linear regression predicts an output using a linear function:

```text
ŷ = wx + b
```

| Symbol | Meaning |
|:---|:---|
| `x` | Input feature |
| `ŷ` | Predicted value |
| `w` | Weight (slope) |
| `b` | Bias (intercept) |

The model adjusts `w` and `b` to make its predictions closer to the actual values.

### 2. The Loss Function

To measure prediction error, the model uses Mean Squared Error:

```text
           n
MSE = (1/n) Σ (yᵢ - ŷᵢ)²
          i=1
```

Here, `yᵢ` is the actual value and `ŷᵢ` is the predicted value.

The objective is to minimize MSE.

### 3. Gradient Descent

Gradient descent updates the model parameters iteratively:

```text
w ← w - α · ∂MSE/∂w
b ← b - α · ∂MSE/∂b
```

Where `α` (learning rate) controls the size of each update.

- **Too small:** learning can be slow.
- **Appropriate:** the model can converge efficiently.
- **Too large:** updates can overshoot the minimum and cause divergence.

## Experiments

One of the first things I explored was how the learning rate affects training.

| Learning rate | Expected behavior |
|:---:|:---|
| `0.001` | Smaller updates, slower convergence |
| `0.01` | Larger updates, potentially faster convergence |
| `0.1` | Updates may be too large and cause divergence |

These are observations to investigate on the current dataset, not universal rules. The behavior depends on the data and the optimization problem.

## Tech Stack

- **Language:** Python
- **Approach:** Implementation from scratch
- **Core concepts:** Linear regression, MSE, derivatives, gradient descent

## Project Structure

```text
linear-regression-from-scratch/
├── README.md
└── linear_regression.py
```

## Roadmap

- [x] Implement linear predictions
- [x] Calculate Mean Squared Error
- [x] Calculate gradients for weight and bias
- [x] Implement gradient descent
- [x] Experiment with learning rates
- [ ] Plot the loss curve
- [ ] Compare different learning rates systematically
- [ ] Compare gradient descent with an analytical solution
- [ ] Test on additional datasets

## Why This Project?

I want to understand machine learning beyond simply using existing libraries. Implementing fundamental algorithms from scratch helps me connect the mathematics with the code and build a stronger foundation for studying more advanced ML topics.

---

<p align="center">
  <i>Learning machine learning one algorithm at a time.</i>
</p>
