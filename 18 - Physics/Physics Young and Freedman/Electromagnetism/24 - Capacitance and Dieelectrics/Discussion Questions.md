# Chapter 24: Capacitance and Dielectrics

20 questions. Standardized prompts with original solutions; source numbering follows the 13th edition.

## Q24.1: Breakdown and spacing

What limits how small the separation of a parallel-plate capacitor can be made to increase capacitance?

**Solution:**
At fixed applied voltage, $E=V/d$ rises as d decreases. Dielectric breakdown, tunneling or field emission at very small gaps, and eventual physical contact limit usable spacing. A simple breakdown bound is $d\gtrsim V/E_{\rm break}$.

**Why it works:**
The ideal formula $C=\epsilon A/d$ assumes the gap remains an insulator.

**Grading key points:**

- At fixed applied voltage, $E=V/d$ rises as d decreases.
- Dielectric breakdown, tunneling or field emission at very small gaps, and eventual physical contact limit usable spacing.
- A simple breakdown bound is $d\gtrsim V/E_{\rm break}$.

Source: [PDF page 836](source-page-836.png); source question Q24.1.

## Q24.2: Microscopic interpretation of capacitance

Why does a parallel-plate capacitor at fixed voltage store charge proportional to area and inversely proportional to separation?

**Solution:**
The required field is $E=V/d$, so the necessary free surface charge density is $\sigma=\epsilon V/d$. A larger area accommodates proportionally more separated charge at that density, giving $Q=\sigma A$ and $C=\epsilon A/d$. A smaller gap requires a larger field and charge density to maintain the same voltage.

**Why it works:**
Charge separation creates the field, and its integral across the gap gives the imposed voltage.

**Grading key points:**

- The required field is $E=V/d$, so the necessary free surface charge density is $\sigma=\epsilon V/d$.
- A larger area accommodates proportionally more separated charge at that density, giving $Q=\sigma A$ and $C=\epsilon A/d$.
- A smaller gap requires a larger field and charge density to maintain the same voltage.

Source: [PDF page 836](source-page-836.png); source question Q24.2.

## Q24.3: Unequal plate areas

When an initially neutral, isolated two-plate capacitor with unequal plate areas is charged by a battery, must its two net plate charges have equal magnitudes?

**Solution:**
In the ideal two-terminal capacitor model, yes: the battery transfers charge from one plate to the other, so their net charges are $+Q$ and $-Q$. Their surface charge densities and detailed distributions can differ. Stray capacitance to other conductors or preexisting net charge can invalidate the simple equal-and-opposite net-charge model.

**Why it works:**
Charge conservation applies to transferred charge; equal areas are not required.

**Grading key points:**

- In the ideal two-terminal capacitor model, yes: the battery transfers charge from one plate to the other, so their net charges are $+Q$ and $-Q$.
- Their surface charge densities and detailed distributions can differ.
- Stray capacitance to other conductors or preexisting net charge can invalidate the simple equal-and-opposite net-charge model.

Source: [PDF page 836](source-page-836.png); source question Q24.3.

## Q24.4: Electrostatic stress

Why might very large capacitors creak as they are charged?

**Solution:**
Opposite plates attract with an electric pressure about $\epsilon E^2/2$. As charge grows, this force compresses dielectrics and shifts plates and supports, producing mechanical strain and creaking.

**Why it works:**
Stored electric fields exert mechanical stress as well as storing energy.

**Grading key points:**

- Opposite plates attract with an electric pressure about $\epsilon E^2/2$.
- As charge grows, this force compresses dielectrics and shifts plates and supports, producing mechanical strain and creaking.

Source: [PDF page 836](source-page-836.png); source question Q24.4.

## Q24.5: Fringing and isolated-plate limit

If a parallel-plate capacitor's separation becomes much larger than its plate size, is the gap field uniform? At fixed Q, compare V and C with $Qd/(\epsilon_0A)$ and $\epsilon_0A/d$.

**Solution:**
The field is strongly nonuniform and fringing dominates. For fixed Q the actual voltage is smaller than the uniform-field extrapolation: distant finite plates approach finite isolated-conductor potentials rather than V growing linearly without bound. Therefore the actual $C=Q/V$ is greater than $\epsilon_0A/d$ in this large-separation limit.

