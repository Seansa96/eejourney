
A particle's **position** $x$ is the location of the particle with respect to a chosen reference point that we can consider to be the origin of a coordinate system. The motion of a particle is completely known if the particle's position in space is known at all times.

A graphical representation of  this information is called a position-time graph.

The **displacement** $\Delta x$ of a particle is defined as its change in position in some time interval. Thus, the particle's displacement can be formalized by the expression
$$
\Delta x = x_{f}-x_{0}
$$
Where $f$ is the final position, and $0$ is the initial.

Remember though that a particle's motion is not completely known if we do not know its position at all times. One may be able to draw a position-time graph from a few or even many given points, but that only represents a possibility of its theorized motion unless you can determine its position at every instant within an interval.

One may also find the **average velocity**, the particle's displacement $\Delta x$ over the time interval in which that displacement occurs $\Delta t$. 

$$
v_{x.avg}=\frac{\Delta t}{\Delta x}
$$

As velocity is a vector quantity, its displacement can be positive or negative, depending on the sign of the displacement.

Average speed is instead a scalar quantity, and is different than velocity in that respect, despite its use in everyday language being interchangeable.

It is defined as

$$
[v_{avg}]=\frac{d}{\Delta t}
$$

# Instantaneous Velocity and Speed


We know from Calculus that to determine the velocity of a particle at a given instant of time $t$, we must use the limiting value of ratio which determines the velocity, or 

$$
\lim_{ t \to 0 } \frac{\Delta x}{\Delta t}
$$

This is of course just shorthand for the derivative of the function. Note that when $t$ is infinitesimal, the instantaneous speed and velocity are equal and can represent the distance traveled by the particle at that instant.

## Example 1 - Velocity of Different Objects


Consider the following one-dimensional motions: (A) a ball thrown directly upward rises to a highest point and falls back into the thrower’s hand; (B) a race car starts from rest and speeds up to 100 m/s; and (C) a spacecraft drifts through space at constant velocity. Are there any points in the motion of these objects at which the instantaneous velocity has the same value as the average velocity over the entire motion? If so, identify the point(s).

> [!answer]- Answer
> A) Yes. At the maximum value (when the ball reaches its highest point, before it falls), the ball's velocity is 0, which is what the average velocity is at the end.
> B) Yes, at some point between $0$ and $100 m/s$ the car's instantaneous velocity will equal its average velocity, according to the Mean Value Theorem.
> C) Since it has a constant velocity, its instantaneous velocity is equal to its average velocity at all times.


## Example 2 - Average and Instantaneous Velocity

A particle moves along the x axis. Its position varies with time according to the expression $x=-4t+2t^2$, where $x$ is in meters and $t$ is in seconds, $4$. The position–time graph for this motion is shown in Figure 2.4a. Because the position of the particle is given by a mathematical function, the motion of the particle is known at all times, unlike that of the car in Figure 2.1, where data is only provided at six instants of time. Notice that the particle moves in the negative x direction for the first second of motion, is momentarily at rest at the moment $t=1s$, , and moves in the positive x direction at times $t>1$ s.

A) Determine the displacement of the particle in the time intervals $t=0$ to $t=1$ and $t=1$ to $t=5$.

> [!answer]- Answer
> ![[Pasted image 20260510230909.png]]

### B) Calculate the average velocity during these two time intervals

> [!answer]- Answer
> ![[Pasted image 20260510231216.png]]


### C) Calculate the instantaneous velocity at time $t=2.5s$

> [!answer]- Answer
> ![[Pasted image 20260510231605.png]]


# 2.3 Analysis Model: Particle Under Constant Velocity

An analysis model is a common situation that occurs time and again when solving physics problems.  

# 2.4 The Analysis Model Approach to Problem Solving

* Conceptualize
* Categorize
* Analyze
* Finalize

# 2.5 Acceleration

# 2.7 Analysis Model: Particle Under Constant Acceleration

## Velocity at any point in time equation 
If we take the equation

$$
a_{x.avg}=\frac{v_{xf}-v_{xi}}{t_{f}-t_{i}}
$$

and set $t_i$ to be $0$, and let $t_f$ to be any other later time, as well as let the equation be for $a_x$, we get
$$
a_{x}=\frac{v_{xf}-v_{xi}}{t}
$$
Then solve for $v_{xf}$.

$$
v_{xf}=v_{xi}+at
$$
This allows us to solve for an object's velocity at any point in time if we know its initial velocity. and its constant acceleration.

## Average Velocity under constant acceleration

$$
v_{x.avg}=\frac{v_{xi}+v_{xf}}{2}
$$

## Final position of a particle under constant acceleration Equation

$$
x_{f}=x_{i}+\frac{1}{2}(v_{xi}+v_{xf})t
$$
## Velocity as a function of position for the particle under constant acceleration model

$$
v^2_{xf}=v^2_{xi}+2a(x_{f-x_{i}})
$$


# 2.8 Freely Falling Objects

In the idealized case, in which air resistance is absent, such motion is referred to as **free-fall motion.**

At the Earth's surface, the value of $g$ is approximately $9.8m/s^2$.

In this case, the equation for an object in free fall can be thought of as:

## Particle under constant acceleration in one dimension

$$
y_{f}=y_{i}+v_{i}t-\frac{1}{2}gt^2
$$
## Example 1 - Stone Thrown from a Roof


A stone thrown from the top of a building is given an initial velocity of $20m/s$ straight upward. The stone is launched $50m$ above the ground, and the stone just misses the edge of the roof on its way down.

a) Using $t=0$ as the time the stone leaves the thrower's hand at position $A$, determine the time at which the stone reaches its maximum height.

We should use the particle under constant acceleration due to gravity model.

So, let's first solve for $v_f$.



> [!answer]- Answer
> ![[Pasted image 20260510235550.png]]


### B) Find the maximum height of the stone

To find the maximum height, you would need the average velocity and then multiply it by the time, or just the distance equation, which is

$$
d=rate*time
$$
But this doesn't account for the acceleration by gravity and assumes a constant velocity. Since our model is a particle under constant acceleration due to the gravity, then we must use

$v_{avg}$ in the place of $rate$. To find $v_{avg}$, we use

$$
v_{avg}=\frac{v_{f}-v_{0}}{2}
$$

> [!answer]- Answer
> ![[Pasted image 20260511000422.png]]


### C) Determine the height of the stone when it returns to where it was thrown.


> [!answer]- Answer
> ![[Pasted image 20260511212612.png]]


### D) Determine the position and velocity of the stone at $t=5$ 

> [!answer]- Answer
> ![[Pasted image 20260511214042.png]]
> ![[Pasted image 20260511214055.png]]


# 2.9 Kinematic Equations derived from Calculus

## Displacement of a particle

This is the limit of the Riemann sum of for the total displacement over the interval $t_f - t_i$.

$$
\Delta x=\int^{t_{f}}_{t_{i}}v_{x}(t) dt
$$

