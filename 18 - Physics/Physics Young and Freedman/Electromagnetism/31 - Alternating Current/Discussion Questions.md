# Chapter 31: Alternating Current

18 questions. Standardized prompts with original solutions; source numbering follows the 13th edition.

## Q31.1: Distribution voltage tradeoff

Compare the advantages and disadvantages of household supply values of 240 V and 120 V in the textbook's idealized comparison.

**Solution:**
For a fixed delivered power and power factor, 240 V needs half the current, reducing $I^2R$ losses to one-quarter for the same wiring or allowing smaller conductors. The larger voltage demands appropriate insulation and increases current through a given accidental contact impedance. At 120 V those voltage-related demands are lower but wiring current is larger. The textbook values are the comparison assumptions.

**Why it works:**
Power delivery, heating, and contact current scale differently with voltage.

**Grading key points:**

- For a fixed delivered power and power factor, 240 V needs half the current, reducing $I^2R$ losses to one-quarter for the same wiring or allowing smaller conductors.
- The larger voltage demands appropriate insulation and increases current through a given accidental contact impedance.
- At 120 V those voltage-related demands are lower but wiring current is larger.
- The textbook values are the comparison assumptions.

Source: [PDF page 1070](source-page-1070.png); source question Q31.1.

## Q31.2: AC power despite zero mean current

How can an ac line transmit power when its current averages to zero and reverses direction 120 times per second?

**Solution:**
Power is $p=vi$, not proportional to the average current alone. For a resistive load, voltage and current reverse together and $p=I_{pk}^2R\cos^2\omega t$ is nonnegative, with mean $I_{rms}^2R$. More generally $P=V_{rms}I_{rms}\cos\phi$. 120 reversals per second corresponds to 60 complete cycles per second.

**Why it works:**
The average of a product is not generally the product of the averages.

**Grading key points:**

- Power is $p=vi$, not proportional to the average current alone.
- For a resistive load, voltage and current reverse together and $p=I_{pk}^2R\cos^2\omega t$ is nonnegative, with mean $I_{rms}^2R$.
- More generally $P=V_{rms}I_{rms}\cos\phi$. 120 reversals per second corresponds to 60 complete cycles per second.

Source: [PDF page 1070](source-page-1070.png); source question Q31.2.

## Q31.3: Reactive versus dissipative energy

Why is cycle-average power zero for an ideal inductor or capacitor but positive for a resistor?

**Solution:**
An ideal inductor stores $Li^2/2$ and an ideal capacitor stores $q^2/(2C)$; in periodic steady state each returns to the same energy after a cycle and returns absorbed energy to the circuit. A resistor irreversibly converts energy to heat at $i^2R$, whose average is positive for nonzero current.

**Why it works:**
Reactive energy storage is reversible over a cycle; resistance dissipates energy.

**Grading key points:**

- An ideal inductor stores $Li^2/2$ and an ideal capacitor stores $q^2/(2C)$; in periodic steady state each returns to the same energy after a cycle and returns absorbed energy to the circuit.
- A resistor irreversibly converts energy to heat at $i^2R$, whose average is positive for nonzero current.

Source: [PDF page 1070](source-page-1070.png); source question Q31.3.

## Q31.4: Signed capacitor current in AC

For the fixed reference arrows of Figure 31.9a, does $i=dq/dt$ change sign convention when the left plate charge decreases or the right plate becomes positive?

**Solution:**
No. q remains the signed left-plate charge and positive i is defined into that plate, so $i=dq/dt$ always holds. Left-positive and decreasing gives i<0. If the right plate is positive and increasing, q becomes more negative and i<0; if right-positive decreases, q increases and i>0.

**Why it works:**
The signs of variables change during the cycle; the constitutive equation does not.

**Grading key points:**

- No. q remains the signed left-plate charge and positive i is defined into that plate, so $i=dq/dt$ always holds.
- Left-positive and decreasing gives i<0.
- If the right plate is positive and increasing, q becomes more negative and i<0; if right-positive decreases, q increases and i>0.

Source: [PDF page 1070](source-page-1070.png); source question Q31.4.

## Q31.5: Inductive ballast

Why can an inductor be preferable to a resistor as an ac fluorescent-lamp ballast?

**Solution:**
Its reactance limits current while an ideal inductor dissipates zero average power, exchanging stored magnetic energy with the circuit. A resistor limits current by wasting power as heat. Real ballast coils have winding and core losses, but can dissipate much less than a comparable resistive limiter.

**Why it works:**
Impedance can limit current through reactive opposition rather than irreversible dissipation.

**Grading key points:**

