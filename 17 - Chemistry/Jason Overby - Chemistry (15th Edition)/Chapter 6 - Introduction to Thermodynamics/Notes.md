# Chapter 6 — Energy Relationships in Chemical Reactions

*General Chemistry: The Essential Concepts — Chang and Overby, 6th edition.*

## 6.1 The Nature of Energy and Types of Energy

Energy is the capacity to do work. In chemistry, we are usually interested in how energy changes when particles move, interact, or rearrange during a reaction.

| Form | What it describes |
| --- | --- |
| Kinetic energy | Energy associated with motion. |
| Potential energy | Energy associated with position and interactions. |
| Chemical energy | Potential energy associated with the arrangement of atoms and electrons in substances. |
| Thermal energy | Energy associated with the random motion of particles. |
| Radiant energy | Energy transferred by electromagnetic radiation, including visible light. |

These forms can be converted into one another. A reaction can convert chemical energy into thermal energy, but it does not create energy. **Conservation of energy means that an energy gain somewhere must be accounted for by an energy loss elsewhere.**

### Temperature and Heat

Temperature helps describe the thermal condition of a sample; it does not tell us its total thermal energy. The amount of substance matters too. A larger quantity of water can have more thermal energy than a smaller, hotter quantity.

**Heat is energy transferred because of a temperature difference.** It flows spontaneously from a hotter body to a colder body. A substance has internal energy; heat describes a transfer during a process.

## 6.2 Energy Changes in Chemical Reactions

Before deciding whether energy is gained or lost, define the **system**: the part we are studying. Everything outside that boundary is the **surroundings**.

For a reaction, the system often means the reacting substances. In a calorimetry problem, distinguish these substances from the solution and apparatus that absorb their released energy.

| System | Exchanges matter? | Exchanges energy? |
| --- | --- | --- |
| Open | Yes | Yes |
| Closed | No | Yes |
| Isolated | No | No |

**Closed does not mean insulated.** A sealed container can still exchange energy through its walls.

### Exothermic and Endothermic Processes

The sign of heat, $q$, is written from the system's perspective:

| Process | Direction of heat transfer | Sign of $q$ |
| --- | --- | --- |
| Endothermic | Surroundings into system | Positive |
| Exothermic | System into surroundings | Negative |

So why might an exothermic reaction make a solution warmer? The reaction releases energy, while the solution absorbs it. The same transfer has opposite signs for these two parts of the experiment.

## 6.3 Introduction to Thermodynamics

### Internal Energy and State Functions

Internal energy, $U$, includes the microscopic kinetic and potential energies of the system. For chemical calculations, we usually need its change:

$$
\Delta U=U_f-U_i
$$

A **state function** depends on the condition of the system, rather than the route taken to reach it. Internal energy is a state function: the same initial and final states give the same $\Delta U$.

Heat and work describe how energy crosses the boundary during that route. **$q$ and $w$ are not state functions.** Different paths can give different amounts of each while producing the same total change in internal energy.

### First Law of Thermodynamics

$$
\Delta U=q+w
$$

Here $q$ is heat transferred into the system and $w$ is work done on the system, with their signs included.

| Transfer | Sign |
| --- | --- |
| Heat absorbed by the system | $q>0$ |
| Heat released by the system | $q<0$ |
| Work done on the system | $w>0$ |
| Work done by the system | $w<0$ |

Think of these as two ways to change the same energy balance. Heat entering increases $U$; work performed by the system uses energy and decreases $U$. **An exothermic process does not, by itself, determine the sign of $\Delta U$ if work also occurs.** Add the signed transfers.

### Pressure–Volume Work

A gas that expands against an external pressure pushes its surroundings back. For a **constant external pressure**:

$$
w=-P_{\mathrm{ext}}\Delta V,
\qquad \Delta V=V_f-V_i
$$

- Expansion: $\Delta V>0$, so $w<0$.
- Compression: $\Delta V<0$, so $w>0$.
- No volume change: no pressure–volume work.

The pressure here is the **opposing external pressure**. Expansion into a vacuum has zero pressure–volume work because $P_{\mathrm{ext}}=0$; this alone does not tell us the heat transfer.

Keep the units consistent:

