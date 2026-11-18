# Chapter 31 — Alternating Current

## Chapter objectives

By the end of this chapter, you should be able to:

1. Explain how alternating current differs from direct current, both physically and mathematically.
    
2. Describe sinusoidal voltage and current, including amplitude, frequency, period, angular frequency, and phase.
    
3. Explain what phasors represent and how they simplify the analysis of AC circuits.
    
4. Describe how resistors, inductors, and capacitors respond differently to alternating current.
    
5. Explain reactance, impedance, and phase relationships in AC circuits.
    
6. Analyze series RLC circuits to determine current, voltage, impedance, and phase angle.
    
7. Calculate instantaneous, average, and RMS power in alternating-current circuits.
    
8. Explain electrical resonance and derive the resonant frequency of an RLC circuit.
    
9. Explain how transformers operate through electromagnetic induction and why they are useful for power transmission.
    
10. Connect alternating-current circuit behavior to the underlying physics of electric fields, magnetic fields, energy storage, and electromagnetic induction.
    

## 31.1 — Phasors and Alternating Currents

Core question: How do voltage and current vary with time in AC circuits, and how can phasors represent their amplitudes and phase relationships?

### Conceptual questions

- What is alternating current, and how does it differ from direct current?
    
- What physical processes can generate an alternating voltage?
    
- Why are sinusoidal waveforms particularly useful in electrical engineering?
    
- What is the difference between instantaneous, peak, peak-to-peak, and RMS values?
    
- What do frequency, period, and angular frequency represent?
    
- How are frequency and angular frequency related?
    
- What does the phase of an alternating signal represent?
    
- What does it mean for two AC signals to be in phase or out of phase?
    
- What is a phasor, and how does it represent a sinusoidally varying quantity?
    
- Why can we represent a changing sinusoidal quantity using a rotating vector?
    
- How do we interpret the projection of a rotating phasor onto an axis?
    
- Why must phasors representing different voltages and currents rotate at the same angular frequency for a fixed phasor relationship?
    
- How does phasor addition simplify the addition of sinusoidal signals?
    
- What information is lost when we represent an AC signal only by its magnitude?
    

### Mathematical relationships

A sinusoidal voltage can be represented as:

\[ v(t)=V_m\cos(\omega t+\phi) \]

Similarly, current can be represented as:

\[ i(t)=I_m\cos(\omega t+\phi) \]

where:

- \(V_m\), \(I_m\): peak amplitudes
    
- \(\omega\): angular frequency
    
- \(t\): time
    
- \(\phi\): initial phase angle
    

The relationship between frequency and angular frequency:

\[ \boxed{\omega=2\pi f} \]

\[ T=\frac{1}{f}=\frac{2\pi}{\omega} \]

RMS quantities for sinusoidal waveforms:

\[ V_{\mathrm{rms}}=\frac{V_m}{\sqrt{2}} \]

\[ I_{\mathrm{rms}}=\frac{I_m}{\sqrt{2}} \]

A sinusoidal signal may be represented by a complex phasor:

\[ \tilde V=V_m e^{j\phi} \]

or, equivalently,

\[ \tilde V=V_m\angle\phi \]

These examples use peak-amplitude phasors; RMS-amplitude phasors are also common. Be consistent about which convention you use.

### Problem-solving checklist

#### Sinusoidal waveforms

- Determine frequency from a voltage-versus-time graph.
    
- Calculate angular frequency from frequency or period.
    
- Calculate instantaneous voltage or current at a specified time.
    
- Convert between peak, peak-to-peak, and RMS quantities.
    
- Determine the phase difference between two sinusoidal waveforms.
    
- Identify whether current leads or lags voltage from a graph.
    
- Write a sinusoidal voltage equation from amplitude, frequency, and phase information.
    

#### Phasors

- Convert a sinusoidal voltage or current into phasor notation.
    
- Convert a phasor into its corresponding time-domain sinusoid.
    
- Add two sinusoidal signals of the same frequency using phasors.
    
- Determine a resultant amplitude and phase angle using vector components.
    
- Sketch phasor diagrams for in-phase and out-of-phase signals.
    
- Explain how a phasor diagram relates to the corresponding time-domain graph.
    

