# Chapter 7 — The Electronic Structure of Atoms

*General Chemistry: The Essential Concepts — Chang and Overby, 6th edition.*

## 7.1 From Classical Physics to Quantum Theory

Classical models describe many everyday motions, but they do not adequately explain atomic stability or the light emitted by atoms. To describe these observations, we need the idea that certain energies are **quantized**: only particular values or changes are allowed.

### Wavelength, Frequency, and Light

For a wave traveling at speed $u$:

$$
u=\lambda\nu
$$

$\lambda$ is wavelength, the distance between repeating points. $\nu$ is frequency, the number of cycles per second, measured in hertz: $1\ \mathrm{Hz}=1\ \mathrm{s^{-1}}$. Amplitude describes the size of the oscillation.

For electromagnetic radiation in a vacuum:

$$
c=\lambda\nu,
\qquad c\approx3.00\times10^8\ \mathrm{m/s}
$$

So what happens when wavelength decreases? At the same wave speed, frequency increases. Electromagnetic waves do not require a material medium, and their electric and magnetic fields oscillate perpendicular to one another and to their direction of travel.

From lower frequency to higher frequency, the electromagnetic spectrum runs through radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, and gamma rays. Visible light is approximately $400$–$700\ \mathrm{nm}$, with violet at the shorter-wavelength end.

### Quantized Energy

When solids are heated, they emit electromagnetic radiation over a wide range of wavelengths.  Measurements taken in the latter nineteenth century showed that the amount of radiant energy emitted by an object at a certain temperature depends on its wavelength.

Planck accounted for the radiation from heated matter by introducing energy exchanges in discrete amounts. For a photon:

$$
E_{\gamma}=h\nu=\frac{hc}{\lambda}
$$

$h\approx6.63\times10^{-34}\ \mathrm{J\cdot s}$ is Planck's constant. $E_{\gamma}$ is the energy of **one photon**, so shorter wavelength means greater energy per photon.

For $N$ photons of the same frequency, $E_{\mathrm{total}}=Nh\nu$. Greater intensity at a fixed frequency means more energy arriving per unit area per unit time, corresponding to more photons; each photon still has energy $h\nu$.

**Keep the scale and units straight:** convert wavelength to meters when using $c$ in meters per second, and multiply a per-photon energy by Avogadro's number only when a per-mole value is wanted.

$$
1\ \mathrm{nm}=10^{-9}\ \mathrm{m}
$$

## 7.2 The Photoelectric Effect

Light can eject electrons from a metal, but only if its frequency reaches a material-dependent threshold. In the one-photon description, one electron absorbs one photon's energy.

The number of electrons ejected is generally proportional to the intensity of the light, but the energies of the ejected electrons were not.

Part of that energy is needed to remove the electron. Any excess can become kinetic energy:

Einstein made an assumption that a beam of light is really a stream of particles composed of **photons**, which are particles of light. He deduced that each photon possesses an energy $E$ given by the equation $E=hv$ which we used previously, where $v$ is the frequency of light. 

This has the same form as before because electromagnetic radiation is emitted as well as absorbed in the form of photons.

The frequency needed to eject the electron that we referred to is called the **threshold frequency**.  Shining a beam of light onto a metal surface can be thought of as shooting a beam of particles--photons--at the metal atoms.

If the frequency of photons is such that $hv$ is equal to the energy that binds the electrons in the metal, which is the work function, then the light will just be able to knock the electrons loose.

$$
h\nu=\Phi+K_{\max}
$$
If we rewrite the expression to be in terms of $K_max$, or the energy of the emitted electron, we get

$$
K_{max}=hv - \Phi
$$

We see that the energy of the emitted electron rises as the frequency/energy of the photon rises, and we can think of the work function as the amount of energy it's "removing" from the photon.

We also see that the more intense the light, the greater the electrons emitted by the target metal, which corresponds to our understanding that a higher frequency increases the kinetic energy of the ejected electrons.

$$
\nu_0=\frac{\Phi}{h}
$$

| Change | Consequence in this model |
| --- | --- |
| Frequency below $\nu_0$ | No photoelectrons, even if intensity increases. |
| Frequency at the threshold | Electrons can just escape, with approximately zero maximum kinetic energy. |
| Higher frequency above threshold | Greater maximum electron kinetic energy. |
| Greater intensity at a fixed frequency above threshold | More electrons can be emitted per unit time; their maximum kinetic energy is unchanged. |

