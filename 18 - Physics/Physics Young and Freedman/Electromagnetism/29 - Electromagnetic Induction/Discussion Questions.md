# Chapter 29: Electromagnetic Induction

### Highest Priority — Do These Now

1. Q29.3 — Mutual induction and Lenz's law x
    
2. Q29.5 — Magnetic flux and field orientation x
    
3. Q29.7 — Motional emf and charge separation x
    
4. Q29.10 — Rotation and changing magnetic flux x
    
5. Q29.11 — Motional emf in an open circuit x
    
6. Q29.12 — Induced electric fields and nonconservative work x
    
7. Q29.13 — Scaling induced emf and electric fields
    
8. Q29.16 — Displacement current in capacitors
    
9. Q29.17 — Understanding Maxwell's four equations
    

### Secondary Priority — If Time Permits

- Q29.1 — Eddy-current braking
    
- Q29.2 — Generator frequency and emf
    
- Q29.9 — Lenz's law and magnetic forces
    
- Q29.15 — Conduction versus displacement current
    

Skip for now: Q29.4, Q29.6, Q29.8, Q29.14, Q29.18.

If you're especially pressed for time, prioritize Q29.3, Q29.5, Q29.7, Q29.10, Q29.13, Q29.16, and Q29.17.


18 questions. Standardized prompts with original solutions; source numbering follows the 13th edition.

## Q29.1: Eddy-current braking

Why does pulling a copper sheet out from between magnet poles require a force that grows with speed?

**Solution:**
As portions leave the field, changing flux drives eddy currents. Their magnetic forces oppose the flux-reducing motion, so an external pulling force is required. At low speeds with approximately fixed resistance, induced emf and current grow with speed, increasing drag; the input work becomes Joule heat.

**Why it works:**
Lenz's law fixes the opposing force direction and energy conservation identifies the heat source.

**Grading key points:**

- As portions leave the field, changing flux drives eddy currents.
- Their magnetic forces oppose the flux-reducing motion, so an external pulling force is required.
- At low speeds with approximately fixed resistance, induced emf and current grow with speed, increasing drag; the input work becomes Joule heat.

Source: [PDF page 1008](source-page-1008.png); source question Q29.1.

## Q29.2: Generator frequency and load torque

For a rotating loop generator, why do doubling angular speed double reversal frequency and maximum emf? What happens to required torque?

**Solution:**
For fixed flux amplitude, $\Phi=NBA\cos\omega t$ and $\mathcal E=NBA\omega\sin\omega t$. Thus electrical frequency and emf amplitude both double. With a fixed resistive load and negligible inductance, current amplitude doubles, torque amplitude and average torque double, and average power quadruples. With an open circuit there is negligible electromagnetic load torque; with other loads its change depends on impedance.

**Why it works:**
Differentiating flux introduces a factor of angular frequency; torque additionally depends on the current drawn.

**Grading key points:**

- For fixed flux amplitude, $\Phi=NBA\cos\omega t$ and $\mathcal E=NBA\omega\sin\omega t$.
- Thus electrical frequency and emf amplitude both double.
- With a fixed resistive load and negligible inductance, current amplitude doubles, torque amplitude and average torque double, and average power quadruples.
- With an open circuit there is negligible electromagnetic load torque; with other loads its change depends on impedance.

Source: [PDF page 1008](source-page-1008.png); source question Q29.2.

## Q29.3: Mutual induction of side-by-side loops

Two coplanar loops lie side by side without overlapping. If current in one increases, does the induced current in the other have the same or opposite sense? What if it decreases?

**Solution:**
For increasing current the induced current has the same circulation sense. The source loop's return field through the neighboring loop points opposite to its own central field, so the neighboring loop produces a field opposing that increasing return flux. For decreasing current the induced current has the opposite circulation sense.

**Why it works:**
The sign depends on the field at the second loop, not merely on the source current's clockwise label.

**Grading key points:**

- For increasing current the induced current has the same circulation sense.
- The source loop's return field through the neighboring loop points opposite to its own central field, so the neighboring loop produces a field opposing that increasing return flux.
- For decreasing current the induced current has the opposite circulation sense.

Source: [PDF page 1008](source-page-1008.png); source question Q29.3.

## Q29.4: Motional-emf dimensions

Verify that vBL has units of volts.

**Solution:**
$[vBL]=(\mathrm{m/s})(\mathrm{N/(A\,m)})(\mathrm m)=\mathrm{N\,m/(A\,s)}=\mathrm{J/C}=\mathrm V$.

**Why it works:**
Current times time is charge, so force times length divided by charge is voltage.

**Grading key points:**

- $[vBL]=(\mathrm{m/s})(\mathrm{N/(A\,m)})(\mathrm m)=\mathrm{N\,m/(A\,s)}=\mathrm{J/C}=\mathrm V$.

