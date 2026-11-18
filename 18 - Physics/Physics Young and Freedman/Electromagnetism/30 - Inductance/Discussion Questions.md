# Chapter 30: Inductance

14 questions. Standardized prompts with original solutions; source numbering follows the 13th edition.

## Q30.1: Inductive spark

Why does a trolley contact spark when it momentarily loses contact with its overhead supply?

**Solution:**
The motor and circuit have inductance storing $LI^2/2$. Interrupting current rapidly requires a large induced emf opposing its fall. The resulting voltage across the separating contacts can ionize the air and sustain an arc, dissipating stored energy.

**Why it works:**
Inductance resists rapid current change and converts stored field energy during interruption.

**Grading key points:**

- The motor and circuit have inductance storing $LI^2/2$.
- Interrupting current rapidly requires a large induced emf opposing its fall.
- The resulting voltage across the separating contacts can ionize the air and sustain an arc, dissipating stored energy.

Source: [PDF page 1039](source-page-1039.png); source question Q30.1.

## Q30.2: Henry units

Show that Wb/A and ohm-second are equivalent units of inductance.

**Solution:**
Since $1\ \mathrm{Wb}=1\ \mathrm{V\,s}$, $1\ \mathrm{Wb/A}=1\ \mathrm{(V/A)\,s}=1\ \Omega\,\mathrm s$. Both equal one henry.

**Why it works:**
Faraday's law relates flux-change rate to voltage, linking the two unit definitions.

**Grading key points:**

- Since $1\ \mathrm{Wb}=1\ \mathrm{V\,s}$, $1\ \mathrm{Wb/A}=1\ \mathrm{(V/A)\,s}=1\ \Omega\,\mathrm s$.
- Both equal one henry.

Source: [PDF page 1039](source-page-1039.png); source question Q30.2.

## Q30.3: Mutual-inductance orientation

In Figure 30.1 the neighboring coil axes are initially parallel. What happens to mutual inductance if coil 2 turns 90 degrees so its axis is vertical?

**Solution:**
Its magnitude decreases, ideally to zero for the symmetric orientation pictured: much less of coil 1's field passes normally through coil 2. Exact residual coupling depends on coil geometry and surrounding material.

**Why it works:**
Mutual inductance measures linked flux per source current, and rotating the area normal reduces that flux.

**Grading key points:**

- Its magnitude decreases, ideally to zero for the symmetric orientation pictured: much less of coil 1's field passes normally through coil 2.
- Exact residual coupling depends on coil geometry and surrounding material.

Source: [PDF page 1039](source-page-1039.png); source question Q30.3.

## Q30.4: Toroid symmetry

Why is self-inductance particularly easy to calculate for a tightly wound toroidal solenoid?

**Solution:**
Rotational symmetry makes B tangential and constant around each circular Amperian path, with $B(r)=\mu NI/(2\pi r)$ in the ideal core. Leakage is small, and the linked flux can be integrated over a known cross section. For a thin core this gives $L\simeq\mu N^2A/(2\pi R)$.

**Why it works:**
Symmetry simplifies both Ampere's law for B and the flux-linkage integral.

**Grading key points:**

- Rotational symmetry makes B tangential and constant around each circular Amperian path, with $B(r)=\mu NI/(2\pi r)$ in the ideal core.
- Leakage is small, and the linked flux can be integrated over a known cross section.
- For a thin core this gives $L\simeq\mu N^2A/(2\pi R)$.

Source: [PDF page 1039](source-page-1039.png); source question Q30.4.

## Q30.5: Coupled-coil equivalent inductance

Two nearly touching identical coaxial coils each have self-inductance L. Find their aiding series and parallel equivalent inductances, and discuss cancellation.

**Solution:**
Let mutual inductance be M. Series aiding gives $2L+2M$, approximately 4L for nearly perfect coupling M≈L. Parallel aiding with symmetric current sharing gives $(L+M)/2$, approximately L. Series opposing gives $2L-2M$, ideally zero for M=L but small and positive with real leakage. Opposing parallel connection is a singular ideal-coupling limit and must not be treated as a generic independent-inductor parallel formula.

**Why it works:**
Each coil links the other's flux; signs and current division determine the mutual terms.

**Grading key points:**

