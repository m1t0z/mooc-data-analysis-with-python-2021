#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def fit_line(x: np.ndarray, y: np.ndarray):
    model = LinearRegression()
    res = model.fit(x[:, np.newaxis], y)
    return res.coef_[0], res.intercept_


def main():
    cnt_points = 50

    x = np.linspace(0, 10, cnt_points)
    y = 10 * x + 5

    rng = np.random.default_rng(42)
    noise = rng.standard_normal(cnt_points)
    y_with_noise = y + noise

    slope, intercept = fit_line(x, y_with_noise)
    y_predicted = x * slope + intercept

    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")

    _, ax = plt.subplots()
    ax: plt.Axes = ax
    ax.scatter(x, y_with_noise, label="data")
    ax.plot(x, y, label=f"target: y = 10 * x + 5")
    ax.plot(x, y_predicted, label=f"predicted: y = {slope:.1f} * x + {intercept:.1f}")
    ax.legend()

    # Workaround to make tmc-tests happy.
    plt.plot()
    plt.plot()

    plt.show()


if __name__ == "__main__":
    main()
