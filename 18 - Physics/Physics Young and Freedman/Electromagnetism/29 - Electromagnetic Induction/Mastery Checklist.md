# Chapter 29 — Electromagnetic Induction

## Mastery checklist

Use a checkbox only when you can answer or perform the task without copying a worked solution. Revisit unchecked items after practice. The questions and challenges below are original study prompts aligned to the chapter, not copied textbook exercises.

## Chapter objectives

By the end of this chapter, you should be able to:

- [ ] Explain the experimental evidence for electromagnetic induction and distinguish emf from current.
- [ ] Calculate magnetic flux and induced emf when field, area, or orientation changes.
- [ ] Determine induced-current directions with Faraday’s and Lenz’s laws.
- [ ] Analyze motional emf and account for mechanical-to-electrical energy conversion.
- [ ] Explain nonconservative induced electric fields and calculate them using symmetry.
- [ ] Explain eddy currents, magnetic braking, and energy dissipation.
- [ ] Use displacement current and interpret Maxwell’s equations.
- [ ] Distinguish superconductivity, persistent currents, and the Meissner effect.

## 29.1 — Induction Experiments

**Core question:** What changes in a magnetic system produce an induced emf?

### Conceptual questions

- [ ] Why can a moving magnet induce a current in a nearby coil without touching it?
- [ ] What happens when the magnet is stationary relative to the coil, and why?
- [ ] How can changing the current in one coil affect a nearby, electrically disconnected coil?
- [ ] Why can changing a loop’s area or orientation produce induction in a steady magnetic field?
- [ ] How do induced emf and induced current differ, particularly for an open circuit?
- [ ] Why is relative motion alone insufficient as a universal criterion for induction?

### Mathematical relationships

Magnetic flux through a chosen surface:
$$
\Phi_B=\int_S\vec B\cdot d\vec A.
$$
For a flat surface in a uniform field:
$$
\Phi_B=BA\cos\theta,
$$
where $\theta$ is measured from the **area normal**, not the plane. Flux is measured in webers: $1\,\mathrm{Wb}=1\,\mathrm{T\,m^2}$.
For a resistive closed loop when self-inductance is negligible:
$$
i=\frac{\mathcal E}{R}.
$$

### Problem-solving checklist

- [ ] Predict qualitatively whether an emf occurs when a magnet approaches, recedes, or remains stationary.
- [ ] Compare the effects of changing field strength, loop area, and orientation.
- [ ] Distinguish an induced voltage across an open conductor from current in a closed circuit.
- [ ] Identify which physical quantity is changing in each induction experiment.

**Keep in mind:** A magnetic field can be large while its flux is constant; induction depends on the change of flux, not simply its presence.

### Teaching challenge

A loop translates entirely within a uniform, steady magnetic field without changing its orientation or area. Explain why motion need not produce a net emf around the loop.

- [ ] I can explain this clearly, including the governing principle, signs, assumptions, and physical interpretation.

## 29.2 — Faraday’s Law

**Core question:** How does the rate of change of linked magnetic flux determine emf?

### Conceptual questions

- [ ] What is the difference between magnetic field, flux through one turn, and flux linkage?
- [ ] How does choosing an area normal fix the positive circulation direction?
- [ ] Why is the emf proportional to a derivative rather than to flux itself?
- [ ] How can field magnitude, area, or angle each contribute to changing flux?
- [ ] Why does increasing the number of identical turns increase the emf?
- [ ] What distinguishes average induced emf from instantaneous induced emf?

### Mathematical relationships

For a single circuit:
$$
\mathcal E=-\frac{d\Phi_B}{dt}.
$$
For $N$ fixed turns with the same flux through each:
$$
\mathcal E=-N\frac{d\Phi_B}{dt},
\qquad
\mathcal E_{\mathrm{avg}}=-N\frac{\Delta\Phi_B}{\Delta t}.
$$
More generally, with flux linkage $\Lambda=\sum_k\Phi_{B,k}$:
$$
\mathcal E=-\frac{d\Lambda}{dt}.
$$
For a uniform field and flat loop, evaluate $\Phi_B(t)=B(t)A(t)\cos\theta(t)$ **before differentiating**.

