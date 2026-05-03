# Math behind filters
## Divergence
The divergence of a vector field $\mathbf{F} = (F_x, F_y, F_z)$ is defined as:
$$\nabla \cdot \mathbf{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}$$
This measures the rate at which the vector field is expanding or contracting at a given point.

- $\nabla \cdot \mathbf{F} > 0$ indicates a source, where the field is diverging from that point.
- $\nabla \cdot \mathbf{F} < 0$ indicates a sink, where the field is converging towards that point.
- $\nabla \cdot \mathbf{F} = 0$ indicates a solenoidal field, where there is no net flow in or out of that point.
- A positive divergence could be seen as if every vector passing through a point is moving faster than it enters, indicating a source of the field.
- A negative divergence could be seen as if every vector passing through a point is moving slower than it enters, indicating a sink of the field.
## Laplacian
The Laplacian of a scalar field $\phi$ is defined as:
$$\nabla^2 \phi = \nabla \cdot (\nabla \phi)$$
$$\nabla^2 \phi = \frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} + \frac{\partial^2 \phi}{\partial z^2}$$
This measures the rate at which the average value of $\phi$ around a point differs from the value of $\phi$ at that point.
- If $\nabla^2 \phi > 0$, it indicates that the value of $\phi$ at that point is less than the average value around it, suggesting a local minimum.
- If $\nabla^2 \phi < 0$, it indicates that the value of $\phi$ at that point is greater than the average value around it, suggesting a local maximum.
- If $\nabla^2 \phi = 0$, it indicates that the value of $\phi$ at that point is equal to the average value around it, suggesting a saddle point or a flat region.

Laplacian can be thought as the sum of the second derivatives, which gives us an idea if the function is convex or concave at that point. A positive Laplacian indicates a convex shape, while a negative Laplacian indicates a concave shape.

It is also defined as the divergence of the gradient of a scalar field, which can be interpreted as the net flow of the gradient field at a point.