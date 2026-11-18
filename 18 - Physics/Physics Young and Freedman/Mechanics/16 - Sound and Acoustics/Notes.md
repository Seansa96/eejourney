# Sound Waves

Recall that a longitudinal wave has particles moving parallel to the direction in which the disturbance travels. Sound in air works this way: the particles oscillate back and forth, producing compressions and rarefactions that travel through the air.

Sound needs a material medium. It can travel through gases, liquids, and solids, but not through a vacuum. The wave transfers energy while the particles oscillate around their equilibrium positions; they do not travel from the source to your ear with the sound.

The approximate range of human hearing is $20$ to $20{,}000\ \mathrm{Hz}$. Lower frequencies are **infrasonic**, and higher frequencies are **ultrasonic**. These are still sound waves even when we cannot hear them.

## Displacement and Pressure

We can describe a sinusoidal sound wave moving in the positive $x$-direction with the same kind of wave function used in the previous chapter:

$$
y(x,t)=A\cos(kx-\omega t)
$$

Here $y$ is the particle's displacement from its equilibrium position $x$. Despite the letter $y$, this displacement is **along** the direction of propagation. A sinusoidal graph of a sound wave does not mean the air particles are moving up and down.

We can also describe the same wave using its **pressure fluctuation**, $p(x,t)$. This is the amount above or below the equilibrium pressure, not the full absolute pressure:

$$
p_{\mathrm{absolute}}=p_0+p(x,t)
$$

Your eardrum responds to a pressure difference across it, so pressure is often the more useful description.

The connection between displacement and pressure is

$$
p(x,t)=-B\frac{\partial y}{\partial x}
$$

where $B$ is the **bulk modulus**, which measures how strongly the medium resists compression. A larger $B$ means a greater pressure change is needed for the same fractional change in volume.

Why do we use a spatial derivative rather than just the displacement itself? If neighboring particles all shift the same distance, their spacing does not change. Compression depends on the *difference* in their displacements: whether they move closer together or farther apart.

For the sinusoidal displacement above,

$$
p(x,t)=BkA\sin(kx-\omega t), \qquad p_{\max}=BkA
$$

The pressure amplitude $p_{\max}$ is measured in pascals; the displacement amplitude $A$ is measured in meters. They describe different aspects of the same wave.

Pressure and displacement are one-quarter cycle out of phase. At a compression or rarefaction, the displacement is zero even though the pressure fluctuation has its greatest magnitude. At maximum particle displacement, the pressure fluctuation is zero.

**MAXIMUM PRESSURE DOES NOT OCCUR AT MAXIMUM PARTICLE DISPLACEMENT.** What determines pressure is how neighboring particles are crowded together, rather than how far one particle is from equilibrium.

> **needs expansion — Pressure-Displacement Relationship:** Examine a short cylinder of fluid, relate its volume change to the difference in endpoint displacements, and explain the limit giving $\partial y/\partial x$. Use the bulk-modulus definition to establish the negative sign.

> **needs expansion — Pressure Amplitude of a Sinusoidal Sound Wave:** Differentiate the displacement function with respect to position, explain the substitution into $p=-B\,\partial y/\partial x$, and identify the coefficient $p_{\max}=BkA$.

## How We Perceive Sound

The main physical distinctions are:

- **Pitch** is primarily associated with frequency. Higher frequency generally means a higher perceived pitch.
- **Loudness** depends on sound amplitude and intensity, but also on frequency and the listener. Equal intensities at different frequencies need not sound equally loud.
- **Timbre**, or tone quality, depends on the mixture of harmonics and on how the sound starts and dies away.

A clarinet and a recorder can produce the same fundamental frequency and still sound different because they contain different amounts of the harmonics. The **attack** and **decay** of the sound also help distinguish instruments.

**Fourier analysis** separates a complicated waveform into its frequency components. Musical tones often contain a fundamental and harmonics; noise generally contains a broader mixture that need not form a harmonic series.

# Speed of Sound Waves

As with a wave on a string, the wave speed depends on a restoring effect and inertia. For sound in a fluid, the restoring effect comes from resistance to compression, while the inertia depends on the mass per unit volume.

The **speed of a longitudinal wave in a fluid** is

$$
v=\sqrt{\frac{B}{\rho}}
$$

where $\rho$ is the equilibrium density in kilograms per cubic meter. Greater stiffness increases the speed; greater density, with stiffness held constant, decreases it.