**Why it works:**
The infinite-sheet approximation fails when the gap is comparable to or larger than the plate dimensions.

**Grading key points:**

- The field is strongly nonuniform and fringing dominates.
- For fixed Q the actual voltage is smaller than the uniform-field extrapolation: distant finite plates approach finite isolated-conductor potentials rather than V growing linearly without bound.
- Therefore the actual $C=Q/V$ is greater than $\epsilon_0A/d$ in this large-separation limit.

Source: [PDF page 836](source-page-836.png); source question Q24.5.

## Q24.6: Fixed voltage separation change

An ideal parallel-plate capacitor stays connected to a battery while its spacing doubles. How do field, charge, and stored energy change?

**Solution:**
V stays fixed and C halves. Therefore $E=V/d$ halves, $Q=CV$ halves, and $U=CV^2/2$ halves, neglecting fringing.

**Why it works:**
A connected ideal battery constrains voltage and permits charge to flow back.

**Grading key points:**

- V stays fixed and C halves.
- Therefore $E=V/d$ halves, $Q=CV$ halves, and $U=CV^2/2$ halves, neglecting fringing.

Source: [PDF page 836](source-page-836.png); source question Q24.6.

## Q24.7: Fixed charge separation change

A charged ideal parallel-plate capacitor is disconnected before its spacing doubles. How do field, voltage, and stored energy change?

**Solution:**
Q is fixed and C halves. Thus $E=Q/(\epsilon_0A)$ is unchanged, $V=Q/C$ doubles, and $U=Q^2/(2C)$ doubles. The added energy is supplied by the external pulling force.

**Why it works:**
Disconnecting conserves charge rather than voltage.

**Grading key points:**

- Q is fixed and C halves.
- Thus $E=Q/(\epsilon_0A)$ is unchanged, $V=Q/C$ doubles, and $U=Q^2/(2C)$ doubles.
- The added energy is supplied by the external pulling force.

Source: [PDF page 836](source-page-836.png); source question Q24.7.

## Q24.8: Comparing equal-voltage capacitors

Two otherwise identical parallel-plate capacitors have gaps d and 2d and the same voltage. Compare field, charge, and energy density.

**Solution:**
The smaller-gap capacitor has twice the field, twice the charge, and four times the energy density: $E\propto1/d$, $Q\propto1/d$, and $u=\epsilon_0E^2/2\propto1/d^2$.

**Why it works:**
Energy density depends quadratically on field, while charge depends linearly on field for fixed area.

**Grading key points:**

- The smaller-gap capacitor has twice the field, twice the charge, and four times the energy density: $E\propto1/d$, $Q\propto1/d$, and $u=\epsilon_0E^2/2\propto1/d^2$.

Source: [PDF page 836](source-page-836.png); source question Q24.8.

## Q24.9: Mechanical work and source energy

Where does work done separating the attracting plates of a capacitor go?

**Solution:**
If isolated, it increases stored field energy. If held at fixed voltage, the field energy decreases while charge returns energy to the battery: for a change $dC<0$, $dU=V^2dC/2<0$, external work is $-V^2dC/2>0$, and the battery receives $-V^2dC$, the sum. Mechanical losses may also occur in real hardware.

**Why it works:**
The energy balance must include both the capacitor and any connected source.

**Grading key points:**

- If isolated, it increases stored field energy.
- If held at fixed voltage, the field energy decreases while charge returns energy to the battery: for a change $dC<0$, $dU=V^2dC/2<0$, external work is $-V^2dC/2>0$, and the battery receives $-V^2dC$, the sum.
- Mechanical losses may also occur in real hardware.

Source: [PDF page 836](source-page-836.png); source question Q24.9.

## Q24.10: Dielectric screening at fixed charge

An isolated charged capacitor is immersed in insulating oil of dielectric constant K. Does the gap field change, and how could it be measured?

**Solution:**
For complete filling in the ideal parallel-plate model, the field decreases to $E_0/K$ because induced bound charges oppose the original field. Measure the voltage with a sufficiently high-input-impedance electrometer, then use $E\simeq V/d$; a field probe is another option. Ordinary voltmeter loading can disturb an isolated capacitor.

**Why it works:**
Polarization reduces the total field at fixed free charge.

**Grading key points:**