Teaching challenge: Explain how a rotating vector can represent a sinusoidal voltage, and demonstrate why two signals with identical frequencies but different phase angles reach their maxima at different times.

## 31.2 — Resistance and Reactance

Core question: How do resistors, capacitors, and inductors respond differently to alternating current, and why does that produce phase differences between voltage and current?

This is one of the most conceptually important sections in the chapter.

### Conceptual questions

#### Resistors

- Why are voltage and current in phase for an ideal resistor?
    
- Why does an ideal resistor dissipate energy rather than store and return it?
    
- Does resistance depend on the frequency of an applied alternating current in the ideal circuit model?
    
- Why does Ohm's law apply instantaneously to an ideal resistor?
    

#### Capacitors

- Why can alternating current continually charge and discharge a capacitor?
    
- Why can current flow in the external circuit even though charges do not cross the ideal dielectric?
    
- Why does current lead voltage by \(90^\circ\) in an ideal capacitor?
    
- Why does capacitive reactance decrease as frequency increases?
    
- What happens to an ideal capacitor's behavior as frequency approaches zero?
    
- How does a capacitor store and return energy during each AC cycle?
    
- Why does a capacitor resist rapid changes in voltage rather than current?
    

#### Inductors

- Why does a changing current produce an induced EMF in an inductor?
    
- How does Lenz's law explain an inductor's opposition to changes in current?
    
- Why does current lag voltage by \(90^\circ\) in an ideal inductor?
    
- Why does inductive reactance increase as frequency increases?
    
- What happens to an ideal inductor's reactance as frequency approaches zero?
    
- How does an inductor store and return energy through its magnetic field?
    
- Why does an inductor resist rapid changes in current rather than voltage?
    

### Mathematical relationships

For an ideal resistor:

\[ v_R(t)=Ri_R(t) \]

For an ideal capacitor:

\[ i_C(t)=C\frac{dv_C}{dt} \]

For an ideal inductor:

\[ v_L(t)=L\frac{di_L}{dt} \]

Capacitive reactance:

\[ \boxed{X_C=\frac{1}{\omega C}} \]

Inductive reactance:

\[ \boxed{X_L=\omega L} \]

Impedances in complex notation:

\[ Z_R=R \]

\[ Z_L=j\omega L \]

\[ Z_C=\frac{1}{j\omega C}=-\frac{j}{\omega C} \]

### Phase relationships

|Component|Phase relationship|Frequency response|
|---|---|---|
|Resistor|Voltage and current in phase|\(R\) constant|
|Capacitor|Current leads voltage by \(90^\circ\)|\(X_C\) decreases with \(f\)|
|Inductor|Current lags voltage by \(90^\circ\)|\(X_L\) increases with \(f\)|

These relationships assume ideal components operating in sinusoidal steady state.

### Problem-solving checklist

- Calculate capacitive reactance for a known capacitance and frequency.
    
- Calculate inductive reactance for a known inductance and frequency.
    
- Determine how reactance changes when frequency doubles or halves.
    
- Calculate RMS current through an ideal resistor, capacitor, or inductor connected to an AC source.
    
- Determine the phase relationship between current and voltage across each element.
    
- Construct voltage-current phasor diagrams for individual circuit elements.
    
- Derive \(X_L=\omega L\) from Faraday's law and the ideal inductor voltage equation.
    
- Derive \(X_C=1/(\omega C)\) using the capacitor current-voltage relationship.
    
- Analyze the limiting behavior of inductors and capacitors as \(\omega\to0\) and \(\omega\to\infty\).
    
- Determine the maximum energy stored in a capacitor or inductor during an AC cycle.
    

Teaching challenge: Explain why a capacitor presents very high impedance at low frequencies but low impedance at high frequencies, while an inductor exhibits the opposite behavior.

Your explanation should connect the mathematics to the physical behavior of electric and magnetic fields rather than relying only on reactance equations.

## 31.3 — The L-R-C Series Circuit

Core question: How do resistance, inductance, and capacitance combine to determine the current, impedance, and phase angle in a series AC circuit?

### Conceptual questions

- What is impedance, and how does it differ from resistance?
    
- Why must impedance account for both magnitude and phase?
    
- Why is the current the same through all components in a series RLC circuit?
    
