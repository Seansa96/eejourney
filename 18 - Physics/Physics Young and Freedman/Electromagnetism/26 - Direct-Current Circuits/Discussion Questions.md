# Chapter 26: Direct-Current Circuits

21 questions. Standardized prompts with original solutions; source numbering follows the 13th edition.

## Q26.1: Rated bulb resistance

Compare the resistances of 120-V, 60-W and 120-W bulbs. Compare voltage drops when they are in series across 120 V and when in parallel.

**Solution:**
Using rated hot resistances, $R=V^2/P$: the 60-W bulb is 240 ohms and the 120-W bulb 120 ohms. In series the same current gives a greater drop across the 60-W bulb (80 V versus 40 V in a constant-resistance model). In parallel each has 120 V. Real filament resistances change away from their rated temperatures.

**Why it works:**
Voltage drops divide in proportion to resistance in series; parallel branches share voltage.

**Grading key points:**

- Using rated hot resistances, $R=V^2/P$: the 60-W bulb is 240 ohms and the 120-W bulb 120 ohms.
- In series the same current gives a greater drop across the 60-W bulb (80 V versus 40 V in a constant-resistance model).
- In parallel each has 120 V.
- Real filament resistances change away from their rated temperatures.

Source: [PDF page 900](source-page-900.png); source question Q26.1.

## Q26.2: Unequal series bulb overload

A 25-W and a 200-W bulb, each rated 120 V, are placed in series across 240 V. Which is likely to burn out first and why?

**Solution:**
The 25-W bulb has the larger rated resistance: 576 ohms versus 72 ohms. The constant-hot-resistance model gives $I=240/648\approx0.370$ A and about 213 V across the 25-W bulb, dissipating about 79 W, far above its rating. The 200-W bulb gets only about 27 V. Thus the 25-W bulb is severely overloaded.

**Why it works:**
Equal series current concentrates power and voltage in the higher-resistance bulb; exact hot values evolve during the transient.

**Grading key points:**

- The 25-W bulb has the larger rated resistance: 576 ohms versus 72 ohms.
- The constant-hot-resistance model gives $I=240/648\approx0.370$ A and about 213 V across the 25-W bulb, dissipating about 79 W, far above its rating.
- The 200-W bulb gets only about 27 V.
- Thus the 25-W bulb is severely overloaded.

Source: [PDF page 900](source-page-900.png); source question Q26.2.

## Q26.3: Series versus parallel loading

What happens to individual bulb brightness as identical bulbs are added in series or parallel to a flashlight battery? Which arrangement tends to last longer?

**Solution:**
Adding series bulbs raises total resistance and makes each dimmer. Adding parallel bulbs leaves each brightness unchanged for an ideal source but increases total current; a real battery's voltage sag can dim them. For the same number of bulbs, series connection draws less current and generally lasts longer, but provides much less light.

**Why it works:**
Battery lifetime depends on discharge rate and useful-light criterion; equal brightness and equal runtime are not implied.

**Grading key points:**

- Adding series bulbs raises total resistance and makes each dimmer.
- Adding parallel bulbs leaves each brightness unchanged for an ideal source but increases total current; a real battery's voltage sag can dim them.
- For the same number of bulbs, series connection draws less current and generally lasts longer, but provides much less light.

Source: [PDF page 900](source-page-900.png); source question Q26.3.

## Q26.4: Mixed series-parallel bulb network

In Figure Q26.4 bulb A forms one battery branch and B and C form a series branch. Compare brightness, current, and voltage. What happens if each bulb is removed?

**Solution:**
For identical constant R, A has V and current V/R; B and C each have V/2 and current V/(2R). A is brightest, with four times either other's power. Removing A leaves B and C lit in series. Removing B opens their branch, extinguishing both B and C while A remains lit; removing C has the analogous result. With an ideal battery unaffected branches keep their brightness; a real battery can change terminal voltage.

**Why it works:**
The diagram has A in parallel with the series pair B-C; opening one branch need not open the other.

**Grading key points:**

- For identical constant R, A has V and current V/R; B and C each have V/2 and current V/(2R).
- A is brightest, with four times either other's power.
- Removing A leaves B and C lit in series.
- Removing B opens their branch, extinguishing both B and C while A remains lit; removing C has the analogous result.
- With an ideal battery unaffected branches keep their brightness; a real battery can change terminal voltage.

Source: [PDF page 900](source-page-900.png); source question Q26.4.

## Q26.5: Series-resistor statements