- Its reactance limits current while an ideal inductor dissipates zero average power, exchanging stored magnetic energy with the circuit.
- A resistor limits current by wasting power as heat.
- Real ballast coils have winding and core losses, but can dissipate much less than a comparable resistive limiter.

Source: [PDF page 1070](source-page-1070.png); source question Q31.5.

## Q31.6: Passive inductor voltage convention

In Figure 31.8a, explain why $v_{ab}=L\,di/dt$ puts a above b for increasing positive current. Does the equation change when current reverses or decreases?

**Solution:**
With current referenced from a to b, the passive terminal voltage is $v_{ab}=L\,di/dt$. Positive increasing current requires a positive driving voltage a to b to overcome the opposing induced emf. Positive decreasing current gives negative voltage. Negative current increasing in magnitude also has $di/dt<0$; negative current decreasing in magnitude has $di/dt>0$. The same equation holds throughout.

**Why it works:**
Faraday's induced emf is opposite the changing current; terminal voltage under the passive convention has the stated derivative sign.

**Grading key points:**

- With current referenced from a to b, the passive terminal voltage is $v_{ab}=L\,di/dt$.
- Positive increasing current requires a positive driving voltage a to b to overcome the opposing induced emf.
- Positive decreasing current gives negative voltage.
- Negative current increasing in magnitude also has $di/dt<0$; negative current decreasing in magnitude has $di/dt>0$.
- The same equation holds throughout.

Source: [PDF page 1070](source-page-1070.png); source question Q31.6.

## Q31.7: Zero power factor

Can an ac series RLC circuit have exactly zero power factor?

**Solution:**
For a finite nonzero current and positive R, no: $\cos\phi=R/\sqrt{R^2+(X_L-X_C)^2}>0$. It can approach zero far from resonance with very small R. A purely reactive ideal circuit with R=0 and nonzero net reactance has exactly zero power factor. The lossless exact-resonance limit is singular and has no finite steady current under a nonzero ideal voltage source.

**Why it works:**
Any positive resistance carrying current dissipates positive average power.

**Grading key points:**

- For a finite nonzero current and positive R, no: $\cos\phi=R/\sqrt{R^2+(X_L-X_C)^2}>0$.
- It can approach zero far from resonance with very small R.
- A purely reactive ideal circuit with R=0 and nonzero net reactance has exactly zero power factor.
- The lossless exact-resonance limit is singular and has no finite steady current under a nonzero ideal voltage source.

Source: [PDF page 1070](source-page-1070.png); source question Q31.7.

## Q31.8: Instantaneous voltage versus amplitude

Can instantaneous voltage across C, L, or R in a series RLC circuit exceed the source's instantaneous voltage?

**Solution:**
Yes for all three. Kirchhoff's law adds signed instantaneous voltages, so reactive contributions can cancel. For nonzero phase angle the source can pass through zero while resistor current and $v_R$ are nonzero, even though the resistor voltage amplitude never exceeds source amplitude because $R\le Z$. L and C amplitudes themselves can also exceed the source amplitude.

**Why it works:**
An instantaneous comparison differs from an amplitude bound, and signed voltages are not summed as magnitudes.

**Grading key points:**

- Yes for all three.
- Kirchhoff's law adds signed instantaneous voltages, so reactive contributions can cancel.
- For nonzero phase angle the source can pass through zero while resistor current and $v_R$ are nonzero, even though the resistor voltage amplitude never exceeds source amplitude because $R\le Z$.
- L and C amplitudes themselves can also exceed the source amplitude.

Source: [PDF page 1070](source-page-1070.png); source question Q31.8.

## Q31.9: Nearly reactive phase

Far from resonance with resistance much smaller than the net reactance, what are phase angle and power factor?

**Solution:**
If $X_L>X_C$, voltage leads current and $\phi\approx+90^\circ$. If $X_C>X_L$, voltage lags current and $\phi\approx-90^\circ$. In both cases $\cos\phi\approx0$ because $\tan\phi=(X_L-X_C)/R$ and $R\ll|X_L-X_C|$.

**Why it works:**
Far from resonance prevents the two individually large reactances from nearly cancelling.

**Grading key points:**

- If $X_L>X_C$, voltage leads current and $\phi\approx+90^\circ$.
- If $X_C>X_L$, voltage lags current and $\phi\approx-90^\circ$.
- In both cases $\cos\phi\approx0$ because $\tan\phi=(X_L-X_C)/R$ and $R\ll|X_L-X_C|$.

Source: [PDF page 1070](source-page-1070.png), [PDF page 1071](source-page-1071.png); source question Q31.9.

## Q31.10: Resonant voltage magnification

