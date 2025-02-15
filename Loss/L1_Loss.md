# L1 Loss

## Table of Contents
1. [What is L1 Loss](#what-is-l1-loss)
   - [Key Properties of L1 Loss](#key-properties-of-l1-loss)  
   - [How does L1 Loss Work (Mathematically)](#how-does-l1-loss-works-mathematical-example)
2. [Features of L1 Loss](#features-of-l1-loss)
   - [1. Robust to outliers](#l1-regularization-lasso)
   - [2. Pushes Weights to 0 (L1 Loss has Constant Gradient, unlike Smooth Gradient in L2)](#2-pushes-weights-to-0-l1-loss-has-constant-gradient-unlike-smooth-gradient-in-l2)
   - [3. Encourages Sparsity)](#3-encourages-sparsity)



## What is L1 Loss

L1 Loss, also called Mean Absolute Error (MAE), is a type of loss function that calculates the absolute difference between the predicted and actual values.

        L1_Loss = (1/n) * Σ | y_i - ŷ_i |

Where:

y_i = Actual value (ground truth)  
ŷ_i= Predicted value  
n = Total number of data points

### Key Properties of L1 Loss

* Measures absolute error (instead of squared error like L2).
* Penalizes large errors linearly (instead of quadratically like L2).
* Robust to outliers (does not square the error, making it less sensitive to extreme values).

---

### How does L1 Loss Works (Mathematical Example)

L1 loss calculates the absolute difference between each predicted and actual value and averages them over all data points.

**Example Calculation**  
Given a dataset with actual values:

    y_actual = [10, 20, 30, 40, 50]

And model predictions:

    y_predicted = [12, 18, 29, 42, 47]

Step 1: Compute Absolute Errors


    ∣10−12∣=2
    ∣20−18∣=2
    ∣30−29∣=1
    ∣40−42∣=2
    ∣50−47∣=3
    

Step 2: Compute Mean Absolute Error (L1 Loss)

L1_Loss = (2+2+1+2+3) / 5 = 10/5 = 2  

📌 Result: The L1 Loss for this example is 2.0.

---


## Features of L1 Loss:

## 1. Robust to outliers

A model is robust to outliers if it does not get heavily influenced by extreme values. This means: 

* A single outlier does not dominate the model’s predictions.
* The model remains stable even with noisy data.

### How L1 Loss Achieves This

* L1 Loss treats all errors equally (linearly):
    * L1 Loss penalizes all errors at the same rate, whether small or large.
    * Unlike L2 Loss (MSE), which squares the errors, making large errors (outliers) contribute much more to the loss.

* Mathematical Explaination
    * Suppose we have an outlier point where y = 1000 and our prediction ŷ = 10.

    * L1 Loss : |1000-10| = 990
    * L2 Loss : (1000-10)^2 = 980100

    * The outlier contributes 990 to L1 Loss but 980100 to L2 Loss, showing how L2 Loss is heavily dominated by outliers, while L1 Loss remains stable.
    * L1 Loss does not exaggerate the impact of large errors, meaning it does not let outliers dominate the learning process.
    * L2 Loss is highly sensitive to outliers, because squared errors make large differences much larger.

### When is L1 Loss Used:
* L1 Loss is preferred when data contains outliers, such as:

    * Real-world financial data (stock prices)
    * Sensor readings (which can have occasional misreadings)
    * Medical data (some extreme values can exist in patient vitals)


## 2. Pushes Weights to 0 (L1 Loss has Constant Gradient, unlike Smooth Gradient in L2)

The key property of L1 regularization is that its gradient is constant (±λ), unlike L2 regularization (which has a smooth gradient).

The gradient of L1 regularization is ±λ, which leads to small weights being completely eliminated over time.

Unlike L2 Regularization (Ridge), which only shrinks weights but never makes them exactly zero, L1 removes features entirely.

Gradient of L1 Regularization

                [ 1,  if w > 0
     ​d/dw |w| = [ -1, if w < 0
                [ 0,  if w = 0  

This means:

* For small weights, the gradient is always pushing them towards zero.
* If w is small enough, it will be driven completely to zero.


Gradient of L2 Regularization

    d/dw |w| = 2w


This means:

* The shrinkage effect is proportional to the weight size.
* Smaller weights shrink slower, so they never become exactly zero.

## 3. Encourages Sparsity

### What is Sparsity?

A model is sparse if many of its parameters (weights) are exactly zero. This makes the model:

* More interpretable (fewer parameters to analyze).
* Faster to compute (fewer active weights).
* Less prone to overfitting (fewer unnecessary connections).

L1 Loss pushes many weights to exactly zero, meaning it removes unnecessary parameters.

L2 Loss only shrinks weights but never eliminates them, meaning all parameters remain in the model.

This makes L1 ideal for feature selection in high-dimensional models.

### L1 Regularization is used when:

* We want sparse models (e.g., text classification, genetics).
* We need automatic feature selection (removes unimportant variables).
* The dataset is high-dimensional with many irrelevant features.
