# Chapter 23 — Electric Potential

## Chapter objectives

By the end of this chapter, you should be able to:

1. Explain electric potential energy and its relationship to electric forces and work.
    
2. Distinguish electric potential, electric potential energy, and electric field both conceptually and mathematically.
    
3. Calculate electric potential differences and understand their physical significance.
    
4. Determine electric potential from point charges, continuous charge distributions, and known electric fields.
    
5. Apply conservation of energy to the motion of charged particles in electric fields.
    
6. Explain equipotential surfaces and their relationship to electric field direction.
    
7. Use the potential gradient to determine electric fields from scalar potential functions.
    
8. Recognize when calculating electric potential is simpler than calculating electric fields directly.
    

## 23.1 — Electric Potential Energy

Core question: How does the configuration of electric charges determine the potential energy stored in an electrostatic system, and how does that energy relate to work and motion?

### Conceptual questions

- What is electric potential energy, and how is it related to the configuration of charged objects?
    
- Why is the electrostatic force considered a conservative force?
    
- What does it mean for work done by an electric field to be path-independent?
    
- How does the work done by an electric field relate to changes in electric potential energy?
    
- Why does the electric potential energy of two like charges increase as they move closer together?
    
- Why does the electric potential energy of two opposite charges decrease as they move closer together?
    
- What is the difference between work done by the electric field and work done by an external agent?
    
- How does the sign of a charge affect its potential energy in an electric field?
    
- Why is electric potential energy defined relative to a reference configuration?
    
- Why is infinity commonly chosen as the zero-potential-energy reference for isolated charge distributions?
    
- How does conservation of energy explain the acceleration or deceleration of a charged particle in an electric field?
    
- How is electric potential energy analogous to gravitational potential energy, and where does that analogy become misleading?
    

### Mathematical relationships

The relationship between work and potential energy:

$$
W_{\text{field}}=-\Delta U=U_i-U_f
$$

For electrostatic forces:

$$
\Delta U=-\int_A^B\vec F\cdot d\vec l
$$

For two point charges with $U(\infty)=0$:

$$
U=\frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r}
$$

For a system of multiple point charges:

$$
U=\frac{1}{4\pi\varepsilon_0} \sum_{i<j}\frac{q_iq_j}{r_{ij}}
$$

Conservation of mechanical energy for a particle acted upon only by electrostatic forces:

$$
K_i+U_i=K_f+U_f
$$

### Problem-solving checklist

- Calculate the electric potential energy of two point charges separated by a known distance.
    
- Calculate the change in potential energy when the separation between two charges changes.
    
- Determine the work performed by the electric field when a charge moves between two positions.
    
- Determine the external work required to assemble a configuration of point charges quasistatically.
    
- Calculate the total potential energy of a three-charge or four-charge system.
    
- Use conservation of energy to calculate the final speed of a charged particle.
    
- Determine whether a charged particle accelerates or decelerates based on changes in potential energy.
    
- Determine whether work done by the electric field is positive, negative, or zero.
    
- Explain why two different paths between the same endpoints produce the same electrostatic work.
    

Teaching challenge: Two positively charged particles are initially held close together and then released.

Explain why they accelerate away from one another, where their kinetic energy comes from, and why the total mechanical energy of the isolated system remains constant.

## 23.2 — Electric Potential

Core question: What is electric potential, and why is it useful to describe electrical interactions using energy per unit charge rather than electric force?

### Conceptual questions

- What is electric potential, and how does it differ from electric potential energy?
    
- What does it physically mean for a point in space to have an electric potential of $10\,\text{V}$?
    
- Why is electric potential a scalar quantity even though electric field is a vector?
    
- What is voltage, and how does it relate to electric potential difference?
    
- Why is electric potential difference more physically important than absolute electric potential?
    
- What is the relationship between the work done by an electric field and electric potential difference?
    
- Why does a positive charge tend to accelerate toward lower electric potential when only the electrostatic force acts on it?
    
- Why does a negative charge tend to accelerate toward higher electric potential?
    
- Does a charge necessarily move toward a location of lower electric potential energy?
    
- Can electric potential be zero at a point where the electric field is nonzero?
    
