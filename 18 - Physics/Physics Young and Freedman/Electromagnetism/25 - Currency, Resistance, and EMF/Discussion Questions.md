# Chapter 25: Current, Resistance, and Electromotive Force

24 questions. Standardized prompts with original solutions; source numbering follows the 13th edition.

## Q25.1: Steady conduction versus electrostatics

Does $\rho=E/J$ requiring a field in a resistive conductor contradict the statement that a conductor has zero interior field?

**Solution:**
No. Zero interior field applies to electrostatic equilibrium with no sustained current. A resistive conductor carrying steady current needs a nonzero field to drive carrier drift against scattering.

**Why it works:**
A steady nonequilibrium current is different from an electrostatic equilibrium.

**Grading key points:**

- No.
- Zero interior field applies to electrostatic equilibrium with no sustained current.
- A resistive conductor carrying steady current needs a nonzero field to drive carrier drift against scattering.

Source: [PDF page 868](source-page-868.png); source question Q25.1.

## Q25.2: Geometric resistance scaling

A cylindrical rod has resistance R. What is its resistance if length and diameter are both tripled, with material and temperature unchanged?

**Solution:**
The new area is 9A and the new length is 3L, so $R'=\rho(3L)/(9A)=R/3$.

**Why it works:**
Resistance depends on length divided by cross-sectional area; area scales as diameter squared.

**Grading key points:**

- The new area is 9A and the new length is 3L, so $R'=\rho(3L)/(9A)=R/3$.

Source: [PDF page 868](source-page-868.png); source question Q25.2.

## Q25.3: Material resistivity

What happens to a rod's resistivity if its length and diameter are tripled but material and temperature stay the same?

**Solution:**
Its resistivity remains $\rho$. Dimensions change resistance, not the bulk material parameter under the stated assumptions.

**Why it works:**
Resistivity is a material property in the macroscopic ohmic model.

**Grading key points:**

- Its resistivity remains $\rho$.
- Dimensions change resistance, not the bulk material parameter under the stated assumptions.

Source: [PDF page 868](source-page-868.png); source question Q25.3.

## Q25.4: Current continuity and drift

Two copper wires of different diameters are joined. What happens to electron drift speed on going from the wider wire into the narrower wire, and what causes the change?

**Solution:**
The steady current is the same and $I=neAv_d$. With the same carrier density, the smaller area requires a larger drift-speed magnitude. A surface-charge distribution establishes the appropriate electric field; electric forces drive the altered drift, with scattering setting its average value.

**Why it works:**
Charge conservation fixes current, while area and carrier density determine average drift speed.

**Grading key points:**

- The steady current is the same and $I=neAv_d$.
- With the same carrier density, the smaller area requires a larger drift-speed magnitude.
- A surface-charge distribution establishes the appropriate electric field; electric forces drive the altered drift, with scattering setting its average value.

Source: [PDF page 868](source-page-868.png); source question Q25.4.

## Q25.5: Terminal voltage under load

When can a nominal 1.5-V battery have less than 1.5 V across its terminals?

**Solution:**
During discharge through a load, its terminal voltage is $V=\mathcal E-Ir$, below its emf for positive current and internal resistance. Depletion and chemistry can also change the actual emf from its nominal rating.

**Why it works:**
Some of the emf is lost as an internal resistive voltage drop.

**Grading key points:**

- During discharge through a load, its terminal voltage is $V=\mathcal E-Ir$, below its emf for positive current and internal resistance.
- Depletion and chemistry can also change the actual emf from its nominal rating.

Source: [PDF page 868](source-page-868.png); source question Q25.5.

## Q25.6: Reversed terminal polarity

Can a battery's terminal voltage oppose its own emf? Describe a possible circuit condition.

**Solution:**
Yes in the simple emf-plus-resistance model if an external circuit forces discharge-direction current $I>\mathcal E/r$, so $V=\mathcal E-Ir<0$. For example, a much stronger series-aiding source can drive excessive current through a weak cell. Ordinary charging instead gives $V=\mathcal E+Ir$ with the usual terminal polarity; it does not by itself reverse V.

**Why it works:**
Terminal voltage includes the signed internal-resistance drop as well as the chemical emf.

**Grading key points:**

- Yes in the simple emf-plus-resistance model if an external circuit forces discharge-direction current $I>\mathcal E/r$, so $V=\mathcal E-Ir<0$.
- For example, a much stronger series-aiding source can drive excessive current through a weak cell.
- Ordinary charging instead gives $V=\mathcal E+Ir$ with the usual terminal polarity; it does not by itself reverse V.

Source: [PDF page 868](source-page-868.png); source question Q25.6.

## Q25.7: Measuring internal resistance

