# Exploring Lagrange and Piecewise Linear Interpolation Techniques

## Project Description

This project investigates two interpolation techniques: **Lagrange interpolation** and **piecewise linear interpolation**. Using the function \( f(x) = e^{-x^2} \) and the error function \( \text{erf}(x) \), we explore how the number and placement of interpolation nodes affect the accuracy of approximation.

The goal is to study interpolation methods, evaluate their accuracy, and understand their practical applications, including the approximation of the error function.

---

## Tasks Completed

1. **Implementation of the Lagrange Basis Polynomial**:
   - Developed the function `l_i(i, x, x_nodes)`, which calculates the \( i \)-th Lagrange basis polynomial.

2. **Lagrange Interpolation Polynomial**:
   - Implemented the function `L(x, x_nodes, y_nodes)` to compute the Lagrange interpolation polynomial.

3. **Interpolation Analysis**:
   - Plotted graphs of the original function and the Lagrange interpolation polynomial for uniformly spaced nodes.
   - Investigated the approximation error in \( L_\infty \)-space as the number of nodes increases.

4. **Optimal Node Placement**:
   - Performed the same analysis for optimally placed nodes (Chebyshev nodes).

5. **Piecewise Linear Interpolation**:
   - Conducted an error analysis for piecewise linear interpolation.
   - Compared error dependencies in \( L_\infty \)-space for all three interpolation methods.

6. **Error Function \( \text{erf}(x) \)**:
   - Calculated \( \text{erf}(x) \) at \( x = 2 \) using piecewise linear interpolation with varying numbers of nodes (\( n = 3, 5, 7, 9 \)).
   - Compared the results for different node counts.

---

## Technologies Used

- **Programming Language**: Python  
- **Libraries**:
  - `numpy` — for numerical computations.
  - `matplotlib` — for plotting graphs.
  - `scipy` — for working with the error function and integrals.

---

## Results

1. **Uniformly Spaced Nodes**:
   - Increasing the number of nodes improves interpolation accuracy.
   - However, oscillations near the boundaries of the interval (Runge’s phenomenon) introduce approximation errors.

2. **Optimally Placed Nodes (Chebyshev Nodes)**:
   - Chebyshev nodes significantly reduce interpolation errors.
   - Oscillations at the interval boundaries are minimized.

3. **Piecewise Linear Interpolation**:
   - Offers high approximation accuracy with relatively few nodes.
   - Efficient for approximating the error function \( \text{erf}(x) \).

4. **Error Function \( \text{erf}(x) \)**:
   - Piecewise linear interpolation provides increasingly accurate results as the number of nodes increases.

---

## Conclusion

The project explored three interpolation approaches:
- Global Lagrange interpolation with uniformly spaced nodes.
- Global Lagrange interpolation with optimally placed (Chebyshev) nodes.
- Local piecewise linear interpolation.

Key insights:
- Boundary oscillations in uniform node placement can be resolved using Chebyshev nodes.
- Piecewise linear interpolation is a balanced approach, offering high accuracy with minimal complexity.



