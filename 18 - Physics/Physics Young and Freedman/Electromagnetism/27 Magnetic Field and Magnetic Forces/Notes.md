# Terms

# Equations

## **Magnetic Forces**: 

From
$$
F = |q|v_{\perp}B = |q|v \sin \phi
$$
Where $q$ is the charge, $v_{\perp}$ is the component of the charge's velocity that is perpendicular to the magnetic field $B$. 
$$
\vec F = q\vec v \times \vec B
$$
Uses Teslas (1 T = 1 N/A * m)
## Magnetic Field Lines and Flux



Uses a Weber ($1 Wb$ $=$ $1 T * m^2$ ).

## Motion in a Magnetic Field

## Magnetic Force on a Conductor

## Magnetic Torque

$$
\tau = IBA \sin \phi
$$
$$
\tau = \vec u \times \vec B 
$$

$$
U = -\vec u \cdot \vec B=- \mu B \cos \phi 
$$

# Magnetism

## Class Notes

![[class_notes_1-magnets.pdf]]

## Class Notes 2

![[class_botes_2_magnets.pdf]]


## Book Notes

A bar magnet has ends free to rotate, typically one pointing north, the other south. An object that contains iron but is not itself magnetized is attracted by either pole of a permanent magnet. This is the attraction that acts between a magnet and the unmagnetized steel door of a refrigerator.

Compass readings deviate somewhat from geographic north, which is called a magnetic declination or magnetic variation. The magnetic field is not horizontal at most points on the earth's surface, and its angle up or down is called magnetic inclination. 

Magnetic field lines show the direction that a compass would point at each location.

### Magnetic Poles Versus Electric Charge

While magnetic poles share some similarities to electric charge, it is not analogous. There is no experimental evidence that a single isolated magnetic pole exists: poles always appear in pairs.  If a bar magnet is broken in two, each end becomes a pole.  Therefore, at this time it is determined that there is no such thing as a **magnetic monopole**. 

Magnetism is directly related to current, or moving charge, which was discovered in 1820 by Hans Christian Oersted, a Danish scientist.  He found that a compass needle was deflected by a current-carrying wire.

Andre Ampere also carried out similar experiments, as did Michael Faraday and Joseph Henry. We now know that the magnetic forces between two bodies are fundamentally due to interactions between moving electrons in the atoms of the bodies.  There are also electric interactions between them, but they are far weaker than the magnetic interactions because the two bodies are electrically neutral.

Inside a magnetized body, there is a coordinated motion of certain of the atomic electrons. In an unmagnetized body these motions are not coordinated.

### Test Your Understanding
Suppose you cut off the part of the
compass needle shown in Fig. 27.5a that is painted gray. You discard this part, drill a hole
in the remaining red part, and place the red part on the pivot at the center of the compass.
Will the red part still swing east and west when a current is applied as in Fig. 27.5b?

> [!answer]- Answer
> Yes, as breaking apart a permanent magnet just makes the new ends the new North and South poles.

# Magnetic Field

## Book Notes

Recall that:

1. A distribution of electric charge at rest creates an electric field $\vec E$ in the surrounding space.
2. The electric field exerts a force $\vec F=q\vec E$ on any other charge $q$ that is present in the field.

Magnetic Interactions are much the same way:

1. A moving charge or a current creates a magnetic field in the surrounding space (in **addition to** its magnetic field). 
2. The magnetic field exerts a force $\vec F$ on any other moving charge or current that is present in the field.

So in the presence of a magnetic field, what force is exerted on a moving charge in a current?

A magnetic field is a vector field, which is a vector quantity associated with each point in space. At any position the direction of $\vec B$ is defined as the direction in which the north pole of a compass needle tends to point.

### Magnetic Forces on Moving Charges

There are four key characteristics of the magnetic force on a moving charge.

1. Magnitude is proportional to the magnitude of the charge.
2. The magnitude of the force is also proportional to the magnitude of the field.
3. The magnetic force depends on the particle's velocity. A charged particle at rest experiences NO MAGNETIC FORCE.
4. The magnetic force does not have the same direction as the magnetic field, but instead is always perpendicular to both the field and the velocity of the moving charge $\vec n$. 
### Right-Hand Rule

![[Pasted image 20261011193736.png]]

**IF THE CHARGE IS NEGATIVE, THE DIRECTION OF THE FORCE IS OPPOSITE TO THAT GIVEN BY THE RIGHT HAND RULE**. 

### Sum of the forces by both fields

### Problem Solving Strategy for Magnetic Forces

1. Draw the velocity and magnetic field vectors with their tails together.
2. Determine the angle between them.
3. $\vec F$ is perpendicular to the plane containing $\vec v$ and $\vec B$. The right hand rule gives the direction of their cross product, and if $q$ is negative, the $\vec F$ is opposite to the cross product.
$$
\vec F = q(\vec E + \vec v \times \vec B)
$$
When a charged particle moves through a region of space where both electric and magnetic fields are present, both fields exert forces on the particle. 

# Magnetic Field Lines and Magnetic Flux

We can represent any magnetic field by magnetic field lines. The lines, just as in Electric fields, are tangent to the magnetic field vector $\vec B$ at that point.

Recall that the magnetic field lines always point perpendicular to the actual magnetic force.

### Magnetic Flux and Gauss's Law for Magnetism

**Magnetic Flux** $\phi_B$ is defined similarly through a surface just as we defined electric flux. We can divide any surface into elements of area $dA$. For each element we then determine the normal components of $B$ to the surface at the position of that element. 

