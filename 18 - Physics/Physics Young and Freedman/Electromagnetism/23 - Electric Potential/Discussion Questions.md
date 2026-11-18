# Chapter 23: Electric Potential

21 questions. Standardized prompts with original solutions; source numbering follows the 13th edition.

## Q23.1: Potential as energy per charge

Why introduce electric potential if potential energy is proportional to it?

**Solution:**
Potential $V=U/q$ describes the source configuration independently of the test charge. Once V is known, the potential energy of any test charge is $qV$ and its change is $q\Delta V$.

**Why it works:**
Separating a source property from the test charge makes the same field description reusable.

**Grading key points:**

- Potential $V=U/q$ describes the source configuration independently of the test charge.
- Once V is known, the potential energy of any test charge is $qV$ and its change is $q\Delta V$.

Source: [PDF page 804](source-page-804.png); source question Q23.1.

## Q23.2: Equipotential transport

Can a test charge travel from infinity to the midpoint of an equal-and-opposite charge pair with no electric work on any portion of its path?

**Solution:**
Yes. Approach within the perpendicular-bisector plane, where the distances to the two charges are equal and $V=kq/r-kq/r=0$. Every displacement tangent to this plane has $\mathbf E\cdot d\mathbf l=0$, so each segment involves zero electric work.

**Why it works:**
An equipotential path can have nonzero transverse field but zero tangential electrical work.

**Grading key points:**

- Yes.
- Approach within the perpendicular-bisector plane, where the distances to the two charges are equal and $V=kq/r-kq/r=0$.
- Every displacement tangent to this plane has $\mathbf E\cdot d\mathbf l=0$, so each segment involves zero electric work.

Source: [PDF page 804](source-page-804.png); source question Q23.2.

## Q23.3: Cancellation of pair energies

Can two nonzero point charges at finite separation have the same interaction energy as at infinite separation? Can three?

**Solution:**
For two, no: $U=kq_1q_2/r$ is nonzero for finite r and nonzero charges. For three, yes, because pair terms can cancel. At the vertices of an equilateral triangle take charges $q,q,-q/2$; then $U=(k/r)(q^2-q^2/2-q^2/2)=0$.

**Why it works:**
System energy is a signed sum over distinct pairs, not the sum of charge magnitudes.

**Grading key points:**

- For two, no: $U=kq_1q_2/r$ is nonzero for finite r and nonzero charges.
- For three, yes, because pair terms can cancel.
- At the vertices of an equilateral triangle take charges $q,q,-q/2$; then $U=(k/r)(q^2-q^2/2-q^2/2)=0$.

Source: [PDF page 804](source-page-804.png); source question Q23.3.

## Q23.4: Potential reference invariance

If potential has an arbitrary zero, how can a voltmeter have a definite reading?

**Solution:**
It measures a potential difference $V_a-V_b$. Adding the same constant to both endpoint potentials cancels and leaves the reading unchanged.

**Why it works:**
Observable work per charge depends on differences rather than an absolute reference.

**Grading key points:**

- It measures a potential difference $V_a-V_b$.
- Adding the same constant to both endpoint potentials cancels and leaves the reading unchanged.

Source: [PDF page 804](source-page-804.png); source question Q23.4.

## Q23.5: Path independence

If the electrostatic field is zero along one path from A to B, what is $V_B-V_A$? Must the field be zero along every other connecting path?

**Solution:**
The difference is zero because $V_B-V_A=-\int_A^B\mathbf E\cdot d\mathbf l=0$. Other paths may pass through nonzero fields; their signed integrals still vanish. For example, a conductor connects equal-potential endpoints while an alternative path leaves and returns through the exterior field.

**Why it works:**
Electrostatic integrals are path independent even though the local field need not be.

**Grading key points:**

- The difference is zero because $V_B-V_A=-\int_A^B\mathbf E\cdot d\mathbf l=0$.
- Other paths may pass through nonzero fields; their signed integrals still vanish.
- For example, a conductor connects equal-potential endpoints while an alternative path leaves and returns through the exterior field.

Source: [PDF page 804](source-page-804.png); source question Q23.5.

## Q23.6: Constant versus zero potential

