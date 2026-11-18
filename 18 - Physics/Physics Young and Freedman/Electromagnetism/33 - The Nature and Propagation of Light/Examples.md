# Chapter 33 — Worked Examples

*Young and Freedman, University Physics with Modern Physics, 13th edition, Chapter 33, printed pp. 1087–1098.*

The six numbered examples below transcribe the textbook questions and solutions, with equations reformatted for Obsidian. Original numerical rounding and equation references are retained. Figure scans are stored in the adjacent `Figures` folder. The conceptual example has a single solution rather than the three-part solution headings used by the other examples.

# Example 33.1 — Reflection and refraction

## Question

In Fig. 33.11, material $a$ is water and material $b$ is glass with index of refraction 1.52. The incident ray makes an angle of $60.0^\circ$ with the normal; find the directions of the reflected and refracted rays.

![[Figures/Figure 33.11 - Water to glass.png]]

*Figure 33.11. Reflection and refraction of light passing from water to glass.*

## Solution

### Identify and Set Up

This is a problem in geometric optics. We are given the angle of incidence $\theta_a=60.0^\circ$ and the indexes of refraction $n_a=1.33$ and $n_b=1.52$. We must find the angles of reflection and refraction, $\theta_r$ and $\theta_b$; to do this we use Eqs. (33.2) and (33.4), respectively. Figure 33.11 shows the rays and angles; $n_b$ is slightly greater than $n_a$, so by Snell's law [Eq. (33.4)] $\theta_b$ is slightly smaller than $\theta_a$, as the figure shows.

### Execute

According to Eq. (33.2), the angle the reflected ray makes with the normal is the same as that of the incident ray, so $\theta_r=\theta_a=60.0^\circ$.

To find the direction of the refracted ray we use Snell's law, Eq. (33.4):

$$
n_a\sin\theta_a=n_b\sin\theta_b
$$

$$
\sin\theta_b=\frac{n_a}{n_b}\sin\theta_a
=\frac{1.33}{1.52}\sin60.0^\circ=0.758
$$

$$
\theta_b=\arcsin(0.758)=49.3^\circ
$$

### Evaluate

The second material has a larger refractive index than the first, as in Fig. 33.8a. Hence the refracted ray is bent toward the normal and $\theta_b<\theta_a$.

# Example 33.2 — Index of refraction in the eye

## Question

The wavelength of the red light from a helium-neon laser is 633 nm in air but 474 nm in the aqueous humor inside your eyeball. Calculate the index of refraction of the aqueous humor and the speed and frequency of the light in it.


## Solution

### Identify and Set Up

The key ideas here are (i) the definition of index of refraction $n$ in terms of the wave speed $v$ in a medium and the speed $c$ in vacuum, and (ii) the relationship between wavelength $\lambda_0$ in vacuum and wavelength $\lambda$ in a medium of index $n$. We use Eq. (33.1), $n=c/v$; Eq. (33.5), $\lambda=\lambda_0/n$; and $v=\lambda f$.

### Execute

The index of refraction of air is very close to unity, so we assume that the wavelength $\lambda_0$ in vacuum is the same as that in air, 633 nm. Then from Eq. (33.5),

$$
\lambda=\frac{\lambda_0}{n}
\qquad
n=\frac{\lambda_0}{\lambda}
=\frac{633\ \mathrm{nm}}{474\ \mathrm{nm}}=1.34
$$

This is about the same index of refraction as for water. Then, using $n=c/v$ and $v=\lambda f$, we find

$$
v=\frac{c}{n}
=\frac{3.00\times10^8\ \mathrm{m/s}}{1.34}
=2.25\times10^8\ \mathrm{m/s}
$$

$$
f=\frac{v}{\lambda}
=\frac{2.25\times10^8\ \mathrm{m/s}}{474\times10^{-9}\ \mathrm{m}}
=4.74\times10^{14}\ \mathrm{Hz}
$$

### Evaluate

Note that while the speed and wavelength have different values in air and in the aqueous humor, the frequency in air, $f_0$, is the same as the frequency in the aqueous humor:

$$
f_0=\frac{c}{\lambda_0}
=\frac{3.00\times10^8\ \mathrm{m/s}}{633\times10^{-9}\ \mathrm{m}}
=4.74\times10^{14}\ \mathrm{Hz}
$$

When a light wave passes from one material into another, the wave speed and wavelength both change but the wave frequency is unchanged.

# Example 33.3 — A twice-reflected ray

## Question

Two mirrors are perpendicular to each other. A ray traveling in a plane perpendicular to both mirrors is reflected from one mirror, then the other, as shown in Fig. 33.12. What is the ray's final direction relative to its original direction?

![[Figures/Figure 33.12 - Perpendicular mirrors.png]]

*Figure 33.12. A ray moving in the $xy$-plane. The first reflection changes the sign of the $y$-component of its velocity, and the second reflection changes the sign of the $x$-component. For a different ray with a $z$-component of velocity, a third mirror (perpendicular to the two shown) could be used to change the sign of that component.*

## Solution

### Identify and Set Up

This problem involves the law of reflection, which we must apply twice (once for each mirror).

### Execute

For mirror 1 the angle of incidence is $\theta_1$, and this equals the angle of reflection. The sum of interior angles in the triangle shown in the figure is $180^\circ$, so we see that the angles of incidence and reflection for mirror 2 are both $90^\circ-\theta_1$. The total change in direction of the ray after both reflections is therefore $2(90^\circ-\theta_1)+2\theta_1=180^\circ$. That is, the ray's final direction is opposite to its original direction.

