# Chapter 30 — Inductance

## Mastery checklist

Use a checkbox only when you can answer or perform the task without copying a worked solution. Revisit unchecked items after practice. The questions and challenges below are original study prompts aligned to the chapter, not copied textbook exercises.

## Chapter objectives

By the end of this chapter, you should be able to:

- [ ] Relate changing current in one circuit to induced emf in another through mutual inductance.
- [ ] Define self-inductance and distinguish induced emf from passive terminal voltage.
- [ ] Calculate stored magnetic energy and magnetic-field energy density.
- [ ] Analyze current growth, decay, and energy flow in R-L circuits.
- [ ] Describe L-C oscillations using charge, current, energy, and phase.
- [ ] Classify damped L-R-C transients and relate their behavior to mechanical oscillators.

## 30.1 — Mutual Inductance

**Core question:** How does changing current in one circuit induce an emf in another?

### Conceptual questions

- [ ] How does current in coil 1 produce flux linkage in coil 2?
- [ ] Why does a steady current produce no mutual induced emf in a stationary linear system?
- [ ] What features of coil geometry, orientation, and core material affect mutual inductance?
- [ ] Why do flux through one turn and total flux linkage differ?
- [ ] Under what assumptions does mutual inductance have the same value in both directions?
- [ ] Why can an open receiving coil have induced emf but no sustained current?

### Mathematical relationships

Let $\Phi_{21}$ be the average flux through one turn of coil 2 due to current $i_1$. For fixed geometry and a linear reciprocal magnetic system:
$$
N_2\Phi_{21}=Mi_1,
\qquad
N_1\Phi_{12}=Mi_2.
$$
With compatible winding/reference conventions and constant $M$:
$$
\mathcal E_2=-M\frac{di_1}{dt},
\qquad
\mathcal E_1=-M\frac{di_2}{dt}.
$$
$$
1\,\mathrm H=1\,\frac{\mathrm{Wb}}{\mathrm A}
=1\,\frac{\mathrm{V\,s}}{\mathrm A}.
$$
For two fully overlapping ideal long solenoids with common length $\ell$, common area $A$, and linear permeability $\mu$:
$$
M=\frac{\mu N_1N_2A}{\ell}.
$$

### Problem-solving checklist

- [ ] Find mutual inductance from flux linkage and current.
- [ ] Calculate induced emf from a known current-versus-time function or graph.
- [ ] Derive M for a simple fully linked ideal-solenoid geometry.
- [ ] Determine polarity using winding orientations and Lenz’s law.
- [ ] State when geometry changes require differentiating the full flux linkage rather than using constant M.

**Keep in mind:** An induced emf depends on the source current’s rate of change, not on the source current alone.

### Teaching challenge

A receiving coil’s voltmeter deflects when a nearby coil is switched on, but returns to zero while the source current remains steady. Explain both parts.

- [ ] I can explain this clearly, including the governing principle, signs, assumptions, and physical interpretation.

## 30.2 — Self-Inductance and Inductors

**Core question:** How does a circuit’s own changing current generate an opposing emf?

### Conceptual questions

- [ ] How does a current create flux linked with its own circuit?
- [ ] Why does an inductor oppose changes in current rather than oppose current itself?
- [ ] What determines inductance in an ideal linear coil?
- [ ] Why are self-induced emf and passive terminal-voltage drop written with opposite signs?
- [ ] Why is inductor current continuous when its voltage remains finite?
- [ ] Why can rapidly interrupting a current produce a large voltage?

### Mathematical relationships

For constant inductance in a linear system:
$$
\Lambda=N\Phi_B=Li,
\qquad
\mathcal E_{\mathrm{self}}=-L\frac{di}{dt}.
$$
With current entering terminal $a$ and leaving terminal $b$ in the passive convention:
$$
v_{ab}=L\frac{di}{dt}.
$$
The terminal relation assumes an ideal inductor. Include a real coil’s resistance separately.

