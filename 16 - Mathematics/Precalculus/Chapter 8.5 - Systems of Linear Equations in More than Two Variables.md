# Methods

For these types of systems, you can use either the method of substitution or method of elimination. The method of elimination is typically shorter and more straightforward. It also leads to the matrix technique.


## Example 1 

$$
\begin{cases}
x-2y+3z=4 \\
2x+y-4z=3 \\
-3x+4y-z=-2
\end{cases}
$$

> [!answer]- Answer
> ![[Pasted image 20260520111408.png]]

# Matrices

Any system of three linear equations in three variables has either a unique solution, an infinite number of solutions, or no solution. 

If we look at how we solved Example 1, we see that the symbols used for the variables don't matter.  The coefficients of the variables are what we have to consider. Thus, if different symbols are used, the solution is the same.

It is easier then to simplify this process. We introduce a scheme for keeping track of the coefficients in such a way that we do not have to write down the variables.  We check that the coefficients are in the same order in each equation and that the terms not involving variables are to the right of the equal signs. We then list the numbers as follows:

$$
\begin{bmatrix}
1 & -2&3&4\\ \\
2&1&-4&3 \\ \\
-3&4&-1&-2 \\
\end{bmatrix}
$$

You may (or not) be surprised to learn that an array of numbers of this type is called a matrix. The rows of the matrix are the numbers that appear next to each other horizontally:

First row shall be $R_1$, second shall be $R_{2}$, third shall be $R_3$ and so on. The columns are thus the vertical slices of numbers, $C_1$, $C_2$, $C_3$.