Source: [PDF page 1008](source-page-1008.png); source question Q29.4.

## Q29.5: Flux orientation

A straight wire passes through a ring's center perpendicular to the ring plane. Does an increasing wire current induce a circulating current in the ring?

**Solution:**
Not in the ideal coaxial geometry. The wire's magnetic field circles within the ring plane, so its normal component and flux through the ring are zero at all times. The changing current therefore produces no net emf around that ring.

**Why it works:**
Faraday's law uses normal magnetic flux, not merely a changing field magnitude somewhere nearby.

**Grading key points:**

- Not in the ideal coaxial geometry.
- The wire's magnetic field circles within the ring plane, so its normal component and flux through the ring are zero at all times.
- The changing current therefore produces no net emf around that ring.

Source: [PDF page 1008](source-page-1008.png); source question Q29.5.

## Q29.6: Magnet falling through a copper pipe

Can a magnet dropped through a vertical copper pipe reach terminal speed without air resistance? Why?

**Solution:**
Yes. Its moving field induces eddy currents in the pipe. Those currents create a force opposing motion and dissipate energy as heat. Where the drag increases with speed, a terminal speed is reached when magnetic drag balances weight; then gravitational power $mgv$ becomes heat. The pipe need not be ferromagnetic.

**Why it works:**
Induction provides a dissipative braking mechanism even in nonmagnetic copper.

**Grading key points:**

- Yes.
- Its moving field induces eddy currents in the pipe.
- Those currents create a force opposing motion and dissipate energy as heat.
- Where the drag increases with speed, a terminal speed is reached when magnetic drag balances weight; then gravitational power $mgv$ becomes heat.
- The pipe need not be ferromagnetic.

Source: [PDF page 1008](source-page-1008.png); source question Q29.6.

## Q29.7: Motional charge separation in an aircraft

A plane flies horizontally over Antarctica in an approximately upward vertical magnetic field. Which wingtip has higher potential as seen by a forward-facing passenger? Does heading matter?

**Solution:**
The right wingtip is at higher potential. Positive charges are driven by $\mathbf v\times\mathbf B$ toward the right until the internal electric force balances the magnetic force. For an upward field and horizontal flight, the passenger-relative right direction remains the same for every horizontal heading.

**Why it works:**
The vector product sets charge separation; changing heading rotates the aircraft-relative geometry together.

**Grading key points:**

- The right wingtip is at higher potential.
- Positive charges are driven by $\mathbf v\times\mathbf B$ toward the right until the internal electric force balances the magnetic force.
- For an upward field and horizontal flight, the passenger-relative right direction remains the same for every horizontal heading.

Source: [PDF page 1008](source-page-1008.png); source question Q29.7.

## Q29.8: Lenz force on nested loops

In Exercise 29.19 a small coplanar ring lies inside a larger battery-driven loop. Just after its switch closes, what force does the large loop exert on the ring? Distinguish local forces and net translation.

**Solution:**
The small ring's induced circulation opposes the increasing through-flux, hence opposes the larger loop's circulation. The resulting local magnetic forces tend to contract the small ring and repel nearby opposed-current portions of the outer loop. For exactly concentric coplanar loops the net translational force is zero by symmetry. If displaced from the center, the small ring tends toward the weaker-field central region, away from the nearest outer wire. Both responses oppose the increase in linked flux.

**Why it works:**
Distinguish distributed radial forces from their vector sum; Lenz's law opposes the change of linked flux.

**Grading key points:**

- The small ring's induced circulation opposes the increasing through-flux, hence opposes the larger loop's circulation.
- The resulting local magnetic forces tend to contract the small ring and repel nearby opposed-current portions of the outer loop.
- For exactly concentric coplanar loops the net translational force is zero by symmetry.
- If displaced from the center, the small ring tends toward the weaker-field central region, away from the nearest outer wire.
- Both responses oppose the increase in linked flux.

Source: [PDF page 1008](source-page-1008.png); source question Q29.8.

## Q29.9: Induction near a decaying wire current

A rectangular metal loop lies near a long wire with two sides parallel to it. If the wire current decreases, is the loop attracted or repelled?

**Solution:**
It is attracted during the induced-current transient. The induced loop current reinforces the decreasing original flux; on the nearer parallel side its current matches the wire's, giving attraction. The opposite current on the farther side gives weaker repulsion, leaving net attraction toward the wire.

**Why it works:**
The near-side $1/r$ force dominates, and approach tends to maintain the declining flux.

**Grading key points:**

- It is attracted during the induced-current transient.
- The induced loop current reinforces the decreasing original flux; on the nearer parallel side its current matches the wire's, giving attraction.
- The opposite current on the farther side gives weaker repulsion, leaving net attraction toward the wire.

Source: [PDF page 1008](source-page-1008.png); source question Q29.9.