For an ideal long solenoid:
$$
L=\frac{\mu N^2A}{\ell}.
$$
For a finite voltage:
$$
i(t_2)-i(t_1)=\frac1L\int_{t_1}^{t_2}v_L(t)\,dt.
$$

### Problem-solving checklist

- [ ] Calculate self-inductance from flux linkage and current.
- [ ] Derive long-solenoid inductance from its magnetic field and geometry.
- [ ] Find voltage magnitude and polarity for increasing and decreasing current.
- [ ] Read di/dt from a current graph and sketch the corresponding inductor voltage.
- [ ] Explain voltage spikes at switching without assuming that inductor current instantaneously becomes zero.

**Keep in mind:** An ideal inductor is a short in established DC steady state, not at every instant after a switch changes.

### Teaching challenge

A coil carries current to the right, but the current magnitude is decreasing. Explain the induced-emf direction and whether the coil is absorbing or releasing magnetic energy.

- [ ] I can explain this clearly, including the governing principle, signs, assumptions, and physical interpretation.

## 30.3 — Magnetic-Field Energy

**Core question:** Where is an inductor’s energy stored, and how is it transferred?

### Conceptual questions

- [ ] Why is external work required to establish current in an initially unenergized inductor?
- [ ] How does integrating instantaneous power give the stored-energy formula?
- [ ] Why is magnetic energy nonnegative even when current is negative?
- [ ] Why can a real coil dissipate heat while maintaining constant stored magnetic energy?
- [ ] How is total energy related to energy density distributed through space?
- [ ] What material assumptions permit the simple B²/(2μ) formula?

### Mathematical relationships

For a constant, linear inductance:
$$
U_B=\frac12Li^2,
\qquad
p_L=v_Li=Li\frac{di}{dt}=\frac{dU_B}{dt}.
$$
In vacuum:
$$
u_B=\frac{B^2}{2\mu_0}.
$$
In a linear, isotropic medium with constant permeability:
$$
u_B=\frac{B^2}{2\mu},
\qquad
U_B=\int_Vu_B\,dV.
$$
The simple material formula is not a general energy law for nonlinear or hysteretic magnetic media.

### Problem-solving checklist

- [ ] Calculate stored energy from L and i, or solve for either from a specified energy.
- [ ] Calculate magnetic energy density and total energy for a uniform-field volume.
- [ ] Verify solenoid energy using both ½Li² and a field-volume calculation.
- [ ] Determine whether an inductor is absorbing or returning energy from the signs of v and i.
- [ ] Separate resistive heating in a real winding from magnetic energy storage.

**Keep in mind:** Resistance converts energy to heat; ideal inductance stores and returns it. A real coil can do both.

### Teaching challenge

A real coil carries a constant current and becomes warm. Explain why that does not imply that its magnetic-field energy is decreasing.

- [ ] I can explain this clearly, including the governing principle, signs, assumptions, and physical interpretation.

## 30.4 — The R-L Circuit

**Core question:** How do resistance and inductance set the timescale of a current transient?

### Conceptual questions

- [ ] Why does current rise gradually after a DC source is connected to an inductor?
- [ ] What fixes the initial current and final current?
- [ ] How does the time constant depend on L and the total resistance in the active current path?
- [ ] What happens to resistor voltage and inductor voltage during current growth?
- [ ] What closed path lets current decay after the source is removed?
- [ ] How is initial magnetic energy dissipated during decay?

### Mathematical relationships