- Why can't we simply add the RMS voltages across the resistor, inductor, and capacitor as ordinary scalars?
    
- How do phasors represent the voltage contributions of each circuit element?
    
- Why do the inductive and capacitive voltage contributions point in opposite directions on a phasor diagram?
    
- What determines whether a circuit behaves predominantly inductively or capacitively?
    
- Why does the phase angle between source voltage and current depend on the net reactance?
    
- Under what conditions are source voltage and current in phase?
    
- What is the difference between impedance magnitude and complex impedance?
    
- How do Kirchhoff's voltage and current laws apply to AC circuits?
    
- Why can individual reactive-component voltages exceed the source voltage without violating Kirchhoff's voltage law?
    

### Mathematical relationships

The complex impedance of a series RLC circuit:

\[ \boxed{Z=R+j\left(X_L-X_C\right)} \]

Its magnitude:

\[ \boxed{|Z|=\sqrt{R^2+(X_L-X_C)^2}} \]

The phase angle:

\[ \boxed{\phi=\tan^{-1}\left(\frac{X_L-X_C}{R}\right)} \]

For a circuit driven by an RMS source voltage:

\[ I_{\mathrm{rms}}=\frac{V_{\mathrm{rms}}}{|Z|} \]

Individual RMS voltage magnitudes:

\[ V_R=I_{\mathrm{rms}}R \]

\[ V_L=I_{\mathrm{rms}}X_L \]

\[ V_C=I_{\mathrm{rms}}X_C \]

The source RMS voltage magnitude satisfies:

\[ \boxed{V_{\mathrm{rms}}=\sqrt{V_R^2+(V_L-V_C)^2}} \]

### Problem-solving checklist

- Calculate inductive and capacitive reactances in a series RLC circuit.
    
- Calculate the total complex impedance and its magnitude.
    
- Determine RMS and peak source current.
    
- Calculate the RMS voltage across each circuit element.
    
- Determine whether the circuit is predominantly inductive or capacitive.
    
- Calculate the phase angle between source voltage and current.
    
- Determine whether current leads or lags the source voltage.
    
- Construct a complete series RLC phasor diagram.
    
- Solve for an unknown resistance, capacitance, or inductance from impedance and phase information.
    
- Analyze changes in current and phase when source frequency varies.
    
- Apply Kirchhoff's voltage law using complex phasors.
    
- Verify that the phasor sum of component voltages equals the source voltage.
    

Teaching challenge: In a series RLC circuit, the RMS voltage across the inductor and capacitor can individually be greater than the RMS source voltage.

Explain how this is possible without violating energy conservation or Kirchhoff's voltage law.

## 31.4 — Power in Alternating-Current Circuits

Core question: How is electrical energy transferred, dissipated, stored, and returned in AC circuits, and why does phase difference affect average power?

### Conceptual questions

- What is instantaneous electrical power in an AC circuit?
    
- Why can instantaneous power vary throughout each cycle?
    
- Why is average power in an ideal resistor positive?
    
- Why is average power in an ideal capacitor or inductor zero?
    
- How do capacitors and inductors temporarily store energy and return it to the circuit?
    
- What is the power factor, and what does it physically represent?
    
- Why does a phase difference between source voltage and current reduce average real power at fixed RMS voltage and current?
    
- What is the difference between real, reactive, and apparent power?
    
- Why is reactive power relevant even though it does not represent net energy consumption over a cycle?
    
- Why can a system have significant current while delivering relatively little real power?
    
- Why do electrical utilities care about power factor?
    
- How can adding capacitance improve the power factor of an inductive load?
    

### Mathematical relationships

Instantaneous power:

\[ p(t)=v(t)i(t) \]

Average power for sinusoidal steady-state AC:

\[ \boxed{P_{\mathrm{avg}}=V_{\mathrm{rms}}I_{\mathrm{rms}}\cos\phi} \]

Power factor:

\[ \boxed{\mathrm{PF}=\cos\phi} \]

For a series RLC circuit:

\[ P_{\mathrm{avg}}=I_{\mathrm{rms}}^2R \]

Apparent power magnitude:

\[ |S|=V_{\mathrm{rms}}I_{\mathrm{rms}} \]

