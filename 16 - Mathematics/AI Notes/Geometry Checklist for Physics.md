Yes. I’d organize the practice by the actual geometric skill you need rather than by physics chapter.

1. **Parallel/perpendicular lines and angle chasing**

Example:  
Two parallel horizontal lines are cut by a diagonal transversal. One acute angle is \(37^\circ\). Find every other angle formed.

Then make it slightly more physics-like:

> A ramp makes an angle \(\theta\) with the horizontal. A normal force is perpendicular to the ramp, and gravity is vertical. Prove that the angle between gravity and the inward normal is also \(\theta\).

This is the kind of thing that helps with inclines, electric fields, and torque diagrams.

2. **Right-triangle construction from a vector**

Example:

> A force of magnitude \(80\text{ N}\) acts \(35^\circ\) above the horizontal. Find its horizontal and vertical components.

The important part is not just computing

\[ F_x=F\cos\theta,\qquad F_y=F\sin\theta, \]

but being able to draw the right triangle yourself and explain why \(F_x\) is adjacent to \(\theta\).

3. **Projection onto a chosen direction**

Example:

> A \(50\text{ N}\) force acts at \(40^\circ\) to a lever arm. What component of the force is perpendicular to the lever arm?

You want to recognize that the relevant component is

\[ F_\perp=F\sin 40^\circ. \]

This directly prepares you for torque, work, flux, and vector components.

4. **Similar triangles**

Example:

> A \(2\text{ m}\) pole casts a \(3\text{ m}\) shadow. At the same time, a building casts a \(24\text{ m}\) shadow. Find the building height.

Then a more physics-relevant version:

> Two rays or vectors produce triangles with the same angles. Use similarity to derive one unknown distance in terms of the others.

Similar-triangle reasoning shows up surprisingly often in optics, fields, geometry of motion, and derivations.

5. **Finding a segment from geometry**

Example:

> A cable of length \(L\) runs from the ground to the top of a vertical pole and makes angle \(\theta\) with the ground. Express the height \(h\) and horizontal distance \(x\) in terms of \(L\) and \(\theta\).

You should get

\[ h=L\sin\theta,\qquad x=L\cos\theta. \]

This is exactly the kind of “develop an expression for a segment” practice you were asking about.

6. **Finding an angle from lengths**

Example:

> A right triangle has vertical height \(h\) and horizontal base \(x\). Derive an expression for the angle \(\theta\) at the base.

\[ \tan\theta=\frac{h}{x} \]

so

\[ \theta=\tan^{-1}\left(\frac{h}{x}\right). \]

This is basically your original drawing.

7. **Circles, radii, and tangents**

Example:

> A line is tangent to a circle at point \(P\). Draw the radius from the center to \(P\). What angle does the radius make with the tangent?

Answer:

\[ 90^\circ. \]

Then extend it:

> Given the center, radius, and an external point, construct the right triangle formed by the radius, tangent segment, and line to the center.

This geometry matters a lot for circular motion and rotational mechanics.

8. **Cylindrical geometry**

Example:

> A cylinder has radius \(r\) and length \(L\). Derive its lateral surface area without memorizing the formula.

Unwrap it into a rectangle:

\[ \text{width}=2\pi r,\qquad \text{height}=L, \]

so

\[ A=2\pi rL. \]

This is exactly the geometry behind the Gaussian cylinder for an infinite line charge.

9. **Spherical shells and “subtracting volumes”**

Example:

> A spherical shell has inner radius \(a\) and outer radius \(b\). Derive the volume of the material.

\[ V=\frac43\pi b^3-\frac43\pi a^3 \]

or

\[ V=\frac43\pi(b^3-a^3). \]

Then make it Gauss-law-like:

> A Gaussian sphere of radius \(r\) lies within material extending from \(a\) to \(b\), with \(a<r<b\). What volume of charged material is enclosed?

\[ V_{\text{enc}}=\frac43\pi(r^3-a^3). \]

That is probably very close to the kind of expression that bothered you before.

10. **Area and surface normal geometry**

Example:

> A flat surface of area \(A\) is tilted so that its normal makes angle \(\theta\) with a uniform vector field \(\vec E\). What is the effective projected area perpendicular to the field?

\[ A_\perp=A\cos\theta. \]

That leads directly into electric flux:

\[ \Phi=EA\cos\theta. \]

The crucial geometric skill is understanding that the angle is between the field and the **surface normal**, not usually between the field and the surface itself.

