"""
Reusable SimpleLinearRegression class trained with gradient descent.
Intended for educational demos and small, 1D problems.
"""
from __future__ import annotations
from typing import Iterable, Union
import numpy as np
import matplotlib.pyplot as plt

ArrayLike = Union[np.ndarray, Iterable[float], float]


class SimpleLinearRegression:
    """
    Minimal linear regression (y = m x + b) trained with gradient descent
    to minimize mean squared error.

    Parameters
    ----------
    learning_rate : float
        Step size for gradient descent updates.
    iterations : int
        Number of gradient descent steps.
    """

    def __init__(self, learning_rate: float = 0.01, iterations: int = 1000) -> None:
        self.learning_rate = float(learning_rate)
        self.iterations = int(iterations)
        self.m: float = 0.0  # slope
        self.b: float = 0.0  # intercept

    def fit(self, X: ArrayLike, Y: ArrayLike) -> None:
        """Fit parameters m and b using gradient descent."""
        X_arr = np.asarray(X).reshape(-1)
        Y_arr = np.asarray(Y).reshape(-1)
        n = len(X_arr)
        if n == 0:
            raise ValueError("Empty training data.")

        for _ in range(self.iterations):
            # Predictions for current parameters
            y_hat = self.m * X_arr + self.b
            # Gradients of MSE wrt m and b
            dm = (-2.0 / n) * np.sum(X_arr * (Y_arr - y_hat))
            db = (-2.0 / n) * np.sum(Y_arr - y_hat)
            # Update step
            self.m -= self.learning_rate * dm
            self.b -= self.learning_rate * db

    def predict(self, X: ArrayLike) -> np.ndarray:
        X_arr = np.asarray(X)
        return self.m * X_arr + self.b

    def plot_regression_line(self, X: ArrayLike, Y: ArrayLike) -> None:
        """Scatter raw data and plot the fitted line."""
        X_arr = np.asarray(X).reshape(-1)
        Y_arr = np.asarray(Y).reshape(-1)
        Y_pred = self.predict(X_arr)

        plt.scatter(X_arr, Y_arr, color="blue", label="Actual data")
        plt.plot(X_arr, Y_pred, color="red", label="Fitted line")
        plt.title("Linear Regression Using Gradient Descent")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.show()