Reactive power:

\[ Q=V_{\mathrm{rms}}I_{\mathrm{rms}}\sin\phi \]

And:

\[ |S|^2=P^2+Q^2 \]

### Problem-solving checklist

- Calculate instantaneous power from time-dependent voltage and current functions.
    
- Calculate average power for a purely resistive AC load.
    
- Calculate average power for a series RLC circuit.
    
- Determine power factor from the circuit's phase angle.
    
- Calculate real, reactive, and apparent power.
    
- Construct and interpret a power triangle.
    
- Determine whether the reactive power is inductive or capacitive.
    
- Calculate energy dissipated over a known time interval.
    
- Determine the resistance responsible for real power dissipation.
    
- Solve for a required capacitor value to improve power factor under specified load conditions.
    
- Explain why \(V_{\mathrm{rms}}I_{\mathrm{rms}}\) is not always equal to average power.
    

Teaching challenge: Two AC circuits operate at the same RMS voltage and draw the same RMS current, but one has a power factor of \(1.0\) and the other \(0.5\).

Explain why the circuits consume different amounts of average real power despite having the same RMS voltage and current.

## 31.5 — Resonance in Alternating-Current Circuits

Core question: Why does an RLC circuit respond especially strongly to a particular frequency, and how does resonance relate to energy transfer between electric and magnetic fields?

### Conceptual questions

- What is electrical resonance?
    
- Why does resonance occur when inductive and capacitive reactances have equal magnitudes?
    
- What happens to the net reactance at resonance?
    
- Why is impedance minimized in a series RLC circuit at resonance?
    
- Why is current maximized at resonance for a fixed-amplitude sinusoidal voltage source?
    
- Why are source voltage and current in phase at resonance?
    
- How does energy transfer between the capacitor's electric field and the inductor's magnetic field?
    
- Why does resistance cause energy dissipation and damp oscillations?
    
- What is the quality factor \(Q\), and what does it tell us about the resonance?
    
- What is bandwidth, and how does it relate to the sharpness of the resonance?
    
- Why can the voltages across the inductor and capacitor become much larger than the applied source voltage near resonance?
    
- How do series and parallel resonance differ?
    
- How is resonance used in filters, radio tuning, and signal selection?
    

### Mathematical relationships

At resonance:

\[ X_L=X_C \]

Therefore:

\[ \omega_0 L=\frac{1}{\omega_0 C} \]

The resonance angular frequency is:

\[ \boxed{\omega_0=\frac{1}{\sqrt{LC}}} \]

The resonance frequency is:

\[ \boxed{f_0=\frac{1}{2\pi\sqrt{LC}}} \]

For a series RLC circuit at resonance:

\[ |Z|=R \]

\[ I_{\mathrm{rms,max}}=\frac{V_{\mathrm{rms}}}{R} \]

Series-circuit quality factor:

\[ \boxed{Q=\frac{\omega_0L}{R}} \]

Bandwidth in angular frequency for an ideal series RLC circuit:

\[ \Delta\omega=\frac{R}{L} \]

Thus:

\[ Q=\frac{\omega_0}{\Delta\omega} \]

### Problem-solving checklist

- Calculate resonant frequency from inductance and capacitance.
    
- Solve for the required capacitance or inductance to achieve a target resonance frequency.
    
- Calculate circuit impedance and current at resonance.
    
- Compare circuit current below, at, and above resonance.
    
- Determine whether the circuit is inductive or capacitive on either side of resonance.
    
- Calculate the voltage magnitudes across the inductor and capacitor at resonance.
    
- Calculate the quality factor of a series RLC circuit.
    
- Determine bandwidth from the circuit parameters.
    
- Calculate half-power frequencies.
    
- Interpret a resonance curve showing current amplitude versus frequency.
    
- Determine how resistance affects resonance sharpness and peak current.
    
- Explain the exchange of energy between the capacitor and inductor during oscillation.
    

Teaching challenge: Explain why the current in a series RLC circuit becomes largest at resonance even though the inductor and capacitor may each have substantial reactance.

Then explain why the current decreases when the source frequency moves either above or below resonance.

## 31.6 — Transformers

Core question: How can alternating magnetic flux transfer electrical energy between two circuits, and why does changing voltage also change current?