Why can a capacitor rated for 200 or 400 V be overstressed in a series RLC circuit connected to a 120-V rms source?

**Solution:**
Near resonance $X_L\approx X_C$, so Z can be close to R and current large. Then $V_{C,rms}=I_{rms}X_C$ can greatly exceed 120 V; at resonance its ratio to source rms voltage is $X_C/R$, the series quality factor. Capacitor and inductor voltages nearly cancel in the source sum. Peak source voltage is also $\sqrt2$ times rms, and component ratings must be interpreted correctly.

**Why it works:**
Small net impedance does not imply small individual reactive voltages.

**Grading key points:**

- Near resonance $X_L\approx X_C$, so Z can be close to R and current large.
- Then $V_{C,rms}=I_{rms}X_C$ can greatly exceed 120 V; at resonance its ratio to source rms voltage is $X_C/R$, the series quality factor.
- Capacitor and inductor voltages nearly cancel in the source sum.
- Peak source voltage is also $\sqrt2$ times rms, and component ratings must be interpreted correctly.

Source: [PDF page 1071](source-page-1071.png); source question Q31.10.

## Q31.11: Inferring load parameters from rated real power

Example 31.6 specifies a 1500-W, 120-V-rms hair dryer. If inductance is included instead of assuming a pure resistor, how do inferred R, rms current, and real power compare?

**Solution:**
Holding the stated measured rating P=1500 W and line voltage fixed, a lagging power factor requires $I_{rms}=P/(V_{rms}\cos\phi)>12.5$ A. Then $R=P/I_{rms}^2<9.60$ ohms; rated real power remains 1500 W. If the intended experiment instead adds inductance to a fixed physical R at fixed voltage, R stays unchanged while current and real power decrease. The rating-based inference and fixed-R modification are different constraints.

**Why it works:**
Real power is $VI\cos\phi=I^2R$; the answer depends on which measured or physical quantity is held fixed.

**Grading key points:**

- Holding the stated measured rating P=1500 W and line voltage fixed, a lagging power factor requires $I_{rms}=P/(V_{rms}\cos\phi)>12.5$ A.
- Then $R=P/I_{rms}^2<9.60$ ohms; rated real power remains 1500 W.
- If the intended experiment instead adds inductance to a fixed physical R at fixed voltage, R stays unchanged while current and real power decrease.
- The rating-based inference and fixed-R modification are different constraints.

Source: [PDF page 1071](source-page-1071.png); source question Q31.11.

## Q31.12: RC current and dielectric insertion

A lamp and air-filled capacitor are in series with an ac source. What happens to brightness when dielectric fills the capacitor?

**Solution:**
It generally increases at fixed frequency and source voltage. C rises, $X_C=1/(\omega C)$ falls, and the series impedance $\sqrt{R^2+X_C^2}$ decreases, increasing lamp current and power. This assumes an insulating dielectric and no significant added losses.

**Why it works:**
Higher capacitance makes a series capacitor less restrictive to ac current.

**Grading key points:**

- It generally increases at fixed frequency and source voltage.
- C rises, $X_C=1/(\omega C)$ falls, and the series impedance $\sqrt{R^2+X_C^2}$ decreases, increasing lamp current and power.
- This assumes an insulating dielectric and no significant added losses.

Source: [PDF page 1071](source-page-1071.png); source question Q31.12.

## Q31.13: RL current and an iron core

A lamp and coil are in series with an ac source. What happens when an iron rod is inserted into the coil?

**Solution:**
For the usual unsaturated-core model, L rises, $X_L=\omega L$ rises, current falls, and the lamp dims. Real iron also introduces core loss and nonlinear behavior, but the elementary prediction is dimming.

**Why it works:**
Increasing series inductive reactance increases impedance at fixed frequency.

**Grading key points:**

- For the usual unsaturated-core model, L rises, $X_L=\omega L$ rises, current falls, and the lamp dims.
- Real iron also introduces core loss and nonlinear behavior, but the elementary prediction is dimming.

Source: [PDF page 1071](source-page-1071.png); source question Q31.13.

## Q31.14: Removing one reactance

A lamp, capacitor, and inductor are in series with an ac source. What happens when L is replaced by a wire, or when C is replaced by a wire while L stays?

**Solution:**
No unconditional brighter/dimmer answer is possible. Initially $Z^2=R^2+(X_L-X_C)^2$. Removing L gives $R^2+X_C^2$: it brightens if $X_L>2X_C$, dims if $0<X_L<2X_C$, and is unchanged at equality. Removing C brightens if $X_C>2X_L$, dims if $0<X_C<2X_L$, and is unchanged at equality. Near initial resonance, either removal dims it. Physically opening the circuit rather than replacing a component by wire extinguishes the lamp.

