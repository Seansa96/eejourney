


# Example 1

$$
\int 4x[x^2+5]^3dx
$$
> [!answer]- Answer
> ![[Pasted image 20260421145232.png]]



# Symmetry in Definite Integrals

For a definite integral, when you have an even or odd function, that allows certain manipulations to become possible.

These particular identities are of note:

For an even function, where $f(-x)=f(x)$
$$
\int^{b}_{a}f(x)dx=2\int^{a}_{0}f(x)dx
$$

This is because, since the outputs (y-values) are symmetric about the y-axis, then they evaluate to the same thing, or equal each other. If two values equal each other, then we can simply find one half, and double that value to get the full integral.

For example, if you square something, it'll remove the sign. So for the even function $x^2$, $-2$ results in the same y value as $2$. So if we wanted to find $f(-2)+f(2)$, we could do both functions, or we could just do $2*f(-2)$. We would still get $4$. 

For an odd function, where $f(-x)=-f(x)$

$$
\int^{b}_{a}f(x)dx=0
$$

This is because the values instead of resulting in the same value, cancel each other out. Say you have a function $x^3$. If you do $f(-2)+f(2)$, you'll get $-8$ and $8$, which when added together cancel out.