- Can electric field be zero at a point where electric potential is nonzero?
    
- What does it mean to say that electric potential is defined relative to a reference point?
    
- What are the physical interpretations of a volt and an electronvolt?
    
- Why does the electric potential decrease in the direction of the electric field?
    

### Mathematical relationships

The definition of electric potential:

$$
\boxed{V=\frac{U}{q}}
$$

For differences between two locations:

$$
\boxed{\Delta V=\frac{\Delta U}{q}}
$$

Therefore:

$$
\Delta U=q\Delta V
$$

Work done by the electric field:

$$
W_{\text{field}}=-q\Delta V
$$

Potential difference in terms of the electric field:

$$
\boxed{V_B-V_A=-\int_A^B\vec E\cdot d\vec l}
$$

For a uniform electric field:

$$
\Delta V=-Ed\cos\theta
$$

where $d$ is the displacement magnitude and $\theta$ is the angle between the displacement and the electric field.

### Problem-solving checklist

- Convert between electric potential energy, charge, and electric potential.
    
- Calculate the potential difference between two points in a uniform electric field.
    
- Determine the change in potential energy of a positive or negative charge moved through a known voltage difference.
    
- Calculate the work performed by an electric field when moving a charge between two potentials.
    
- Determine the final kinetic energy and speed of a charged particle accelerated through a voltage difference.
    
- Convert between joules and electronvolts.
    
- Determine whether a particle gains or loses kinetic energy when moving between specified electric potentials.
    
- Interpret positive and negative potential differences using sign conventions.
    
- Calculate the potential difference between two points using a line integral of the electric field.
    
- Identify how changes to the reference potential affect electric potential values without changing observable forces or potential differences.
    

Teaching challenge: An electron is released from rest in a uniform electric field.

Explain why it accelerates opposite to the electric field direction, toward increasing electric potential, while its electric potential energy decreases.

Your explanation should distinguish the signs of $q$, $\Delta V$, and $\Delta U$.

## 23.3 — Calculating Electric Potential

Core question: How do we calculate electric potential at a point in space from one or more charges, and how does this differ from calculating the electric field?

### Conceptual questions

- Why is electric potential easier to calculate than electric field for many charge configurations?
    
- How does the scalar nature of electric potential simplify superposition?
    
- Why can we add electric potentials algebraically without resolving vector components?
    
- How do positive and negative source charges contribute to electric potential?
    
- Why does electric potential from a point charge vary as $1/r$, while electric field magnitude varies as $1/r^2$?
    
- Why do we commonly define $V=0$ at infinity for isolated finite charge distributions?
    
- When is choosing infinity as the zero-potential reference inappropriate?
    
- What is the difference between calculating the potential from a point charge and from a continuous charge distribution?
    
- How do we express an infinitesimal contribution $dV$ from a charge element $dq$?
    
- How does symmetry simplify the electric potential calculation for a ring, rod, or other charge distribution?
    
- Can contributions to electric potential cancel while contributions to electric field remain nonzero?
    
- Can electric potential be constant throughout a region even if the individual source charges are nonzero?
    
- What is the relationship between electric potential and the work required to assemble a system of charges?
    

### Mathematical relationships

Electric potential from a point charge:

$$
\boxed{V=\frac{1}{4\pi\varepsilon_0}\frac{q}{r}}
$$

Electric potential from multiple point charges:

$$
V=\frac{1}{4\pi\varepsilon_0} \sum_i\frac{q_i}{r_i}
$$

Electric potential from a continuous charge distribution:

$$
\boxed{V=\frac{1}{4\pi\varepsilon_0}\int\frac{dq}{r}}
$$

Charge elements can be expressed as:

$$
dq=\lambda\,dl
$$

$$
dq=\sigma\,dA
$$

$$
dq=\rho\,dV
$$

These formulas assume the potential reference at infinity is appropriate and that the relevant integrals converge.

For charge distributions extending to infinity, potential differences may be well-defined even when the integral defining $V$ relative to infinity diverges.

### Problem-solving checklist

#### Discrete charge distributions

- Calculate electric potential at a point due to a single point charge.
    