If the electrostatic field is zero throughout a connected region, is the potential necessarily zero?

**Solution:**
No. Since $\mathbf E=-\nabla V$, V is spatially constant throughout that connected region, but its constant value depends on the chosen reference.

**Why it works:**
Zero gradient fixes variation, not the additive constant.

**Grading key points:**

- No.
- Since $\mathbf E=-\nabla V$, V is spatially constant throughout that connected region, but its constant value depends on the chosen reference.

Source: [PDF page 804](source-page-804.png); source question Q23.6.

## Q23.7: Conservative electric field

Why is the line integral of an electrostatic field around any closed path zero?

**Solution:**
Returning to the starting point gives $\Delta V=0$, so $\oint\mathbf E\cdot d\mathbf l=-\Delta V=0$. This holds wherever the electrostatic field is defined along the path, regardless of the locations of stationary charges. It does not hold generally for induced electric fields from changing magnetic flux.

**Why it works:**
A static electric field derives from a single-valued scalar potential.

**Grading key points:**

- Returning to the starting point gives $\Delta V=0$, so $\oint\mathbf E\cdot d\mathbf l=-\Delta V=0$.
- This holds wherever the electrostatic field is defined along the path, regardless of the locations of stationary charges.
- It does not hold generally for induced electric fields from changing magnetic flux.

Source: [PDF page 804](source-page-804.png); source question Q23.7.

## Q23.8: Battery polarity and series voltages

Two ideal 1.5-V cells are placed end to end. Find the exposed-terminal voltage when opposite terminals touch and when positive terminals touch.

**Solution:**
With a positive terminal touching a negative terminal, the potential rises add to 3.0 V. With positive terminals together, the two equal rises oppose and the exposed negative terminals have zero potential difference.

**Why it works:**
Signed potential changes add along a path; orientation determines addition or cancellation.

**Grading key points:**

- With a positive terminal touching a negative terminal, the potential rises add to 3.0 V.
- With positive terminals together, the two equal rises oppose and the exposed negative terminals have zero potential difference.

Source: [PDF page 804](source-page-804.png); source question Q23.8.

## Q23.9: Voltage versus delivered energy

Why can a carpet-induced discharge at several thousand volts be mild while contact with a power line at comparable voltage can be fatal?

**Solution:**
A static body charge has small capacitance and limited energy $U=CV^2/2$; discharge quickly reduces its voltage. A power supply can maintain voltage and drive current through the body for much longer, delivering much more energy. Current path, impedance, and duration all matter.

**Why it works:**
Voltage alone does not specify charge availability, delivered power, or exposure duration.

**Grading key points:**

- A static body charge has small capacitance and limited energy $U=CV^2/2$; discharge quickly reduces its voltage.
- A power supply can maintain voltage and drive current through the body for much longer, delivering much more energy.
- Current path, impedance, and duration all matter.

Source: [PDF page 804](source-page-804.png); source question Q23.9.

## Q23.10: Field requires a gradient

Can the electric field at a point be determined from the potential value at that single point?

**Solution:**
No. $\mathbf E=-\nabla V$ requires spatial variation near the point. A constant potential and a linearly varying potential can share one value while having different fields there.

**Why it works:**
A function's value does not determine its derivatives.

**Grading key points:**

- No. $\mathbf E=-\nabla V$ requires spatial variation near the point.
- A constant potential and a linearly varying potential can share one value while having different fields there.

Source: [PDF page 804](source-page-804.png); source question Q23.10.

## Q23.11: Equipotential intersection at a null

Why can equal-potential branches appear to cross at the center of Figure 23.23c without defining contradictory field directions?

**Solution:**
The center is a field-null point, $\mathbf E=0$, where there is no nonzero field direction to constrain the surface normal. Distinct potential values never intersect. Branches of the same level set can meet at a critical point where $\nabla V=0$.

**Why it works:**
The usual unique perpendicular-direction argument assumes a nonzero gradient.

**Grading key points:**

- The center is a field-null point, $\mathbf E=0$, where there is no nonzero field direction to constrain the surface normal.
- Distinct potential values never intersect.
- Branches of the same level set can meet at a critical point where $\nabla V=0$.