The normal component is then compared to the angle between it and $B$. This is expressed by
$$
B\cos \phi dA=B \cdot dA
$$
And the total magnetic flux is then

$$
\int \vec B \cdot \vec A
$$
As this is a dot product, the magnetic flux is a scalar quantity. If $B$ is uniform over a plane surface with a total area $A$, then the normal component of $B$ and the angle $\phi$ are the same at all points on the surface, or
$$
BA\cos \phi
$$
Since there is no magnetic monopole, compared to electric flux, 
**The total magnetic flux through a closed surface is always zero.**

or

$$
\oint_{C} \vec B \cdot d\vec A = 0
$$
If you draw a closed surface anywhere in any of the field maps, you will see that every field line that enters the surface also exits from it: the net flux through the surface is zero. Magnetic field lines always form closed loops, and they do not have end points.

The magnitude of the magnetic field is equal to the flux per unit area across an area at right angles to the magnetic field, so the magnetic field can also be considered magnetic flux density.

$$
B = \frac{d \phi_{B}}{dA_{\perp}}
$$
# Motion of Charged Particles in a Magnetic Field

When a charged particle moves in a magnetic field, it is acted on by the magnetic force (recall that it is $F=qv \times B$).

The force is always perpendicular to $\vec v$ so it cannot change the magnitude of the velocity, only its direction. Because of this, the magnetic force never does work on the particle, even if the magnetic field is not uniform.

Motion of a charged particle under the action of a magnetic field alone is always motion with constant speed. Thus, the path is a circle, traced with constant speed $v$. Since this centripetal acceleration is $\frac{v^2}{R}$ and only the magnetic force acts, then:

$$
F= |q|vB = m \frac{v^2}{R}
$$
where $m$ is the mass of the particle. If we solve for radius $R$, we get:

$$
R= \frac{mv^2}{|q|vB}
$$
It can also be rewritten in terms of momentum, where $p=mv$ is the magnitude of the particle's momentum. If the charge is negative, then the particle moves clockwise around the orbit.

# Magnetic Force on a Current-Carrying Conductor

When an electric current flows through a conductor placed in a magnetic field, the moving charges in the conductor then experience a magnetic force perpendicular to both their direction of motion and the magnetic field. This force is then transferred to the conductor itself.

To determine this force, we first start with magnetic force 
$$
\vec F= q\vec v \times \vec B
$$
![[Pasted image 20261012181910.png]]


![[Pasted image 20261012181924.png]]

## Non-linear Magnetic Force on a conductor

If the conductor isn't straight, then we divide it into infinitesimal segments
$$
d\vec l
$$
Then the force on each segment $d\vec F$ is

$$
d\vec F = I \vec{dl} \times \vec B
$$
And then integrating this expression along the wire, we find the total force on a conductor of any shape using a line integral.

Remember that the current is not a vector, but the length $l$ or $d\vec l$. 

When the moving charges are negative, such as electrons in a metal, then the upward current corresponds to a downward drift velocity.  Since $q$ is now negative, the direction of the force $\vec F$ is the same as before. So these equations are applicable for both signs of charge even when both are present.

# Force and Torque on a Current Loop

Current-carrying conductors usually form closed loops, so we typically need to find the total magnetic force and torque on a conductor in the form of a loop.

Many devices like loudspeakers and galvanometers use the magnetic force or torque on a conducting loop. It can be that the total force on the loop is zero, but that there is a net torque acting on the loop. This is for a uniform magnetic field.

It is notable that, when the loop is rotated slightly from its stable equilibrium position of $\phi = 0$, the net torque tends to rotate it back toward that position, much like the restoring force of a mass-spring system.

Meanwhile the position $\phi = 180$ is an unstable equilibrium position--when displaced from this point, it tends to rotate away from it.

For a current carrying loop, the magnitude of the torque is:

$$
\tau = IBA\ \sin \phi
$$
The product $IA$ is the magnetic dipole moment (similar to the electric dipole moment $q=\rho d$), or just the magnetic moment of the loop. It is also expressed as:

$$
\mu = IA
$$
Putting the magnitude of the torque in terms of $\mu$, then we have

$$
\tau = \mu B \sin \phi
$$

## Potential Energy for a Magnetic Dipole

When a magnetic dipole changes orientation in a magnetic field, the field does work on it. Thus, for an infinitesimal angular displacement $d\phi$, the work $dW$ is given by 
$$
\tau d\phi
$$
and there is then a change in potential energy. Since it ranges from $0$ to $\pi$, and $W=-\Delta U$, then it is least when the angle is parallel or 0, and greatest when it is anti-parallel or $\pi$. 

Since we know that
$$
U = -p \cdot E
$$
for the potential energy for the work done on an electric dipole, then similarly, for a magnetic dipole it is just

$$
U = -\mu \cdot B
$$



# Diagrams

## Magnetic Fields in a Closed Loop

![[magnetic_field_closed_loop.pdf]]


## Magnetic Field Dot Diagrams

![[magneticfield_dotdiagrams.pdf]]


## Current and Magnetic Field

![[current_and_magnetic_field.pdf]]


## Magnetic Force Magnitudes 

![[magnetic-force-magnitudes.pdf]]


![[Pasted image 20261011201620.png]]


## Charged particle moving in a plane perpendicular to a uniform magnetic field

![[Pasted image 20261011205938.png]]