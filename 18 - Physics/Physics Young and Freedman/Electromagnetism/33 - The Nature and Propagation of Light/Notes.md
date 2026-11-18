# Chapter 33 — The Nature and Propagation of Light

*University Physics with Modern Physics — Young and Freedman, 13th edition.*

# The Nature of Light

## Wave and Particle Descriptions

Light is an electromagnetic wave. Recall that accelerating electric charges produce electromagnetic radiation, whose electric and magnetic fields oscillate perpendicular to each other and to the direction of propagation.

The wave description is especially useful for understanding propagation, interference, and polarization. When light is emitted or absorbed, its energy is transferred in discrete packets called **photons**. These descriptions concern different aspects of the same phenomenon.

All electromagnetic radiation travels at the same speed in vacuum:

$$
c=2.99792458\times10^8\ \mathrm{m/s}
\approx3.00\times10^8\ \mathrm{m/s}
$$

Hot objects emit a range of wavelengths through thermal radiation. At a high enough temperature, enough of that radiation is visible for the object to glow. Gas discharges provide another source of light. A laser differs from an ordinary source because its emission is coordinated, producing a highly directional, coherent beam with a narrow range of frequencies.

## Wave Fronts and Rays

A **wave front** is a surface connecting adjacent points at the same phase of oscillation. For example, a diagram may show successive surfaces where the electric field reaches its maximum. Corresponding wave fronts one complete cycle apart are separated by one wavelength.

A **ray** is an imaginary line showing the direction of propagation. In a homogeneous, isotropic material, rays are straight and perpendicular to the wave fronts.

- A pointlike source produces spherical wave fronts; its rays spread radially outward.
- Far from that source, a small part of a spherical wave front is approximately flat. We can treat it as a plane wave with parallel rays.
- A material is **homogeneous** when its properties are the same from place to place, and **isotropic** when they are the same in every direction.

**A RAY IS A DIRECTIONAL MODEL, NOT AN EXTRA PHYSICAL OBJECT.** Geometric optics follows rays; physical optics keeps the wave behavior explicit. The ray model is useful when diffraction effects are negligible for the situation being studied.

# Reflection and Refraction

When light reaches an interface between two transparent materials, part generally returns into the first material by **reflection**, while part enters the second material by **refraction**, or transmission.

At a smooth surface, reflected rays have definite directions: **specular reflection**. A rough surface produces **diffuse reflection**, with rays leaving in many directions because the local surface normals differ. The law of reflection still applies at each small surface element.

## Index of Refraction

The **index of refraction** compares the vacuum speed of light with its speed in a material:

$$
n=\frac{c}{v}
\qquad\text{or}\qquad
v=\frac{c}{n}
\tag{33.1}
$$

$n$ has no units. For the transparent optical materials discussed here, a larger index means a **smaller wave speed**. Vacuum has $n=1$; air is close enough to 1 for most chapter problems. Water is approximately 1.33 and typical crown glass approximately 1.52, with the precise value depending on wavelength and conditions.

## Angles at an Interface

Draw the **normal**, perpendicular to the surface at the point where the ray arrives. Measure the incident, reflected, and refracted angles from that normal, not from the surface.

The incident ray, reflected ray, refracted ray, and normal lie in one plane: the **plane of incidence**.

### Law of Reflection

$$
\theta_r=\theta_a
\tag{33.2}
$$

$\theta_a$ is the incident angle and $\theta_r$ is the reflected angle. The rays are on opposite sides of the normal in the incident medium.

### Snell's Law of Refraction

$$
n_a\sin\theta_a=n_b\sin\theta_b
\tag{33.4}
$$

The subscripts identify the materials: $a$ is where the light comes from; $b$ is where it is transmitted. $\theta_b$ is the refracted angle.

| Transition | Speed change | Direction of transmitted ray |
| --- | --- | --- |
| Into a larger $n$ | Slower | Toward the normal: $\theta_b<\theta_a$ |
| Into a smaller $n$ | Faster | Away from the normal, if transmission occurs |
| Normal incidence | Speed may change | No change in direction |

**NO BENDING DOES NOT MEAN NO REFRACTION EFFECTS.** At normal incidence, speed and wavelength can still change. If the two indexes are equal, Snell's law also gives no bending.

For several surfaces, draw a new normal at each interface. An angle measured from one surface's normal cannot automatically be reused at another surface.


## Frequency and Wavelength in a Material