### Evaluate

An alternative viewpoint is that reflection reverses the sign of the component of light velocity perpendicular to the surface but leaves the other components unchanged. We invite you to verify this in detail. You should also be able to use this result to show that when a ray of light is successively reflected by three mirrors forming a corner of a cube (a “corner reflector”), its final direction is again opposite to its original direction. This principle is widely used in tail-light lenses and bicycle reflectors to improve their night-time visibility. Apollo astronauts placed arrays of corner reflectors on the moon. By use of laser beams reflected from these arrays, the earth–moon distance has been measured to within 0.15 m.

# Conceptual Example 33.4 — A leaky periscope

## Question

A submarine periscope uses two $45^\circ$–$45^\circ$–$90^\circ$ prisms with total internal reflection on the sides adjacent to the $45^\circ$ angles. Explain why the periscope will no longer work if it springs a leak and the bottom prism is covered with water.

![[Figures/Figure 33.14a - Total reflection in a prism.png]]

*Related chapter figure: Fig. 33.14(a), illustrating total internal reflection at the $45^\circ$ faces of a glass prism. The conceptual example does not specify a separate figure.*

## Solution

The critical angle for water ($n_b=1.33$) on glass ($n_a=1.52$) is

$$
\theta_{\mathrm{crit}}=\arcsin\frac{1.33}{1.52}=61.0^\circ
$$

The $45^\circ$ angle of incidence for a totally reflecting prism is smaller than this new $61^\circ$ critical angle, so total internal reflection does not occur at the glass–water interface. Most of the light is transmitted into the water, and very little is reflected back into the prism.

# Example 33.5 — Two polarizers in combination

## Question

In Fig. 33.25 the incident unpolarized light has intensity $I_0$. Find the intensities transmitted by the first and second polarizers if the angle between the axes of the two filters is $30^\circ$.

![[Figures/Figure 33.25 - Polarizer and analyzer.png]]

*Figure 33.25. An ideal analyzer transmits only the electric field component parallel to its transmission direction (that is, its polarizing axis).*

## Solution

### Identify and Set Up

This problem involves a polarizer (a polarizing filter on which unpolarized light shines, producing polarized light) and an analyzer (a second polarizing filter on which the polarized light shines). We are given the intensity $I_0$ of the incident light and the angle $\phi=30^\circ$ between the axes of the polarizers. We use Malus's law, Eq. (33.7), to solve for the intensities of the light emerging from each polarizer.

### Execute

The incident light is unpolarized, so the intensity of the linearly polarized light transmitted by the first polarizer is $I_0/2$. From Eq. (33.7) with $\phi=30^\circ$, the second polarizer reduces the intensity by a further factor of $\cos^230^\circ=3/4$. Thus the intensity transmitted by the second polarizer is

$$
\left(\frac{I_0}{2}\right)\left(\frac34\right)=\frac38 I_0
$$

### Evaluate

Note that the intensity decreases after each passage through a polarizer. The only situation in which the transmitted intensity does not decrease is if the polarizer is ideal (so it absorbs none of the light that passes through it) and if the incident light is linearly polarized along the polarizing axis, so $\phi=0$.

# Example 33.6 — Reflection from a swimming pool's surface

## Question

Sunlight reflects off the smooth surface of a swimming pool. (a) For what angle of reflection is the reflected light completely polarized? (b) What is the corresponding angle of refraction? (c) At night, an underwater floodlight is turned on in the pool. Repeat parts (a) and (b) for rays from the floodlight that strike the surface from below.

![[Figures/Figure 33.29 - Swimming pool sketches.png]]

*Figure 33.29. Our sketches for this problem.*

## Solution

### Identify and Set Up

This problem involves polarization by reflection at an air–water interface in parts (a) and (b) and at a water–air interface in part (c). Figure 33.29 shows our sketches. For both cases our first target variable is the polarizing angle $\theta_p$, which we find using Brewster's law, Eq. (33.8). For this angle of reflection, the angle of refraction $\theta_b$ is the complement of $\theta_p$ (that is, $\theta_b=90^\circ-\theta_p$).

### Execute

(a) During the day (shown in the upper part of Fig. 33.29) the light moves in air toward water, so $n_a=1.00$ (air) and $n_b=1.33$ (water). From Eq. (33.8),

$$
\theta_p=\arctan\frac{n_b}{n_a}
=\arctan\frac{1.33}{1.00}=53.1^\circ
$$

(b) The incident light is at the polarizing angle, so the reflected and refracted rays are perpendicular; hence

$$
\theta_b=90^\circ-\theta_p=90^\circ-53.1^\circ=36.9^\circ
$$

(c) At night (shown in the lower part of Fig. 33.29) the light moves in water toward air, so now $n_a=1.33$ and $n_b=1.00$. Again using Eq. (33.8), we have

$$
\theta_p=\arctan\frac{1.00}{1.33}=36.9^\circ
$$

$$
\theta_b=90^\circ-36.9^\circ=53.1^\circ
$$

### Evaluate

We check our answer in part (b) by using Snell's law, $n_a\sin\theta_a=n_b\sin\theta_b$, to solve for $\theta_b$:

$$
\sin\theta_b=\frac{n_a\sin\theta_p}{n_b}
=\frac{1.00\sin53.1^\circ}{1.33}=0.600
$$

$$
\theta_b=\arcsin(0.600)=36.9^\circ
$$

Note that the two polarizing angles found in parts (a) and (c) add to $90^\circ$. This is not an accident; can you see why?