- For complete filling in the ideal parallel-plate model, the field decreases to $E_0/K$ because induced bound charges oppose the original field.
- Measure the voltage with a sufficiently high-input-impedance electrometer, then use $E\simeq V/d$; a field probe is another option.
- Ordinary voltmeter loading can disturb an isolated capacitor.

Source: [PDF page 836](source-page-836.png), [PDF page 837](source-page-837.png); source question Q24.10.

## Q24.11: Dielectric suitability

Why is ordinary water seldom used as a capacitor dielectric despite its large dielectric constant, about 80.4?

**Solution:**
Dissolved ions make ordinary water conduct, producing leakage, heating, and electrochemical reactions. Its dielectric properties also vary with temperature, purity, and frequency. A large dielectric constant alone does not guarantee a low-loss, high-breakdown insulator.

**Why it works:**
Capacitor performance requires electrical insulation and stability in addition to high permittivity.

**Grading key points:**

- Dissolved ions make ordinary water conduct, producing leakage, heating, and electrochemical reactions.
- Its dielectric properties also vary with temperature, purity, and frequency.
- A large dielectric constant alone does not guarantee a low-loss, high-breakdown insulator.

Source: [PDF page 837](source-page-837.png); source question Q24.11.

## Q24.12: Permittivity versus breakdown field

Distinguish dielectric constant from dielectric strength. Is there a simple universal relationship between them?

**Solution:**
Dielectric constant $K=\epsilon/\epsilon_0$ is dimensionless and measures polarization response in a stated regime. Dielectric strength is the maximum tolerable electric-field scale before breakdown and has units V/m. They describe different physical properties and have no simple universal proportionality.

**Why it works:**
Response to a field and failure under a field are different material characteristics.

**Grading key points:**

- Dielectric constant $K=\epsilon/\epsilon_0$ is dimensionless and measures polarization response in a stated regime.
- Dielectric strength is the maximum tolerable electric-field scale before breakdown and has units V/m.
- They describe different physical properties and have no simple universal proportionality.

Source: [PDF page 837](source-page-837.png); source question Q24.12.

## Q24.13: Localized dielectric damage

Why can small breakdown holes in a Mylar capacitor leave capacitance almost unchanged but greatly reduce breakdown voltage?

**Solution:**
Most of the area and dielectric thickness remain unchanged, so the total capacitance changes little. A small damaged region can create a much weaker insulation path and concentrate the local field; breakdown is controlled by that weakest location.

**Why it works:**
Capacitance sums contributions over area, while failure can begin at one defect.

**Grading key points:**

- Most of the area and dielectric thickness remain unchanged, so the total capacitance changes little.
- A small damaged region can create a much weaker insulation path and concentrate the local field; breakdown is controlled by that weakest location.

Source: [PDF page 837](source-page-837.png); source question Q24.13.

## Q24.14: Dielectric insertion force

What force acts on a dielectric slab brought into a charged capacitor gap, and what does that imply about energy?

**Solution:**
The slab is pulled into the high-field gap. For an isolated capacitor, insertion raises C and lowers $U=Q^2/(2C)$; the decrease can supply mechanical work. At fixed voltage the capacitor energy instead rises, but the source supplies more energy than that rise, leaving mechanical work. The electrical boundary condition must be specified.

**Why it works:**
Forces follow the energy of the whole constrained system, including a connected battery when present.

**Grading key points:**

- The slab is pulled into the high-field gap.
- For an isolated capacitor, insertion raises C and lowers $U=Q^2/(2C)$; the decrease can supply mechanical work.
- At fixed voltage the capacitor energy instead rises, but the source supplies more energy than that rise, leaving mechanical work.
- The electrical boundary condition must be specified.

Source: [PDF page 837](source-page-837.png); source question Q24.14.

## Q24.15: Capacitive moisture sensing

How can placing a fish between capacitor plates help assess its freshness as it dries?

**Solution:**
Water has a high low-frequency permittivity. As the fish loses water, its effective dielectric response generally decreases, reducing capacitance for the same geometry. A calibrated capacitance measurement can therefore indicate drying and, indirectly, freshness; temperature, geometry, and conductivity must be controlled.

**Why it works:**
Moisture changes effective permittivity, which changes C at fixed plate geometry.

**Grading key points:**

- Water has a high low-frequency permittivity.
- As the fish loses water, its effective dielectric response generally decreases, reducing capacitance for the same geometry.
- A calibrated capacitance measurement can therefore indicate drying and, indirectly, freshness; temperature, geometry, and conductivity must be controlled.