The source fixes the frequency. At a stationary boundary, the transmitted wave has the same frequency as the incident wave; the boundary does not continually accumulate or remove cycles.

$$
f=\frac{c}{\lambda_0}=\frac{v}{\lambda}
$$

Here $\lambda_0$ is the vacuum wavelength and $\lambda$ is the wavelength in the material:

$$
\lambda=\frac{\lambda_0}{n}
\tag{33.5}
$$

So what becomes shorter when light enters glass? Its wavelength, because the wave travels more slowly while completing the same number of cycles per second. **The frequency does not decrease with the speed.** Between two media, $\lambda_b/\lambda_a=n_a/n_b$.

**needs expansion — Wavelength in a Material:** connect unchanged frequency, $v=f\lambda$, and $n=c/v$, explaining which wavelength is measured in vacuum.

Refraction also explains why a submerged object can appear displaced: the eye traces arriving rays backward as though they had traveled straight. The actual object lies along the refracted paths, not necessarily along that apparent straight continuation.

# Total Internal Reflection

Light going from a larger refractive index to a smaller one bends away from the normal. As the incident angle increases, the transmitted ray approaches the surface.

At the **critical angle**, $\theta_{\mathrm{crit}}$, the limiting refracted angle is $90^\circ$:

$$
\sin\theta_{\mathrm{crit}}=\frac{n_b}{n_a},
\qquad n_a>n_b
\tag{33.6}
$$

Beyond this angle, Snell's law would require $\sin\theta_b>1$. There is no propagating refracted ray into the second medium, and the light is totally internally reflected in the ideal lossless situation.

**CHECK BOTH REQUIREMENTS:** the incident medium must have the larger index, and the incident angle must exceed the critical angle. At the critical angle itself, the transmitted ray is the grazing limit; the book includes this boundary with total reflection because the transmitted power across the interface tends to zero.

For glass to air with $n_a=1.52$, the critical angle is approximately $41.1^\circ$. Reversing the direction to air-to-glass does not give total internal reflection.

**needs expansion — Critical-Angle Equation:** use the grazing transmitted ray in Snell's law, and explain why the index ratio must be less than one.

## Prisms, Optical Fibers, and Gems

A glass prism can redirect light using internal reflections rather than a metallic mirror coating. Whether it works depends on the index of the material **outside** the reflecting face as well as the glass itself. Covering that face with water can raise the critical angle enough to prevent total reflection.

An optical fiber confines light in a higher-index interior surrounded by a lower-index material, provided its rays meet the boundary at suitable angles. Bending the fiber too sharply can spoil those conditions and let light escape.

Diamond's high index produces a small critical angle. Appropriate cuts encourage repeated internal reflection and return light through the front faces. Its strong dispersion adds the separation into colors.

# Dispersion

**Dispersion** is the dependence of wave speed, and hence refractive index, on frequency or wavelength. The wavelength used to label optical index data is commonly the **vacuum wavelength**.

For the usual visible-light behavior of the materials in this chapter, violet light has a larger index than red light. Violet therefore travels more slowly and is deviated more strongly by a prism; red is deviated less.

White light contains many wavelengths. A prism sends them in different directions because they experience different indexes. **The prism separates existing frequency components; it does not create the colors by changing their frequencies.** A large index alone does not guarantee large dispersion: the variation of index across the wavelengths matters.

The dependence relation is expressed by $\lambda = \lambda_0 / n$, where lambda is the wavelength after dispersion and lambda-nought is before. $n$ is the index of refraction for that material. For some materials $n$ decreases with increasing wavelength and decreasing frequency. However, in some materials $n$ increases with decreasing wavelength and increasing frequency. 

In these materials, light of longer wavelength has a greater speed than shorter wavelengths.

![[Pasted image 20261029131503.png]]
## Rainbows

A primary rainbow combines refraction into a water drop, one internal reflection, and refraction back out. Dispersion causes different colors to leave at different angles. The sun is behind the observer, and the rainbow is centered on the direction opposite the sun.

Red appears on the outer edge of the primary bow, at roughly $42^\circ$ from that opposite-sun direction; violet is on the inner edge, near $41^\circ$. Different drops supply the different rays reaching the observer.

A secondary rainbow involves **two internal reflections**. It is fainter, lies outside the primary bow, and has its color order reversed. The reflections involved in forming a rainbow need not be total internal reflections.

# Polarization