Is internal resistance equal to open-circuit voltage divided by short-circuit current?

**Solution:**
In the linear Thevenin model, yes: $V_{oc}=\mathcal E$ and $I_{sc}=\mathcal E/r$, hence $r=V_{oc}/I_{sc}$. Real sources may be nonlinear, temperature dependent, or current limited, so this relation is model dependent and is not a recommendation to short a battery.

**Why it works:**
The quotient follows directly from the source's linear voltage-current relation.

**Grading key points:**

- In the linear Thevenin model, yes: $V_{oc}=\mathcal E$ and $I_{sc}=\mathcal E/r$, hence $r=V_{oc}/I_{sc}$.
- Real sources may be nonlinear, temperature dependent, or current limited, so this relation is model dependent and is not a recommendation to short a battery.

Source: [PDF page 868](source-page-868.png); source question Q25.7.

## Q25.8: Current depends on load

Should a battery label specify one current it supplies as though it were a fixed output like emf?

**Solution:**
No single operating current is fixed independently of the load: $I=\mathcal E/(R+r)$. A label can usefully state a maximum rated current or capacity in ampere-hours, but these are different from the actual current in an arbitrary circuit.

**Why it works:**
The complete circuit determines current; emf is a source characteristic.

**Grading key points:**

- No single operating current is fixed independently of the load: $I=\mathcal E/(R+r)$.
- A label can usefully state a maximum rated current or capacity in ampere-hours, but these are different from the actual current in an arbitrary circuit.

Source: [PDF page 868](source-page-868.png); source question Q25.8.

## Q25.9: Flow versus accumulated charge

How can 10 A be ordinary when putting a net charge of 1 C on an isolated object is difficult?

**Solution:**
Current measures charge passing a cross section per time, not net charge accumulating in the wire. At 10 A, 10 C passes each second while nearly the same charge leaves every segment as enters, so the conductor remains nearly neutral.

**Why it works:**
A large balanced throughput need not produce a large stored excess charge.

**Grading key points:**

- Current measures charge passing a cross section per time, not net charge accumulating in the wire.
- At 10 A, 10 C passes each second while nearly the same charge leaves every segment as enters, so the conductor remains nearly neutral.

Source: [PDF page 868](source-page-868.png); source question Q25.9.

## Q25.10: Charge continuity and energy loss

Compare electron drift speeds in equal-diameter wires just before and after a resistor, and compare their electrical potential energies.

**Solution:**
For the same wire material and steady current, drift-speed magnitudes are equal because n and A are equal. Electrons lose electric potential energy while traversing the resistor; for an electron moving from higher to lower U, the electric potential rises because $U=-eV$. Energy goes into lattice heating rather than progressively accumulating as drift kinetic energy.

**Why it works:**
Current is conserved while electrical energy is transferred to matter by scattering.

**Grading key points:**

- For the same wire material and steady current, drift-speed magnitudes are equal because n and A are equal.
- Electrons lose electric potential energy while traversing the resistor; for an electron moving from higher to lower U, the electric potential rises because $U=-eV$.
- Energy goes into lattice heating rather than progressively accumulating as drift kinetic energy.

Source: [PDF page 868](source-page-868.png); source question Q25.10.

## Q25.11: Joule heating and temperature coefficient

Why does current heat a resistor, and how does that change its resistance?

**Solution:**
The field does work on carriers, which transfer energy to the lattice through scattering. The electrical power is $I^2R$. For an ordinary metal, increased lattice vibration usually raises resistance as temperature rises; semiconductors and other materials need not follow that trend.

**Why it works:**
Electrical work becomes thermal energy, and the resistance response depends on the material's temperature coefficient.

**Grading key points:**

- The field does work on carriers, which transfer energy to the lattice through scattering.
- The electrical power is $I^2R$.
- For an ordinary metal, increased lattice vibration usually raises resistance as temperature rises; semiconductors and other materials need not follow that trend.

Source: [PDF page 868](source-page-868.png); source question Q25.11.

## Q25.12: Nonohmic heating curve

Which curve in Figure Q25.12 best describes current versus voltage for a metal resistor that heats substantially?

![Four candidate current-versus-voltage graphs, labeled a through d.](18%20-%20Physics/Physics%20Young%20and%20Freedman/assets/figure-q25-12.png)

**Solution:**
Curve (d): I rises but the slope decreases as heating raises resistance. Curve (a) would be the approximately fixed-temperature ohmic limit; (b) suggests decreasing resistance with increasing voltage, and (c) makes current decrease over the shown positive-voltage range.

**Why it works:**
Self-heating with positive temperature coefficient makes I grow less than proportionally with V.

**Grading key points:**