For the series chain a--R1--b--R2--c with $R_2>R_1$ and current from a to c, assess claims (a) equal currents, (b) larger current in R1, (c) equal powers, (d) larger power in R2, (e) equal voltage drops, (f) Va=Vc, (g) Vb<Vc, (h) Vc<Vb.

**Solution:**
For nonzero indicated current: (a) true; (b) false; (c) false; (d) true since $P=I^2R$; (e) false since $\Delta V=IR$; (f) false; (g) false; (h) true. The potentials obey $V_a>V_b>V_c$.

**Why it works:**
Series current is continuous and electric potential decreases along positive current through a positive resistance.

**Grading key points:**

- For nonzero indicated current: (a) true; (b) false; (c) false; (d) true since $P=I^2R$; (e) false since $\Delta V=IR$; (f) false; (g) false; (h) true.
- The potentials obey $V_a>V_b>V_c$.

Source: [PDF page 900](source-page-900.png); source question Q26.5.

## Q26.6: Parallel-resistor statements

In Figure Q26.6, R1 and R2 connect the same two nodes with $R_2>R_1$; I1 and I2 are branch currents, I3 and I4 total currents. Assess (a) I1=I2, (b) I3=I4, (c) I1>I2, (d) equal powers, (e) P2>P1, (f) Vcd=Vef=Vab, (g) Vc>Vd, (h) Vf>Ve, (i) Vc>Ve.

**Solution:**
For the nonzero indicated current: (a) false; (b) true; (c) true; (d) false; (e) false; (f) true; (g) true; (h) false; (i) false because c and e are on the same ideal-wire node. At common V, $I_1=V/R_1>I_2$ and $P_1=V^2/R_1>P_2$.

**Why it works:**
Parallel branches share voltage and divide current inversely with resistance; ideal-wire nodes are equipotential.

**Grading key points:**

- For the nonzero indicated current: (a) false; (b) true; (c) true; (d) false; (e) false; (f) true; (g) true; (h) false; (i) false because c and e are on the same ideal-wire node.
- At common V, $I_1=V/R_1>I_2$ and $P_1=V^2/R_1>P_2$.

Source: [PDF page 900](source-page-900.png); source question Q26.6.

## Q26.7: Battery internal drop

Why do car lights dim when the starter operates?

**Solution:**
The starter draws a large additional current through the battery's and wiring's finite internal resistance. The common terminal voltage decreases by the added internal drop, reducing power in the lights.

**Why it works:**
Parallel loads can interact through a shared nonideal source.

**Grading key points:**

- The starter draws a large additional current through the battery's and wiring's finite internal resistance.
- The common terminal voltage decreases by the added internal drop, reducing power in the lights.

Source: [PDF page 900](source-page-900.png); source question Q26.7.

## Q26.8: Parallel conducting strips

Three identical metal strips form parallel paths in Figure Q26.8. What happens to total current if one strip is cut out?

**Solution:**
Equivalent resistance increases from $R_s/3$ to $R_s/2$, so total current decreases. With an ideal fixed voltage it becomes two-thirds of the original value; source resistance changes the exact ratio.

**Why it works:**
Removing one parallel conductance reduces the total conductance.

**Grading key points:**

- Equivalent resistance increases from $R_s/3$ to $R_s/2$, so total current decreases.
- With an ideal fixed voltage it becomes two-thirds of the original value; source resistance changes the exact ratio.

Source: [PDF page 900](source-page-900.png); source question Q26.8.

## Q26.9: Closing an additional parallel branch

In Figure Q26.9 a bulb is in series with a fixed resistor and a parallel resistor bank. Closing S adds another branch to the bank. What happens to brightness?

**Solution:**
It increases. Closing S reduces the parallel bank's equivalent resistance, reducing total series resistance and increasing current through the bulb.

**Why it works:**
The switch changes the equivalent resistance in series with the lamp; it does not short the lamp.

**Grading key points:**

- It increases.
- Closing S reduces the parallel bank's equivalent resistance, reducing total series resistance and increasing current through the bulb.

Source: [PDF page 900](source-page-900.png); source question Q26.9.

## Q26.10: Nonideal source load interaction

In Figure Q26.10, a lamp is across a real battery and closing S connects a second resistive branch. What happens to lamp brightness?

**Solution:**
It decreases. The extra branch increases battery current, increases the internal $Ir$ drop, and lowers terminal voltage across the lamp.

**Why it works:**
Adding a parallel load to a nonideal source can reduce every branch's voltage.

**Grading key points:**

- It decreases.
- The extra branch increases battery current, increases the internal $Ir$ drop, and lowers terminal voltage across the lamp.