- Calculate the net electric potential at a point due to multiple point charges.
    
- Find locations where the net electric potential is zero for two point charges.
    
- Determine the potential at the midpoint of two equal and opposite charges.
    
- Compare locations where electric potential is zero to locations where electric field is zero.
    
- Calculate the potential energy of a test charge placed at a point in a known potential field.
    

#### Continuous charge distributions

- Calculate the electric potential along the axis of a uniformly charged ring.
    
- Set up and evaluate the potential integral for a uniformly charged rod.
    
- Calculate the potential of a uniformly charged spherical shell inside and outside the shell.
    
- Calculate the potential of a uniformly charged solid sphere inside and outside the sphere.
    
- Express the total electric potential as an integral over a known linear, surface, or volume charge density.
    
- Select appropriate integration variables and limits for a continuous charge distribution.
    

#### Integrating potential and energy

- Calculate the external work required to bring a charge from infinity to a point near other charges.
    
- Determine the electric potential energy of a charge placed within a multiple-charge configuration.
    
- Use electric potential to calculate the speed of a moving charged particle.
    
- Compare the usefulness of electric potential methods and direct Coulomb-force calculations.
    

Teaching challenge: Two equal and opposite point charges are separated by a fixed distance.

Explain why the electric potential at the midpoint is zero, even though the electric field at the midpoint is not zero.

Then extend your explanation to why adding potentials is mathematically simpler than adding electric field vectors.

## 23.4 — Equipotential Surfaces

Core question: What are equipotential surfaces, and how do they reveal the geometry and behavior of electric fields?

### Conceptual questions

- What is an equipotential surface?
    
- Why does moving a charge along an equipotential surface require zero net electrostatic work?
    
- Why are electric field lines perpendicular to equipotential surfaces?
    
- What would happen if an electric field had a component tangent to an equipotential surface?
    
- Why can two equipotential surfaces with different potential values never intersect?
    
- How does the spacing between equipotential surfaces relate to electric field strength?
    
- What do equipotential surfaces look like around an isolated point charge?
    
- What do equipotential surfaces look like in a uniform electric field?
    
- Why is the surface of a conductor in electrostatic equilibrium an equipotential?
    
- Why is the potential constant throughout the conducting material in electrostatic equilibrium?
    
- How do equipotential surfaces differ from electric field lines?
    
- Can an equipotential surface have a nonzero electric field at points on it?
    
- Can a region have uniform potential without containing any electric field?
    

### Mathematical relationships

Along an equipotential surface:

$$
\Delta V=0
$$

Therefore, the work done by the electrostatic field is:

$$
W_{\text{field}}=-q\Delta V=0
$$

For infinitesimal displacement:

$$
dV=-\vec E\cdot d\vec l
$$

Thus, for displacement tangent to an equipotential surface:

$$
\vec E\cdot d\vec l=0
$$

The electric field is therefore perpendicular to equipotential surfaces wherever the field is nonzero.

### Problem-solving checklist

- Sketch equipotential surfaces around an isolated positive or negative point charge.
    
- Sketch equipotential surfaces for an electric dipole.
    
- Sketch equipotential lines between two oppositely charged parallel plates.
    
- Determine electric field direction from an equipotential diagram.
    
- Estimate electric field magnitude using the separation between nearby equipotential surfaces.
    
- Calculate the work required to move a charge along an equipotential path.
    
- Determine the potential difference between two points using an equipotential map.
    
- Identify which regions of an equipotential diagram have stronger or weaker electric fields.
    
- Explain why equipotential surfaces and electric field lines meet at right angles.
    
- Sketch the equipotential regions of a conductor in electrostatic equilibrium.
    

Teaching challenge: A charged particle moves along a curved path that lies entirely on an equipotential surface.

Explain why the electric field does no net work on the particle, even though the electric field may be nonzero at every point along the path.

Then explain why this does not necessarily mean the particle experiences no force.

## 23.5 — Potential Gradient

Core question: How can we determine the magnitude and direction of an electric field from the way electric potential changes with position?

This is arguably the most important mathematical connection in the chapter, especially for more advanced electromagnetism.

### Conceptual questions