$$
1\ \mathrm{L\cdot atm}=101.325\ \mathrm{J}
$$

**needs expansion — Pressure–Volume Work Equation:** connect force, piston displacement, pressure, and volume change, including why expansion receives a negative sign.

## 6.4 Enthalpy of Chemical Reactions

Recall that energy transferred as heat can also be used to expand a system. This is why heat measured at constant pressure and heat measured at constant volume need not be equal for the same reaction.

Enthalpy is defined as:

$$
H=U+PV
$$

$H$ and $U$ have energy units, and both are state functions. In general:

$$
\Delta H=\Delta U+\Delta(PV)
$$

For the closed systems considered here, with pressure–volume work as the only work mode:

| Conditions | Measured heat equals |
| --- | --- |
| Constant volume | $q_v=\Delta U$ |
| Constant pressure | $q_p=\Delta H$ |

**These equalities require their stated conditions.** Enthalpy is useful because many laboratory reactions occur at nearly constant atmospheric pressure.

At constant pressure:

$$
\Delta H=\Delta U+P\Delta V
$$

**needs expansion — Constant-Pressure Heat and Enthalpy:** connect the first law, expansion work, and the definition of $H$ to explain why $q_p=\Delta H$.

### Reading a Thermochemical Equation

A thermochemical equation includes a balanced reaction, the physical states, and its enthalpy change.

$$
\Delta H_{\mathrm{rxn}}=H_{\mathrm{products}}-H_{\mathrm{reactants}}
$$

At constant pressure, a negative $\Delta H$ describes an exothermic reaction; a positive $\Delta H$ describes an endothermic one.

The enthalpy change belongs to the **reaction in the proportions written**:

- Multiply every coefficient by a factor: multiply $\Delta H$ by that factor.
- Reverse the reaction: reverse the sign of $\Delta H$.
- Change a physical state: the enthalpy change generally changes too. Producing liquid water and producing water vapor are different processes.

When a reaction value is expressed per mole of reaction, use the coefficients to determine how many moles of a particular reactant correspond to that value. **Do not automatically treat it as energy per mole of every substance in the equation.** For a given sample, convert mass to moles and scale using the appropriate coefficient.

### Comparing $\Delta H$ and $\Delta U$

When the gases behave ideally, the initial and final temperatures are the same, and changes in solid/liquid volume are negligible:

$$
\Delta H=\Delta U+\Delta n_gRT
$$

Here $\Delta n_g$ is moles of gaseous products minus moles of gaseous reactants for the amount of reaction considered. $T$ is the absolute temperature in kelvin. Count **only gases**; aqueous substances are not gaseous particles.

Use an $R$ consistent with the energy units, such as $8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}$. Equal gas amounts give a zero gas correction under these assumptions. For reactions involving only condensed phases, $\Delta H$ and $\Delta U$ are often approximately equal because the volume changes are small.

**needs expansion — Enthalpy–Internal Energy Relation for Ideal-Gas Reactions:** explain the substitution of $PV=nRT$ and how it produces the gas-mole correction.

## 6.5 Calorimetry

Calorimetry measures an energy transfer by observing a temperature change. The key is to identify **which object the temperature change belongs to** before calculating its heat.

### Specific Heat and Heat Capacity

The book uses $s$ for specific heat; it is also often written $c$. Specific heat describes the heat needed per unit mass per degree. Heat capacity, $C$, describes the entire sample or apparatus.

$$
C=ms
$$

For a temperature change without a phase change, treating the specific heat as constant:

$$
q=ms\Delta T=C\Delta T,
\qquad \Delta T=T_f-T_i
$$

| Quantity | Meaning | Typical units |
| --- | --- | --- |
| $m$ | Mass of the sample | $\mathrm{g}$ |
| $s$ | Specific heat | $\mathrm{J\,g^{-1}\,{}^{\circ}C^{-1}}$ |
| $C$ | Heat capacity of the whole sample | $\mathrm{J/{}^{\circ}C}$ |
| $q$ | Heat absorbed or released | $\mathrm{J}$ |

A temperature **difference** has the same numerical value in kelvin and Celsius. This does not allow Celsius in $PV=nRT$.

