# 3.1 Coordinate Systems

Cartesian coordinates are the primary mode for describing position in two dimensions. This is also referred to as rectangular coordinates.

Sometimes though, it is more convenient to represent a point in a plane by its plane polar coordinates, $(r,\theta)$. In this polar coordinate system, $r$ is the distance rom the origin to the point having Cartesian coordinates (x,y), and $\theta$ is the angle between a fixed axis and a line drawn from the origin to the point.

Thus, to represent a Polar coordinate in terms of its Cartesian coordinates, it can be thought of thusly:

$$
x=r\cos(\theta)
$$

$$
y=r\sin(\theta)
$$

And conversely, if we know the Cartesian coordinates, the definitions of trigonometry tell us that the Polar coordinates are given by

$$
\tan \theta = \frac{y}{x}
$$
$$
r=\sqrt{ x^2 + y^2 }
$$
## Example 3.1 Polar Coordinates

The Cartesian coordinates of a point in the $xy$ plane are (x,y)=$(-3.5, -2.5)$. Find the polar coordinates.

> [!answer]- Answer
> ![[Pasted image 20260513000527.png]]

# Scalars and Vectors

A scalar quantity is completely specified by a single value with an appropriate unit and has no direction.

A vector quantity is completely specified by a number with an appropriate unit (the magnitude) and a direction.

Vectors are typically denoted with an arrow above a boldface letter:

$$
\vec{A}
$$
# 3.3 Basic Vector Arithmetic

Vector addition is done using the "head to tail" method, where the head of a given vector serves as the continuation point for the next, making its tail the starting point.

![[Pasted image 20260513001222.png]]

An infinite number of vectors can be added in this manner, the resultant vector, $R$, being from the tail of vector $\vec{first}$ to the head or tip of $\vec{last}$.

![[Pasted image 20260513001458.png]]
When two vectors are added, the sum is independent of the order of addition. When three or more vectors are added, their sum is independent of the way in which the individual vectors are grouped together.

Order is important when multiplying vectors, however.

Vector Subtraction uses the definition of a negative vector.  The negative of the vector $\vec{A}$ is defined as the vector that when added to $\vec{A}$ gives zero for the vector sum.

Thus, the operation $\vec{A}-\vec{B}$ is evaluated as:

$$
\vec{A}+(-\vec{B})
$$

And then represented visually:


 ![[Pasted image 20260514153401.png]]

Scalar multiplication is also quite straightforward.  If a a vector $\vec{A}$ is multiplied by a positive scalar quantity $m$, the product $m\vec{A}$  is a vector that has the same direction as $\vec{A}$ and magnitude $\vec{A}$. If vector $\vec{A}$ is multiplied by a negative scalar quantity, $-m$, then the product $-\vec{A}$ is directed opposite of $\vec{A}$.

For exact vector addition, you'll need to utilize the law of sines and cosines, but this only works with two vectors, since the geometric form of anything past two vectors will not be a triangle.
## Example 3.2 - A Vacation Trip


A car travels $20km$ due north and then $35km$ in a direction $60\degree$ west of north.


Find the magnitude and direction of the car's resultant displacement. Solve the problem algebraically using trigonometry.


> [!answer]- Answer
> ![[Pasted image 20260514160850.png]]

# 3.4 - Components of a Vector and Unit Vectors

The projections along the coordinate axes of a vector can be said to be its components, or more specifically, its rectangular components.

The vector can thus be said to be an expression of the sum of the two rectangular components.

You can see it as follows:

![[Pasted image 20260514161502.png]]

So, the magnitudes of the components are just the lengths of the two sides of a right triangle. So, we want the hypotenuse, $A$, then we simply use the Pythagorean identity to obtain it:

$$
A=\sqrt{ A^2_{x}+A^2_{y} }
$$

And we can obtain its angle tangent to the point of origin as

$$
\theta=\arctan\left( \frac{A_{y}}{A_{B}} \right)
$$

## Unit Vectors

Typically, vector quantities are expressed in terms of unit vectors. These are dimensionless vectors with a magnitude of exactly 1. These are simply used to specify a given direction and have no physical significance.

The conventional standards for unit vectors in regards to symbols are:

$$
\hat{i},\hat{j}, \hat{k}
$$
These represent the $$x,y,z$$
axes respectively.

## Example Resultant Vector

![[Pasted image 20260514163442.png]]

For vectors with three component vectors, we simply tack on $A_z,\hat{k}$, and $B_{Z},\hat{k}$

In this case, $R$ is equal to $$R=\sqrt{ R^2_{x}+R^2_{y}+R^2_{z}}$$

The angle $\theta$ that $\vec{R}$ makes with the x-axis is found from 
$$
\cos \theta_{x}=\frac{R_{x}}{R}
$$

## Example 3.3 - The Sum of Two Vectors

Find the sum of two vectors $\vec{A}$ and $\vec{B}$ and given by

$$
\vec{A}=(2.0\hat{i}+2.0\hat{j}); \vec{B}=(2.0\hat{j}-4.0\hat{j})
$$
> [!answer]- Answer
> ![[Pasted image 20260516202048.png]]


## Example 3.4 - The Resultant Displacement

A particle undergoes three consecutive displacements: $\vec{\Delta}r_{1}=15\hat{i}+30\hat{j} +12\hat{k}$cm, $\vec{\Delta}r_{2}=(23\hat{i}-14\hat{j}-5.0\hat{k})$, $\Delta  \vec{r_{3}}=(-13\hat{i}+15\hat{j})$cm. Find unit-vector notation for the resultant displacement and its magnitude.

> [!answer]- Answer
> ![[Pasted image 20260516203933.png]]

## Example 3.5 - Taking a Hike

A hiker begins a trip by first walking $25$km southeast from her car. She stops and sets up her tent for the night. on the second day, she walks $40$km in a direction $60\degree$ north of east, at which point she discovers a forest ranger's tower.

A) Determine the components of the hiker's displacement for each day.
B) Determine the components of the hiker's resultant displacement $\vec{R}$ for the trip. Find an expression for $\vec{R}$ in terms of unit vectors.

> [!answer]- Answer
> ![[Pasted image 20260516212306.png]]