This does not mean sound always travels more slowly in a denser material. Water is denser than air, but its much greater resistance to compression gives it a higher sound speed. We have to compare both $B$ and $\rho$.

> **needs expansion — Sound Speed in a Fluid:** Follow a piston-driven compression, distinguish the piston speed from the wave speed, express the mass brought into motion, and apply the impulse-momentum theorem using the pressure change supplied by the bulk modulus.

For a longitudinal wave in a slender solid rod whose sides can expand and contract freely,

$$
v=\sqrt{\frac{Y}{\rho}}
$$

where $Y$ is Young's modulus. This is a rod formula. Longitudinal waves in a bulk solid are constrained differently and depend on both bulk and shear elastic properties.

> **needs expansion — Longitudinal Wave Speed in a Solid Rod:** Relate longitudinal stress to strain using Young's modulus and explain why free lateral motion makes this different from a wave in a bulk solid.

## Sound Speed in an Ideal Gas

For the rapid compressions and expansions in a sound wave, the relevant gas bulk modulus is

$$
B=\gamma p_0
$$

where $p_0$ is equilibrium pressure and $\gamma$ is the ratio of heat capacities. For air under the conditions used in the chapter, $\gamma\approx1.40$.

Combining this with the ideal-gas relationship gives

$$
v=\sqrt{\frac{\gamma RT}{M}}
$$

where $R$ is the gas constant, $T$ is absolute temperature in kelvins, and $M$ is molar mass in kilograms per mole.

**USE KELVINS HERE, NOT CELSIUS DEGREES.** Add $273.15$ to the Celsius temperature before substituting.

For a given ideal gas with approximately constant $\gamma$, the speed varies as $\sqrt{T}$. It does not depend independently on pressure at fixed temperature: pressure changes both the bulk modulus and the density, leaving their ratio unchanged.

At about $20^\circ\mathrm{C}$, the text uses $344\ \mathrm{m/s}$ for air. Changing frequency in the same ideal medium changes the wavelength through $v=\lambda f$, rather than changing this propagation speed.

> **needs expansion — Sound Speed in an Ideal Gas:** Explain the rapid-compression assumption behind $B=\gamma p_0$, then use $\rho=p_0M/(RT)$ to show why pressure cancels from $B/\rho$.

# Sound Intensity

**Intensity**, $I$, is the time-average power crossing a unit area perpendicular to propagation. Its units are watts per square meter. It describes energy transfer, rather than directly measuring perceived loudness.

For a sinusoidal traveling sound wave,

$$
I=\frac12\rho v\omega^2A^2
=\frac12\sqrt{\rho B}\,\omega^2A^2
$$

or, using pressure amplitude,

$$
I=\frac{p_{\max}^2}{2\rho v}
=\frac{p_{\max}^2}{2\sqrt{\rho B}}
$$

These describe the same intensity. For a fixed medium, doubling pressure amplitude quadruples intensity. At fixed intensity, pressure amplitude stays the same when frequency changes, but displacement amplitude varies inversely with frequency. A low-frequency wave therefore needs a greater particle-displacement amplitude than a high-frequency wave of equal intensity.

> **needs expansion — Intensity of a Sinusoidal Sound Wave:** Start from instantaneous power per area as pressure fluctuation times particle velocity, substitute the two wave expressions, and average over a cycle. Explain the substitutions giving the pressure-amplitude form.

## Spreading of Sound

For uniform emission in all directions without absorption,

$$
I=\frac{P_{\mathrm{av}}}{4\pi r^2}
$$

The power spreads over a larger spherical area as distance increases. If emission is restricted to a hemisphere, the relevant area is $2\pi r^2$ instead.

The inverse-square model requires the right geometry. A directional source or reflections from a room can change how intensity varies with distance.

## The Decibel Scale

Because the range of audible intensities is enormous, we use a logarithmic **sound intensity level**, $\beta$:

$$
\beta=(10\ \mathrm{dB})\log_{10}\left(\frac{I}{I_0}\right),
\qquad I_0=10^{-12}\ \mathrm{W/m^2}
$$

The reference $I_0$ is approximately the threshold of hearing at $1000\ \mathrm{Hz}$, not an intensity that every listener can hear at every frequency.