## Q29.10: Rotation without changing flux

Can a square loop rotate about an axis along one side in a uniform constant B without induced emf?

**Solution:**
Yes, if the side's rotation axis is parallel to B. The loop's area normal remains perpendicular to B, so flux is always zero. If B has a component perpendicular to the axis, the normal generally sweeps through that component and flux varies, producing emf except at special instants.

**Why it works:**
Rotation matters only insofar as it changes $\mathbf B\cdot\mathbf A$.

**Grading key points:**

- Yes, if the side's rotation axis is parallel to B.
- The loop's area normal remains perpendicular to B, so flux is always zero.
- If B has a component perpendicular to the axis, the normal generally sweeps through that component and flux varies, producing emf except at special instants.

Source: [PDF page 1008](source-page-1008.png); source question Q29.10.

## Q29.11: Open slidewire circuit

If the U-shaped conductor in a moving-slidewire example has a break, what external force is needed to keep the bar at constant speed, neglecting friction?

**Solution:**
After a brief charge-separation transient, no sustained loop current flows, so the usual magnetic drag $I\ell B$ vanishes and no sustained external force is needed. A motional potential difference can still exist across the moving bar.

**Why it works:**
An emf without a closed conducting path need not produce the current responsible for braking.

**Grading key points:**

- After a brief charge-separation transient, no sustained loop current flows, so the usual magnetic drag $I\ell B$ vanishes and no sustained external force is needed.
- A motional potential difference can still exist across the moving bar.

Source: [PDF page 1008](source-page-1008.png); source question Q29.11.

## Q29.12: Nonconservative electric work

For a wire loop driven by changing magnetic flux, is it meaningful to ask about work on an electron around the loop? Is it meaningful to call that a potential difference around the complete loop?

**Solution:**
Electrical work is meaningful: $W=q\oint\mathbf E\cdot d\mathbf l=q\mathcal E$ for an effectively frozen-time circuit, with orientation and charge sign included; exact moving-particle work uses the time-dependent trajectory. In a resistive steady circulation this work is transferred to the lattice, not necessarily retained as electron kinetic energy. There is no single-valued scalar-potential difference equal to this nonzero closed-loop emf; the electron returns to the same position.

**Why it works:**
Induced E is nonconservative, so work per charge cannot generally be represented solely by an endpoint electrostatic potential difference.

**Grading key points:**

- Electrical work is meaningful: $W=q\oint\mathbf E\cdot d\mathbf l=q\mathcal E$ for an effectively frozen-time circuit, with orientation and charge sign included; exact moving-particle work uses the time-dependent trajectory.
- In a resistive steady circulation this work is transferred to the lattice, not necessarily retained as electron kinetic energy.
- There is no single-valued scalar-potential difference equal to this nonzero closed-loop emf; the electron returns to the same position.

Source: [PDF page 1008](source-page-1008.png); source question Q29.12.

## Q29.13: Scaling induced emf and field

A circular ring is perpendicular to a spatially uniform B increasing steadily. If its radius doubles, how do induced emf and tangential electric field at the ring change?

**Solution:**
Emf magnitude $\pi r^2|dB/dt|$ increases by 4. From $2\pi r E=\pi r^2|dB/dt|$, $E=(r/2)|dB/dt|$, so the induced tangential field doubles.

**Why it works:**
Emf is the line integral of E around a circumference that also changes length.

**Grading key points:**

- Emf magnitude $\pi r^2|dB/dt|$ increases by 4.
- From $2\pi r E=\pi r^2|dB/dt|$, $E=(r/2)|dB/dt|$, so the induced tangential field doubles.

Source: [PDF page 1008](source-page-1008.png), [PDF page 1009](source-page-1009.png); source question Q29.13.

## Q29.14: Mixed-state superconducting transport

A type-II superconductor between its lower and upper critical fields contains normal vortex cores and superconducting regions. What resistance does a long thin cylinder have?

**Solution:**
It can have zero dc resistance when a connected superconducting path carries subcritical current and vortices are pinned. Normal vortex cores alone do not force the sample's measured resistance to be nonzero. If vortices move, flux-flow dissipation produces finite resistance; current, field, pinning, and geometry therefore matter. In the elementary stationary mixed-state idealization the expected answer is zero.

**Why it works:**
A normal region does not necessarily lie in series with all current paths, and vortex dynamics determines dissipation.

**Grading key points:**

- It can have zero dc resistance when a connected superconducting path carries subcritical current and vortices are pinned.
- Normal vortex cores alone do not force the sample's measured resistance to be nonzero.
- If vortices move, flux-flow dissipation produces finite resistance; current, field, pinning, and geometry therefore matter.
- In the elementary stationary mixed-state idealization the expected answer is zero.

Source: [PDF page 1009](source-page-1009.png); source question Q29.14.