For a coil rotating at constant angular speed in uniform $B$, with $\theta=\omega t$:
$$
\Phi_B=BA\cos(\omega t),
\qquad
\mathcal E=NBA\omega\sin(\omega t).
$$

### Problem-solving checklist

- [ ] Differentiate a specified flux function to obtain signed emf.
- [ ] Calculate average emf from a flux change over a finite interval.
- [ ] Set up a flux integral for a nonuniform magnetic field.
- [ ] Analyze a loop entering or leaving a finite field region.
- [ ] Determine the peak emf and frequency of an ideal rotating-coil generator.
- [ ] Explain generator back emf and how source energy constrains the process.

**Keep in mind:** Use flux through one turn when multiplying by N. Do not multiply by N again if the given quantity is already total flux linkage.

### Teaching challenge

At one instant a rotating coil has zero magnetic flux. Explain why its induced-emf magnitude can nevertheless be maximum.

- [ ] I can explain this clearly, including the governing principle, signs, assumptions, and physical interpretation.

## 29.3 — Lenz’s Law

**Core question:** Why does an induced response oppose the flux change that produces it?

### Conceptual questions

- [ ] Why does the induced field oppose a change of flux rather than always oppose the external field?
- [ ] What induced-field direction accompanies increasing outward flux? Decreasing outward flux?
- [ ] How do you translate an induced-field direction into a clockwise or counterclockwise current?
- [ ] Why must a clockwise/counterclockwise answer specify the viewing side?
- [ ] How does Lenz’s law express conservation of energy?
- [ ] Why does an opposing induced response not necessarily prevent the imposed flux change?

### Mathematical relationships

The sign in Faraday’s law encodes Lenz’s law:
$$
\mathcal E=-\frac{d\Phi_B}{dt}.
$$
Choose the positive normal and contour together with the right-hand rule. A negative result means emf acts opposite the chosen positive contour; it is not a negative **magnitude**.

For a resistive loop:
$$
P_{\mathrm{thermal}}=i^2R.
$$

### Problem-solving checklist

- [ ] Determine the sign of the original flux and its derivative separately.
- [ ] Infer the induced magnetic-field direction before assigning current direction.
- [ ] Analyze a magnet approaching and receding from a loop.
- [ ] Explain the drag force or opposing torque in a generator.
- [ ] Check a direction prediction against the energy balance.

**Keep in mind:** Oppose the change, not automatically the original field, motion, or current.

### Teaching challenge

A field points into the page but is becoming weaker. Explain why the induced field points into the page too, without violating Lenz’s law.

- [ ] I can explain this clearly, including the governing principle, signs, assumptions, and physical interpretation.

## 29.4 — Motional Electromotive Force

**Core question:** How does conductor motion through a magnetic field separate charges and drive a circuit?

### Conceptual questions

- [ ] How does the magnetic Lorentz force separate charges in a moving rod?
- [ ] How do the directions of velocity, magnetic field, and rod orientation determine polarity?
- [ ] Why can a moving rod have an emf even when the circuit is open?
- [ ] When is the shortcut Bℓv valid, and when must you use an integral?
- [ ] Why can a magnetic field redirect charges without supplying their energy?
- [ ] Where does the energy dissipated in a slidewire circuit come from?

### Mathematical relationships

