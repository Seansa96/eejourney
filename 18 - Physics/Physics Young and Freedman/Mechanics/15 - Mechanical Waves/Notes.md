# Types of Mechanical Waves

A **mechanical wave** is a disturbance that travels through a material, which we call the **medium**. The disturbance moves from one part of the medium to the next because neighboring particles exert forces on each other.

Imagine giving one end of a stretched rope a quick upward shake. The section beside your hand moves first, then the next section, and so on. The disturbance travels down the rope, but each section only moves away from its equilibrium position and returns.

**THE WAVE TRAVELS THROUGH THE MEDIUM; THE PARTICLES OF THE MEDIUM DO NOT TRAVEL ALONG WITH IT.**

This is similar to people doing a wave in a stadium. The pattern moves around the stands, even though each person stays at their own seat. Energy is transferred from one region to another without an accompanying transport of the medium along the wave.

## Transverse and Longitudinal Waves

We distinguish the types by comparing the motion of the particles to the direction the wave travels:

- **Transverse wave:** The particles move perpendicular to the direction of propagation, as with the up-and-down motion of a rope carrying a wave horizontally.
- **Longitudinal wave:** The particles move parallel to the direction of propagation, as with fluid pushed back and forth by a piston in a tube.
- **Combined motion:** Some waves involve both components. The surface-water example in the text has particles moving in approximately circular paths while the disturbance travels along the surface.

All of these systems have an equilibrium state and forces that tend to restore that state after a disturbance. Their particles also have inertia, so the response takes time. These mechanical properties determine the **wave speed**, $v$.

Be careful here: wave speed is the speed of the disturbance, not the instantaneous speed of a particle being disturbed.

# Periodic Waves

A single shake produces a **wave pulse**. If we repeatedly move the end of the rope, we produce a **periodic wave** instead.

When that driving motion is simple harmonic motion, the resulting wave is **sinusoidal**. Each particle undergoes SHM with the same frequency, but particles at different positions generally reach the same part of their motion at different times.

The quantities describing this motion are:

- $A$, the **amplitude**: the greatest displacement of a particle from equilibrium. This is not the full distance from a trough to a crest; that is $2A$.
- $T$, the **period**: the time for one complete oscillation at a particular point.
- $f$, the **frequency**: the number of complete oscillations per second, measured in hertz.
- $\lambda$, the **wavelength**: the distance between corresponding points on successive repetitions, such as neighboring crests.

Recall that

$$
f=\frac{1}{T}, \qquad \omega=2\pi f
$$

where $\omega$ is the angular frequency in radians per second.

The wave advances one wavelength during each period, so the **wavelength-frequency relationship** is

$$
v=\frac{\lambda}{T}=\lambda f
$$

In the ideal media considered in this chapter, changing the driving frequency does not change the wave speed. If we increase the frequency while leaving the medium unchanged, the wavelength must decrease so that $\lambda f$ stays the same.

## Periodic Longitudinal Waves

A piston moving back and forth in a fluid produces alternating **compressions**, where pressure and density are higher, and **rarefactions**, where they are lower.

The particles move back and forth, while the pattern of compressions and rarefactions travels through them. The wavelength is measured from one compression to the next, or one rarefaction to the next. It is not the distance from a compression to the neighboring rarefaction.

The same relationship $v=\lambda f$ applies. Particles one wavelength apart oscillate in phase: they are at the same stage of their motion at the same time.

# Mathematical Description of a Wave

Amplitude, frequency, and wavelength tell us a great deal, but suppose we want the displacement of one particular particle at one particular time. For that we need a **wave function**:

$$
y=y(x,t)
$$

Here $x$ identifies the particle by its equilibrium position, $t$ is the time, and $y$ is its displacement from equilibrium. For a transverse wave on a horizontal string, $y$ is the vertical displacement.

## Wave Function for a Sinusoidal Wave

For a sinusoidal wave traveling in the positive $x$-direction, one convenient form is

$$
y(x,t)=A\cos(kx-\omega t)
$$

where the **wave number** is

$$
k=\frac{2\pi}{\lambda}
$$

The units of $k$ are radians per meter. It tells us how quickly the phase changes with position, just as $\omega$ tells us how quickly it changes with time.

The quantity $kx-\omega t$ is the **phase**. It identifies which part of the oscillation is occurring at that position and time. A phase difference of $2\pi$ is one full cycle; a difference of $\pi$ is half a cycle.

For the same choice of initial phase, a wave traveling in the negative $x$-direction is

$$
y(x,t)=A\cos(kx+\omega t)
$$

The signs tell us how the pattern moves. For the first expression, increasing time requires increasing $x$ to follow the same crest. For the second, the crest moves toward decreasing $x$.

