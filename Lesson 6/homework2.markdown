# Assignment: Calculating the Area of an Ellipse Using the Monte Carlo Method

## Objective
Use the Monte Carlo method to estimate the area of an ellipse and visualize the process. This assignment reinforces concepts of random sampling, geometric computations, and data visualization in Python.

## Problem Description
An ellipse centered at the origin \((0, 0)\) is defined by its semi-major axis \(a\) (along the x-axis) and semi-minor axis \(b\) (along the y-axis). The equation of the ellipse is:
\[
\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1
\]
The analytical area of the ellipse is given by:
\[
\text{Area} = \pi a b
\]
Your task is to estimate this area using the Monte Carlo method by:
1. Enclosing the ellipse in a bounding rectangle.
2. Generating random points within the rectangle.
3. Determining the fraction of points that lie inside the ellipse.
4. Using this fraction to estimate the area.

## Instructions
1. **Setup**:
   - Use Python with libraries `numpy` for random number generation and `matplotlib` for visualization.
   - Define an ellipse with semi-major axis \(a = 4\) and semi-minor axis \(b = 3\).
   - Use at least 100,000 random points for the simulation.

2. **Monte Carlo Method**:
   - Compute the bounding rectangle (dimensions are \([-a, a]\) for x and \([-b, b]\) for y).
   - Generate random points uniformly within the rectangle.
   - Check if each point \((x, y)\) satisfies the ellipse equation: \(\frac{x^2}{a^2} + \frac{y^2}{b^2} \leq 1\).
   - Estimate the area as: \(\text{Area} \approx \text{(Fraction of points inside)} \times \text{(Rectangle area)}\).
   - The rectangle area is \(4ab\).

3. **Visualization**:
   - Plot the ellipse boundary.
   - Scatter plot the random points, using different colors for points inside and outside the ellipse.
   - Display the estimated area and the analytical area (\(\pi a b\)) in the plot title or legend.

4. **Analysis**:
   - Compare the estimated area with the analytical area.
   - Experiment with different numbers of points (e.g., 1,000, 10,000, 100,000) and report how the accuracy changes.

## Requirements
- Submit a Python script or Jupyter Notebook that includes:
  - Complete, commented code implementing the Monte Carlo method.
  - A plot showing the ellipse, random points, and area estimates.
- A report:
  summarizing:
    - The estimated area for 100,000 points.
    - The analytical area.
    - Observations on how accuracy changes with the number of points.
- Ensure the code is reproducible (e.g., set a random seed).