Source: [PDF page 837](source-page-837.png); source question Q24.15.

## Q24.16: Thin-film capacitance

Why can an electrolytic capacitor with an extremely thin oxide film achieve a large capacitance?

**Solution:**
The thin insulating oxide makes d very small in $C\simeq\epsilon A/d$; etched electrode surfaces can also make A large. The conductive electrolyte serves as the opposing electrical contact. The tradeoffs include polarity restrictions, leakage, and breakdown limits.

**Why it works:**
Large area and a very thin insulating layer increase capacitance.

**Grading key points:**

- The thin insulating oxide makes d very small in $C\simeq\epsilon A/d$; etched electrode surfaces can also make A large.
- The conductive electrolyte serves as the opposing electrical contact.
- The tradeoffs include polarity restrictions, leakage, and breakdown limits.

Source: [PDF page 837](source-page-837.png); source question Q24.16.

## Q24.17: Flux with dielectric at fixed free charge

For the Gaussian surface enclosing one plate in Figure 24.22, how does electric flux change when dielectric K fills an initially empty isolated capacitor?

**Solution:**
It decreases by factor K. At fixed free charge Q, polarization adds enclosed bound charge $-(1-1/K)Q$, leaving total enclosed charge $Q/K$. Hence $\Phi_E=Q/(K\epsilon_0)$. The displacement-field flux remains Q.

**Why it works:**
Gauss's law for E counts free plus bound charge, whereas the D formulation counts free charge.

**Grading key points:**

- It decreases by factor K.
- At fixed free charge Q, polarization adds enclosed bound charge $-(1-1/K)Q$, leaving total enclosed charge $Q/K$.
- Hence $\Phi_E=Q/(K\epsilon_0)$.
- The displacement-field flux remains Q.

Source: [PDF page 837](source-page-837.png); source question Q24.17.

## Q24.18: Fixed charge versus fixed voltage insertion

Describe changes to E, Q, and U when a dielectric K completely fills a parallel-plate capacitor (a) at fixed voltage and (b) after disconnection.

**Solution:**
At fixed V, C becomes KC: E stays fixed, Q becomes KQ, and U becomes KU. At fixed Q, C again becomes KC: E becomes E/K, Q stays fixed, and U becomes U/K. These statements assume a linear dielectric and negligible fringing.

**Why it works:**
The same increase in capacitance has different consequences depending on whether voltage or free charge is constrained.

**Grading key points:**

- At fixed V, C becomes KC: E stays fixed, Q becomes KQ, and U becomes KU.
- At fixed Q, C again becomes KC: E becomes E/K, Q stays fixed, and U becomes U/K.
- These statements assume a linear dielectric and negligible fringing.

Source: [PDF page 837](source-page-837.png); source question Q24.18.

## Q24.19: Thermal disorder of dipoles

Why does the dielectric constant of a polar liquid tend to decrease as temperature rises?

**Solution:**
The field tends to align permanent molecular dipoles, while thermal motion randomizes them. Higher temperature reduces their orientational alignment and therefore the orientational contribution to polarization and K, for comparable density and field.

**Why it works:**
Thermal agitation competes with dipole-field alignment energy.

**Grading key points:**

- The field tends to align permanent molecular dipoles, while thermal motion randomizes them.
- Higher temperature reduces their orientational alignment and therefore the orientational contribution to polarization and K, for comparable density and field.

Source: [PDF page 837](source-page-837.png); source question Q24.19.

## Q24.20: Perfect conductor as a dielectric limit

In the electrostatic screening analogy, is a perfect conductor described by K approaching zero or infinity?

**Solution:**
The formal screening limit is $K\to\infty$: mobile charges rearrange until the internal static field vanishes for finite applied forcing. This is an electrostatic analogy, not a complete finite-frequency dielectric model of a metal.

**Why it works:**
Complete screening is the extreme limit of polarization response, not its absence.

**Grading key points:**

- The formal screening limit is $K\to\infty$: mobile charges rearrange until the internal static field vanishes for finite applied forcing.
- This is an electrostatic analogy, not a complete finite-frequency dielectric model of a metal.

Source: [PDF page 837](source-page-837.png); source question Q24.20.
