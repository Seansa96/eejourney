
# 2.3 - Acceleration

Accelerometer - A device that measures the change in acceleration, which is a vector quantity. This is opposed to a speedometer, which measures speed, a scalar quantity.

Acceleration is just the time rate of change of velocity. Like velocity though, it has a magnitude and direction, hence it is a vector.

A basic mechanical accelerometer works by attaching a heavy ball to a spring and suspending it from the housing on top.  

## End of section questions and answers

Suppose two metal balls of different materials, but the same size and shape, were dropped simultaneously from a high-altitude balloon. Let one ball be more massive (heavier) than the other. Which ball will strike the ground first, or would they hit at the same time?

Original answer:
They would both hit at the same time, as the time of impact would be determined by terminal velocity, of which both will reach and both will not exceed, resulting in similar trajectories and thus similar times of impact.

*Why did I think this?*

To me, I assumed that both objects would have the same terminal velocity, and that due to the high altitude air resistance would not prove a sufficient factor.  However, it turns out that air resistance is a factor, which I did not intuit.

> [!answer]- Answer
> As the falling balls gain speed, the upward air resistance would increase the same on each (same size and shape). However, when the air resistance is sufficient to balance the weight of the lighter ball, it would reach terminal velocity and cease to accelerate. So, the heavier ball, having greater terminal velocity, reaches the ground first.

*What does this mean? Do I understand the reasoning?*

From what I can surmise, terminal velocity must mean then a point where air resistance upon an object is great enough to prevent further acceleration of it. This must mean that air resistance either has a finite "force" it can apply, for lack of a better term, or at least that the amount of air resistance is proportional to some other factor I am not aware of or do not recall.

In my mind, "terminal velocity" was a uniform standard all objects reach due to the force of gravity near Earth, but I know understand at least that air resistance is the true cause of the "terminal" portion, and that is serves as the counterbalance to this gravitational acceleration.

**So what's missing?**

**Drag.** More specifically:

$$
F_{drag}=\frac{1}{2}pC_{d}Av^2
$$

where

$p=$air density
$C_d=$ drag coefficient (shape dependent)
$A=$ Cross-sectional area
$v=$ velocity

When any of these factors increase, drag increases.

So if something is bigger (greater $A$), its drag is greater. If it's traveling faster, drag is greater. If air density is greater, drag is greater. If the shape of the object has a higher drag co-efficient, drag is greater.  

When $F_{drag}$ is equal to the force of gravity, terminal velocity for an entity is reached.

# 2.4 - Uniform Circular Motion

An object in *uniform* circular motion has a constant speed, but not a constant velocity or acceleration.  This is because the direction of the car is constantly changing despite its speed remaining constant, thus changing acceleration and velocity which do account for direction.

For an object in uniform circular motion, the acceleration cannot be in the direction of the velocity otherwise then both derivatives would be positive, and thus it would speed up, which would violate the constancy. 

Likewise, it must also not oppose the direction of the velocity, or it would cause the object to slow down. So, it must instead be tangential to the curve on which the object moves across. This is called **centripetal acceleration**, or "center-seeking".

An object moving in a circle of radius $r$ with a constant speed $v$ can have its centripetal acceleration $a_c$ in terms of tangential speed, represented by

$$
a_{c}=\frac{v^2}{r}
$$
Thus, it can be observed that speed has a significant effect on the centripetal acceleration, increasing it, while the greater the radius of the circle, the lower the acceleration.

# Projectile Motion

An object projected (thrown) horizontally, will actually (neglecting air resistance), reach the ground the same time as an object dropped from the same height, because both fall with acceleration $g$. A purely horizontal force only changes that particular vector component, and not the vector related to the downward motion.

In other words, velocity in one direction does not influence velocity or acceleration in another direction, assuming no external forces.

If an object is projected at an angle $\theta$ however, then it will follow a symmetric curved path, where air resistance is neglected. This path is the result of the combined vertical and horizontal motions. The projectile will go up and down vertically as it travels horizontally with a constant velocity.

The path an object takes depends on the project angle, neglecting air resistance.  The range is maximum when the object is projected at an angle of $45 \degree$ relative to level ground.  

Projections at complementary angles have the same range as long as there is no air resistance.

As an object travels fast enough to encounter air resistance, the projectile path is no longer symmetric. Air resistance reduces the velocity of the projectile, particularly in the horizontal direction.  The maximum range thus then occurs at an angle less than $45 \degree$.

# Important Equations

Distance traveled by a dropped object
$$
d=\frac{1}{2}gt^2
$$


Centripetal Acceleration

$$
a_{c}=\frac{v^2}{r}
$$

Average Speed

$$
v=\frac{d}{t}
$$

Acceleration

$$
a=\frac{\Delta v}{\Delta t}= \frac{v_{f}-v_{0}}{t}
$$
