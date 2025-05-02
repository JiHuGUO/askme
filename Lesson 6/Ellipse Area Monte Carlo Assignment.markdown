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
  - A brief report (in comments or markdown) summarizing:
    - The estimated area for 100,000 points.
    - The analytical area.
    - Observations on how accuracy changes with the number of points.
- Ensure the code is reproducible (e.g., set a random seed).

## Sample Solution
Below is a sample implementation to guide you. Your submission should be original but can follow a similar structure.

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 4  # Semi-major axis
b = 3  # Semi-minor axis
num_points = 100000
np.random.seed(42)  # For reproducibility

# Analytical area
analytical_area = np.pi * a * b

# Bounding rectangle
rect_area = 4 * a * b  # (2a) * (2b)

# Generate random points
x = np.random.uniform(-a, a, num_points)
y = np.random.uniform(-b, b, num_points)

# Check if points are inside the ellipse
inside = (x**2 / a**2) + (y**2 / b**2) <= 1

# Estimate area
fraction_inside = np.sum(inside) / num_points
estimated_area = fraction_inside * rect_area

# Print results
print(f"Estimated area: {estimated_area:.4f}")
print(f"Analytical area: {analytical_area:.4f}")
print(f"Error: {abs(estimated_area - analytical_area):.4f}")

# Visualization
plt.figure(figsize=(8, 6))
# Plot ellipse
theta = np.linspace(0, 2 * np.pi, 100)
x_ellipse = a * np.cos(theta)
y_ellipse = b * np.sin(theta)
plt.plot(x_ellipse, y_ellipse, 'k-', label='Ellipse')
# Plot points
plt.scatter(x[inside], y[inside], c='blue', s=1, alpha=0.5, label='Inside Points')
plt.scatter(x[~inside], y[~inside], c='red', s=1, alpha=0.5, label='Outside Points')
plt.gca().set_aspect('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Monte Carlo Ellipse Area Estimation\nEstimated: {estimated_area:.4f}, Analytical: {analytical_area:.4f}')
plt.legend()
plt.savefig('ellipse_area_monte_carlo.png')
plt.show()

# Experiment with different numbers of points
for n in [1000, 10000, 100000]:
    x = np.random.uniform(-a, a, n)
    y = np.random.uniform(-b, b, n)
    inside = (x**2 / a**2) + (y**2 / b**2) <= 1
    area = (np.sum(inside) / n) * rect_area
    print(f"Points: {n}, Estimated area: {area:.4f}, Error: {abs(area - analytical_area):.4f}")
```

## Submission Guidelines
- Submit your work as a `.py` file or `.ipynb` file.
- Include your name and date in the file.
- Ensure the code runs without errors and produces the required plot.
- Submit by [insert deadline] to [insert submission method].

## Grading Criteria
- **Correctness (40%)**: Code correctly implements the Monte Carlo method and produces accurate results.
- **Visualization (30%)**: Plot is clear, includes the ellipse, points, and area information.
- **Analysis (20%)**: Report discusses results and accuracy trends.
- **Code Quality (10%)**: Code is well-commented, organized, and follows Python conventions.

## Tips
- Use `np.random.seed` for reproducibility during testing, but explore results without it.
- Test with smaller numbers of points first to debug your code.
- Ensure the plot has equal aspect ratio (`plt.gca().set_aspect('equal')`) for accurate visualization.