- What does the gradient of electric potential represent geometrically?
    
- Why does the electric field point in the direction of the greatest decrease in electric potential?
    
- Why is the electric field equal to the negative gradient of potential?
    
- What does the magnitude of the potential gradient tell us about electric field strength?
    
- How is the potential gradient related to directional derivatives from multivariable calculus?
    
- Why is the electric field perpendicular to equipotential surfaces?
    
- What does it mean for electric potential to vary in the $x$, $y$, or $z$ direction?
    
- How can we recover the electric field components from a known scalar potential function?
    
- How does the relationship between electric field and potential simplify one-dimensional problems?
    
- Why can the electric field be zero at a point even though the electric potential is nonzero?
    
- What is the difference between a region of constant potential and a point where the potential gradient is zero?
    
- How do the gradient and line integral describe opposite mathematical operations between electric field and potential?
    

### Mathematical relationships

The electric field is the negative gradient of the electric potential:

$$
\boxed{\vec E=-\nabla V}
$$

In Cartesian coordinates:

$$
\vec E= -\left( \frac{\partial V}{\partial x}\hat i+ \frac{\partial V}{\partial y}\hat j+ \frac{\partial V}{\partial z}\hat k \right)
$$

The individual field components are:

$$
E_x=-\frac{\partial V}{\partial x}
$$

$$
E_y=-\frac{\partial V}{\partial y}
$$

$$
E_z=-\frac{\partial V}{\partial z}
$$

For a one-dimensional potential function:

$$
\boxed{E_x=-\frac{dV}{dx}}
$$

The directional rate of change of potential along a unit vector $\hat u$ is:

$$
D_{\hat u}V=\nabla V\cdot\hat u
$$

This also gives:

$$
D_{\hat u}V=-\vec E\cdot\hat u
$$

### Problem-solving checklist

#### One-dimensional potential functions

- Calculate the electric field from a potential function $V(x)$.
    
- Determine the electric field direction from the slope of a potential-versus-position graph.
    
- Identify points where the electric field is zero using $dV/dx=0$.
    
- Determine regions where the electric field points in the positive or negative $x$-direction.
    
- Calculate the potential difference between two positions given an electric field function $E(x)$.
    
- Construct qualitative graphs of $E(x)$ from graphs of $V(x)$.
    

#### Multivariable potential functions

- Calculate $\vec E(x,y,z)$ from a scalar potential function.
    
- Evaluate the electric field vector at a particular point.
    
- Determine the magnitude and direction of the electric field from its Cartesian components.
    
- Find points where the electric field vanishes by solving $\nabla V=\vec 0$.
    
- Calculate the directional derivative of electric potential along a specified direction.
    
- Determine the direction in which electric potential increases or decreases most rapidly.
    
- Find the tangent plane to an equipotential surface using the gradient as its normal vector.
    

#### Connecting fields and potential

- Recover the potential difference between two points by integrating a known electric field.
    
- Verify that the gradient of a known point-charge potential reproduces Coulomb's electric field.
    
- Determine whether a given electric field can be represented by an electrostatic scalar potential.
    
- Explain why the electrostatic line integral around a closed path equals zero.
    
- Apply the gradient relationship to explain electric field directions on an equipotential map.
    

Teaching challenge: Consider the scalar potential function

$$
V(x,y)=3x^2+2y^2-4xy
$$

Derive the electric field, determine where it vanishes, and explain geometrically why the electric field is perpendicular to the level curves of the potential function.

Then explain how this relates to the gradient and directional derivatives you've already studied in Calculus III.

# Final Chapter Mastery Assessment

These eight problems are intended to test your ability to combine concepts across different sections.

|#|Problem|Primary concepts|
|---|---|---|
|1|Three fixed charges arranged in a triangle; calculate total potential energy|Energy, superposition, assembling charge systems|
|2|An electron accelerated between two plates with a known potential difference|Voltage, kinetic energy, charge signs|
|3|Two point charges producing zero potential but nonzero electric field|Scalar versus vector superposition|
|4|Calculate electric potential along the axis of a uniformly charged ring|Continuous charge distributions, integration, symmetry|
|5|Determine potential inside and outside a uniformly charged solid sphere|Gauss's law, field integration, continuity|
|6|Interpret an equipotential contour map|Field direction, potential difference, field magnitude|
|7|Given $V(x,y,z)$, calculate the electric field at a point|Partial derivatives, gradient, vector calculus|
|8|Given $\vec E(x,y)$, determine potential differences and whether the field is electrostatic|Line integrals, conservative fields, path independence|