- Curve (d): I rises but the slope decreases as heating raises resistance.
- Curve (a) would be the approximately fixed-temperature ohmic limit; (b) suggests decreasing resistance with increasing voltage, and (c) makes current decrease over the shown positive-voltage range.

Source: [PDF page 868](source-page-868.png); source question Q25.12.

## Q25.13: Cold-filament inrush

Why do incandescent bulbs often fail at switch-on?

**Solution:**
A cold tungsten filament has much lower resistance than a hot filament, so applying the line voltage produces a large initial current. Rapid heating and thermal stress can break an already thinned or weakened filament.

**Why it works:**
A positive temperature coefficient makes the cold-start current larger than the steady hot current.

**Grading key points:**

- A cold tungsten filament has much lower resistance than a hot filament, so applying the line voltage produces a large initial current.
- Rapid heating and thermal stress can break an already thinned or weakened filament.

Source: [PDF page 869](source-page-869.png); source question Q25.13.

## Q25.14: Series bulb power

Two identical bulbs A and B are in series with a battery. Compare brightness. Then replace B by a wire and compare A's brightness with before.

**Solution:**
In series the same current flows through equal resistances, so the bulbs have equal power and brightness. Replacing B by a wire lowers total resistance, increases current through A, and makes A brighter. With an ideal voltage source and constant bulb resistance the current doubles and A's power quadruples; real filaments change resistance as they heat.

**Why it works:**
Brightness tracks dissipated power, and changing the total series resistance changes the shared current.

**Grading key points:**

- In series the same current flows through equal resistances, so the bulbs have equal power and brightness.
- Replacing B by a wire lowers total resistance, increases current through A, and makes A brighter.
- With an ideal voltage source and constant bulb resistance the current doubles and A's power quadruples; real filaments change resistance as they heat.

Source: [PDF page 869](source-page-869.png); source question Q25.14.

## Q25.15: Meter position in a series loop

If an ideal ammeter and bulb swap positions in an otherwise unchanged series circuit, what happens to the reading and brightness?

**Solution:**
Both remain the same. Every element of a single steady-current loop carries the same current, and an ideal ammeter adds zero resistance regardless of position.

**Why it works:**
Charge is not consumed by the bulb; it transfers energy while current remains continuous.

**Grading key points:**

- Both remain the same.
- Every element of a single steady-current loop carries the same current, and an ideal ammeter adds zero resistance regardless of position.

Source: [PDF page 869](source-page-869.png); source question Q25.15.

## Q25.16: Series ammeter versus series voltmeter

Compare a bulb's brightness with an ideal ammeter in series versus an ideal voltmeter in series.

**Solution:**
With the ammeter, its zero resistance allows normal circuit current and the bulb glows. An ideal voltmeter has infinite resistance; placed in series it opens the circuit, giving zero steady current and no glow.

**Why it works:**
Meter resistance and connection topology determine loading; voltmeters normally connect in parallel.

**Grading key points:**

- With the ammeter, its zero resistance allows normal circuit current and the bulb glows.
- An ideal voltmeter has infinite resistance; placed in series it opens the circuit, giving zero steady current and no glow.

Source: [PDF page 869](source-page-869.png); source question Q25.16.

## Q25.17: Battery round-trip efficiency

Why is recoverable storage-battery energy less than charging energy?

**Solution:**
Internal resistance converts energy to heat during both charging and discharge, and electrochemical reactions and polarization can introduce additional losses. Over a complete cycle, the recovered electrical energy is the input minus these losses.

**Why it works:**
Energy is conserved overall, but some becomes unavailable thermal or chemical energy.

**Grading key points:**

- Internal resistance converts energy to heat during both charging and discharge, and electrochemical reactions and polarization can introduce additional losses.
- Over a complete cycle, the recovered electrical energy is the input minus these losses.

Source: [PDF page 869](source-page-869.png); source question Q25.17.

## Q25.18: Emf versus high-current capability

Can eight flashlight cells in series replace a roughly 12-V car battery for starting an engine?

**Solution:**
Usually not. Similar total emf does not imply comparable internal resistance or current capability. Small cells' combined internal resistance makes terminal voltage collapse under starter demand and causes substantial internal heating.

**Why it works:**
A starter requires large current and power, not merely the correct open-circuit voltage.

**Grading key points:**

- Usually not.
- Similar total emf does not imply comparable internal resistance or current capability.
- Small cells' combined internal resistance makes terminal voltage collapse under starter demand and causes substantial internal heating.

Source: [PDF page 869](source-page-869.png); source question Q25.18.

## Q25.19: Voltage and wire mass

Why can a 24-V aircraft system use lighter wiring than a 12-V system for similar electrical power?

