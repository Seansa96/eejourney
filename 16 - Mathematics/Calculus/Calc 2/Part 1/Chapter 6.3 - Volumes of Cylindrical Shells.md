
# Shell Method

Some volume problems are very difficult to near impossible by hand with the methods of the previous chapter.  

Consider the following:

Find the volume of the region bounded by $y=2x^2-x^3$, and $y=0$. 

Slicing perpendicular to the y-axis gets us a washer, but trying to compute the inner radius means we'd have to solve that cubic equation $y=2x^2-x^3$, which is not trivial.

We can use the **method of cylindrical shells**, with an inner radius $r_{1}$ and an outer radius $r_{2}$, and its height $h$. Its volume $V$ is calculated as follows:

$$
V=V_{2}-V_{1}
$$
$$
= \pi r^2_{2}h-\pi r^2_{1}h=\pi(r^2_{2}h-r^2_{1}h)
$$
$$
=\pi(r_{2}+r_{1})(r_{2}-r_{1})h
$$
$$
=2\pi\left( \frac{r_{2}+r_{1}}{2} \right)h(r_{2}-r_{1})
$$
Where $2\pi\left( \frac{r_{2}+r_{1}}{2} \right)$ represents the circumference $2\pi r$, $h$ is the height, and $r_{2}-r_{1}$is the shell's thickness.

If we let $\Delta r$ be the thickness of the shell, then we get the formula

$$
V=2\pi rh\Delta r
$$

## Example 1 - Find the Volume of the Solid

Find the volume of the solid obtained by rotating the region bounded by $y=x-x^2$ and $y=0$ .

> [!answer]- Answer
> ![[Pasted image 20260512215355.png]]

## Example 2 - Find the Volume of the Solid

Find the Volume of the Solid obtained by rotating about the y-axis bounded by $y=2x^2-x^3$ and $y=0$.

> [!answer]- Answer
> ![[Pasted image 20260512215947.png]]

## Example 3 - Find the volume of the solid

Find the volume of the solid obtained by rotating about the y-axis the region between $y=x$ and $y=x^2$.


> [!answer]- Answer
> ![[Pasted image 20260512220713.png]]


# Shell Method about the x-axis

The shell method also works just as fine when rotating about the x-axis.  It's best to draw a diagram to make sure we identify the proper radius and height of the shell.

## Example 1 - Find the volume of the solid (x-axis)


Use cylindrical shells to find the volume of the shell obtained by rotating about the x-axis, the region under the curve, $y=\sqrt{ x }$ from $0$ to $1$.

> [!answer]- Answer
> ![[Pasted image 20260512221610.png]]


## Example 2 - Find the Volume of the solid (x-axis not the coordinate axis)

Find the volume of the solid obtained by rotating the region bounded by $y=x-x^2$ and $y=0$ about the line $x=2$.

> [!answer]- Answer
> ![[Pasted image 20260512222802.png]]


# Disks and Washers vs Cylindrical Shells

When considering which method to use, check:

* Is the region more easily bounded by top and bottom ($y=f(x)$) or by left and right ($x=f(y)$)?
* Which is easier to work with for this problem?
* Are the limits of integration easier to find for one versus the other?
* Does the region require two separate integrals when using $x$ as the variable but only one integral in $y$? Are we able to evaluate the integral we set up with our choice of variable?

If one variable is easier to use than the other, then that typically decides the method to employ.