11. **Static equilibrium with hanging masses**

Example:

> A \(20\text{ kg}\) mass hangs from two cables. The left cable makes \(30^\circ\) with the horizontal and the right cable makes \(45^\circ\). Find the two tensions.

You first construct two component triangles:

\[ T_{1x},T_{1y},T_{2x},T_{2y}. \]

Then use

\[ \sum F_x=0,\qquad \sum F_y=0. \]

This is especially good practice because it combines angle interpretation, right triangles, components, and algebra.

12. **Torque and lever-arm geometry**

Example:

> A wrench of length \(0.30\text{ m}\) has a \(100\text{ N}\) force applied at \(40^\circ\) to the wrench. Find the torque.

You should be able to solve it in two equivalent geometric ways:

\[ \tau=rF\sin\theta \]

or find

\[ F_\perp=F\sin\theta \]

first and then

\[ \tau=rF_\perp. \]

A very useful variation is:

> Find the perpendicular moment arm instead of the perpendicular force component.

13. **Centripetal acceleration geometry**

Example:

> A ball moves in a horizontal circle on a string. At one instant its velocity points east. Draw the directions of velocity, centripetal acceleration, and net force.

Then:

> If the string is tilted so that tension has both vertical and horizontal components, determine which component produces the centripetal acceleration.

This is less about triangle calculation and more about understanding that “radial” and “tangential” are geometric directions.

14. **2D electric-field superposition**

Example:

> Two equal positive charges are located at \((-a,0)\) and \((a,0)\). Find the electric field at \((0,y)\).

For each charge, draw the field vector and construct its component triangle.

By symmetry, the horizontal components cancel and the vertical components add.

This is fantastic practice because it forces you to identify:

- the displacement vector,
- the field direction,
- the angle,
- which components cancel,
- which components reinforce.

15. **Asymmetric 2D vector superposition**

Example:

> A charge \(q_1\) is at \((0,0)\), a charge \(q_2\) is at \((3,0)\), and you want the field at \((2,4)\). Find the net electric field.

Now symmetry does not rescue you. You have to calculate distances such as

\[ r=\sqrt{(\Delta x)^2+(\Delta y)^2} \]

and generate the direction from geometry.

That is a very good bridge between ordinary geometry and vector calculus.

16. **Parallel-plate capacitor particle deflection**

Example:

> A proton enters horizontally between parallel plates with initial speed \(v_0\). The electric field points vertically downward. Find its trajectory.

The geometry separates naturally into:

\[ x=v_0t \]

and

\[ y=\frac12at^2, \]

where

\[ a=\frac{qE}{m}. \]

Then eliminate \(t\) using

\[ t=\frac{x}{v_0}. \]

This builds intuition for why the path is parabolic.

17. **Gaussian surface selection**

Example:

> For each charge distribution, choose a Gaussian surface and explain geometrically why it works:
> 
> - point charge,
> - infinite line charge,
> - infinite plane,
> - uniformly charged sphere.

You want the associations to become automatic:

\[ \text{point}\rightarrow\text{sphere} \]\[ \text{line}\rightarrow\text{coaxial cylinder} \]\[ \text{plane}\rightarrow\text{pillbox} \]

The important exercise is not just naming the surface but explaining:

> Where is \(\vec E\) parallel to \(d\vec A\)? Where is it perpendicular? Where is \(E\) constant?

18. **Charge density translated into geometry**

Example:

> A rod of length \(L\) has uniform linear charge density \(\lambda\). Find its total charge.

\[ Q=\lambda L. \]

Then:

> A disk of area \(A\) has surface charge density \(\sigma\).

\[ Q=\sigma A. \]

Then:

> A sphere of volume \(V\) has volume charge density \(\rho\).

\[ Q=\rho V. \]

Then make them partial:

> How much charge is enclosed only up to radius \(r\)?

That forces you to combine density with the appropriate geometric measure.

If you want the **highest-yield subset**, I would probably focus on just these eight:

\[ \boxed{ \begin{array}{l} \text{angle chasing}\\ \text{right-triangle construction}\\ \text{vector projection}\\ \text{similar triangles}\\ \text{cylinder/sphere geometry}\\ \text{surface normals}\\ \text{2D vector superposition}\\ \text{geometric symmetry} \end{array}} \]

Those eight account for a huge fraction of the geometry that has been showing up in the physics topics you've found difficult.