Magnetic force:
$$
\vec F_B=q\,\vec v\times\vec B.
$$
Motional contribution along a conductor:
$$
\mathcal E_{\mathrm{mot}}=\int_a^b(\vec v\times\vec B)\cdot d\vec\ell.
$$
For a straight rod of length $\ell$, with $\vec v$, $\vec B$, and the rod mutually perpendicular:
$$
|\mathcal E|=B\ell v.
$$
In an ideal slidewire loop with total resistance $R$, neglecting self-inductance:
$$
i=\frac{B\ell v}{R},
\qquad
F_{\mathrm{drag}}=\frac{B^2\ell^2v}{R},
\qquad
F_{\mathrm{ext}}v=i^2R
$$
for constant speed with the external force balancing magnetic drag.

### Problem-solving checklist

- [ ] Find rod polarity using the force on a positive test charge.
- [ ] Calculate emf for a moving straight conductor and identify zero-emf orientations.
- [ ] Find induced current and magnetic drag in a slidewire loop.
- [ ] Use mechanical power and thermal power as an independent check.
- [ ] Avoid adding the motional and flux-rule results twice when they describe the same effect.

**Keep in mind:** The applied mechanical agent supplies the electrical energy; the magnetic field is not a fuel source.

### Teaching challenge

A conducting rod moves through a uniform field, first with its circuit open and then closed. Compare charge separation, current, magnetic drag, and required mechanical power.

- [ ] I can explain this clearly, including the governing principle, signs, assumptions, and physical interpretation.

## 29.5 — Induced Electric Fields

**Core question:** How can a changing magnetic field produce an electric field without a conducting loop?

### Conceptual questions

- [ ] Why does an induced electric field exist even if no wire is present?
- [ ] How is this field different from an electrostatic field produced by stationary charges?
- [ ] Why can the circulation of the induced field around a closed path be nonzero?
- [ ] Why cannot the total induced field generally be represented everywhere by a single-valued scalar potential alone?
- [ ] What symmetry lets you take E outside a circulation integral?
- [ ] Can a point outside the region of changing B still have a nonzero induced electric field?

### Mathematical relationships

For a **stationary** contour and surface:
$$
\oint_C\vec E\cdot d\vec\ell
=-\frac{d}{dt}\int_S\vec B\cdot d\vec A.
$$
For cylindrical symmetry, with uniform axial $B(t)$ confined to radius $a$, the azimuthal field magnitudes are:
$$
|E_\phi(r)|=
\begin{cases}
\dfrac r2\left|\dfrac{dB}{dt}\right|,&r\le a,\\[6pt]
\dfrac{a^2}{2r}\left|\dfrac{dB}{dt}\right|,&r\ge a.
\end{cases}
$$
Determine circulation direction with Lenz’s law. Electrostatic fields instead satisfy $\oint\vec E_{\mathrm{es}}\cdot d\vec\ell=0$.

### Problem-solving checklist

- [ ] Calculate the induced electric field inside and outside an ideal changing-flux region.
- [ ] Use enclosed flux rather than the entire circular-path area when the field is spatially confined.
- [ ] Find the force on a charge in an induced electric field.
- [ ] Compare electrostatic potential differences with nonconservative circulation.
- [ ] State why the stationary-contour law differs from a moving-conductor emf calculation.

**Keep in mind:** Zero local B does not imply zero induced E; Faraday’s law links circulation to the flux enclosed by the whole path.

### Teaching challenge

Outside an ideal long solenoid, B is approximately zero. If the interior B changes, explain how E outside can still be nonzero.

- [ ] I can explain this clearly, including the governing principle, signs, assumptions, and physical interpretation.

## 29.6 — Eddy Currents

**Core question:** How do induced currents in extended conductors produce forces and heating?

### Conceptual questions

- [ ] How can a solid conductor contain circulating currents without a separate wire loop?
- [ ] What changes of flux produce eddy currents in a moving plate or disk?
- [ ] Why can magnetic braking operate without mechanical contact?
- [ ] Why does braking weaken as motion slows in an ordinary resistive conductor?
- [ ] How do slots or laminations reduce unwanted eddy-current losses?
- [ ] How can eddy currents be useful in heating, braking, and metal detection?

### Mathematical relationships