**More photons cannot substitute for insufficient energy per photon in this model.** This observation is why light's wave description alone was insufficient: light also transfers energy in particlelike packets.

**needs expansion — Photoelectric Energy Equation:** account separately for electron removal and excess kinetic energy, then connect the threshold frequency to the work function.

## 7.3 Bohr's Theory of the Hydrogen Atom

### Why Atoms Produce Line Spectra

A heated solid can produce a broad, continuous spectrum. Excited, isolated atoms instead emit particular wavelengths, producing a **line spectrum**. These lines indicate specific differences between allowed atomic energy levels.

Emissions are characteristics of the element, and thus each element has its own unique line spectra to identify it by. Such a process is typically done through discharge tubes filled with gas with electrodes at either end. As the electrons flow from negative to positive, they collide with gas molecules and emit light corresponding to its allowed energy levels.

Bohr proposed discrete energy levels for hydrogen's electron.  These represent orbits the electron is allowed to travel about. This of course means its energy is quantized, and the resulting energy level differences are fixed. The model's fixed circular orbits have since been replaced by quantum mechanics, but its hydrogen energy levels remain useful:

$$
E_n=-\frac{R_H}{n^2},
\qquad n=1,2,3,\ldots
$$

Here the book uses $R_H=2.18\times10^{-18}\ \mathrm{J}$, an **energy constant**. Do not confuse it with the Rydberg constant expressed in inverse meters.

The zero of energy is assigned to the separated proton and electron. Negative $E_n$ means the electron is bound. Increasing $n$ makes the energy less negative and brings the electron closer to the ionization limit.

- **Ground state:** the lowest allowed energy; for hydrogen, $n=1$.
- **Excited state:** a higher allowed energy, such as $n=2$ or $n=3$ for hydrogen.
- **Ionization:** removal of the bound electron, requiring energy to reach the separated-particle limit.

### Absorption and Emission

Use final minus initial for the **atom's** energy change:

$$
\Delta E_{\mathrm{atom}}=E_f-E_i
=R_H\left(\frac{1}{n_i^2}-\frac{1}{n_f^2}\right)
$$

| Transition | Atom's energy change | Radiation |
| --- | --- | --- |
| Lower energy to higher energy | $\Delta E_{\mathrm{atom}}>0$ | Photon absorbed |
| Higher energy to lower energy | $\Delta E_{\mathrm{atom}}<0$ | Photon emitted |

For either direction, the corresponding photon's energy is positive:

$$
E_{\gamma}=\left|\Delta E_{\mathrm{atom}}\right|=h\nu,
\qquad
\lambda=\frac{hc}{\left|\Delta E_{\mathrm{atom}}\right|}
$$

**The negative sign in emission belongs to the atom's energy loss.** It does not give a negative photon frequency or wavelength. A larger energy gap corresponds to a shorter wavelength.

Hydrogen emission series are grouped by their final level: Lyman ends at $n_f=1$, Balmer at $n_f=2$, and Paschen at $n_f=3$.

The equation above is for **hydrogen**. Hydrogenlike, one-electron ions can also be described by an adapted Bohr model, but do not apply this hydrogen formula unchanged to many-electron atoms.

**needs expansion — Bohr Energy Levels and Hydrogen Transition Equation:** explain the allowed energy levels and the subtraction of initial from final energy, keeping the atom's signed energy change separate from the photon's energy.

## 7.4 The Dual Nature of the Electron

If light can show both wave and particle behavior, could matter do the same? De Broglie related a moving particle's wavelength to its momentum:

$$
\lambda=\frac{h}{p}\approx\frac{h}{mv}
$$

$p$ is momentum; $m$ is mass and $v$ is speed in the nonrelativistic expression $p=mv$. Use kilograms with SI values of $h$. Greater momentum produces a shorter wavelength.

An electron's small mass makes its wave behavior significant on atomic scales. For ordinary objects, the associated wavelength is so small that wave effects are usually unobservable. Electron diffraction provides experimental evidence that electrons behave as waves.