- Let mutual inductance be M.
- Series aiding gives $2L+2M$, approximately 4L for nearly perfect coupling M≈L.
- Parallel aiding with symmetric current sharing gives $(L+M)/2$, approximately L.
- Series opposing gives $2L-2M$, ideally zero for M=L but small and positive with real leakage.
- Opposing parallel connection is a singular ideal-coupling limit and must not be treated as a generic independent-inductor parallel formula.

Source: [PDF page 1039](source-page-1039.png); source question Q30.5.

## Q30.6: Coil-size scaling

Two closely wound circular coils have the same number of turns, but one has twice the radius. Compare self-inductances.

**Solution:**
For geometrically similar coils, doubling all linear dimensions doubles L: field scales as NI/R, area as R², and flux linkage therefore as N²IR. Thus the larger coil has approximately twice the inductance under that similarity assumption. If only loop radius changes while wire thickness and winding cross section are fixed, logarithmic geometry factors also change, so no exact ratio follows from radius and turns alone.

**Why it works:**
Inductance depends on complete geometry; the simple factor-two result uses geometric similarity.

**Grading key points:**

- For geometrically similar coils, doubling all linear dimensions doubles L: field scales as NI/R, area as R², and flux linkage therefore as N²IR.
- Thus the larger coil has approximately twice the inductance under that similarity assumption.
- If only loop radius changes while wire thickness and winding cross section are fixed, logarithmic geometry factors also change, so no exact ratio follows from radius and turns alone.

Source: [PDF page 1039](source-page-1039.png); source question Q30.6.

## Q30.7: Noninductive winding

Would winding half a resistor wire in one sense and half in the opposite sense reduce its inductance?

**Solution:**
Yes if the opposite sections are closely coupled and carry equal currents so their fields largely cancel. A closely adjacent bifilar out-and-back arrangement is especially effective. Merely putting two opposite-wound halves far apart leaves much of their self-field and will not guarantee negligible inductance.

**Why it works:**
Cancellation requires overlapping opposing flux, not just equal numbers of clockwise and counterclockwise turns somewhere.

**Grading key points:**

- Yes if the opposite sections are closely coupled and carry equal currents so their fields largely cancel.
- A closely adjacent bifilar out-and-back arrangement is especially effective.
- Merely putting two opposite-wound halves far apart leaves much of their self-field and will not guarantee negligible inductance.

Source: [PDF page 1039](source-page-1039.png); source question Q30.7.

## Q30.8: Fixed B versus fixed current energy

For the same B, compare magnetic energy density in vacuum and a linear material of permeability $\mu>\mu_0$. Does a fixed-current solenoid store less energy with a magnetic core?

**Solution:**
At the same B, $u=B^2/(2\mu)$ is smaller in the higher-permeability material. At fixed solenoid current, however, $B=\mu nI$, so $u=\mu n^2I^2/2$ and $U=LI^2/2$ increase with permeability. For real nonlinear hysteretic ferromagnets, use the appropriate integral energy relation rather than assuming constant mu.

**Why it works:**
The answer changes when the controlled variable changes from field B to current I.

**Grading key points:**

- At the same B, $u=B^2/(2\mu)$ is smaller in the higher-permeability material.
- At fixed solenoid current, however, $B=\mu nI$, so $u=\mu n^2I^2/2$ and $U=LI^2/2$ increase with permeability.
- For real nonlinear hysteretic ferromagnets, use the appropriate integral energy relation rather than assuming constant mu.

Source: [PDF page 1039](source-page-1039.png); source question Q30.8.

## Q30.9: Signed current in an LC oscillator

The LC equation gives $L\,di/dt=-q/C$ at initial positive charge. How can current increase from zero if its derivative is negative?

**Solution:**
The defined positive current direction is the one that increases the chosen signed plate charge. During initial discharge the actual current is negative and grows in magnitude while i becomes more negative, so $di/dt<0$.

**Why it works:**
Increasing current magnitude does not imply increasing algebraic current.

**Grading key points:**

- The defined positive current direction is the one that increases the chosen signed plate charge.
- During initial discharge the actual current is negative and grows in magnitude while i becomes more negative, so $di/dt<0$.

Source: [PDF page 1039](source-page-1039.png); source question Q30.9.

## Q30.10: Charge derivative convention

Why is $i=dq/dt$, rather than $-dq/dt$, consistent in the textbook LC derivation even while the capacitor discharges?