For a selected current path, induction is governed by
$$
\mathcal E=-\frac{d\Phi_B}{dt}.
$$
A lumped-loop model gives $P=i^2R$. For a conductor described locally:
$$
P=\int_V\vec J\cdot\vec E\,dV.
$$
For an isotropic ohmic conductor, $\vec J=\sigma\vec E$ and the local heating rate is $\vec J\cdot\vec E=J^2/\sigma$. Actual current paths depend on the geometry.

### Problem-solving checklist

- [ ] Sketch plausible eddy-current loops near the entering and leaving edges of a field region.
- [ ] Predict magnetic force direction using Lenz’s law.
- [ ] Explain how motion or a time-varying applied field produces thermal energy.
- [ ] Compare solid and laminated conducting cores qualitatively.
- [ ] State when a uniform steady field and rigid translation do not give sustained bulk eddy currents.

**Keep in mind:** Do not apply Bℓv/R to a whole metal plate without defining a justified effective circuit.

### Teaching challenge

A conducting plate swings through a localized magnetic field and slows. Explain the sequence from flux change to current to force to heat.

- [ ] I can explain this clearly, including the governing principle, signs, assumptions, and physical interpretation.

## 29.7 — Displacement Current and Maxwell’s Equations

**Core question:** How does a changing electric flux complete the connection between electric and magnetic fields?

### Conceptual questions

- [ ] Why does the original steady-current form of Ampère’s law become ambiguous for a charging capacitor?
- [ ] What is displacement current, and how does it differ from charge crossing a dielectric?
- [ ] Why must two surfaces with the same boundary yield the same magnetic circulation?
- [ ] How does a changing electric field produce magnetic circulation between capacitor plates?
- [ ] What does each of Maxwell’s four integral equations say physically?
- [ ] Why do changing electric and magnetic fields suggest the possibility of electromagnetic waves?

### Mathematical relationships

In vacuum, through a chosen surface:
$$
I_D=\varepsilon_0\frac{d\Phi_E}{dt},
\qquad
\Phi_E=\int_S\vec E\cdot d\vec A.
$$
Maxwell’s integral equations in vacuum, using fixed surfaces and contours:
$$
\oint_S\vec E\cdot d\vec A=\frac{Q_{\mathrm{encl}}}{\varepsilon_0},
\qquad
\oint_S\vec B\cdot d\vec A=0,
$$
$$
\oint_C\vec E\cdot d\vec\ell=-\frac{d\Phi_B}{dt},
$$
$$
\oint_C\vec B\cdot d\vec\ell
=\mu_0 I_{\mathrm{cond,encl}}
+\mu_0\varepsilon_0\frac{d\Phi_E}{dt}.
$$
For an ideal vacuum parallel-plate capacitor, neglecting fringing, the displacement current through the full plate area equals the charging conduction current. For uniform circular plates of radius $a$:
$$
B(r)=
\begin{cases}
\dfrac{\mu_0 I r}{2\pi a^2},&r\le a,\\[6pt]
\dfrac{\mu_0 I}{2\pi r},&r\ge a.
\end{cases}
$$

### Problem-solving checklist

- [ ] Calculate displacement current from the rate of electric-flux change.
- [ ] Relate changing capacitor charge to electric field and displacement current.
- [ ] Calculate the magnetic field between ideal circular capacitor plates.
- [ ] Distinguish a closed-surface flux integral from a closed-contour circulation integral.
- [ ] Explain charge conservation and surface independence in the corrected Ampère law.

**Keep in mind:** Displacement current is not electrons traveling across the insulating gap. Use the vacuum equations only under their stated material assumptions.

### Teaching challenge

Span an Amperian loop once with a surface cutting the wire and once with a surface passing between charging capacitor plates. Explain why the two calculations agree.

- [ ] I can explain this clearly, including the governing principle, signs, assumptions, and physical interpretation.

## 29.8 — Superconductivity