### Standing Waves and Allowed States

In de Broglie's explanation of the old Bohr model, an allowed electron wave fits a whole number of wavelengths around the orbit:

$$
2\pi r=n\lambda
$$

$r$ is the orbit radius and $n$ is a positive integer. The fit condition helps explain why arbitrary orbit sizes were excluded in that model. It is a historical stepping stone to quantum mechanics, rather than a modern picture of an electron following a circular track.

**needs expansion — De Broglie Standing-Wave Condition:** explain why the circumference must accommodate an integer number of wavelengths and how this restricts the old model's allowed states.

## 7.5 Quantum Mechanics

### Uncertainty and Orbitals

The **Heisenberg uncertainty principle** places a fundamental limit on simultaneously specifying an electron's position and momentum precisely. This is part of quantum behavior, rather than simply a defect in the measuring instrument.

Consequently, an electron is not described by a definite orbit with a known position and velocity at every instant. Quantum mechanics describes allowed states using a **wave function**, $\psi$.

The quantity $|\psi|^2$ describes probability density. Regions with greater probability density are more likely to contain the electron when equal small volumes are compared. To obtain probability over an extended region, the density must be accumulated over that region.

An **atomic orbital** is a wave function describing an electron's spatial state. Orbital drawings represent the associated probability distribution; they do not show a path traveled by the electron.

For hydrogen, the Schrödinger equation can be solved exactly within the nonrelativistic model. Many-electron atoms require approximations because electron–electron interactions complicate the problem.

**needs expansion — Schrödinger Equation and Orbital Probability Density:** connect the wave function, allowed energies, and probability interpretation without treating an orbital as a physical container.

## 7.6 Quantum Numbers

Three quantum numbers label an orbital. A fourth labels an electron's spin state.

| Number | Allowed values | What it specifies |
| --- | --- | --- |
| Principal, $n$ | $1,2,3,\ldots$ | Shell; related to orbital size and energy. |
| Angular momentum, $\ell$ | Integers from $0$ to $n-1$ | Subshell and orbital shape. |
| Magnetic, $m_{\ell}$ | Integers from $-\ell$ to $+\ell$ | Orbital within the subshell; associated with spatial orientation. |
| Spin, $m_s$ | $+\tfrac12$ or $-\tfrac12$ | One of two electron spin states. |

The restrictions depend on one another. For example, a $2p$ electron has $n=2$, $\ell=1$, one of three allowed $m_{\ell}$ values, and either spin value. A $2d$ orbital is impossible: $d$ requires $\ell=2$, while $n=2$ permits only $\ell=0,1$.

Spin is an intrinsic quantum property with magnetic effects. The arrows used to represent it are labels; an electron should not be pictured literally as a small rotating ball.

### Shell, Subshell, and Orbital

- Same $n$: same **shell**.
- Same $n$ and $\ell$: same **subshell**.
- Same $n$, $\ell$, and $m_{\ell}$: same **orbital**.

| Subshell | $\ell$ | Orbitals, $2\ell+1$ | Maximum electrons |
| --- | --- | --- | --- |
| $s$ | $0$ | $1$ | $2$ |
| $p$ | $1$ | $3$ | $6$ |
| $d$ | $2$ | $5$ | $10$ |
| $f$ | $3$ | $7$ | $14$ |

For a complete shell:

$$
N_{\mathrm{orbitals}}=n^2,
\qquad N_{\mathrm{electrons,max}}=2n^2
$$

**A shell's capacity does not specify the order in which its subshells fill.** The third shell can hold $18$ electrons, but the usual ground-state building pattern reaches $4s$ before filling $3d$.

**needs expansion — Orbital and Shell Capacity Formulas:** count the allowed $m_{\ell}$ values for every allowed $\ell$, then account for the two spin states per orbital.

## 7.7 Atomic Orbitals

Orbital boundary surfaces usually enclose a chosen large fraction of the probability, approximately $90\%$ in the book's illustrations. **The drawn boundary is not a wall or an exact outer limit.**

| Type | Shape and arrangement |
| --- | --- |
| $s$ | Spherical distribution; one orbital per $s$ subshell. |
| $p$ | Three orbitals conventionally oriented along the $x$, $y$, and $z$ axes; each has two lobes. |
| $d$ | Five orbitals. Four have the familiar four-lobed shapes; $d_{z^2}$ has two lobes and a ring. |
| $f$ | Seven orbitals with more complicated shapes. |