**Why it works:**
Brightness depends on the magnitude of net reactance, not on counting circuit elements.

**Grading key points:**

- No unconditional brighter/dimmer answer is possible.
- Initially $Z^2=R^2+(X_L-X_C)^2$.
- Removing L gives $R^2+X_C^2$: it brightens if $X_L>2X_C$, dims if $0<X_L<2X_C$, and is unchanged at equality.
- Removing C brightens if $X_C>2X_L$, dims if $0<X_C<2X_L$, and is unchanged at equality.
- Near initial resonance, either removal dims it.
- Physically opening the circuit rather than replacing a component by wire extinguishes the lamp.

Source: [PDF page 1071](source-page-1071.png); source question Q31.14.

## Q31.15: Removing both reactive elements

Can removing both L and C from a series lamp circuit leave its brightness unchanged, with both replaced by wire?

**Solution:**
Yes, if it was initially at series resonance, $X_L=X_C$. The original impedance is then R, the same as the lamp alone. For nonzero finite L and C this requires $\omega=1/\sqrt{LC}$ under the ideal model.

**Why it works:**
Opposite reactances cancel, leaving the same current as in the purely resistive circuit.

**Grading key points:**

- Yes, if it was initially at series resonance, $X_L=X_C$.
- The original impedance is then R, the same as the lamp alone.
- For nonzero finite L and C this requires $\omega=1/\sqrt{LC}$ under the ideal model.

Source: [PDF page 1071](source-page-1071.png); source question Q31.15.

## Q31.16: Transformer on DC

Can an ordinary transformer operate from steady dc? What if a 120-V-ac transformer is connected to 120 V dc?

**Solution:**
A transient secondary emf occurs when current changes at connection or disconnection, but steady dc provides no sustained transformer action. The core can saturate and the primary current becomes limited mainly by winding resistance rather than its normal ac reactance, causing overheating and possible failure.

**Why it works:**
Induction requires changing flux; the ac voltage rating does not guarantee safe dc current.

**Grading key points:**

- A transient secondary emf occurs when current changes at connection or disconnection, but steady dc provides no sustained transformer action.
- The core can saturate and the primary current becomes limited mainly by winding resistance rather than its normal ac reactance, causing overheating and possible failure.

Source: [PDF page 1071](source-page-1071.png); source question Q31.16.

## Q31.17: Transformer ratio and reflected resistance

For an ideal transformer at fixed primary voltage and fixed secondary load R, what changes when only secondary turns N2 double?

**Solution:**
The secondary voltage doubles since $V_2/V_1=N_2/N_1$. The load's physical resistance R is unchanged, but its effective resistance seen from the primary is $R_{in}=(N_1/N_2)^2R$, which falls by a factor of 4. Secondary current doubles and primary current quadruples for the fixed resistive load.

**Why it works:**
The phrase effective secondary resistance refers to the resistance reflected through the transformer, not a physical change in the load.

**Grading key points:**

- The secondary voltage doubles since $V_2/V_1=N_2/N_1$.
- The load's physical resistance R is unchanged, but its effective resistance seen from the primary is $R_{in}=(N_1/N_2)^2R$, which falls by a factor of 4.
- Secondary current doubles and primary current quadruples for the fixed resistive load.

Source: [PDF page 1071](source-page-1071.png); source question Q31.17.

## Q31.18: AC and DC compatibility

Give examples of devices that can use either ac or dc, require ac, or require dc, and explain why.

**Solution:**
A simple incandescent bulb or resistive heater can use either at matching rms voltage and suitable rating. An ordinary transformer and a mains induction motor require appropriately alternating excitation. A bare polarized electrolytic capacitor circuit or conventional brushed permanent-magnet dc motor requires the specified dc supply for normal operation. Many electronic appliances accept ac or dc only because internal rectifiers and converters condition the input; compatibility must follow the actual design.

**Why it works:**
Heating depends mainly on rms current, induction needs time-varying flux, and polarized or commutated circuits impose supply constraints.

**Grading key points:**

- A simple incandescent bulb or resistive heater can use either at matching rms voltage and suitable rating.
- An ordinary transformer and a mains induction motor require appropriately alternating excitation.
- A bare polarized electrolytic capacitor circuit or conventional brushed permanent-magnet dc motor requires the specified dc supply for normal operation.
- Many electronic appliances accept ac or dc only because internal rectifiers and converters condition the input; compatibility must follow the actual design.

Source: [PDF page 1071](source-page-1071.png); source question Q31.18.