Polarization describes the orientation and time behavior of the **electric field** of an electromagnetic wave. It is a feature of transverse waves. The electric and magnetic fields remain perpendicular to the direction of propagation.

For **linearly polarized** light, the electric field oscillates along a fixed transverse direction. Ordinary unpolarized light is a mixture with randomly varying transverse polarization directions. It is not light with no electric field, nor a longitudinal wave.

This use of “polarization” is distinct from the electric-charge displacement inside a dielectric discussed in electrostatics.

In polarization, we are typically concerned only with the behavior of electrons and thus the electric field, not the magnetic field.  

## Polarizing Filters

An ideal polarizer transmits the electric-field component parallel to its **transmission axis** and blocks the perpendicular component. The emerging light is linearly polarized along that axis.

In many light sources, there are a large amount of molecules with random orientations and so the emitted light is a random mixture of waves linearly polarized in all possible transverse directions. The light is then said to be **unpolarized** or **natural light**. To create polarized light from such sources, it requires a filter analogous to the slot for mechanical waves.

For a conducting-wire grid, the transmitted direction is **perpendicular to the wires**: the field parallel to the wires drives currents and is strongly suppressed. The physical wire direction and the transmission axis are not the same.

For unpolarized incident intensity $I_0$, an ideal polarizer transmits:

$$
I_1=\frac{I_0}{2}
$$

This result is independent of the filter's orientation. Real polarizers also absorb some light along their transmission axis and may transmit a small amount of the nominally blocked component.

**needs expansion — Half-Intensity Rule for Unpolarized Light:** resolve the randomly oriented field into perpendicular components and explain their equal average intensity contributions.

## Malus's Law

When the incident light is **already linearly polarized**, the intensity transmitted through an ideal analyzer is:

$$
I=I_{\max}\cos^2\phi
\tag{33.7}
$$

$\phi$ is the angle between the incident polarization direction and the analyzer's transmission axis. In this ideal case, $I_{\max}$ equals the intensity incident on the analyzer.

| Relative direction | Result |
| --- | --- |
| Aligned, $\phi=0^\circ$ | Full incident polarized intensity transmitted |
| $\phi=45^\circ$ | Half transmitted |
| Crossed, $\phi=90^\circ$ | Zero transmitted |

The field amplitude is multiplied by $\cos\phi$; intensity is multiplied by $\cos^2\phi$. **DO NOT CONFUSE AMPLITUDE WITH INTENSITY.**

For a sequence of filters, first determine the polarization and intensity arriving at each one. Unpolarized light loses half its intensity at the first ideal filter; afterward, use Malus's law with the angle between successive axes. Do not apply the half-intensity rule again at every filter.

**needs expansion — Malus's Law:** connect the transmitted field component to the fact that electromagnetic-wave intensity is proportional to the square of field amplitude.

## Polarization by Reflection and Brewster's Law

Reflection from a transparent dielectric surface generally favors the component perpendicular to the plane of incidence, making the reflected light partially polarized.

At the **polarizing angle**, or **Brewster angle**, $\theta_p$, the reflected light from unpolarized illumination is completely linearly polarized perpendicular to the plane of incidence. The reflected and refracted rays are perpendicular:

$$
\tan\theta_p=\frac{n_b}{n_a}
\tag{33.8}
$$

$$
\theta_p+\theta_b=90^\circ
$$

Use the index ratio for the actual direction of incidence. The transmitted light is still generally only **partially polarized**. Brewster's angle does not mean that all incident light is reflected, nor that all reflected light disappears; only the reflected component polarized in the plane of incidence vanishes.

Polarizing sunglasses suppress glare from a horizontal surface by using a vertical transmission axis. Such glare is predominantly horizontally polarized.

**needs expansion — Brewster's Law:** use the perpendicular reflected and refracted rays with Snell's law, explaining why the relevant angles are complementary.

## Circular and Elliptical Polarization

Two coherent, perpendicular electric-field components can combine into different polarization states:

| Relationship | Combined field at a fixed point |
| --- | --- |
| In phase, or opposite in phase | Oscillates along a fixed line |
| Equal amplitudes and a quarter-cycle phase difference | Rotates with constant magnitude: circular polarization |
| More general amplitudes and phase difference | Usually traces an ellipse: elliptical polarization |

For circular polarization, the rotating field remains transverse; the light does not propagate around a circle. A direction such as “clockwise” must specify the viewing direction.