Source: [PDF page 901](source-page-901.png); source question Q26.10.

## Q26.11: Ideal source load independence

Repeat Q26.10 for an ideal battery with zero internal resistance.

**Solution:**
The original lamp's brightness is unchanged. Closing the extra branch increases total source current but the ideal battery holds terminal voltage fixed.

**Why it works:**
An ideal voltage source imposes the same branch voltage regardless of additional parallel loading.

**Grading key points:**

- The original lamp's brightness is unchanged.
- Closing the extra branch increases total source current but the ideal battery holds terminal voltage fixed.

Source: [PDF page 901](source-page-901.png); source question Q26.11.

## Q26.12: Additional branch in a three-lamp network

In Figure Q26.12, the battery supplies a branch of two series lamps and a branch of one lamp. S connects an additional resistor branch. Compare lamp brightness changes for ideal and real batteries.

**Solution:**
For an ideal battery, all preexisting lamp voltages and brightnesses remain unchanged. For a real battery with internal resistance, closing S increases total loading and lowers terminal voltage, so all lamps dim. The newly connected resistor carries additional current.

**Why it works:**
The additional branch is in parallel with the original lamp branches, and only source nonideality couples their voltages.

**Grading key points:**

- For an ideal battery, all preexisting lamp voltages and brightnesses remain unchanged.
- For a real battery with internal resistance, closing S increases total loading and lowers terminal voltage, so all lamps dim.
- The newly connected resistor carries additional current.

Source: [PDF page 901](source-page-901.png); source question Q26.12.

## Q26.13: Networks beyond series-parallel reduction

Can a resistor network fail to reduce through series and parallel substitutions alone? Give an example.

**Solution:**
Yes. An unbalanced Wheatstone bridge has a resistor joining the midpoints of two divider branches; generally no initial pair shares only a degree-two node or both endpoint nodes. Kirchhoff equations, nodal analysis, or delta-wye conversion can solve it.

**Why it works:**
Series and parallel reductions require specific connectivity conditions, not just a visually complicated drawing.

**Grading key points:**

- Yes.
- An unbalanced Wheatstone bridge has a resistor joining the midpoints of two divider branches; generally no initial pair shares only a degree-two node or both endpoint nodes.
- Kirchhoff equations, nodal analysis, or delta-wye conversion can solve it.

Source: [PDF page 901](source-page-901.png); source question Q26.13.

## Q26.14: Charging a battery

If a stronger source reverses current through a battery, must that battery's emf reverse?

**Solution:**
No. The chemical emf retains its polarity while the externally imposed current can flow against it, charging a rechargeable cell. The terminal voltage then typically exceeds the emf because of the internal resistive drop in the charging direction.

**Why it works:**
The direction of energy transfer can reverse without reversing the source's chemical polarity.

**Grading key points:**

- No.
- The chemical emf retains its polarity while the externally imposed current can flow against it, charging a rechargeable cell.
- The terminal voltage then typically exceeds the emf because of the internal resistive drop in the charging direction.

Source: [PDF page 901](source-page-901.png); source question Q26.14.

## Q26.15: Series and parallel cells

Why do two-cell flashlights commonly use series cells? What advantage can identical cells in parallel offer?

**Solution:**
Series cells add emfs to supply the higher voltage required by the lamp. Matched parallel cells retain one-cell emf but can share current, lower effective internal resistance, and increase available capacity. Real parallel operation requires compatible cell characteristics.

**Why it works:**
Series connections add voltage; parallel connections add current capability and capacity at common voltage.

**Grading key points:**

- Series cells add emfs to supply the higher voltage required by the lamp.
- Matched parallel cells retain one-cell emf but can share current, lower effective internal resistance, and increase available capacity.
- Real parallel operation requires compatible cell characteristics.

Source: [PDF page 901](source-page-901.png); source question Q26.15.

## Q26.16: Wire heating and current rating

Why can thicker household wire carry more current safely? How do length and material matter?

**Solution:**
Larger area lowers resistance per length $\rho/A$ and heating per length $I^2\rho/A$, while the surface and installation determine heat removal. Material resistivity and thermal properties affect the allowable current. For a long uniformly cooled wire, ampacity need not scale directly with total length, since both heating and cooling grow with length; total voltage drop does grow with length. Insulation and enclosure also matter.

**Why it works:**
Safe current is a thermal design limit, whereas total resistance and voltage drop also depend on length.

**Grading key points:**