For a warming sample, $\Delta T>0$ and $q>0$. A cooling sample has $q<0$. A larger specific heat means more heat is required for the same mass and temperature rise; it does not mean the sample must become hotter.

### Constant-Volume and Constant-Pressure Calorimeters

If the combined reaction, solution, and apparatus are effectively insulated from the outside, their heat transfers balance:

$$
q_{\mathrm{rxn}}+q_{\mathrm{solution}}+q_{\mathrm{apparatus}}=0
$$

In a **bomb calorimeter**, the reacting sample is held at fixed volume. If the calibrated $C_{\mathrm{cal}}$ includes the bomb and surrounding water:

$$
q_{\mathrm{rxn}}=-C_{\mathrm{cal}}\Delta T
$$

This reaction heat gives $\Delta U$ under the usual calorimetry assumptions. **Do not add the water's heat again if it is already included in $C_{\mathrm{cal}}$.**

In a **constant-pressure calorimeter**, such as an insulated cup, the solution absorbs or releases heat. If the apparatus heat capacity is negligible:

$$
q_{\mathrm{rxn}}=-m_{\mathrm{solution}}s_{\mathrm{solution}}\Delta T
$$

This gives $\Delta H$ for the reaction under the conditions above. Use the mass of the **combined solution**, and use water's specific heat or density only when that approximation is justified or given.

For a molar reaction value, scale this measured heat by the amount that actually reacted, accounting for the balanced equation and any limiting reactant. The temperature rise belongs to the solution; its positive heat becomes the reaction's negative heat.

**needs expansion — Calorimetric Heat Balance:** set up the separate heat terms, explain the insulation assumption, and show how to isolate the reaction heat or an unknown final temperature.

## 6.6 Standard Enthalpy of Formation and Reaction

### Choosing a Reference

We can measure enthalpy differences without knowing an absolute enthalpy for each substance. Standard enthalpies of formation provide a common reference for these differences.

The **standard enthalpy of formation**, $\Delta H_f^{\circ}$, is the enthalpy change for forming **one mole** of a substance from its elements in their reference forms under standard-state conditions.

By convention:

$$
\Delta H_f^{\circ}(\text{element in its reference form})=0
$$

For example, graphite and $\mathrm{O_2(g)}$ have zero reference formation enthalpies at the conditions used in the book; diamond and $\mathrm{O_3(g)}$ do not. **An element's reference value of zero does not mean that it contains no internal energy.**

The book uses $1\ \mathrm{atm}$ in its calculations, while noting that thermodynamic standard pressure is $1\ \mathrm{bar}$. Its tabulated formation values are at $25\,{}^{\circ}\mathrm{C}$. The standard-state symbol does not itself specify a temperature; use the conditions attached to the data.

Formation equations may use fractional coefficients to produce exactly one mole of product. Check both the elemental forms and the product's physical state.

### Hess's Law

Recall that enthalpy is a state function. If several reactions add to the desired overall reaction, their enthalpy changes add too:

$$
\Delta H_{\mathrm{overall}}=\sum_j\Delta H_j
$$

Reverse or multiply each reaction as needed, make the same change to its enthalpy, then cancel substances that occur on both sides. Only identical substances in identical physical states cancel. These steps form an energy-accounting route; they do not have to describe the actual reaction mechanism.

**needs expansion — Hess's Law of Heat Summation:** arrange a reaction cycle and explain why intermediate substances cancel while the total enthalpy change is preserved.

### Calculating from Formation Enthalpies

$$
\Delta H_{\mathrm{rxn}}^{\circ}
=\sum_{\mathrm{products}}\nu_i\Delta H_{f,i}^{\circ}
-\sum_{\mathrm{reactants}}\nu_i\Delta H_{f,i}^{\circ}
$$

$\nu_i$ is the balanced coefficient for substance $i$. Multiply each tabulated formation enthalpy by its coefficient, total each side, then subtract **products minus reactants**. A negative tabulated value stays negative during substitution; the subtraction of the reactant sum is a separate operation.

**needs expansion — Standard Reaction Enthalpy from Formation Enthalpies:** connect the formula to Hess's law by decomposing reactants into their reference elements and forming the products.