## Q29.15: Conduction plus displacement current

Can conduction current and displacement current both exist inside a conductor?

**Solution:**
Yes in time-dependent conditions: $\mathbf J_{cond}=\sigma\mathbf E$ and the vacuum-form displacement term is $\epsilon_0\partial\mathbf E/\partial t$. In a linear material formulation the latter is $\partial\mathbf D/\partial t$, with consistent separation of free and polarization currents. For a good conductor at low frequency the conduction term usually dominates; at steady dc the displacement term vanishes.

**Why it works:**
The two terms describe different responses and need not be mutually exclusive in space.

**Grading key points:**

- Yes in time-dependent conditions: $\mathbf J_{cond}=\sigma\mathbf E$ and the vacuum-form displacement term is $\epsilon_0\partial\mathbf E/\partial t$.
- In a linear material formulation the latter is $\partial\mathbf D/\partial t$, with consistent separation of free and polarization currents.
- For a good conductor at low frequency the conduction term usually dominates; at steady dc the displacement term vanishes.

Source: [PDF page 1009](source-page-1009.png); source question Q29.15.

## Q29.16: Dielectric gap versus lead current

Does equality of the charging-current and displacement-current expressions mean conduction current flows through an ideal capacitor's dielectric and equals displacement current there?

**Solution:**
No. Conduction current flows through the leads and charges the plates; in an ideal insulating gap it is zero. The displacement-current flux through the gap equals the lead current when formulated as $d\int\mathbf D\cdot d\mathbf A/dt$. If using only $\epsilon_0d\Phi_E/dt$ inside a dielectric, include polarization current separately; for fixed K it is the free lead current divided by K. Real leakage is an additional conduction current.

**Why it works:**
Equality across alternative spanning surfaces is not a claim that metallic conduction occurs through an ideal insulator.

**Grading key points:**

- No.
- Conduction current flows through the leads and charges the plates; in an ideal insulating gap it is zero.
- The displacement-current flux through the gap equals the lead current when formulated as $d\int\mathbf D\cdot d\mathbf A/dt$.
- If using only $\epsilon_0d\Phi_E/dt$ inside a dielectric, include polarization current separately; for fixed K it is the free lead current divided by K.
- Real leakage is an additional conduction current.

Source: [PDF page 1009](source-page-1009.png); source question Q29.16.

## Q29.17: Maxwell-equation matching

Match (a) changing magnetic flux produces circulating E, (b) charge motion and changing E produce circulating B, (c) E starts and ends on charge, (d) B has no monopole endpoints, to Maxwell equations.

**Solution:**
(a) Faraday: $\oint\mathbf E\cdot d\boldsymbol\ell=-d\Phi_B/dt$. (b) Ampere-Maxwell in vacuum: $\oint\mathbf B\cdot d\boldsymbol\ell=\mu_0I_{enc}+\mu_0\epsilon_0d\Phi_E/dt$. (c) Electric Gauss: $\oint\mathbf E\cdot d\mathbf A=Q_{enc}/\epsilon_0$. (d) Magnetic Gauss: $\oint\mathbf B\cdot d\mathbf A=0$.

**Why it works:**
Circulation equations describe curls; closed-surface equations describe sources and sinks.

**Grading key points:**

- (a) Faraday: $\oint\mathbf E\cdot d\boldsymbol\ell=-d\Phi_B/dt$. (b) Ampere-Maxwell in vacuum: $\oint\mathbf B\cdot d\boldsymbol\ell=\mu_0I_{enc}+\mu_0\epsilon_0d\Phi_E/dt$. (c) Electric Gauss: $\oint\mathbf E\cdot d\mathbf A=Q_{enc}/\epsilon_0$. (d) Magnetic Gauss: $\oint\mathbf B\cdot d\mathbf A=0$.

Source: [PDF page 1009](source-page-1009.png); source question Q29.17.

## Q29.18: Hypothetical magnetic current

If magnetic monopole current contributed to Faraday's law, what electric-field pattern would surround a long straight steady monopole current?

**Solution:**
The induced electric field would form circles around the monopole-current axis, analogous to B around an electric current. In the symmetric Maxwell convention where positive magnetic current enters Faraday's law with a minus sign, the E circulation follows a left-hand rule relative to positive magnetic current. The handedness must be stated with the sign convention.

**Why it works:**
A nonzero enclosed magnetic current would support electric circulation even without changing magnetic flux.

**Grading key points:**

- The induced electric field would form circles around the monopole-current axis, analogous to B around an electric current.
- In the symmetric Maxwell convention where positive magnetic current enters Faraday's law with a minus sign, the E circulation follows a left-hand rule relative to positive magnetic current.
- The handedness must be stated with the sign convention.

Source: [PDF page 1009](source-page-1009.png); source question Q29.18.