**Solution:**
At the same power, $I=P/V$ is halved when V doubles. For a specified allowable wire heating, $P_{loss}=I^2R$ permits greater resistance and therefore a smaller wire area. The exact area saving depends on voltage-drop and thermal design constraints.

**Why it works:**
Higher distribution voltage reduces required current and associated resistive losses.

**Grading key points:**

- At the same power, $I=P/V$ is halved when V doubles.
- For a specified allowable wire heating, $P_{loss}=I^2R$ permits greater resistance and therefore a smaller wire area.
- The exact area saving depends on voltage-drop and thermal design constraints.

Source: [PDF page 869](source-page-869.png); source question Q25.19.

## Q25.20: Transmission voltage tradeoffs

What are the advantages and disadvantages of very high voltage for long-distance power transmission?

**Solution:**
For fixed real power and power factor, higher voltage lowers current and therefore $I^2R$ loss and required conductor size. Disadvantages include insulation and clearance requirements, corona losses, more demanding equipment, and increased arc and contact hazards.

**Why it works:**
Transmission loss depends on current squared, while insulation stresses depend on voltage and field.

**Grading key points:**

- For fixed real power and power factor, higher voltage lowers current and therefore $I^2R$ loss and required conductor size.
- Disadvantages include insulation and clearance requirements, corona losses, more demanding equipment, and increased arc and contact hazards.

Source: [PDF page 869](source-page-869.png); source question Q25.20.

## Q25.21: Distribution-voltage tradeoffs

Discuss the tradeoff behind household voltages of order 120 V and low vehicle voltages of order 12 V.

**Solution:**
Household voltages balance useful power delivery at moderate currents against insulation and contact hazards; much lower voltage would require much heavier wiring. A vehicle's low voltage suits a compact chemical battery system and reduces some insulation and contact concerns, but requires high starter currents and thick cables. These are engineering compromises, not uniquely optimal values.

**Why it works:**
Useful power is VI, while wire loss and insulation requirements favor different voltage choices.

**Grading key points:**

- Household voltages balance useful power delivery at moderate currents against insulation and contact hazards; much lower voltage would require much heavier wiring.
- A vehicle's low voltage suits a compact chemical battery system and reduces some insulation and contact concerns, but requires high starter currents and thick cables.
- These are engineering compromises, not uniquely optimal values.

Source: [PDF page 869](source-page-869.png); source question Q25.21.

## Q25.22: Fuse thermal design

What material and design characteristics let a fuse open a circuit above a specified current?

**Solution:**
The fusible element must have a reproducible melting threshold and suitable resistivity, cross section, heat capacity, and heat loss so excessive $I^2R$ heating melts it on the specified time-current curve. It should add modest loss at normal current and its enclosure must safely interrupt the arc.

**Why it works:**
Fuse action follows a thermal energy balance, not a universal current threshold determined by melting point alone.

**Grading key points:**

- The fusible element must have a reproducible melting threshold and suitable resistivity, cross section, heat capacity, and heat loss so excessive $I^2R$ heating melts it on the specified time-current curve.
- It should add modest loss at normal current and its enclosure must safely interrupt the arc.

Source: [PDF page 869](source-page-869.png); source question Q25.22.

## Q25.23: Current-limited high-voltage sources

Why can a high-voltage source with large internal resistance be safer than one of the same emf with small internal resistance?

**Solution:**
For a connected load, $I=\mathcal E/(r+R_{load})$; larger r limits sustained current and reduces delivered power. This reduces one hazard mechanism, although stored output capacitance and its discharge energy can still matter.

**Why it works:**
Open-circuit voltage alone does not determine fault current or stored energy.

**Grading key points:**

- For a connected load, $I=\mathcal E/(r+R_{load})$; larger r limits sustained current and reduces delivered power.
- This reduces one hazard mechanism, although stored output capacitance and its discharge energy can still matter.

Source: [PDF page 869](source-page-869.png); source question Q25.23.

## Q25.24: Thermal conduction along thin wires

If metal conducts heat well, why do appliance cords not become as hot as heating elements merely by thermal conduction?

**Solution:**
Conductive heat flow scales as $kA\Delta T/\ell$. The cords have small cross sections, appreciable length, and lose heat to air and surroundings, limiting conducted heat from the hot element. Their electrical resistance is also chosen low enough to limit their own Joule heating.

**Why it works:**
High material conductivity does not overcome a small area, a long path, and distributed cooling.

**Grading key points:**

- Conductive heat flow scales as $kA\Delta T/\ell$.
- The cords have small cross sections, appreciable length, and lose heat to air and surroundings, limiting conducted heat from the hot element.
- Their electrical resistance is also chosen low enough to limit their own Joule heating.

Source: [PDF page 869](source-page-869.png); source question Q25.24.