**Solution:**
q is the signed charge on a designated plate and the positive i arrow is chosen into that plate. During its discharge q decreases and i is negative. If positive current were defined as leaving that plate, the relation would instead be $i=-dq/dt$; all loop signs would change consistently.

**Why it works:**
The relation is fixed by signed variable definitions and charge conservation, not by choosing a new sign in each phase.

**Grading key points:**

- q is the signed charge on a designated plate and the positive i arrow is chosen into that plate.
- During its discharge q decreases and i is negative.
- If positive current were defined as leaving that plate, the relation would instead be $i=-dq/dt$; all loop signs would change consistently.

Source: [PDF page 1039](source-page-1039.png); source question Q30.10.

## Q30.11: Voltage jump and current continuity

In a series RL switching circuit, why can voltage change suddenly while inductor current remains continuous?

**Solution:**
The constitutive relation is $v_L=L\,di/dt$. A finite step in voltage produces a finite step in the current's slope, not in current itself. A finite current jump would require a voltage impulse with integral $L\Delta i$; ordinary finite source voltages do not provide it.

**Why it works:**
An inductor constrains current continuity under finite applied voltage, while its voltage may have a step.

**Grading key points:**

- The constitutive relation is $v_L=L\,di/dt$.
- A finite step in voltage produces a finite step in the current's slope, not in current itself.
- A finite current jump would require a voltage impulse with integral $L\Delta i$; ordinary finite source voltages do not provide it.

Source: [PDF page 1039](source-page-1039.png); source question Q30.11.

## Q30.12: Series-current continuity

In the textbook RL circuit, is resistor current always the same as inductor current?

**Solution:**
Yes in the ideal lumped series circuit in each specified switch configuration, because there is no branching or charge-storage element between them. Real parasitic capacitances can produce very brief departures from the ideal model.

**Why it works:**
Kirchhoff's junction rule enforces equal current in a single unbranched path.

**Grading key points:**

- Yes in the ideal lumped series circuit in each specified switch configuration, because there is no branching or charge-storage element between them.
- Real parasitic capacitances can produce very brief departures from the ideal model.

Source: [PDF page 1039](source-page-1039.png); source question Q30.12.

## Q30.13: Interrupting inductive current

Why does opening a switch in an inductive circuit produce an arc, and can the current stop instantaneously?

**Solution:**
A rapid current decrease creates a large $L\,di/dt$ voltage, often breaking down air across the contacts. Stored magnetic energy then flows into the arc, resistance, radiation, or parasitic capacitance. A nonzero current cannot drop discontinuously under a finite voltage; exact instantaneous cessation would require an ideal voltage impulse.

**Why it works:**
Inductor flux linkage and stored energy must be accounted for during interruption.

**Grading key points:**

- A rapid current decrease creates a large $L\,di/dt$ voltage, often breaking down air across the contacts.
- Stored magnetic energy then flows into the arc, resistance, radiation, or parasitic capacitance.
- A nonzero current cannot drop discontinuously under a finite voltage; exact instantaneous cessation would require an ideal voltage impulse.

Source: [PDF page 1039](source-page-1039.png); source question Q30.13.

## Q30.14: Damping threshold

How can a free series RLC circuit be classified as underdamped or overdamped? Is comparing energy loss per cycle sufficient?

**Solution:**
From $L\ddot q+R\dot q+q/C=0$, let $\alpha=R/(2L)$ and $\omega_0=1/\sqrt{LC}$. Underdamped means $\alpha<\omega_0$ or $R<2\sqrt{L/C}$; overdamped means the reverse; equality is critical damping. In an overdamped circuit there is no oscillation cycle. An energy-loss-per-cycle comparison can estimate weak damping through Q, but is not a reliable exact threshold test.

**Why it works:**
The characteristic roots determine whether oscillatory solutions exist; a cycle-based test presupposes oscillation.

**Grading key points:**

- From $L\ddot q+R\dot q+q/C=0$, let $\alpha=R/(2L)$ and $\omega_0=1/\sqrt{LC}$.
- Underdamped means $\alpha<\omega_0$ or $R<2\sqrt{L/C}$; overdamped means the reverse; equality is critical damping.
- In an overdamped circuit there is no oscillation cycle.
- An energy-loss-per-cycle comparison can estimate weak damping through Q, but is not a reliable exact threshold test.

Source: [PDF page 1039](source-page-1039.png); source question Q30.14.