An increase of $10\ \mathrm{dB}$ means ten times the intensity. Doubling intensity gives an increase of approximately $3.0\ \mathrm{dB}$. A reading of $0\ \mathrm{dB}$ means $I=I_0$, not that there is no sound.

To compare two levels,

$$
\beta_2-\beta_1=(10\ \mathrm{dB})\log_{10}\left(\frac{I_2}{I_1}\right)
$$

For an inverse-square source, doubling distance reduces intensity to one quarter and decreases the level by about $6.0\ \mathrm{dB}$.

**DECIBELS ARE A LOGARITHMIC LEVEL, NOT AN INTENSITY IN WATTS PER SQUARE METER.** If combining independent sound sources, combine the appropriate intensities before converting to a level. For coherent waves, interference must also be accounted for.

> **needs expansion — Sound Intensity Level and Level Differences:** Apply logarithm rules to eliminate the reference intensity when subtracting levels, invert the definition to obtain intensity, and connect the result to inverse-square spreading.

# Standing Sound Waves and Normal Modes

Sound reflects at the ends of a pipe. Incoming and reflected waves can combine into a standing wave, with fixed locations where the displacement amplitude is zero or greatest.

But sound also has pressure variations, so we must specify **which quantity** has a node or antinode.

| End condition | Particle displacement | Pressure fluctuation |
|---|---|---|
| Closed, rigid end | Node | Antinode |
| Open end, ideal approximation | Antinode | Node |

At a closed end, the particles cannot move through the wall. Pressure can still vary strongly there. At an open end, the pressure stays approximately matched to the atmosphere, but the air can oscillate in and out.

Thus a displacement node is a pressure antinode, and a displacement antinode is a pressure node. For a standing wave, their positions are a quarter-wavelength apart.

This explains why the quiet points in the ideal speaker-and-wall example occur at displacement antinodes: the ear detects pressure variation, and those points are pressure nodes.

> **needs expansion — Pressure and Displacement in a Standing Sound Wave:** Use $p=-B\,\partial y/\partial x$ on the standing-wave displacement function and identify the spatial nodes and antinodes of each quantity.

## Pipes Open at Both Ends

An **open pipe** has displacement antinodes at both ends. The allowed wavelengths and frequencies are

$$
\lambda_n=\frac{2L}{n}, \qquad f_n=\frac{nv}{2L}=nf_1,
\qquad n=1,2,3,\ldots
$$

The fundamental has $\lambda_1=2L$ and $f_1=v/(2L)$. All integer harmonics are allowed, as with a string fixed at both ends, although the displacement patterns have different end conditions.

> **needs expansion — Normal Modes of an Open Pipe:** Fit displacement antinodes at both ends, explain why the length contains an integer number of half-wavelengths, and obtain the allowed frequencies using $v=\lambda f$.

## Pipes Closed at One End

A **stopped pipe** is open at one end and closed at the other. Its fundamental fits a displacement node at the closed end and an antinode at the open end, so the length is one quarter-wavelength:

$$
\lambda_n=\frac{4L}{n}, \qquad f_n=\frac{nv}{4L}=nf_1,
\qquad n=1,3,5,\ldots
$$

Only odd harmonics satisfy both boundaries. The fundamental is $f_1=v/(4L)$, half that of an open pipe of the same length.

Be careful with overtone numbering. The first overtone is the next allowed frequency above the fundamental. For a stopped pipe it is the **third harmonic**; the second overtone is the **fifth harmonic**.

> **needs expansion — Normal Modes of a Stopped Pipe:** Fit a node at one end and an antinode at the other, show why only odd numbers of quarter-wavelengths fit, and distinguish the harmonic index from the overtone count.

These pipe formulas neglect the small end correction: the effective pressure node lies slightly beyond an open end. They are good approximations when the pipe diameter is small compared with the wavelength.

# Resonance and Sound

The natural frequencies tell us how a system can vibrate freely. When an external source drives it, the driving frequency determines the frequency of its forced motion, while the response amplitude depends on how closely that frequency matches a normal mode.

Near a normal-mode frequency, the response can become much larger. This is **resonance**. A graph of response amplitude against driving frequency has peaks near the resonant frequencies.

For example, a nearby organ pipe can make a guitar string vibrate strongly if the driving sound matches one of the string's normal-mode frequencies. The two systems share the resonant frequency, but their wavelengths need not match because their wave speeds differ.

Real systems lose energy through damping and sound radiation, limiting the amplitude. In an ideal system without losses, a sustained resonant drive could keep increasing the oscillation energy.

The sound heard in a seashell comes from the cavity emphasizing parts of the surrounding noise. Likewise, blowing across a bottle drives its air into oscillation, with the air volume and geometry influencing the resonant response.

## Resonance and Instruments

An instrument usually contains several modes at once. Their relative strengths help determine its timbre. Changing a string's vibrating length or a wind instrument's effective air-column length changes its allowed frequencies.

A string and a stopped pipe have different fundamental relationships:

$$
f_{1,\mathrm{string}}=\frac{v_{\mathrm{string}}}{2L_{\mathrm{string}}},
\qquad
f_{1,\mathrm{pipe}}=\frac{v_{\mathrm{air}}}{4L_{\mathrm{pipe}}}
$$

If their fundamentals resonate together, equate the frequencies. Do not assume equal lengths or equal wave speeds.

> **needs expansion — Resonance Matching Between a String and a Stopped Pipe:** Equate the two fundamental frequencies and explain which medium and boundary conditions belong to each length and speed before substituting a length ratio.

# Interference of Waves

When two sound waves overlap, we add their disturbances at the same position and time. For sources with the same frequency and a stable relative phase, this produces a stable interference pattern.

Suppose two speakers emit in phase. Equal travel distances give equal travel times, so their waves arrive in phase and reinforce each other. A difference in path length can instead make a compression from one arrive with a rarefaction from the other.

For in-phase sources, with path difference $\Delta r$,

$$
\Delta r=m\lambda \quad\text{constructive interference}
$$

$$
\Delta r=\left(m+\frac12\right)\lambda \quad\text{destructive interference},
\qquad m=0,1,2,\ldots
$$

Complete cancellation additionally requires equal amplitudes at the listening point. If the amplitudes differ, destructive interference gives a minimum rather than necessarily silence. If the sources start out of phase, the phase difference at emission must also be included.

> **needs expansion — Path Difference and Interference Conditions:** Convert path difference into phase difference using $2\pi\Delta r/\lambda$, include the source phase difference, and identify the conditions for reinforcement and cancellation.

Interference does not destroy energy. In the two-speaker pattern, energy is directed toward constructive regions and away from destructive ones.

This is also different from the standing wave made by equal waves traveling in opposite directions. A two-speaker interference pattern can still have an overall outward flow of energy.

# Beats

What happens if two waves have nearly, but not exactly, the same frequency?

At one listening point, they gradually move in and out of phase. Sometimes they reinforce, and sometimes they nearly cancel, so the sound becomes louder and softer repeatedly. These variations are **beats**.

The beat frequency is

$$
f_{\mathrm{beat}}=|f_a-f_b|
$$

For example, $440\ \mathrm{Hz}$ and $443\ \mathrm{Hz}$ produce three beats per second. The same beat rate would come from $440\ \mathrm{Hz}$ and $437\ \mathrm{Hz}$, so the beat rate alone does not tell us whether the unknown frequency is higher or lower.

The rapid oscillation is associated with the average frequency, while the slow change in its amplitude produces the beats. With equal component amplitudes, the minimum can reach zero; unequal amplitudes leave a nonzero minimum.

> **needs expansion — Beat Frequency by Cycle Counting:** Find the time for the higher-frequency wave to gain one complete cycle on the other, then take the reciprocal of that time.

> **needs expansion — Beat Frequency from Superposition:** Add two sinusoidal functions using a trigonometric identity, identify the rapid oscillation and slow envelope, and explain why the observed intensity maxima occur at the frequency difference rather than half that difference.

Listening for beats is useful in tuning. As the two frequencies approach equality, the beats become slower and disappear at agreement.

# The Doppler Effect

An approaching siren sounds higher in pitch than the same siren moving away. This change in detected frequency due to motion of the source or listener is the **Doppler effect**.

For sound, the important velocities are measured relative to the medium. The source's motion changes the spacing of the emitted wavefronts; the listener's motion changes how quickly it encounters them.

**MOVING THE SOURCE DOES NOT CHANGE THE SPEED OF SOUND RELATIVE TO THE AIR.** That speed is still set by the medium.

## Moving Listener and Moving Source

A listener moving toward a stationary source encounters wavefronts more frequently. A source moving toward a stationary listener emits successive wavefronts from progressively closer positions, reducing their spacing.