These forms assume a particular starting phase. A constant phase angle can be included when the initial displacement and direction of motion require it.

> **needs expansion — Sinusoidal Traveling-Wave Function:** Explain the delay $x/v$ between the source and a point downstream, and why we substitute $t-x/v$ into the source's motion. Connect the forms using $\lambda$, $T$, $k$, and $\omega$.

The corresponding **phase-speed relationship** is

$$
v=\frac{\omega}{k}
$$

> **needs expansion — Phase-Speed Relationship:** Follow a point of constant phase and explain what is held constant when differentiating $kx-\omega t$.

## Two Different Graphs

A graph of $y$ versus $x$ at a fixed time is a snapshot of the string. The horizontal spacing of repetitions is the wavelength.

A graph of $y$ versus $t$ at a fixed position follows one particle as time passes. The horizontal spacing of repetitions is the period.

These can both look like cosine curves, but **THEIR HORIZONTAL AXES REPRESENT DIFFERENT THINGS**. A snapshot shows where the particles are; a time graph shows how one particle moves.

## Particle Velocity and Acceleration

To find the transverse velocity of a particle, we differentiate with respect to time while holding its position label $x$ constant. This is a **partial derivative**:

$$
v_y(x,t)=\frac{\partial y}{\partial t}
$$

For $y=A\cos(kx-\omega t)$, the results are

$$
v_y=\omega A\sin(kx-\omega t)
$$

$$
a_y=\frac{\partial^2y}{\partial t^2}=-\omega^2A\cos(kx-\omega t)=-\omega^2y
$$

The greatest particle speed is $\omega A$, and the greatest acceleration magnitude is $\omega^2A$. At maximum displacement the particle is momentarily at rest, with acceleration directed toward equilibrium. At equilibrium it has its greatest speed and zero acceleration.

Again, $v_y$ is the particle's transverse velocity. It is not the propagation speed $v=\omega/k$.

> **needs expansion — Particle Velocity and Acceleration in a Sinusoidal Wave:** Work through the time derivatives, keeping $x$ fixed and explaining the chain-rule signs.

## The Wave Equation

For the ideal string, the wave function obeys

$$
\frac{\partial^2y}{\partial x^2}=\frac{1}{v^2}\frac{\partial^2y}{\partial t^2}
$$

The spatial derivative describes how the slope changes along the string, while the time derivative describes the particle's acceleration. So the string's curvature is connected to how its particles accelerate. A portion curving upward accelerates upward, and one curving downward accelerates downward.

This equation also describes nonsinusoidal disturbances. Its usefulness goes beyond a single cosine-shaped wave.

> **needs expansion — One-Dimensional Wave Equation:** Compare the second spatial and time derivatives and explain the substitution $v=\omega/k$.

# Speed of a Transverse Wave

What actually sets the speed of a wave on a string?

The tension supplies the restoring force, while the mass of the string supplies inertia. Greater tension makes a disturbance propagate faster; greater mass per unit length makes it propagate more slowly.

For an ideal flexible string with small transverse disturbances,

$$
v=\sqrt{\frac{F}{\mu}}
$$

where $F$ is the tension in newtons and $\mu$ is the **linear mass density**, or mass per unit length:

$$
\mu=\frac{m}{L}
$$

Use kilograms per meter for $\mu$, rather than the total mass of the string. The total mass alone does not tell us how much material must be accelerated in each unit of length.

Quadrupling the tension doubles the wave speed. Quadrupling the linear mass density halves it. Changing amplitude or frequency does not change the speed in this ideal model.

## Two Ways of Obtaining the Wave Speed

The text first considers a disturbance that progressively brings more string into transverse motion. Its total transverse momentum increases because more mass is moving, even when the transverse velocity of each moving portion stays constant.

The second method examines the forces on a short string segment. Tension acts along the string on both sides, and the difference in the transverse components produces acceleration. Passing to an infinitesimal segment connects Newton's second law to the wave equation.

> **needs expansion — Transverse Wave Speed, Impulse-Momentum Method:** Explain the growing moving mass $\mu vt$, the force-triangle substitution, and the distinction between $v$ and $v_y$.

> **needs expansion — Transverse Wave Speed, Newton's Second Law Method:** Draw the forces on a segment, relate their transverse components to the endpoint slopes, and explain the $\Delta x\to0$ limit before comparing with the wave equation.

The larger pattern is a competition between restoring effects and inertia. Other mechanical waves have their own expressions for these properties; the string formula should not be applied directly to every medium.

# Energy in Wave Motion