For a constant source emf $\mathcal E$, ideal $L$, and total series resistance $R$:
$$
L\frac{di}{dt}+Ri=\mathcal E,
\qquad
\tau=\frac LR.
$$
Starting with $i(0)=0$:
$$
i(t)=\frac{\mathcal E}{R}\left(1-e^{-t/\tau}\right).
$$
More generally, for a fixed post-switch circuit:
$$
i(t)=i_\infty+\bigl[i(0^+)-i_\infty\bigr]e^{-t/\tau}.
$$
For source-free decay through a closed R-L loop:
$$
i(t)=I_0e^{-t/\tau},
\qquad
U_B(t)=\frac12LI_0^2e^{-2t/\tau}.
$$
During growth, the source power satisfies
$$
\mathcal E i=i^2R+\frac{dU_B}{dt}.
$$

### Problem-solving checklist

- [ ] Draw the actual circuit before and after switching.
- [ ] Apply current continuity: i(0⁺)=i(0⁻) for finite voltage.
- [ ] Calculate current, di/dt, and component voltages at a specified time.
- [ ] Find the time to reach a specified fraction of final current or initial current.
- [ ] Distinguish the current decay timescale τ from the energy decay timescale τ/2.
- [ ] Check initial and final limits and account for all resistance in the discharge loop.

**Keep in mind:** Removing the source is not the same as breaking every possible current path. An ideal open interruption of nonzero current is not described by the simple exponential-decay circuit.

### Teaching challenge

After a source is disconnected, an inductor discharges through a resistor. Explain why its voltage reverses while its current initially keeps the same direction.

- [ ] I can explain this clearly, including the governing principle, signs, assumptions, and physical interpretation.

## 30.5 — The L-C Circuit

**Core question:** Why does energy exchange between a capacitor and an inductor produce oscillation?

### Conceptual questions

- [ ] What happens immediately after a charged capacitor is connected to an ideal inductor?
- [ ] Why does current continue after the capacitor charge first reaches zero?
- [ ] How are charge and current shifted in phase?
- [ ] At what points are electric-field energy and magnetic-field energy largest?
- [ ] How does an L-C circuit correspond to a mass-spring oscillator?
- [ ] Why can current direction not be inferred solely from the magnitude of capacitor charge?

### Mathematical relationships

Choose $q$ as the signed charge on a specified capacitor plate and define positive $i$ as current **into that plate**, so $i=dq/dt$. For an ideal source-free loop:
$$
L\frac{d^2q}{dt^2}+\frac qC=0,
\qquad
\omega_0=\frac1{\sqrt{LC}},
\qquad
T=2\pi\sqrt{LC}.
$$
$$
q(t)=Q\cos(\omega_0t+\phi),
\qquad
i(t)=-\omega_0Q\sin(\omega_0t+\phi),
\qquad
I_{\max}=\omega_0Q.
$$
$$
U=\frac{q^2}{2C}+\frac12Li^2
=\frac{Q^2}{2C}
=\frac12LI_{\max}^2.
$$
For a positive discharge-current reference **out of** the chosen plate, instead use $i=-dq/dt$ consistently.

### Problem-solving checklist

- [ ] Derive the charge differential equation from the element laws and loop rule.
- [ ] Calculate frequency, period, maximum charge, and maximum current.
- [ ] Use initial charge and signed current to determine amplitude and phase.
- [ ] Use conservation of energy to find current magnitude at a given charge.
- [ ] Describe the charge, current, and energy sequence over one full cycle.
- [ ] Map q↔x, L↔m, and 1/C↔k in the mechanical analogy.

**Keep in mind:** Charge and current are a quarter-cycle apart; energy is not lost when one storage element momentarily has zero energy.

### Teaching challenge

At the instant the capacitor is uncharged, explain why current is maximum rather than zero and what subsequently charges the capacitor with opposite polarity.

- [ ] I can explain this clearly, including the governing principle, signs, assumptions, and physical interpretation.

## 30.6 — The L-R-C Series Circuit

**Core question:** How does resistance change free electrical oscillations?

### Conceptual questions

