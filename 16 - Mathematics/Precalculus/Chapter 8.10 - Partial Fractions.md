Systems of equations can be used to help decompose rational expressions into sums of simpler expressions.

We may verify that

$$
\frac{2}{x^2-1}=\frac{1}{x-1}+ -\frac{1}{x+1}
$$

by adding the fractions back together.

![[Pasted image 20260520113426.png]]

It is theoretically possible to write any rational expression as a sum of rational expressions whose denominators involve powers of polynomials of degree not greater than two.

Specifically, if $f(x)$ and $g(x)$ are polynomials and the degree of $f(x)$ is less than the degree of $g(x)$, it can be proved that:

$$
\frac{f(x)}{g(x)}=F_{1}+F_{2}+\dots+F_{r}
$$
such that each $F_k$ has one of the forms

$$
\frac{A}{(px+q)^m} or \frac{Ax+B}{(ax^2+bx+c)^n}
$$

where $A$ and $B$ are real numbers, $m$ and $n$ are nonnegative integers, and the quadratic polynomial $ax^2+bx+c$ is irreducible over all real numbers. 

The sum of $F_{1}+F_{2}+\dots+F_{r}$ is the partial fraction decomposition of f(x)/g(x), and each $F_k$ is a partial fraction.

For the partial fraction decomposition to be found, it is essential that f(x) has a lower degree than g(x). If this is not the case, we can use long division to obtain such an expression.

For example, if we have

$$
\frac{x^3-6x^2+5x-3}{x^2-1}
$$

We can obtain:

