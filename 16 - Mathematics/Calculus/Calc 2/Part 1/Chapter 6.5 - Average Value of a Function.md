To compute the average value of a function, we break the interval up into equal $n$ subintervals, each with length $\Delta x=\frac{b-a}{n}$. Then we choose points $x_{i}$  in successive subintervals and calculate the average of those numbers.

Our final expression looks something like this:

$$
\lim_{ n \to \infty } \frac{1}{b-a}\sum^{n}_{i=1}f(x^*_{i})dx
$$
# Example 1 - Find the average value of the function

Find the average value of the function $1+x^2$ on the interval $[-1,2]$.

> [!answer]- Answer
> ![[Pasted image 20260515231827.png]]

# The Mean Value Theorem of Integrals

Similar to [[4.2 - Mean Value Theorem]] for Derivatives, this simply states that if a function is continuous on a closed interval $[a,b]$, then there exists some number $c$ of the function that its area will equal the integral of the function over that interval.


## Example 2 - Find a number $c$

For the function $1+x^2$ on the interval $[-1,2]$, find a number c such that 

$$
\int^{2}_{-1}1+x dx=f(c)[-1,2]
$$


> [!answer]- Answer
> ![[Pasted image 20260516005139.png]]
