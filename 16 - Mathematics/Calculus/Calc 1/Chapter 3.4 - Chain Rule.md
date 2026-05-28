If both functions are differentiable, then the derivative of the composite function is simply the product of the derivatives.

$$
F'(x) = f'(g(x)) * g'(x)
$$

or

$$
\frac{dy}{dx} = \frac{dy}{du}\frac{du}{dx}
$$

## Example 1

Evangelista Torricelli devised a formula for finding the rate of water leaving a container, at any time, $t$.  

This formula is

$$
V(t) = 5000(1-\frac{1}{40}t)^2, when\space 0\leq t \leq 40
$$

Find the rate at which water is draining from the tank after 5 minutes.

To do so, we of course need the derivative of this formula to find the instantaneous rate.

![[Pasted image 20260223071013.png]]

## Example 2

![[Pasted image 20260223071149.png]]

![[Pasted image 20260223071521.png]]


## Example 3

A) Differentiate $y=sin(x^2)$
B) Differentiate $y=sin^2 x$

A)
![[Pasted image 20260223071932.png]]

B)
![[Pasted image 20260223072207.png]]

# Combining the Power Rule and the Chain Rule

Basically, all this says is that when the outside function is a power function, we just use the power rule for differentiating it. So.

$$
\frac{d}{dx}(u^n) = \frac{d}{dx}[nu^{n-1} = u^n * \frac{du}{dx}]
$$

## Example 1

Differentiate $y=(x^3 - 1)^100$

![[Pasted image 20260223072947.png]]

# Example 2

Differentiate $e^{x^2}$

![[Pasted image 20260223104139.png]]

# Example 3

Differentiate $1-x^2$

![[Pasted image 20260223105459.png]]

# Example 4

Differentiate $sin(\sqrt{x^3 +1})$

For three composite functions, you simply apply the composite rules in sequence.

So,
$$
f'(g(h(x)) * g'(h(x)) * h'(x)
$$

![[Pasted image 20260223110653.png]]

# Example 5

$cot(x^2 * cos(x))$