Source: [PDF page 804](source-page-804.png); source question Q23.11.

## Q23.12: Potential decreases along field

A uniform field points east. B is 2.00 m west, C is 2.00 m east, and D is 2.00 m south of A. Compare their potentials with A.

**Solution:**
$V_B-V_A=+2.00E$, $V_C-V_A=-2.00E$, and $V_D-V_A=0$, with E in V/m and distances in m. Thus B is higher, C lower, and D equal.

**Why it works:**
Only the displacement component along the field contributes to $\Delta V=-\mathbf E\cdot\Delta\mathbf r$.

**Grading key points:**

- $V_B-V_A=+2.00E$, $V_C-V_A=-2.00E$, and $V_D-V_A=0$, with E in V/m and distances in m.
- Thus B is higher, C lower, and D equal.

Source: [PDF page 804](source-page-804.png); source question Q23.12.

## Q23.13: Potential sign versus charge sign

Does positive potential imply positive local charge, or negative potential imply negative local charge? Give examples.

**Solution:**
No. An uncharged point near a positive source has positive potential with infinity as zero. A small negative object near a sufficiently large positive source can also have positive total potential; conversely a positive object near a strong negative source can have negative potential. Changing the reference can reverse a potential's sign without moving any charge.

**Why it works:**
Potential is the sum of contributions from all sources plus an arbitrary constant, not a direct label of local charge.

**Grading key points:**

- No.
- An uncharged point near a positive source has positive potential with infinity as zero.
- A small negative object near a sufficiently large positive source can also have positive total potential; conversely a positive object near a strong negative source can have negative potential.
- Changing the reference can reverse a potential's sign without moving any charge.

Source: [PDF page 804](source-page-804.png); source question Q23.13.

## Q23.14: Charging work

For an isolated conducting sphere of fixed radius, is the work to assemble charge Q proportional to $Q^2$?

**Solution:**
Yes. With capacitance C fixed, the potential at intermediate charge q is $q/C$. Bringing in $dq$ quasistatically requires $dW=(q/C)dq$, hence $W=Q^2/(2C)=kQ^2/(2R)$.

**Why it works:**
The charging voltage increases during assembly; using only the final voltage would double-count the work.

**Grading key points:**

- Yes.
- With capacitance C fixed, the potential at intermediate charge q is $q/C$.
- Bringing in $dq$ quasistatically requires $dW=(q/C)dq$, hence $W=Q^2/(2C)=kQ^2/(2R)$.

Source: [PDF page 805](source-page-805.png); source question Q23.14.

## Q23.15: Parallel potential differences

Three plate pairs A, B, C in Figure Q23.15 are all connected between the same nodes a and b, across a 1.5-V battery. What is each plate-pair voltage?

**Solution:**
Each has a 1.5-V potential difference, with polarity set by its connections to a and b. Ideal wires make every plate connected to a equipotential, and similarly for b.

**Why it works:**
Parallel branches share the same two endpoint potentials regardless of plate shape or capacitance.

**Grading key points:**

- Each has a 1.5-V potential difference, with polarity set by its connections to a and b.
- Ideal wires make every plate connected to a equipotential, and similarly for b.

Source: [PDF page 805](source-page-805.png); source question Q23.15.

## Q23.16: Conductor field versus potential

Place a conducting sphere between charged parallel plates. Do its interior field and potential depend on position? Does giving it net charge change those conclusions?

**Solution:**
In electrostatic equilibrium the field inside the metal remains zero at every placement and for any static net charge. Its interior potential is uniform but can change with placement and with its net charge; for a neutral small sphere in a uniform external field it follows the external potential at its center.

**Why it works:**
Zero internal field constrains spatial variation within the conductor, not its common potential relative to the surroundings.

**Grading key points:**

- In electrostatic equilibrium the field inside the metal remains zero at every placement and for any static net charge.
- Its interior potential is uniform but can change with placement and with its net charge; for a neutral small sphere in a uniform external field it follows the external potential at its center.

Source: [PDF page 805](source-page-805.png); source question Q23.16.

## Q23.17: Potential in an empty cavity