- [ ] Why does a source-free circuit lose total electromagnetic energy when R is nonzero?
- [ ] What distinguishes underdamped, critically damped, and overdamped responses?
- [ ] How does the damped frequency differ from the undamped natural frequency?
- [ ] What quantity has an exponential envelope in an underdamped solution?
- [ ] Why is the freely decaying oscillation frequency different in meaning from a driven resonance frequency?
- [ ] Which initial conditions are needed to determine a second-order circuit’s motion?

### Mathematical relationships

For the same signed plate-charge convention as §30.5, in a source-free series circuit:
$$
L\frac{d^2q}{dt^2}+R\frac{dq}{dt}+\frac qC=0.
$$
Define
$$
\alpha=\frac R{2L},
\qquad
\omega_0=\frac1{\sqrt{LC}}.
$$
For underdamping:
$$
q(t)=Qe^{-\alpha t}\cos(\omega_dt+\phi),
\qquad
\omega_d=\sqrt{\omega_0^2-\alpha^2}.
$$
$$
R_{\mathrm{crit}}=2\sqrt{\frac LC}.
$$
- $R<R_{\mathrm{crit}}$: underdamped; oscillatory.
- $R=R_{\mathrm{crit}}$: critically damped; nonoscillatory.
- $R>R_{\mathrm{crit}}$: overdamped; nonoscillatory.

Instantaneous energy balance:
$$
U(t)=\frac{q^2}{2C}+\frac12Li^2,
\qquad
\frac{dU}{dt}=-Ri^2.
$$
The charge envelope decays as $e^{-\alpha t}$. Its square sets an energy scale proportional to $e^{-2\alpha t}$, but instantaneous total energy is not generally an exact pure exponential.

### Problem-solving checklist

- [ ] Classify damping from numerical R, L, and C values.
- [ ] Calculate damped frequency only when the circuit is underdamped.
- [ ] Determine the critical resistance and predict the effect of increasing R.
- [ ] Differentiate the full damped charge function to find current.
- [ ] Use initial charge and current to determine the constants.
- [ ] Explain the mechanical analogy with resistance corresponding to damping.

**Keep in mind:** Chapter 30 treats free transients. Do not replace the damped natural frequency with the driven AC resonance formula merely because both involve L and C.

### Teaching challenge

Two source-free circuits have the same L and C but different resistances. Explain why one can reverse capacitor polarity repeatedly while the other relaxes without oscillation.

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
| 1 | Mutual and self-inductance | Connect changing current, flux linkage, and induced emf |
| 2 | Magnetic energy and R-L circuits | Track stored energy and explain exponential transients |
| 3 | L-C oscillations | Connect phase, energy exchange, and the mass-spring analogy |
| 4 | Damped L-R-C circuits | Classify damping and distinguish free decay from driven AC response |

## A standard problem-solving procedure

1. Draw the circuit in each switch position and identify the active current path.
2. Choose current direction, capacitor plate-charge sign, and passive voltage references.
3. Determine initial conditions from the circuit’s history; use continuity when voltages and currents remain finite.
4. Write the flux-linkage, circuit, or energy equation before substituting numbers.
5. Identify whether the behavior is mutual induction, an R-L transient, an L-C oscillation, or a damped L-R-C response.
6. Solve using consistent signs and the correct initial conditions.
7. Check dimensions, initial and long-time behavior, and where the energy goes.

## The most important connection to master

An inductor’s resistance to current change and its ability to store magnetic energy are two descriptions of the same energy-transfer process. With passive references and constant L:

$$
\boxed{v_L=L\frac{di}{dt},\qquad U_B=\frac12Li^2,\qquad v_Li=\frac{dU_B}{dt}}
$$

Explain how these relationships produce gradual R-L current changes, sustained ideal L-C energy exchange, and damped L-R-C motion when a resistor dissipates energy.

## Source

Young and Freedman, *University Physics with Modern Physics*, 13th edition, Chapter 30, printed pp. 991–1012. Section numbering follows this edition. This is an original learning checklist, not a reproduction of the textbook’s wording or exercises.
