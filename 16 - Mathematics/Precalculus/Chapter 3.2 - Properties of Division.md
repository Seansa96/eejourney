# Synthetic Division

You can use a strategy called synthetic division to long-divide polynomials, typically by a linear binomial of the form $x-c$, where $c$ is a real number.

Say we have

$$
\frac{x^3-2x^2-5x+6}{x-3}
$$

We draw the typically long division structure, then use the zero for the denominator, that being $x=3$, as the divisor, and the dividend is the coefficients of the polynomial kept in the same order. You then bring down the first coefficient, multiply it by the divisor, then add that product to the next coefficient, repeating the process until you have nothing left to add to.

If your remainder is zero, then the quotient is the factor. If you have a remainder, you take the quotient plus the remainder over the divisor.

![[Pasted image 20260520115511.png]]


## Example 1 - Synthetic Division

$$
\frac{2x^3+3x^2-11x-6}{x-2}
$$

> [!answer]- Answer
> ![[Pasted image 20260615210534.png]]


# Long Division

This can be used for more than just a linear denominator or linear divisor. You simply set up the polynomial like you would for normal long division. Then, bring down the leading term of the dividend, and if the divisor's leading term is a smaller degree (it should be), then multiply the divisor by whatever you need to equal the leading dividend term, and multiply that factor to the constant of the divisor as well.

After that, subtract, bring down, repeat, until there are no terms left in the original expression.
## Example 2 - Long Division

$$
\frac{x^3+2x^2-5x-6}{x^2-1}
$$

> [!answer]- Answer
> ![[Pasted image 20260615211810.png]]