### Conceptual questions

- What is a transformer, and what is its fundamental operating principle?
    
- How does Faraday's law explain the induced voltage in the secondary winding?
    
- Why do ordinary transformers require changing magnetic flux?
    
- Why can't a conventional transformer continuously transfer power using steady DC?
    
- What determines whether a transformer steps voltage up or down?
    
- How does the number of turns in each winding affect voltage?
    
- Why does increasing output voltage reduce output current in an ideal transformer delivering a fixed power?
    
- How is energy transferred between the primary and secondary circuits?
    
- Why does an ideal transformer conserve power?
    
- What physical mechanisms make real transformers less than perfectly efficient?
    
- What are eddy currents, and how do laminated transformer cores reduce their effects?
    
- What is magnetic flux leakage?
    
- Why are transformers essential for electrical power transmission?
    
- Why does transmitting power at higher voltage reduce resistive losses for a given delivered power?
    
- What is the difference between transformer voltage regulation and transformer efficiency?
    

### Mathematical relationships

Ideal transformer voltage ratio:

\[ \boxed{\frac{V_s}{V_p}=\frac{N_s}{N_p}} \]

Ideal current ratio in magnitude:

\[ \boxed{\frac{I_s}{I_p}=\frac{N_p}{N_s}} \]

For an ideal transformer:

\[ P_p=P_s \]

Therefore, assuming unity power factor or using apparent-power magnitudes:

\[ V_pI_p=V_sI_s \]

Transformer efficiency using real power:

\[ \eta=\frac{P_{\mathrm{out}}}{P_{\mathrm{in}}}\times100\% \]

Power loss in a transmission line:

\[ P_{\mathrm{loss}}=I_{\mathrm{rms}}^2R \]

### Problem-solving checklist

- Determine the secondary voltage from primary voltage and winding turns.
    
- Calculate the required turns ratio to achieve a target voltage.
    
- Determine whether a transformer is step-up or step-down.
    
- Calculate primary or secondary current for an ideal transformer with a specified load.
    
- Calculate output power and transformer efficiency.
    
- Calculate transmission-line losses at different transmission voltages.
    
- Compare the efficiency of high-voltage and low-voltage transmission for the same delivered power.
    
- Calculate an ideal transformer's reflected load impedance:
    

\[ Z_{\mathrm{in}}=\left(\frac{N_p}{N_s}\right)^2 Z_L \]

- Explain what happens when a DC voltage is applied to a conventional transformer primary.
    
- Apply Faraday's law to determine induced EMF from changing magnetic flux.
    
- Analyze how winding resistance and magnetic losses affect real transformer performance.
    

Teaching challenge: Explain why electrical power is transmitted at very high voltages and then stepped down before distribution to homes.

Your explanation should connect power, current, resistance, transformer operation, and resistive heating.

# Final Chapter Mastery Assessment

These problems combine multiple concepts and test whether you can reason through an unfamiliar AC system.

|#|Problem|Primary concepts|
|---|---|---|
|1|Given \(v(t)=170\cos(120\pi t+\pi/6)\), determine frequency, period, RMS voltage, and phase|Sinusoidal waveforms|
|2|An AC voltage source connected separately to a resistor, capacitor, and inductor|Reactance, phase, frequency response|
|3|A series RLC circuit with known \(R\), \(L\), \(C\), frequency, and source voltage|Impedance, current, phase, voltage|
|4|A series RLC circuit with a known power factor and RMS current|Real power, reactive power, phasors|
|5|An RLC circuit whose source frequency can be varied|Resonance, bandwidth, quality factor|
|6|A series RLC circuit where \(V_L\) and \(V_C\) individually exceed the source voltage|Reactive voltage cancellation, phasor KVL|
|7|A transformer supplying a resistive load through transmission lines|Turns ratio, power conservation, transmission losses|
|8|An AC circuit with an unknown element inferred from measured voltage-current phase|Component identification, reactance|
|9|A circuit transitioning from DC steady state to sinusoidal AC operation|Capacitor and inductor limiting behavior|
|10|An unfamiliar AC circuit with multiple branches|Complex impedance, Kirchhoff's laws, nodal or mesh analysis|

