To find the area between two curves, where on a closed interval, $f(x) > g(x)$ for all values of $x$, you can find the area simply by the the definite integral of $f(x)-g(x)$.

Or,

$$
\int^{1}_{0} |f(x)-g(x)|dx
$$


The logic behind is quite similar to earlier methods, where take the limit of a Riemann sum, such as

$$
\lim_{ n \to \infty } \sum^{n}_{i=1} |f(x_{i})-g(x_{i})| \Delta x
$$

## Example 1

Find the area of the region bounded above by $y=e^x$, bounded below by $y=x$ and bounded on the sides by $x=0$ and $x=1$.

> [!answer]- Answer
> ![[Pasted image 20260501205758.png]]


## Example 2

Find the area of the region enclosed by the parabolas $y=x^2$ and $y=2x-x^2$.

First find points of intersection to define the bounds, then follow the example above.

> [!answer]- Answer
> ![[Pasted image 20260501211137.png]]


## Example 3

Find the approximate area of the region bounded by the curves $y=\frac{x}{\sqrt{ x^2+1 }}$ and $y=x^4-x$.

> [!answer]- Answer
> ![[Pasted image 20260508161240.png]]


# Integrating with respect to y

Some regions are best treated by regarding $x$ as a function of $y$.  If a region is bounded by curves with equations $x=f(y)$, $x=g(y)$, where $y=c$, $y=d$, where $f$ and $y$ are continuous and for $c \leq y \leq d$, and $f(y) \geq g(y)$, then its area is

$$
A= \int^{d}_{c} |f(y)-g(y)|dy
$$


If we write $x_r$ for the right boundary, and $x_L$ for the left boundary, then we have

$$
A=\int^{d}_{c}(x_{R}-x_{L})dy
$$

## Example 1

Find the area enclosed by the line $y=x-1$ and the parabola $y^2=2x+6$.

> [!answer]- Answer
> ![[Pasted image 20260502005118.png]]


## Example 2

Find the area of the region bounded by the curves $y=sin(x)$, $y=cos(x)$, $x=0$, and $x=\pi/2$.

> [!answer]- Answer
> 



