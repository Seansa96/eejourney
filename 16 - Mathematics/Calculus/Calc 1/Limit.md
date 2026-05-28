The limit of a given function is the value it approaches when given some value of x, whether or not the function actually reaches that value.

Put simply, it can be seen as:

$$
lim_{x \to 5}= x + 1
$$
where x can be any value, but as $x + 1$ approaches 6, it can be said to get closer and closer to the limit of the function. Obviously here, $5 + 1$ results in 6, the limit, which is obvious. The point of finding the limit is to find where instant behavior changes. 

It may be that 6 represents some temperature in Celsius of a solution, and we find that as it approaches 6 degrees, a reaction occurs. Thus, we know that we can get quite arbitrarily close to 6 in either way, but we never quite want to reach 6 degrees.

# Standard Notation

$$lim_{x \to a} f(x) = L$$

# One-Sided Limits

A one-sided limit can be said to be on either the left or right-hand side, denoted by a $-$ or $+$ superscript.

To evaluate a limit for the left or right hand side, generally speaking, you would want to use a value as close as possible to the general limit of the function itself.

The general limit is said to exist if both the left and right hand sides are equal to each other. If there is any discrepancy, it does not exist (referred to as DNE).

If either the left or right hand sides do not exist, then the general limit cannot exist either

# Precise Definition of a Limit

Finding the limit of anything is about testing for prediction. It's about discovering whether or not a given system or framework experiences stability at given points.

Consider a phase change of a substance.  We know that the limit exists because the left hand and right limits of that phase change converge at the freezing/melting point. What that implies is that as we apply an input, we get a predictable output around that point. This provides a measure of control, which is the usefulness of the limit itself. It's about building a model for predictable behavior, essentially.

Example Problem:

$$
\lim_{x \to 4} (2x - 3) = 5
$$
First, turn it into the form of

$$f(x) - L$$
so

$$|2x-3| - 5$$

as $2x - 3$ is the function $f(x)$ and $L$ is the limit.

then, we just need to solve the inequality for $\epsilon$

![[Pasted image 20251223165742.png]]

so we end with

$x-4 < (\epsilon / 2)$

from before, we found that according to the precise definition, $0 < |x-4| < \delta$

well, the left side of the inequality that we produced is equal to the domain here. So, that must mean $\epsilon / 2$ is equal to $\delta$.

so we can then set $$|(2x-3)-5| = |2x-8|$$
as these are equal, then using what we've learned above, we know $|x-4|$ is equivalent to $\epsilon/2$, so

![[Pasted image 20251223171250.png]]

which proves that $$
\lim_{x \to 4} (2x - 3) = 5
$$