# Five Questions That Demonstrate Deeper Understanding

These are questions I would prioritize for your teach-back videos because they reveal whether you understand the underlying physics rather than merely the equations.

### 1. Why do capacitors and inductors cause phase shifts, but resistors do not?

Explain this starting with:

\[ i_C=C\frac{dv_C}{dt} \]

and

\[ v_L=L\frac{di_L}{dt} \]

Show how differentiation of a sinusoidal function introduces a phase shift, and connect that to the physical behavior of each component.

### 2. Why does a capacitor oppose low-frequency AC more strongly than high-frequency AC, while an inductor does the opposite?

Explain the different frequency dependencies using both the reactance equations and energy storage in electric and magnetic fields.

### 3. How can a circuit have current flowing while consuming zero average power?

Explain the distinction between instantaneous energy transfer and net energy dissipation over a complete cycle.

Use an ideal capacitor or inductor as your example.

### 4. Why does resonance occur in an RLC circuit?

Explain how the capacitor and inductor exchange stored energy and why their reactive contributions cancel at the resonant frequency.

Discuss why resistance determines the magnitude and sharpness of the resonant response.

### 5. Why does increasing transmission voltage reduce power loss?

Explain why higher voltage permits lower current for the same transmitted real power, and why resistive heating depends on the square of the current.

Connect this reasoning to the fundamental purpose of transformers.

# Suggested Teach-Back Video Structure

I'd divide this chapter into five videos, organizing the concepts according to how they build on one another.

|Video|Topic|Main objective|
|---|---|---|
|1|Alternating Current and Phasors|Explain sinusoidal signals, phase, RMS quantities, and phasor representations|
|2|Resistance, Reactance, and Impedance|Explain the fundamentally different AC behaviors of resistors, capacitors, and inductors|
|3|Series RLC Circuit Analysis|Apply complex impedance, phasor diagrams, and Kirchhoff's laws|
|4|AC Power and Resonance|Explain real versus reactive power, power factor, resonance, and energy exchange|
|5|Transformers and Power Transmission|Connect electromagnetic induction to voltage conversion, efficiency, and practical power systems|

## A standard AC circuit problem-solving procedure

1. Identify the circuit topology. Determine which components are connected in series or parallel, and identify the source voltage and frequency.

2. Convert to the frequency domain. Represent voltage and current as phasors and replace resistors, capacitors, and inductors with their complex impedances.

3. Calculate individual impedances.

\[ Z_R=R,\qquad Z_L=j\omega L,\qquad Z_C=\frac{1}{j\omega C} \]

4. Find the equivalent impedance. Combine series and parallel impedances or apply nodal/mesh analysis for more complex circuits.

5. Calculate currents and voltages. Apply phasor Ohm's law:

\[ \tilde V=\tilde I Z \]

6. Determine phase relationships. Identify whether voltage leads or lags current and interpret whether the circuit behaves inductively or capacitively.

7. Calculate power if requested. Use RMS quantities and include the phase angle when determining average real power.

8. Verify the result. Check Kirchhoff's laws, dimensions, limiting behavior, energy conservation, and whether the answer makes physical sense.

## The most important connection to master

For this chapter, I would emphasize the relationship between energy storage, rates of change, and phase shifts.

Consider the three fundamental element equations:

\[ \boxed{ \begin{aligned} v_R &= Ri_R \\[4pt] i_C &= C\frac{dv_C}{dt} \\[4pt] v_L &= L\frac{di_L}{dt} \end{aligned} } \]

These are much more fundamental than memorizing the phase relationships or impedance formulas.

For the resistor, voltage and current are directly proportional.

For the capacitor, current depends on how rapidly voltage changes.

For the inductor, voltage depends on how rapidly current changes.

And because differentiation of sinusoidal functions produces a \(90^\circ\) phase shift, the different mathematical relationships produce the distinct AC behaviors of these components.

From these three equations, you can derive nearly everything else in the chapter: reactance, impedance, phase relationships, RLC circuit behavior, power factor, and resonance.

If you can derive the AC behavior of a resistor, capacitor, and inductor from their time-domain equations—and explain the physical reason behind each relationship—you'll have a much stronger understanding of AC circuits than someone who has simply memorized impedance formulas.