An isolated charged conductor contains an empty cavity. Compare the potentials in the conductor and cavity.

**Solution:**
The entire connected conductor is at one potential. The empty closed cavity has the same constant potential and zero field: its boundary is at that potential and the unique charge-free electrostatic solution is constant.

**Why it works:**
Electrostatic shielding and the uniqueness theorem fix the cavity potential, regardless of the conductor's total charge.

**Grading key points:**

- The entire connected conductor is at one potential.
- The empty closed cavity has the same constant potential and zero field: its boundary is at that potential and the unique charge-free electrostatic solution is constant.

Source: [PDF page 805](source-page-805.png); source question Q23.17.

## Q23.18: Equipotential shielding and contact hazard

A dc line places a car's metal body 10,000 V above ground. Compare being inside with stepping out while touching the car.

**Solution:**
In the ideal electrostatic conductor model, occupants fully inside the closed metal enclosure and not bridging to ground experience little field, even though the whole enclosure is at high potential. Touching the car and ground simultaneously makes a conducting path across a large potential difference and can drive a dangerous current. Real openings and arcing make this a model, not a safe-exit procedure.

**Why it works:**
A common high potential produces no internal voltage difference; bridging different potentials does.

**Grading key points:**

- In the ideal electrostatic conductor model, occupants fully inside the closed metal enclosure and not bridging to ground experience little field, even though the whole enclosure is at high potential.
- Touching the car and ground simultaneously makes a conducting path across a large potential difference and can drive a dangerous current.
- Real openings and arcing make this a model, not a safe-exit procedure.

Source: [PDF page 805](source-page-805.png); source question Q23.18.

## Q23.19: Corona discharge

Explain St. Elmo's fire at mast tips during storms and why seawater-wet masts enhance it.

**Solution:**
Large atmospheric fields concentrate at conductive sharp tips, ionizing nearby air. Excited molecules emit the bluish corona glow. Conductive seawater films improve electrical connection and charge redistribution along an otherwise poorly conducting mast, enhancing the tip field.

**Why it works:**
Surface curvature concentrates charge and electric field; sufficiently strong fields ionize air.

**Grading key points:**

- Large atmospheric fields concentrate at conductive sharp tips, ionizing nearby air.
- Excited molecules emit the bluish corona glow.
- Conductive seawater films improve electrical connection and charge redistribution along an otherwise poorly conducting mast, enhancing the tip field.

Source: [PDF page 805](source-page-805.png); source question Q23.19.

## Q23.20: Method of images and its domain

Does replacing a very large conducting plane near a positive point charge by an equal negative mirror charge reproduce the field?

**Solution:**
For an ideal infinite grounded plane, yes in the physical half-space containing the real charge. The real-plus-image potential is zero on the plane and satisfies the same boundary conditions there, so uniqueness gives the same external field. It does not reproduce the field inside or behind the conductor, and an arbitrary isolated or biased finite plane needs additional information.

**Why it works:**
Image charges reproduce a boundary-value solution in a specified region; they are not physical charges behind the metal.

**Grading key points:**

- For an ideal infinite grounded plane, yes in the physical half-space containing the real charge.
- The real-plus-image potential is zero on the plane and satisfies the same boundary conditions there, so uniqueness gives the same external field.
- It does not reproduce the field inside or behind the conductor, and an arbitrary isolated or biased finite plane needs additional information.

Source: [PDF page 805](source-page-805.png); source question Q23.20.

## Q23.21: Choice of ground reference

Can Earth's potential be defined as zero even if Earth has nonzero net charge?

**Solution:**
Yes. The potential zero is a reference choice, so assigning zero to Earth is consistent with nonzero charge. Relative to infinity its potential may be nonzero, but voltage differences between nearby circuit points do not depend on that additive constant.

**Why it works:**
Net charge determines potential differences through the field, not a mandatory zero reference.

**Grading key points:**

- Yes.
- The potential zero is a reference choice, so assigning zero to Earth is consistent with nonzero charge.
- Relative to infinity its potential may be nonzero, but voltage differences between nearby circuit points do not depend on that additive constant.

Source: [PDF page 805](source-page-805.png); source question Q23.21.
