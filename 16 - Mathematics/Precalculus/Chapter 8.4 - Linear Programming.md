---
~
---
If a system of inequalities contains only linear inequalities of the form:

$$
ax+by \leq c
$$
or

$$
ax+by \geq c
$$

where $a$, $b$, and $c$ are real numbers, then the graph of the system may be a region $R$ in the $xy$-plane bounded by a polygon, possibly of the type: insert here.

For problems in linear programming, we consider such systems together with an expression of the form:

$$
C+Ax+By+K
$$

where $A$, $B$, and $K$ are real numbers, and ($x,y$) is a point in $R$. Since for each $(x,y)$ we obtain a specific value for $C$, we call $C$ a function of two variables $x$ and $y$.l In linear programming, $C$ is called an objective function, and the inequalities in the system are referred to as the constraints on $C$. The solutions of the system--that is, the pairs $(x,y)$ corresponding to the points in $R$, are called the **feasible solutions** for the problem.

# Guidelines to solving a Linear Programming problem

1. Sketch the region $R$ determined by the system of constraints.
2. Find the vertices of $R$.
3. Calculate the value of the objective function $C$ at each vertex of $R$.
4. Select the maximum or minimum value of $C$.

 But how is each step done?
Let us imagine a piecewise function that reveals the system of constraints.

Let each expression within this function be equal to $P_1$, $P_2$, $P_3$, $P_4$, etc. In this example, we shall say there are only four expressions for simplicity.

Let us say $P_1$, $P_2$, are linear inequalities. We then find their intersection, which represents a vertex of the polygon formed by the area of this system. This will be a point to test later.

Next, it is likely that $P_3$ and $P_4$ are inequalities for $x$ and $y$. We change $P_3$ and $P_4$ to definitions of $x$ and $y$ instead (so, $x=0$ and $y=0$) and then substitute $P_3$ into $P_1$, and $P_4$ into $P_2$ (order doesn't matter, this is just an example). At this point, in addition to the origin (most likely), you have the points needed to find the minimum and maximum values.

Then, simply plug in the vertices into the objective function and recognize what values of $C$ are the largest and smallest. Those are your minimum and maximum values.

## Example 1 - Finding the Minimum and Maximum Values of an Objective Function

Minimum and maximum values of the objective function given by $C=7x+3y$ subject to the following constraints:

$$
f(x)= \begin{cases}
x-2y \geq -10 \\
2x+y \leq 10 \\
x \geq 0 \\
y \geq 0 
\end{cases}$$

> [!answer]- Answer
> ![[Pasted image 20260520101023.png]]