- Larger area lowers resistance per length $\rho/A$ and heating per length $I^2\rho/A$, while the surface and installation determine heat removal.
- Material resistivity and thermal properties affect the allowable current.
- For a long uniformly cooled wire, ampacity need not scale directly with total length, since both heating and cooling grow with length; total voltage drop does grow with length.
- Insulation and enclosure also matter.

Source: [PDF page 901](source-page-901.png); source question Q26.16.

## Q26.17: Loaded battery testing

If battery emf changes little but internal resistance increases with age, what meter arrangement tests freshness?

**Solution:**
Measure terminal voltage under a known representative load, using a voltmeter across the battery; alternatively measure current through a specified load. A high-resistance open-circuit voltmeter alone can miss the increased internal resistance. With known load current, estimate $r=(V_{oc}-V_{load})/I$.

**Why it works:**
The voltage sag under load reveals internal resistance that an unloaded measurement conceals.

**Grading key points:**

- Measure terminal voltage under a known representative load, using a voltmeter across the battery; alternatively measure current through a specified load.
- A high-resistance open-circuit voltmeter alone can miss the increased internal resistance.
- With known load current, estimate $r=(V_{oc}-V_{load})/I$.

Source: [PDF page 901](source-page-901.png); source question Q26.17.

## Q26.18: Zero terminal voltage

Can the terminal voltage of a battery in a circuit be zero? Give a model example.

**Solution:**
Yes. In the idealized emf-plus-internal-resistance model, an external zero-resistance short gives $I=\mathcal E/r$ and $V_{term}=\mathcal E-Ir=0$. Real leads and electrochemical behavior modify the values; this is a conceptual limiting example.

**Why it works:**
Internal emf and internal resistive drop can exactly cancel at the terminals.

**Grading key points:**

- Yes.
- In the idealized emf-plus-internal-resistance model, an external zero-resistance short gives $I=\mathcal E/r$ and $V_{term}=\mathcal E-Ir=0$.
- Real leads and electrochemical behavior modify the values; this is a conceptual limiting example.

Source: [PDF page 901](source-page-901.png); source question Q26.18.

## Q26.19: RC dimensions

Verify that RC has dimensions of time.

**Solution:**
$[R]=\mathrm{V/A}$ and $[C]=\mathrm{C/V}$, so $[RC]=\mathrm{C/A}=\mathrm{s}$, because $1\ \mathrm A=1\ \mathrm{C/s}$.

**Why it works:**
The voltage units cancel and charge divided by current is time.

**Grading key points:**

- $[R]=\mathrm{V/A}$ and $[C]=\mathrm{C/V}$, so $[RC]=\mathrm{C/A}=\mathrm{s}$, because $1\ \mathrm A=1\ \mathrm{C/s}$.

Source: [PDF page 901](source-page-901.png); source question Q26.19.

## Q26.20: Resistance from discharge time

How can a capacitor be used to measure a resistance too large for an ordinary meter?

**Solution:**
Discharge a known capacitor C through the unknown R and measure $V(t)=V_0e^{-t/(RC)}$ with a very-high-input-impedance instrument. At $V=V_0/e$, $R=t/C$; more generally $R=-t/[C\ln(V/V_0)]$. Account for capacitor leakage and meter input resistance, which are parallel paths.

**Why it works:**
The exponential time constant encodes resistance even when current is too small for direct measurement.

**Grading key points:**

- Discharge a known capacitor C through the unknown R and measure $V(t)=V_0e^{-t/(RC)}$ with a very-high-input-impedance instrument.
- At $V=V_0/e$, $R=t/C$; more generally $R=-t/[C\ln(V/V_0)]$.
- Account for capacitor leakage and meter input resistance, which are parallel paths.

Source: [PDF page 901](source-page-901.png); source question Q26.20.

## Q26.21: RC final charge versus transient

In an ideal series RC charging circuit, does the resistor alter the final capacitor charge, and what does it do?

**Solution:**
For a finite positive R and an ideal constant emf, the final current is zero, so the resistor's voltage drop is zero and $Q_{max}=C\mathcal E$ independently of R. It limits initial current to $\mathcal E/R$, sets the time constant RC, and dissipates energy during charging.

**Why it works:**
Resistance controls the transient rate; the final no-current condition fixes the capacitor voltage.

**Grading key points:**

- For a finite positive R and an ideal constant emf, the final current is zero, so the resistor's voltage drop is zero and $Q_{max}=C\mathcal E$ independently of R.
- It limits initial current to $\mathcal E/R$, sets the time constant RC, and dissipates energy during charging.

Source: [PDF page 901](source-page-901.png); source question Q26.21.