A **birefringent** material gives different wave speeds to two perpendicular polarization components. A **quarter-wave plate** introduces a quarter-cycle relative phase shift. It converts linear to circular polarization when the incident linear polarization provides equal components along its two principal axes; other orientations generally give elliptical or unchanged linear polarization.

**needs expansion — Circular Polarization and the Quarter-Wave Plate:** relate perpendicular field components, their amplitudes, and their relative phase, showing why equal components are required for a circle.

Some materials become birefringent under stress. Between crossed polarizers, this changes the transmitted polarization and produces bright or colored patterns. **Photoelasticity** uses those patterns to investigate stress distributions.

# Scattering of Light

An incident electric field drives charges in molecules into oscillation. Those charges reradiate, sending some of the light into other directions: **scattering**.

For molecular scattering in the regime discussed here, the scattering strength varies approximately as:

$$
\text{scattering strength}\propto f^4\propto\frac{1}{\lambda^4}
$$

Compare this wavelength dependence for otherwise comparable conditions and incident intensities. Shorter visible wavelengths are scattered much more strongly than longer ones.

- **Blue sky:** off-axis sunlight reaching the eye has been scattered by atmospheric molecules, which favor shorter wavelengths.
- **Red sunsets:** the direct beam travels a long path through the atmosphere, losing much of its shorter-wavelength light to scattering before reaching the observer.
- **White clouds:** water droplets and ice crystals scatter a broad range of visible wavelengths effectively. The simple molecular $1/\lambda^4$ rule is not the general rule for these larger scatterers.

Scattering also polarizes light. An oscillating charge does not radiate along its oscillation direction. In the ideal single-scattering picture, light observed at $90^\circ$ to the incident beam is linearly polarized perpendicular to the scattering plane. Actual skylight is often only partially polarized because many scattering paths contribute.

**needs expansion — Wavelength Dependence and Polarization of Molecular Scattering:** distinguish the qualitative oscillating-charge argument from the fuller calculation giving the fourth-power dependence.

# Huygens's Principle

Huygens's principle constructs a later wave front from an earlier one. Treat points on the original front as sources of secondary wavelets. After an interval $\Delta t$, each wavelet has traveled a distance $v\Delta t$ in a uniform medium. The new wave front is the forward envelope tangent to these wavelets.

This is a convenient geometrical picture of wave propagation, consistent with the more fundamental electromagnetic description. The secondary wavelets are construction elements; they do not represent additional independent light sources that create extra energy.

## Reflection from Wave Fronts

Incident and reflected waves travel in the same material. Equal propagation distances over equal time intervals lead to the geometry of equal incident and reflected angles.

**needs expansion — Law of Reflection from Huygens's Principle:** construct the incident and reflected wave fronts and identify the congruent right triangles giving $\theta_r=\theta_a$.

## Refraction from Wave Fronts

Parts of an oblique wave front reach the second material at different times. Because propagation speeds differ, the transmitted front changes orientation. The associated ray changes direction with it.

The wave-front construction gives:

$$
\frac{\sin\theta_a}{\sin\theta_b}=\frac{v_a}{v_b}
\tag{33.9}
$$

Using $n=c/v$ turns this into Snell's law. Slower propagation in the second material corresponds to the ray bending toward the normal.

**needs expansion — Snell's Law from Huygens's Principle:** compare wavelet radii $v_a\Delta t$ and $v_b\Delta t$, identify the common geometric length, and explain the substitution from speeds to indexes.

## Mirages

Hot air close to a sun-heated surface is less dense and has a slightly smaller index than cooler air above it. Light travels faster in that lower layer. A wave front therefore turns as it propagates through the changing conditions, and a ray can curve upward toward the observer.

The eye traces that arriving ray backward along a straight line, creating an apparent image below the actual object, as though a reflecting sheet of water were present. The apparent “water” is an optical effect of the changing air conditions.



# Questions for Professor

Example of the fish in water. Aiming the spear I have to aim below, laser I aim at the fish, but the relation is the light from the fish to me, not my observation point to the fish?

![[Pasted image 20261029142522.png]]

![[Pasted image 20261029142537.png]]

In dispersion and refraction in general, the angle of refraction is dependent upon wavelength, so different wavelengths deviate differently?

Polarization and polarizing filters

For filtering from say an isotropic light point source, does it work something like this?

![[Pasted image 20261029144557.png]]