These mechanisms are different, so moving the source and moving the listener at the same relative separation speed do not generally give exactly the same frequency shift.

The text uses the combined formula

$$
f_L=\frac{v+v_L}{v+v_S}f_S
$$

where $f_S$ is source frequency, $f_L$ is detected frequency, and $v$ is the positive sound speed. The signed velocities $v_L$ and $v_S$ use one convention:

**POSITIVE IS FROM THE LISTENER TOWARD THE SOURCE, FOR BOTH VELOCITIES.**

- A listener moving toward the source has $v_L>0$.
- A source moving toward the listener has $v_S<0$.
- A source moving away from the listener has $v_S>0$.

Draw the listener, source, and positive direction first. Then assign signs using the arrows; do not choose signs independently from a memorized “approaching means plus” rule.

For subsonic motion, approach raises the detected frequency and separation lowers it. Equal source and listener velocities relative to the medium give no shift, because the numerator and denominator are equal.

> **needs expansion — Doppler Effect for a Moving Listener:** Count wavefront encounters using the relative speed of listener and wave, keeping the wavelength in the medium fixed for a stationary source.

> **needs expansion — Wavelengths of a Moving Source and the Combined Doppler Formula:** Compare the distance a wavefront and its source move during one emission period, obtain the compressed and stretched wavelengths, and combine this with the listener's encounter rate using the text's sign convention.

## Reflected Sound

A reflection can require two Doppler calculations. First treat the reflecting surface as the listener receiving the original wave. Then treat it as a source re-emitting at that received frequency, and calculate what the final listener detects.

The positive direction may reverse between the two stages. Reassign the source and listener roles before choosing velocity signs.

> **needs expansion — Double Doppler Shift from a Reflection:** Follow the outgoing and returning sound separately, carrying the first detected frequency into the second calculation and redrawing the velocity-sign convention for each stage.

## Electromagnetic Waves

Light and radio waves also show a Doppler effect, but they require a different formula. In vacuum there is no material medium supplying the sound-style velocity reference.

For motion directly along the line of sight,

$$
f_R=\sqrt{\frac{c-u}{c+u}}\,f_S
$$

where $c$ is light speed and $u$ is the source's velocity relative to the receiver, positive for recession. Approaching motion has $u<0$. The text presents this result without deriving it here; its derivation requires special relativity.

> **needs expansion — Relativistic Longitudinal Doppler Effect:** Return to the special-relativity treatment to explain the frequency transformation and why the sound formula cannot be substituted for it.

# Shock Waves

As a source approaches sound speed, wavefronts crowd together in front of it. Once it moves faster than sound, it outruns the small disturbances it creates, and their combined envelope forms a **shock wave**.

In three dimensions this envelope is a cone trailing the moving source. The **Mach number** compares source speed to sound speed:

$$
\mathcal{M}=\frac{v_S}{v}
$$

Here $v_S$ is the positive source speed relative to the air. For supersonic motion, $\mathcal{M}>1$, and the ideal cone's half-angle satisfies

$$
\sin\alpha=\frac{v}{v_S}=\frac{1}{\mathcal{M}}
$$

Greater Mach number gives a narrower cone. The angle is measured between the direction of motion and the cone surface, not across the full cone.

> **needs expansion — Mach Cone Angle:** Draw the wavefront radius $vt$ and the source displacement $v_St$ over the same time interval, identify the tangent right triangle, and explain the sine ratio.

The **sonic boom** is heard when the shock wave reaches the listener. It is not restricted to the instant the aircraft first exceeds sound speed. An aircraft maintaining supersonic flight continues producing a shock wave along its route.

The disturbance arises from the object's motion through the air, so loud engines are not required. A supersonic glider can also produce a sonic boom.

For a plane flying horizontally at height $h$, the ideal constant-speed, constant-sound-speed geometry gives the overhead-to-boom delay

$$
t=\frac{h}{v_S\tan\alpha}
$$

> **needs expansion — Sonic-Boom Arrival Delay:** Draw the aircraft's horizontal displacement since passing overhead, connect it to the altitude using the cone angle, and explain why real changes in sound speed with altitude complicate the simple geometry.

For the chapter's worked examples and scanned figures, see [[18 - Physics/Physics Young and Freedman/Mechanics/16 - Sound and Acoustics/Examples]].