**Core question:** How does superconductivity change resistance and magnetic-flux behavior?

### Conceptual questions

- [ ] What is a superconducting transition, and what does the critical temperature signify?
- [ ] Why can a current persist without resistive heating in a superconducting loop?
- [ ] What is the Meissner effect?
- [ ] Why does zero resistance alone not fully describe flux expulsion during the transition?
- [ ] How can magnetic exclusion produce repulsion or levitation?
- [ ] Why do magnetic-field and current limits matter, and why is complete flux expulsion not a universal description of every superconducting state?

### Mathematical relationships

In an ideal zero-resistance state:
$$
R=0,\qquad P_{\mathrm{Joule}}=i^2R=0.
$$
In the bulk of an ideal Meissner state:
$$
\vec B\approx\vec 0.
$$
This statement excludes the thin field-penetration region near a surface and does not describe the mixed vortex state of a type-II superconductor.

### Problem-solving checklist

- [ ] Distinguish a perfect-conductor model from the Meissner effect.
- [ ] Describe qualitatively what happens when a sample is cooled through its transition in an applied field.
- [ ] Explain persistent currents and the role of screening currents.
- [ ] Connect superconducting magnetic behavior to levitation and magnet applications.
- [ ] Recognize the limits of an idealized B=0 description.

**Keep in mind:** Superconductivity is more than exceptionally low resistance; the equilibrium magnetic response is essential.

### Teaching challenge

Compare a hypothetical perfect conductor that simply preserves its initial flux with a material entering the Meissner state in a weak applied field. Explain the difference.

- [ ] I can explain this clearly, including the governing principle, signs, assumptions, and physical interpretation.

## Chapter-wide mastery check

- [ ] Explain the chapter’s main relationships in words, rather than merely reciting formulas.
- [ ] Draw a labeled sketch and state the reference directions before using signed quantities.
- [ ] Select a governing principle and explain why it fits the problem.
- [ ] State the idealizations and identify when a familiar shortcut does not apply.
- [ ] Check units, initial/final limits, and energy conservation.
- [ ] Explain the physical meaning of a zero, negative, or unexpectedly large result.
- [ ] Solve a new problem that combines at least two sections of this chapter.

## Suggested teaching-video sequence

| Video | Topic | Main objective |
|---|---|---|
| 1 | Experiments, flux, and Faraday’s law | Connect observations to changing flux and induced emf |
| 2 | Lenz’s law and motional emf | Determine direction and trace mechanical-to-electrical energy transfer |
| 3 | Induced electric fields and eddy currents | Explain nonconservative fields, circulating currents, braking, and heating |
| 4 | Displacement current and Maxwell’s equations | Connect changing electric and magnetic fields |
| 5 | Superconductivity | Distinguish zero resistance, flux exclusion, and idealization limits |

## A standard problem-solving procedure

1. Identify the conductor, circuit, or mathematical contour and determine whether it moves.
2. Choose a surface normal and circulation direction with the right-hand rule.
3. Determine the relevant magnetic or electric flux and what makes it change.
4. Select Faraday’s law, the motional-emf integral, or the Ampère–Maxwell law as appropriate.
5. Evaluate the magnitude, then determine direction with the chosen signs and Lenz’s law.
6. Add circuit, force, or energy relations only after stating their assumptions.
7. Check units, zero-change limits, and the energy source.

## The most important connection to master

A changing magnetic flux can drive circulation of electric field or induce emf in a moving circuit. Lenz’s law fixes the response direction, and energy conservation explains why an induced current cannot deliver energy without an appropriate source.

For a stationary contour:

$$
\boxed{\oint_C\vec E\cdot d\vec\ell=-\frac{d\Phi_B}{dt}}
$$

## Source

Young and Freedman, *University Physics with Modern Physics*, 13th edition, Chapter 29, printed pp. 957–981. Section numbering follows this edition. This is an original learning checklist, not a reproduction of the textbook’s wording or exercises.