The two lobes of a $p$ orbital belong to **one orbital**, with a total capacity of two electrons. They are not two separate electron slots.

Also distinguish **electron density at a location** from **probability within a spherical layer**. A layer farther from the nucleus has more volume; its total probability can be large even when the local density is lower. This explains why the hydrogen $1s$ radial-probability maximum is away from the nucleus, although its density is greatest at the nucleus.

### Orbital Energies

In the basic hydrogen model, energy depends only on $n$. Thus $2s$ and $2p$ have the same energy; orbitals with equal energies are **degenerate**.

In many-electron atoms, subshell energy also depends on $\ell$ and electron interactions. Subshells belonging to different shells can overlap in energy. **Do not transfer hydrogen's same-$n$, same-energy rule to every atom.**

## 7.8 Electron Configuration

An electron configuration records how electrons occupy subshells. In $1s^2\,2s^2\,2p^4$, the leading numbers identify shells, the letters identify subshells, and the superscripts count electrons.

For a neutral atom, the superscripts must total its atomic number, $Z$. This example contains eight electrons and describes ground-state oxygen.

### Pauli Exclusion Principle

**No two electrons in the same atom can have all four quantum numbers identical.** Since an orbital already fixes the first three numbers, two electrons in it must have opposite spins.

```text
Allowed pair:     [↑↓]
Not allowed:      [↑↑]
```

An orbital can contain zero, one, or two electrons, never three.

### Hund's Rule

For degenerate orbitals in a subshell, place electrons singly with parallel spins before pairing them.

```text
Ground-state 2p arrangements:
2p²    [↑ ] [↑ ] [  ]
2p³    [↑ ] [↑ ] [↑ ]
2p⁴    [↑↓] [↑ ] [↑ ]
```

The choice of which equivalent box receives the first pair is arbitrary here. Pairing two electrons early can satisfy Pauli while still failing to represent the ground state required by Hund's rule.

### Magnetism

- **Paramagnetic:** one or more unpaired electrons; attracted into an applied magnetic field.
- **Diamagnetic:** all electrons paired; weakly repelled by an applied magnetic field.

Draw the orbital boxes when needed. A partly filled subshell can contain both paired and unpaired electrons; oxygen's $2p^4$ arrangement has **two unpaired electrons**.

## 7.9 The Building-Up Principle

The **Aufbau principle** describes building up ground-state electron configurations as atomic number increases, adding electrons to the available orbitals in the energetically favored arrangement while respecting Pauli and Hund.

A useful usual filling sequence is:

```text
1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p
   → 5s → 4d → 5p → 6s → 4f → 5d → 6p
   → 7s → 5f → 6d → 7p
```

This is a guide, with exceptions. It is not a statement that these subshells maintain one fixed energy order for every element and electron population.

### Noble-Gas Shorthand

The bracketed noble gas represents its entire electron configuration. For example:

$$
\mathrm{K}:\quad[\mathrm{Ar}]\,4s^1
$$

The argon core accounts for $18$ electrons; the remaining $4s$ electron gives potassium's total of $19$. Use the appropriate preceding noble-gas core and count the remaining electrons explicitly.

### Exceptions and Checks

Chromium and copper are important exceptions to mechanically filling $4s^2$ before completing $3d$:

$$
\mathrm{Cr}:\quad[\mathrm{Ar}]\,4s^1\,3d^5
$$

$$
\mathrm{Cu}:\quad[\mathrm{Ar}]\,4s^1\,3d^{10}
$$

The book relates these arrangements to the stability of half-filled and filled $d$ subshells. The deciding quantity is the total atomic energy, including electron interactions. **Do not invent electron transfers for every atom just to create a half-filled subshell.** Other transition metals, lanthanides, and actinides have further irregularities; use an established configuration when the simple pattern is insufficient.

When checking a configuration, verify the electron total, allowed subshells, subshell capacities, opposite spins within pairs, and parallel spins across singly occupied degenerate orbitals. These checks distinguish a forbidden arrangement from an allowed excited arrangement and from the actual ground state.