# Five Questions That Demonstrate Deeper Understanding

These are the questions I'd especially recommend being able to answer verbally, without relying on equations initially.

### 1. How can electric potential be zero while the electric field is nonzero?

Explain how scalar potential contributions can cancel while vector electric field contributions reinforce one another.

Use an electric dipole as a concrete example.

### 2. Why does a negative charge move toward higher electric potential while losing electric potential energy?

Connect the relationship

$$
U=qV
$$

to the fact that the electric field direction is defined by the force on a positive test charge.

### 3. Why is electric potential a scalar while electric field is a vector?

Explain what information each quantity communicates and why calculating potential is often simpler than calculating electric field directly.

### 4. Why is the electric field the negative gradient of potential?

Connect conservative forces, changes in potential energy, directional derivatives, and the gradient.

Explain why the electric field points downhill in electric potential while the direction of force depends on the sign of the charge.

### 5. Why is the zero of electric potential arbitrary?

Explain why setting $V=0$ at infinity is a convenient convention rather than a physical requirement.

Discuss what changes—and what does not change—when a constant is added to an electric potential function.

# Suggested Teach-Back Video Structure

I'd split this chapter into four videos, each centered on one major conceptual connection.

|Video|Topic|Main objective|
|---|---|---|
|1|Electric Potential Energy and Work|Explain conservative forces, energy storage, and the work–energy relationship|
|2|Electric Potential and Voltage|Explain energy per unit charge, voltage differences, and particle motion|
|3|Calculating Potential and Equipotential Surfaces|Use superposition and continuous distributions, then interpret potential geometrically|
|4|Potential Gradient and the Electric Field|Derive and explain $\vec E=-\nabla V$, including its relation to multivariable calculus|

## A standard problem-solving procedure

1. Identify what is being asked. Are you finding electric potential, potential energy, potential difference, work, or electric field?

2. Identify the source of the electric potential. Is it a point charge, collection of charges, continuous distribution, or known electric field?

3. Choose a reference potential. Determine whether infinity is appropriate or whether another reference is specified.

4. Select the appropriate relationship. Use scalar superposition, a charge integral, an electric-field line integral, conservation of energy, or the potential gradient.

5. Apply the correct signs. Distinguish positive and negative source charges, test charges, potential differences, and work.

6. Solve and interpret. Calculate the desired quantity and explain what its sign, magnitude, and direction (where applicable) mean physically.

7. Check the result. Verify units, limiting behavior, reference conventions, and consistency with physical intuition.

## The most important connection to master

If I were to identify one relationship that unifies the entire chapter, it would be:

$$
\boxed{ \vec E=-\nabla V }
$$

This equation connects nearly everything you have studied so far:

- Coulomb's law describes the forces between charges.
    
- Electric fields describe the force per unit charge at each point in space.
    
- Electric potential describes potential energy per unit charge.
    
- Equipotential surfaces represent locations of equal electric potential.
    
- The gradient describes how potential changes with position.
    
- The negative gradient tells us the direction and magnitude of the electric field.
    

Since you've already been working extensively with gradients, directional derivatives, and tangent planes in Calculus III, this chapter gives you an opportunity to connect those abstract mathematical tools to a physical phenomenon.

A particularly worthwhile final exercise would be to start with the electric potential of a point charge,

$$
V(r)=\frac{1}{4\pi\varepsilon_0}\frac{q}{r},
$$

take its negative gradient to recover the electric field,

$$
\vec E(r)=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\hat r,
$$

and then use that electric field to determine the force on another charge.

That single derivation ties together potential, gradients, electric fields, and Coulomb's law. If you can explain each transition physically and mathematically, rather than merely manipulating the equations, you'll have developed a strong foundation for more advanced electromagnetism and electrical engineering.