To start a wave, we do work on the medium. Each disturbed portion then exerts forces and does work on neighboring portions, transferring energy along the medium.

On a string, this transfer depends on both the transverse force and the transverse velocity. A force without motion does no work, and transverse motion without a transverse force at the cut does not transfer energy across that cut.

## Power Carried by a String Wave

The instantaneous power transferred toward increasing $x$ across a point is

$$
P(x,t)=-F\frac{\partial y}{\partial x}\frac{\partial y}{\partial t}
$$

For the sinusoidal traveling wave $y=A\cos(kx-\omega t)$, this becomes

$$
P(x,t)=\sqrt{\mu F}\,\omega^2A^2\sin^2(kx-\omega t)
$$

The power varies with time, even though the wave has constant amplitude. Its maximum and average values are

$$
P_{\max}=\sqrt{\mu F}\,\omega^2A^2
$$

$$
P_{\mathrm{av}}=\frac12\sqrt{\mu F}\,\omega^2A^2
$$

The average is half the maximum because the average of $\sin^2$ over a complete cycle is $1/2$.

For the same string and tension, average power is proportional to $A^2$ and $f^2$. Doubling either amplitude or frequency while holding the other fixed therefore quadruples the average power. This does not mean the wave travels four times faster.

> **needs expansion — Instantaneous and Average Power of a Sinusoidal String Wave:** Explain the force-slope relation and its sign, substitute the spatial and time derivatives, and show why cycle averaging introduces $1/2$.

## Wave Intensity

When waves spread through three dimensions, we also care about how widely the power is distributed. **Intensity**, $I$, is the average power per unit area through a surface perpendicular to propagation. Its units are watts per square meter.

For a source radiating equally in all directions, with no absorption or other losses,

$$
I=\frac{P_{\mathrm{av}}}{4\pi r^2}
$$

The same total power passes through successively larger imaginary spheres. Thus intensity decreases with distance even though the source's power has not changed.

The **inverse-square law for intensity** can also be written

$$
\frac{I_1}{I_2}=\frac{r_2^2}{r_1^2}
$$

Doubling the distance gives one quarter of the intensity. This relationship assumes spherical spreading without absorption; reflections or a directional source can change the situation.

> **needs expansion — Inverse-Square Law for Wave Intensity:** Use conservation of power through concentric spheres and explain why the relevant area is $4\pi r^2$.

# Wave Interference, Boundary Conditions, and Superposition

What happens when a pulse reaches the end of a string? The answer depends on what the end is allowed to do. These restrictions are the **boundary conditions**.

At a **fixed end**, displacement must always be zero. The reflected pulse travels back in the opposite direction and is inverted: an upward incident pulse returns as a downward pulse.

At an ideal **free end**, the end can move transversely and there is no transverse force from the support. The reflected pulse travels back without inversion. The string's slope at the free end is zero in this model.

The reversal in travel direction happens in both cases. Inversion describes a separate change in the sign of the displacement.

## The Principle of Superposition

When waves occupy the same region at the same time, they **interfere**. For the linear wave model used here, the resulting displacement is the algebraic sum of the individual displacements:

$$
y(x,t)=y_1(x,t)+y_2(x,t)
$$

Displacements in the same direction reinforce each other; opposite displacements partly or completely cancel. We add the displacements at the same position and time, not the amplitudes without considering their signs and phases.

After overlapping, ideal pulses continue traveling with their original shapes. Complete cancellation at an instant does not mean the waves or their energy have been permanently destroyed.

Superposition works here because the wave equation is linear. It is not automatically valid for every possible disturbance in every material.

> **needs expansion — Principle of Linear Superposition:** Show why the sum of two solutions also satisfies the linear wave equation, including why both reflected-wave constructions satisfy their boundary conditions.

# Standing Waves on a String

Suppose a sinusoidal wave reflects from a fixed end and overlaps the incoming wave. With equal amplitudes, frequencies, and wavelengths, the two oppositely traveling waves form a **standing wave**.

The pattern no longer advances along the string. Instead, particular points remain at rest while the portions between them oscillate.

- **Nodes** have zero displacement at every instant.
- **Antinodes** have the greatest oscillation amplitude and lie midway between neighboring nodes.

For a fixed end at $x=0$, the text uses

$$
y(x,t)=\bigl(A_{\mathrm{SW}}\sin kx\bigr)\sin\omega t,
\qquad A_{\mathrm{SW}}=2A
$$

where $A$ is the amplitude of either traveling wave. The local oscillation amplitude is $|A_{\mathrm{SW}}\sin kx|$, so it depends on position. $A_{\mathrm{SW}}$ is the maximum amplitude, reached at the antinodes.

