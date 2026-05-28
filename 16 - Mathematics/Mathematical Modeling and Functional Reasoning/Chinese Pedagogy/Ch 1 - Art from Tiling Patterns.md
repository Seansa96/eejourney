
A polygon is said to be concave if every inner angle of $P$ is less than $180 \deg$ and concave otherwise.

Examples:

**Parallelogram**

![[Pasted image 20260422133523.png]]


**Trapezoid**

![[Pasted image 20260422133637.png]]


**Convex Quadrangle**
![[Pasted image 20260422133747.png]]


Meanwhile, a polygon is said to be concave when at least one inner angle exceeds $180$ degrees.  This is typically accompanied by the shape bending inward.

**Concave Quadrangle**

![[Pasted image 20260422134456.png]]

The pointed interior angle, complementary to the exterior, is greater than $180$ degrees, likely around 300 degrees or so, while the exterior angle is much smaller, around $60$ degrees.

For reference, this is referred to as the **Reflex angle.**

# What shapes can tile the plane without gaps?

Try any of the above.

> [!answer]- Answer
> ![[Pasted image 20260422135242.png]]
> ![[Pasted image 20260422135332.png]]
> ![[Pasted image 20260422135423.png]]
> 

In fact, many more can tile the plane. It seems that any concave or convex quadrangle can do so, up to n=7 of n-gons.

# Conway Criterion

A given figure (a closed region on a plane) can tile the plane by only translation and 180 degree rotations if its perimeter can be divided into six parts by six consecutive points, $A, B, C, D, E, F$ , all located on its perimeter, such that:

1. The perimeter part $AB$ is congruent by translation $t$ to the perimeter part $ED$ in which translation $A=E$, translation $B=D$.  IE, $AB // ED$. 
2. Each of the perimeter parts $B, CD, EF, EA$ is centrosymmetric, that is, each of them coincides with itself when the figure is rotated by 180 degrees around its midpoint.
3. Some of the six points may coincide, but at least three of them must be distinct.

# Example 

Does this satisfy the **Conway Criterion?**

Label it to check, defining points of Centro symmetricity.

![[Pasted image 20260422142518.png]]



> [!answer]- Answer
> Yes.
> ![[Pasted image 20260422142757.png]]
