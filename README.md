# Using Linear Transformations for Derivative Calculation

When dealing with the derivative operation for polynomials, we can consider it within the framework of a vector space. This perspective allows us to apply the properties of linearity to the derivative operation. Specifically, we observe that:

$$
\frac{d}{dx} (f(x) + g(x)) = \frac{d}{dx} f(x) + \frac{d}{dx} g(x)
$$

Additionally, we recognize the linearity property when a constant $ c $ multiplies a function:
$$
\frac{d}{dx} cf(x) = c \frac{d}{dx} f(x), \quad c \in \mathbb{R}
$$

With these considerations, we can conceptualize the derivative as a linear transformation. This transformation can be represented by the following matrix:

$$
\begin{bmatrix}
0 & 1 & 0 & 0 & \ldots & 0 \\
0 & 0 & 2 & 0 & \ldots & 0 \\
0 & 0 & 0 & 3 & \ldots & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
\end{bmatrix}_{3 \times 3}
$$

This matrix will have the effect of shifting each coefficient to $\(\frac{d}{dx} x^{n-1}\)$ and multiplying it by $\(n\)$.

## Technologies Used
* Python
* NumPy
* KaTeX
* Flask