The time factor describes the oscillation, while the position factor determines where that oscillation is large, small, or absent. Points between the same pair of nodes oscillate in phase; neighboring segments on opposite sides of a node move oppositely.

> **needs expansion — Standing-Wave Function at a Fixed End:** Add the incident and reflected wave functions, explain the sign required by the fixed boundary, and use the cosine sum-and-difference identities to obtain the product form.

## Node and Antinode Spacing

For this coordinate choice, the nodes are at

$$
x=n\frac{\lambda}{2}, \qquad n=0,1,2,\ldots
$$

Adjacent nodes are $\lambda/2$ apart, as are adjacent antinodes. A node and the nearest antinode are $\lambda/4$ apart.

**A POINT THAT HAS ZERO DISPLACEMENT AT ONE INSTANT IS NOT NECESSARILY A NODE.** Every particle passes through equilibrium, but a node stays there throughout the motion. The entire string can momentarily be straight while the particles between the nodes are moving.

> **needs expansion — Standing-Wave Node and Antinode Positions:** Explain why nodes require the position factor to vanish for all times, then locate the zeros and extrema of $\sin kx$.

## Energy in a Standing Wave

The two traveling waves carry equal average powers in opposite directions. Their standing-wave combination has zero average power transfer across each position.

This does not mean it has no energy. Energy moves locally back and forth, and the moving portions have kinetic energy while deformation stores potential energy. There is no net energy transport along the string when averaged over a cycle.

> **needs expansion — Average Power of a Standing Wave:** Substitute the standing-wave function into the string-power equation and explain why the time average vanishes.

# Normal Modes of a String

Now fix both ends of a string of length $L$. Both ends must be nodes, so only particular standing-wave patterns fit between them.

The length must contain a whole number of half-wavelengths:

$$
L=n\frac{\lambda_n}{2}
$$

Therefore the allowed wavelengths and frequencies are

$$
\lambda_n=\frac{2L}{n}, \qquad f_n=\frac{nv}{2L}=nf_1,
\qquad n=1,2,3,\ldots
$$

The lowest frequency, $f_1=v/(2L)$, is the **fundamental frequency**. Its wavelength is $2L$, not $L$: the string contains only half of a wavelength.

Each of these patterns is a **normal mode**. In a single mode, all moving particles oscillate sinusoidally at the same frequency, with their amplitudes and relative phases set by the pattern. The $n$th mode has $n$ antinodes and $n+1$ nodes, counting the ends.

> **needs expansion — Allowed Wavelengths and Harmonic Frequencies of a String Fixed at Both Ends:** Apply the second boundary condition at $x=L$, explain why the number of half-wavelengths is an integer, and connect $\lambda_n$ to $f_n$ using $v=\lambda f$.

## Harmonics and Overtones

The allowed frequencies are integer multiples of the fundamental, called **harmonics**:

- First harmonic: $f_1$, the fundamental.
- Second harmonic: $2f_1$, the first overtone.
- Third harmonic: $3f_1$, the second overtone.

The overtone count starts above the fundamental. **THE SECOND OVERTONE IS THE THIRD HARMONIC**, not the second.

## Complex Standing Waves

A plucked string usually does not start in the shape of one sinusoidal mode. Its motion is a superposition of several normal modes, each with its own frequency and amplitude.

The mixture of harmonics helps determine the character of the sound. Plucking a guitar string near its end produces a different mixture from plucking it nearer the middle, even when the fundamental frequency is the same.

Representing a complex vibration as a sum of sinusoidal components is **harmonic analysis**; the corresponding sum is a **Fourier series**.

## Standing Waves and String Instruments

Combining the fundamental-frequency relationship with the string wave speed gives

$$
f_1=\frac{1}{2L}\sqrt{\frac{F}{\mu}}
$$

This explains the main ways we change the pitch of a string:

1. Shorten the vibrating length $L$ to raise the fundamental frequency, as when pressing a string against a fingerboard.
2. Increase the tension $F$ to raise it, as when tightening a tuning peg.
3. Increase the linear mass density $\mu$ to lower it. Thick or wound strings can produce lower notes without needing an impractically long instrument.

> **needs expansion — Fundamental Frequency in Terms of String Length, Tension, and Linear Density:** Explain the substitution of $v=\sqrt{F/\mu}$ into $f_1=v/(2L)$ and the assumptions behind both expressions.

The vibrating string drives the surrounding air at the same frequencies. But the sound travels through air at the sound speed, which generally differs from the wave speed on the string. The frequency is shared; the wavelength need not be.

For the worked calculations and their scanned figures, see [[18 - Physics/Physics Young and Freedman/Mechanics/15 - Mechanical Waves/Examples]].
