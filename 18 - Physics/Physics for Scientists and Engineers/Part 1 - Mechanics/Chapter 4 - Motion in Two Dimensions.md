
# 4.1 - Position, Velocity, and Acceleration Vectors
 A displacement vector can be described for a particle as being the difference between its final position vector and its initial position vector, as such:

$$
\Delta \vec{r}\cong \vec{r}_{f}-\vec{r}_{i}
$$
The formula for average velocity  of a particle we already know from [[Chapter 2 - Motion]]. But recall that multiplying or dividing a vector quantity by a positive scalar quantity only changes its magnitude.

Also recall that the speed of a particle is a scalar quantity, $|\vec{v}|$.

# 4.2 Two-Dimensional Motion with Constant Acceleration


## Velocity vector as a function of time  (PUCA2D)


$$
\vec{v}_{f}=x_{i+\vec{a}t}
$$
for constant $\vec{a}$



## Position vector as a function of time (PUCA2D)


$$
\vec{r}_{f}=\vec{r}_{i}+\vec{v}_{i}t+\frac{1}{2}\vec{a}t^2
	$$

The position vector is a composite of the initial position, the displacement produced by velocity, and the displacement produced by velocity over time. Because velocity is a linear increase, when we account for the displacement produced by it--the area under the curve--because the acceleration is constant, the geometric form is quite similar to a triangle.  To find the area of a triangle, one simply takes $\frac{1}{2}bh$, where $b=at$ and $h=t$, producing the component you see in the equation. 
## Example 4.1 - Motion in a Plane

A particle moves in the xy plane starting from the origin at $t=0$ with an initial velocity having an $x$ component of $20$ m/s and a y component of $-15$ m/s. The particle experiences an acceleration in the $x$ direction, given by $n_x=4.0$m/s squared.

A) Determine the total velocity vector at any later time. 

B) Calculate the velocity and speed of the particle at $t=5$s and the angle the velocity vector makes with the x axis. 

C) Determine the x and y coordinates of the particle at any time $t$ and its position vector at this time.

> [!answer]- Answer
> ![[Pasted image 20260518171956.png]]


# 4.3 Projectile Motion

Projectile motion, assuming no air resistance, is always parabolic. This of course relies on two assumptions: the first, that free-fall acceleration is constant over the range of motion and is directed downward, and that the effect of air resistance is negligible. 

Note that this is reasonable as long as the range of motion is small compared with the radius of the Earth, ($6.4 * 10^6$miles), and this assumption encounters significant complications when velocities are high enough. Note that any spin imparted to a projectile can give rise to very interesting aerodynamic phenomena.

The final position of a particle can be considered to be the superposition of its initial position $\vec{r}_{i}$. If there were no gravitational acceleration, the particle would continue to move along a straight path in the direction of $\vec{v}_{t}$. Therefore, the vertical distance through which the particle falls off the straight-line path is the same distance that an object dropped from rest would fall during the same time interval

There are thus two analysis models to be used when it comes to projectile motion: a particle under constant velocity in the horizontal direction, and a particle under constant acceleration in the vertical direction.

## Particle under constant velocity in the Horizontal Direction


### Horizontal Position 
$$
x_{f}=x_{i}+v_{xi}t
$$


## Particle under constant acceleration in the vertical direction

### Vertical Velocity after $t$

$$
v_{yf}=v_{yi}-gt
$$
### Average vertical velocity

$$
v_{yavg}=\frac{v_{yi}+v_{yf}}{2}
$$

###  Vertical vector using average velocity

$$
y_{f}=y_{i}+\frac{1}{2}(v_{yi}+v_{yf})t
$$

### Vertical Position under Constant Acceleration

$$
v_{yf}^2=V^2_{YI}-2g(y_{f}-y_{i})
$$

### Initial $x$ and $y$ components of the velocity of the projectile

$$
v_{x}=v_{i}\cos \theta
$$
$$
v_{y}=v_{i}\sin \theta
$$
## Horizontal Range and Maximum Height of a Projectile

Where projectile motion is concerned, objects often return to the height at which they were launched. Two points in this motion are useful to analyze: the peak point $A$, with Cartesian coordinates $\left( \frac{R}{2} \right),h$ and the point $B$ with coordinates $(R,0)$. The distance $R$ is called the horizontal range of the projectile and the distance $h$ is its maximum height.

### Time a which the projectile reaches the peak

$$
t_{a}=\frac{v_{i}\sin \theta}{g}
$$

### Height in terms of magnitude and direction of the initial velocity vector

$$
h=\frac{v^2_{i}\sin^2\theta}{2g}
$$

Due to the symmetry of the trajectory, the projectile covers the upward part to the top in exactly the same time interval as it requires to come back to the ground from the topmost point. The range $R$ is the horizontal position of the projectile at a time that is twice the time at which it reaches the peak.

### Range Equation for a Symmetric Path

$$
R=\frac{v^2_{i}\sin 2\theta}{g}
$$
This uses the [[Section 4.4 - Multiple Angle Identities#Double Angle identities|Double Angle Identity]] to simplify into a more compact form.

Note also that complementary angles of launch result in the same range, such as 15 and 75 degrees.

## Example 4.2 - The Long Jump

A long jumper leaves the ground at an angle of $20 \degree$ above the horizontal and at a speed of $11.0$ m/s.

A) How far does he jump in the horizontal direction?

B) What is the maximum height reached?

> [!answer]- Answer
> ![[Pasted image 20260527190106.png]]


## Example 4.3 - A Bull's-Eye Every Time

In a popular lecture demonstration, a projectile is aimed directly at a target and fired in such a way that the projectile leaves the gun at the same time the target is dropped from rest. Show that the projectile hits the falling target.

Both objects can be imagined as being in free fall, despite the horizontal component of the gun fired projectile.

The falling object however is modeled only by a particle under constant acceleration in one dimension, while the fired projectile is imagined as the combination of a particle under constant acceleration in the $y$ direction while it is a particle under constant velocity in the $x$ direction, since there is no acceleration in the $x$ direction, only the $y$.

Thus, the answer should show that the $x$ and $y$ components combined result in the same expression as just the $y$ component of the particle under constant acceleration in one dimension, that being the target.

> [!answer]- Answer
> ![[Pasted image 20260527195244.png]]
