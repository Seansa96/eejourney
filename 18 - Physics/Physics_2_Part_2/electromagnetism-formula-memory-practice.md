# Electromagnetism Formula Memory Practice

140 short exercises: five per section, including five for each of Maxwell's four equations. Use the reference formula, substitute the givens, and solve for the one missing value. An answer key is at the end.

**Naming notes:** “Bio-Severt” means **Biot–Savart**. “Inductive capacitance” is interpreted here as **capacitive reactance**, $X_C$. The expression $ILB\sin\theta$ gives the magnetic force on a straight current-carrying wire; it has its own final section for extra practice.

## Constants and conventions

Use these rounded constants throughout:

$$
k=9.00\times10^9\ \mathrm{N\,m^2/C^2},\qquad
\epsilon_0=8.85\times10^{-12}\ \mathrm{F/m}
$$

$$
\mu_0=4\pi\times10^{-7}\ \mathrm{T\,m/A},\qquad
e=1.60\times10^{-19}\ \mathrm C
$$

- $\mu=10^{-6}$ as a unit prefix; $\mathrm{m}=10^{-3}$ as a unit prefix; $\mathrm{n}=10^{-9}$ as a unit prefix. For example, $1\,\mu\mathrm C=10^{-6}\,\mathrm C$ and $1\,\mathrm{mH}=10^{-3}\,\mathrm H$.
- Use degrees for angles. Helpful values: $\sin30^\circ=\cos60^\circ=0.5$ and $\sin90^\circ=\cos0^\circ=1$.
- Give magnitudes unless a signed quantity is requested. Round non-exact numerical answers to three significant figures.
- Fields are uniform wherever a flux is written as $EA\cos\theta$ or $BA\cos\theta$. For flux, $\theta$ is measured from the **surface normal**, not from the surface itself.
- AC voltage and current are sinusoidal. Circuit elements are ideal; impedance and resonance exercises use a **series RLC circuit**.
- $L$ means wire length in wire-force formulas and inductance in circuit formulas. $N$ is the number of turns. $\mathcal E$ is emf, measured in volts. $\tau$ means a time constant or a torque, as indicated by the section.

## 1. Maxwell: Gauss's law for electricity

**Meaning:** Net outward electric flux through a closed surface depends on the charge enclosed.

$$
\Phi_E=\oiint_S\mathbf E\cdot d\mathbf A=\frac{Q_{\mathrm{enc}}}{\epsilon_0}
$$

1. A closed surface encloses $Q_{\mathrm{enc}}=8.85\times10^{-12}\,\mathrm C$. Find $\Phi_E$.
2. A closed surface has $\Phi_E=4.00\,\mathrm{N\,m^2/C}$. Find $Q_{\mathrm{enc}}$.
3. A closed surface encloses $Q_{\mathrm{enc}}=-1.77\times10^{-11}\,\mathrm C$. Find the signed net flux $\Phi_E$.
4. A closed surface has zero net electric flux. Find its net enclosed charge.
5. A closed surface has $\Phi_E=-5.00\,\mathrm{N\,m^2/C}$. Find the signed enclosed charge.

## 2. Maxwell: Gauss's law for magnetism

**Meaning:** The net magnetic flux through any closed surface is zero.

$$
\oiint_S\mathbf B\cdot d\mathbf A=0,\qquad \sum_i\Phi_{B,i}=0
$$

Flux leaving the closed surface is positive; flux entering is negative. Each question partitions the entire closed surface into the listed parts.

1. Two parts have signed magnetic fluxes $+6.00\,\mathrm{mWb}$ and $\Phi_2$. Find $\Phi_2$.
2. Three parts have signed fluxes $+3.00\,\mathrm{mWb}$, $-8.00\,\mathrm{mWb}$, and $\Phi_3$. Find $\Phi_3$.
3. Four parts have signed fluxes $+4.00\,\mathrm{mWb}$, $+2.00\,\mathrm{mWb}$, $-1.00\,\mathrm{mWb}$, and $\Phi_4$. Find $\Phi_4$.
4. Two parts have fluxes $-0.0200\,\mathrm{Wb}$ and $\Phi_2$. Find $\Phi_2$.
5. A closed surface is in a uniform $0.750\,\mathrm T$ magnetic field. Find its total net magnetic flux.

## 3. Maxwell: Faraday's law

**Meaning:** Changing magnetic flux induces an emf.

$$
\oint_C\mathbf E\cdot d\boldsymbol\ell=-\frac{d\Phi_B}{dt}
$$

For $N$ identical turns, with $\Phi_B$ the flux **per turn** and a constant rate of change:

$$
\mathcal E=-N\frac{\Delta\Phi_B}{\Delta t}
$$

Use the signed emf and flux associated with the chosen loop orientation.

1. $N=1$, $\Delta\Phi_B=+0.0600\,\mathrm{Wb}$, and $\Delta t=0.200\,\mathrm s$. Find $\mathcal E$.
2. $N=20$, $\Delta\Phi_B=-0.0100\,\mathrm{Wb}$, and $\Delta t=0.500\,\mathrm s$. Find $\mathcal E$.
3. $\mathcal E=-2.00\,\mathrm V$, $N=10$, and $\Delta t=0.250\,\mathrm s$. Find $\Delta\Phi_B$.
4. $\mathcal E=-3.00\,\mathrm V$, $N=50$, and $\Delta\Phi_B=+0.0120\,\mathrm{Wb}$. Find $\Delta t$.
5. $\mathcal E=+4.00\,\mathrm V$, $\Delta\Phi_B=-0.0200\,\mathrm{Wb}$, and $\Delta t=0.100\,\mathrm s$. Find $N$.

## 4. Maxwell: Ampère–Maxwell law

**Meaning:** Both conduction current and changing electric flux produce magnetic circulation.

$$
\oint_C\mathbf B\cdot d\boldsymbol\ell
=\mu_0\left(I_{\mathrm{enc}}+\epsilon_0\frac{d\Phi_E}{dt}\right)
$$

Define displacement current $I_d=\epsilon_0\,d\Phi_E/dt$ and circulation $\mathcal C_B=\oint_C\mathbf B\cdot d\boldsymbol\ell$. Then:

$$
\mathcal C_B=\mu_0(I_{\mathrm{enc}}+I_d)
$$

1. $I_{\mathrm{enc}}=3.00\,\mathrm A$ and $I_d=0$. Find $\mathcal C_B$ in $\mathrm{T\,m}$.
2. $\mathcal C_B=8\pi\times10^{-7}\,\mathrm{T\,m}$ and $I_d=0$. Find $I_{\mathrm{enc}}$.
3. $d\Phi_E/dt=2.00\times10^{11}\,\mathrm{N\,m^2/(C\,s)}$. Find $I_d$.
4. $I_d=0.885\,\mathrm A$. Find $d\Phi_E/dt$.
5. $\mathcal C_B=20\pi\times10^{-7}\,\mathrm{T\,m}$ and $I_{\mathrm{enc}}=2.00\,\mathrm A$. Find $I_d$.

## 5. Biot–Savart law

**Meaning:** A current element contributes a small magnetic field.

$$
d\mathbf B=\frac{\mu_0}{4\pi}\frac{I\,d\boldsymbol\ell\times\hat{\mathbf r}}{r^2},\qquad
dB=\frac{\mu_0}{4\pi}\frac{I\,d\ell\sin\theta}{r^2}
$$

Here $r$ is the distance from the current element to the field point, and $\theta$ is the angle between the current element and the direction to that point. Treat $d\ell$ as sufficiently short to use the current-element formula numerically.

1. $I=2.00\,\mathrm A$, $d\ell=1.00\times10^{-3}\,\mathrm m$, $r=0.100\,\mathrm m$, and $\theta=90^\circ$. Find $dB$.
2. $dB=4.00\times10^{-8}\,\mathrm T$, $d\ell=1.00\times10^{-3}\,\mathrm m$, $r=0.100\,\mathrm m$, and $\theta=90^\circ$. Find $I$.
3. $dB=3.00\times10^{-8}\,\mathrm T$, $I=3.00\,\mathrm A$, $r=0.100\,\mathrm m$, and $\theta=90^\circ$. Find $d\ell$.
4. $dB=1.00\times10^{-8}\,\mathrm T$, $I=4.00\,\mathrm A$, $d\ell=1.00\times10^{-3}\,\mathrm m$, and $\theta=90^\circ$. Find $r$.
5. $I=6.00\,\mathrm A$, $d\ell=1.00\times10^{-3}\,\mathrm m$, $r=0.100\,\mathrm m$, and $\theta=30^\circ$. Find $dB$.

## 6. Magnetic force on a moving charge

**Meaning:** A moving charge experiences a magnetic force perpendicular to its velocity and the magnetic field.

$$
\mathbf F_B=q\mathbf v\times\mathbf B,\qquad F_B=|q|vB\sin\theta
$$

Here $\theta$ is the angle between velocity and magnetic field.

1. $|q|=2.00\,\mu\mathrm C$, $v=300\,\mathrm{m/s}$, $B=0.500\,\mathrm T$, and $\theta=90^\circ$. Find $F_B$.
2. $F_B=0.00600\,\mathrm N$, $v=2000\,\mathrm{m/s}$, $B=0.500\,\mathrm T$, and $\theta=90^\circ$. Find $|q|$.
3. $F_B=0.00400\,\mathrm N$, $|q|=4.00\,\mu\mathrm C$, $B=0.500\,\mathrm T$, and $\theta=90^\circ$. Find $v$.
4. $F_B=0.00300\,\mathrm N$, $|q|=2.00\,\mu\mathrm C$, $v=3000\,\mathrm{m/s}$, and $\theta=90^\circ$. Find $B$.
5. $|q|=4.00\,\mu\mathrm C$, $v=1000\,\mathrm{m/s}$, $B=0.500\,\mathrm T$, and $\theta=30^\circ$. Find $F_B$.

## 7. Electric dipole moment

**Meaning:** Electric dipole moment measures charge separation. Its direction is from negative charge to positive charge.

$$
\mathbf p=q\mathbf d,\qquad p=qd
$$

$q$ is the magnitude of either charge; $d$ is the full separation between the two charges.

1. $q=2.00\,\mu\mathrm C$ and $d=0.0300\,\mathrm m$. Find $p$.
2. $p=8.00\times10^{-8}\,\mathrm{C\,m}$ and $d=0.0200\,\mathrm m$. Find $q$.
3. $p=1.50\times10^{-7}\,\mathrm{C\,m}$ and $q=5.00\,\mu\mathrm C$. Find $d$.
4. $q=6.00\,\mathrm{nC}$ and $d=0.0500\,\mathrm m$. Find $p$.
5. $p=4.00\times10^{-9}\,\mathrm{C\,m}$ and $q=20.0\,\mathrm{nC}$. Find $d$.

## 8. Time constant

**Meaning:** A time constant sets how quickly an RC or RL circuit approaches its steady state. After one time constant, a decaying quantity is $1/e\approx36.8\%$ of its initial value.

$$
\tau_{RC}=RC,\qquad \tau_{RL}=\frac{L}{R}
$$

Use the resistance seen by the capacitor or inductor; the resistance is supplied directly here.

1. RC circuit: $R=2000\,\Omega$ and $C=5.00\,\mu\mathrm F$. Find $\tau$.
2. RC circuit: $\tau=0.0300\,\mathrm s$ and $C=10.0\,\mu\mathrm F$. Find $R$.
3. RC circuit: $\tau=0.0200\,\mathrm s$ and $R=4000\,\Omega$. Find $C$.
4. RL circuit: $L=0.600\,\mathrm H$ and $R=30.0\,\Omega$. Find $\tau$.
5. RL circuit: $\tau=0.0400\,\mathrm s$ and $R=20.0\,\Omega$. Find $L$.

## 9. Magnetic dipole moment

**Meaning:** A current loop acts like a magnetic dipole. Its moment depends on current, area, and number of turns.

$$
\boldsymbol\mu=NIA\hat{\mathbf n},\qquad \mu=NIA
$$

$A$ is the area of one turn; $\hat{\mathbf n}$ follows the right-hand rule for the current.

1. $N=1$, $I=3.00\,\mathrm A$, and $A=0.0200\,\mathrm{m^2}$. Find $\mu$.
2. $\mu=0.800\,\mathrm{A\,m^2}$, $N=20$, and $A=0.0100\,\mathrm{m^2}$. Find $I$.
3. $\mu=0.300\,\mathrm{A\,m^2}$, $N=10$, and $I=2.00\,\mathrm A$. Find $A$.
4. $\mu=1.20\,\mathrm{A\,m^2}$, $I=3.00\,\mathrm A$, and $A=0.0200\,\mathrm{m^2}$. Find $N$.
5. $N=50$, $I=0.500\,\mathrm A$, and $A=0.00400\,\mathrm{m^2}$. Find $\mu$.

## 10. Torque and force on a current-carrying conductor

**Meaning:** A straight wire segment can experience a magnetic force. A current loop can experience a torque in a uniform magnetic field.

$$
F=ILB\sin\alpha,\qquad \tau=NIAB\sin\theta=\mu B\sin\theta
$$

$\alpha$ is the angle between the wire's current direction and $\mathbf B$. For torque, $\theta$ is the angle between the **loop normal** and $\mathbf B$. A complete closed loop has zero net force in a uniform field, even when it has a nonzero torque.

1. Straight segment: $I=3.00\,\mathrm A$, $L=0.200\,\mathrm m$, $B=0.500\,\mathrm T$, and $\alpha=90^\circ$. Find $F$.
2. Loop: $N=10$, $I=2.00\,\mathrm A$, $A=0.0300\,\mathrm{m^2}$, $B=0.500\,\mathrm T$, and $\theta=90^\circ$. Find $\tau$.
3. Loop: $\tau=0.200\,\mathrm{N\,m}$, $N=20$, $A=0.0100\,\mathrm{m^2}$, $B=0.500\,\mathrm T$, and $\theta=90^\circ$. Find $I$.
4. Loop: $\tau=0.0600\,\mathrm{N\,m}$, $N=10$, $I=3.00\,\mathrm A$, $B=0.400\,\mathrm T$, and $\theta=30^\circ$. Find $A$.
5. Loop: $\tau=0.0800\,\mathrm{N\,m}$, $\mu=0.200\,\mathrm{A\,m^2}$, and $\theta=90^\circ$. Find $B$.

## 11. Electric flux

**Meaning:** Electric flux measures the electric field passing through an oriented surface.

$$
\Phi_E=\int_S\mathbf E\cdot d\mathbf A=EA\cos\theta
$$

The last expression applies to a uniform field and a flat surface.

1. $E=200\,\mathrm{N/C}$, $A=0.300\,\mathrm{m^2}$, and $\theta=0^\circ$. Find $\Phi_E$.
2. $\Phi_E=80.0\,\mathrm{N\,m^2/C}$, $A=0.400\,\mathrm{m^2}$, and $\theta=0^\circ$. Find $E$.
3. $\Phi_E=15.0\,\mathrm{N\,m^2/C}$, $E=100\,\mathrm{N/C}$, and $\theta=60^\circ$. Find $A$.
4. $E=500\,\mathrm{N/C}$, $A=0.200\,\mathrm{m^2}$, and $\theta=60^\circ$. Find $\Phi_E$.
5. $E=300\,\mathrm{N/C}$, $A=0.100\,\mathrm{m^2}$, and $\theta=90^\circ$. Find $\Phi_E$.

## 12. Magnetic flux

**Meaning:** Magnetic flux measures the magnetic field passing through an oriented surface.

$$
\Phi_B=\int_S\mathbf B\cdot d\mathbf A=BA\cos\theta
$$

The last expression applies to a uniform field and a flat surface. $1\,\mathrm{Wb}=1\,\mathrm{T\,m^2}$.

1. $B=0.400\,\mathrm T$, $A=0.200\,\mathrm{m^2}$, and $\theta=0^\circ$. Find $\Phi_B$.
2. $\Phi_B=0.0300\,\mathrm{Wb}$, $A=0.100\,\mathrm{m^2}$, and $\theta=0^\circ$. Find $B$.
3. $\Phi_B=0.0200\,\mathrm{Wb}$, $B=0.500\,\mathrm T$, and $\theta=60^\circ$. Find $A$.
4. $B=0.600\,\mathrm T$, $A=0.0500\,\mathrm{m^2}$, and $\theta=60^\circ$. Find $\Phi_B$.
5. $B=0.800\,\mathrm T$, $A=0.0200\,\mathrm{m^2}$, and $\theta=90^\circ$. Find $\Phi_B$.

## 13. Electric force

**Meaning:** Coulomb's law gives the force magnitude between two point charges in vacuum. Like charges repel; opposite charges attract.

$$
F=k\frac{|q_1q_2|}{r^2}
$$

1. $q_1=2.00\,\mu\mathrm C$, $q_2=3.00\,\mu\mathrm C$, and $r=0.300\,\mathrm m$. Find $F$.
2. $F=0.900\,\mathrm N$, $|q_2|=4.00\,\mu\mathrm C$, and $r=0.200\,\mathrm m$. Find $|q_1|$.
3. $F=0.800\,\mathrm N$, $|q_1|=2.00\,\mu\mathrm C$, and $r=0.300\,\mathrm m$. Find $|q_2|$.
4. $F=0.900\,\mathrm N$, $|q_1|=1.00\,\mu\mathrm C$, and $|q_2|=4.00\,\mu\mathrm C$. Find $r$.
5. $q_1=-5.00\,\mu\mathrm C$, $q_2=+2.00\,\mu\mathrm C$, and $r=0.500\,\mathrm m$. Find $F$.

## 14. Electric field

**Meaning:** Electric field is force per unit positive test charge. A point source charge produces an inverse-square field.

$$
\mathbf E=\frac{\mathbf F}{q_{\mathrm{test}}},\qquad
E=\frac{F}{|q_{\mathrm{test}}|},\qquad E=k\frac{|Q|}{r^2}
$$

The force here is the electric force. $Q$ is the source charge; $q_{\mathrm{test}}$ is the charge placed in the field.

1. $F=0.00600\,\mathrm N$ and $|q_{\mathrm{test}}|=2.00\,\mu\mathrm C$. Find $E$.
2. $E=400\,\mathrm{N/C}$ and $|q_{\mathrm{test}}|=5.00\,\mu\mathrm C$. Find $F$.
3. $F=0.00800\,\mathrm N$ and $E=2000\,\mathrm{N/C}$. Find $|q_{\mathrm{test}}|$.
4. A point charge has $|Q|=2.00\,\mathrm{nC}$. Find $E$ at $r=0.300\,\mathrm m$.
5. A point charge produces $E=900\,\mathrm{N/C}$ at $r=0.200\,\mathrm m$. Find $|Q|$.

## 15. Magnetic field

**Meaning:** These standard results give the magnetic field near a long straight wire, at the center of a circular loop, or inside an ideal long solenoid in vacuum.

$$
B_{\mathrm{wire}}=\frac{\mu_0I}{2\pi r},\qquad
B_{\mathrm{loop}}=\frac{\mu_0NI}{2R},\qquad
B_{\mathrm{solenoid}}=\mu_0nI
$$

$r$ is distance from a straight wire; $R$ is loop radius; $n$ is turns per meter. Ignore end effects for the solenoid.

1. Long straight wire: $I=5.00\,\mathrm A$ and $r=0.100\,\mathrm m$. Find $B$.
2. Long straight wire: $B=2.00\times10^{-5}\,\mathrm T$ and $r=0.0500\,\mathrm m$. Find $I$.
3. Long straight wire: $B=4.00\times10^{-6}\,\mathrm T$ and $I=2.00\,\mathrm A$. Find $r$.
4. Circular loop center: $N=1$, $I=2.00\,\mathrm A$, and $R=0.100\,\mathrm m$. Find $B$.
5. Ideal long solenoid: $n=1000\,\mathrm{m^{-1}}$ and $I=2.00\,\mathrm A$. Find $B$.

## 16. Capacitance

**Meaning:** Capacitance is stored charge per potential difference. For an ideal vacuum parallel-plate capacitor, it depends on plate area and separation.

$$
C=\frac{Q}{V},\qquad C=\frac{\epsilon_0A}{d}
$$

Here $Q$ is the magnitude of charge on either plate, $V$ is the voltage magnitude between plates, and $d$ is plate separation. Ignore fringing in the plate formula.

1. $Q=12.0\,\mu\mathrm C$ and $V=6.00\,\mathrm V$. Find $C$.
2. $C=5.00\,\mu\mathrm F$ and $V=10.0\,\mathrm V$. Find $Q$.
3. $Q=24.0\,\mu\mathrm C$ and $C=3.00\,\mu\mathrm F$. Find $V$.
4. Vacuum parallel plates: $A=0.0200\,\mathrm{m^2}$ and $d=0.00100\,\mathrm m$. Find $C$.
5. Vacuum parallel plates: $C=8.85\times10^{-11}\,\mathrm F$ and $d=0.00200\,\mathrm m$. Find $A$.

## 17. Current

**Meaning:** Current is the rate at which charge flows. Ohm's law relates current, voltage, and resistance in an ohmic resistor.

$$
I=\frac{\Delta Q}{\Delta t}\quad\text{(constant current)},\qquad I=\frac{V}{R}
$$

1. $\Delta Q=12.0\,\mathrm C$ passes in $\Delta t=3.00\,\mathrm s$. Find $I$.
2. $I=0.500\,\mathrm A$ flows for $\Delta t=8.00\,\mathrm s$. Find $\Delta Q$.
3. $\Delta Q=18.0\,\mathrm C$ and $I=3.00\,\mathrm A$. Find $\Delta t$.
4. Resistor: $V=12.0\,\mathrm V$ and $R=6.00\,\Omega$. Find $I$.
5. Resistor: $V=9.00\,\mathrm V$ and $I=0.300\,\mathrm A$. Find $R$.

## 18. Charge

**Meaning:** Charge comes in integer multiples of the elementary charge; current transfers charge over time.

$$
|Q|=Ne,\qquad Q_{\mathrm{electrons}}=-Ne,\qquad \Delta Q=I\Delta t
$$

Here $N$ is the number of elementary charges or excess electrons, as specified. Use constant current for charge-transfer questions.

1. An object has $N=5.00\times10^{12}$ excess electrons. Find its signed charge $Q$.
2. A collection of protons has $Q=+4.80\times10^{-7}\,\mathrm C$. Find the number of protons $N$.
3. An object has $Q=-8.00\times10^{-9}\,\mathrm C$ from excess electrons. Find their number $N$.
4. $I=2.00\,\mathrm A$ flows for $\Delta t=5.00\,\mathrm s$. Find the magnitude of charge transferred.
5. $\Delta Q=15.0\,\mathrm C$ is transferred in $\Delta t=3.00\,\mathrm s$. Find $I$.

## 19. Electric potential

**Meaning:** A point charge produces electric potential; potential also measures potential energy per charge.

$$
V=k\frac{Q}{r},\qquad V=\frac{U}{q}
$$

For the point-charge formula, take $V=0$ at infinity. Signs of charge, potential, and energy matter.

1. A point charge has $Q=+2.00\,\mathrm{nC}$. Find $V$ at $r=0.300\,\mathrm m$.
2. A point charge produces $V=+180\,\mathrm V$ at $r=0.200\,\mathrm m$. Find $Q$.
3. A point charge has $Q=+5.00\,\mathrm{nC}$ and produces $V=+150\,\mathrm V$. Find $r$.
4. A charge has $U=0.0120\,\mathrm J$ and $q=+3.00\,\mu\mathrm C$. Find $V$.
5. A point charge has $Q=-4.00\,\mathrm{nC}$. Find $V$ at $r=0.200\,\mathrm m$.

## 20. Electric potential energy

**Meaning:** Potential energy depends on charge and potential. A pair of point charges has interaction energy that depends on their separation.

$$
U=qV,\qquad U=k\frac{q_1q_2}{r}
$$

For the two-charge formula, take $U=0$ at infinite separation. In $U=qV$, $V$ is the potential produced by other charges.

1. $q=+2.00\,\mu\mathrm C$ and $V=+300\,\mathrm V$. Find $U$.
2. $U=0.00400\,\mathrm J$ and $q=+5.00\,\mu\mathrm C$. Find $V$.
3. $U=-0.00120\,\mathrm J$ and $V=+400\,\mathrm V$. Find $q$.
4. $q_1=+2.00\,\mu\mathrm C$, $q_2=+3.00\,\mu\mathrm C$, and $r=0.300\,\mathrm m$. Find $U$.
5. $q_1=+1.00\,\mu\mathrm C$, $q_2=-2.00\,\mu\mathrm C$, and $r=0.200\,\mathrm m$. Find $U$.

## 21. Inductive reactance

**Meaning:** An inductor's opposition to sinusoidal AC increases with frequency.

$$
X_L=\omega L=2\pi fL,\qquad \omega=2\pi f
$$

$X_L$ is in ohms, $L$ in henries, $f$ in hertz, and $\omega$ in radians per second.

1. $f=50.0\,\mathrm{Hz}$ and $L=0.100\,\mathrm H$. Find $X_L$.
2. $\omega=200\,\mathrm{rad/s}$ and $L=0.300\,\mathrm H$. Find $X_L$.
3. $X_L=40.0\,\Omega$ and $\omega=100\,\mathrm{rad/s}$. Find $L$.
4. $X_L=50.0\,\Omega$ and $L=0.250\,\mathrm H$. Find $\omega$.
5. $X_L=20\pi\,\Omega$ and $L=0.200\,\mathrm H$. Find $f$.

## 22. Capacitive reactance

**Meaning:** A capacitor's opposition to sinusoidal AC decreases with frequency. This section interprets your “inductive capacitance” entry as capacitive reactance.

$$
X_C=\frac{1}{\omega C}=\frac{1}{2\pi fC}
$$

$X_C$ is the positive reactance magnitude in ohms; the capacitor contributes the negative term in $X_L-X_C$.

1. $\omega=1000\,\mathrm{rad/s}$ and $C=10.0\,\mu\mathrm F$. Find $X_C$.
2. $X_C=200\,\Omega$ and $\omega=500\,\mathrm{rad/s}$. Find $C$.
3. $X_C=50.0\,\Omega$ and $C=20.0\,\mu\mathrm F$. Find $\omega$.
4. $f=50.0\,\mathrm{Hz}$ and $C=100\,\mu\mathrm F$. Find $X_C$.
5. $X_C=100\,\Omega$ and $C=10.0\,\mu\mathrm F$. Find $f$.

## 23. RMS current

**Meaning:** RMS current gives the same average resistor heating as an equal DC current.

$$
I_{\mathrm{rms}}=\frac{I_{\mathrm{peak}}}{\sqrt2}
$$

This peak-to-RMS relation assumes a sinusoidal current.

1. $I_{\mathrm{peak}}=10.0\,\mathrm A$. Find $I_{\mathrm{rms}}$.
2. $I_{\mathrm{rms}}=3.00\,\mathrm A$. Find $I_{\mathrm{peak}}$.
3. $I_{\mathrm{peak}}=2\sqrt2\,\mathrm A$. Find $I_{\mathrm{rms}}$.
4. $I_{\mathrm{rms}}=0.500\,\mathrm A$. Find $I_{\mathrm{peak}}$.
5. $I_{\mathrm{peak}}=120\,\mathrm{mA}$. Find $I_{\mathrm{rms}}$ in milliamperes.

## 24. RMS voltage

**Meaning:** RMS voltage gives the same average resistor heating as an equal DC voltage across the same resistor.

$$
V_{\mathrm{rms}}=\frac{V_{\mathrm{peak}}}{\sqrt2}
$$

This peak-to-RMS relation assumes a sinusoidal voltage.

1. $V_{\mathrm{peak}}=100\,\mathrm V$. Find $V_{\mathrm{rms}}$.
2. $V_{\mathrm{rms}}=120\,\mathrm V$. Find $V_{\mathrm{peak}}$.
3. $V_{\mathrm{peak}}=12\sqrt2\,\mathrm V$. Find $V_{\mathrm{rms}}$.
4. $V_{\mathrm{rms}}=5.00\,\mathrm V$. Find $V_{\mathrm{peak}}$.
5. $V_{\mathrm{peak}}=0.800\,\mathrm V$. Find $V_{\mathrm{rms}}$.

## 25. Impedance

**Meaning:** Impedance combines resistance and net reactance in an AC circuit. These formulas use the impedance **magnitude** of a series RLC circuit.

$$
Z=\sqrt{R^2+(X_L-X_C)^2},\qquad
I_{\mathrm{rms}}=\frac{V_{\mathrm{rms}}}{Z}
$$

1. $R=3.00\,\Omega$, $X_L=8.00\,\Omega$, and $X_C=4.00\,\Omega$. Find $Z$.
2. $R=12.0\,\Omega$, $X_L=5.00\,\Omega$, and $X_C=10.0\,\Omega$. Find $Z$.
3. $Z=10.0\,\Omega$, $X_L=10.0\,\Omega$, and $X_C=4.00\,\Omega$. Find $R$.
4. $V_{\mathrm{rms}}=120\,\mathrm V$ and $Z=40.0\,\Omega$. Find $I_{\mathrm{rms}}$.
5. $V_{\mathrm{rms}}=24.0\,\mathrm V$ and $I_{\mathrm{rms}}=2.00\,\mathrm A$. Find $Z$.

## 26. Resonance

**Meaning:** At series RLC resonance, inductive and capacitive reactances cancel, leaving $Z=R$.

$$
X_L=X_C,\qquad \omega_0=\frac{1}{\sqrt{LC}},\qquad
f_0=\frac{1}{2\pi\sqrt{LC}}
$$

1. $L=0.100\,\mathrm H$ and $C=100\,\mu\mathrm F$. Find $f_0$.
2. $L=0.250\,\mathrm H$ and $C=16.0\,\mu\mathrm F$. Find $\omega_0$.
3. $\omega_0=1000\,\mathrm{rad/s}$ and $C=10.0\,\mu\mathrm F$. Find $L$.
4. $\omega_0=200\,\mathrm{rad/s}$ and $L=0.500\,\mathrm H$. Find $C$.
5. At resonance, $X_L=80.0\,\Omega$. Find $X_C$.

## 27. Magnetic force equals centripetal force

**Meaning:** When velocity is perpendicular to a uniform magnetic field and magnetic force is the only force, a nonrelativistic charged particle follows a circular path.

$$
|q|vB=\frac{mv^2}{r},\qquad r=\frac{mv}{|q|B}
$$

All five questions assume these conditions and nonzero speed.

1. $m=2.00\times10^{-6}\,\mathrm{kg}$, $v=3.00\,\mathrm{m/s}$, $|q|=4.00\,\mu\mathrm C$, and $B=0.500\,\mathrm T$. Find $r$.
2. $r=0.200\,\mathrm m$, $|q|=2.00\,\mu\mathrm C$, $B=0.500\,\mathrm T$, and $m=1.00\times10^{-6}\,\mathrm{kg}$. Find $v$.
3. $m=3.00\times10^{-6}\,\mathrm{kg}$, $v=2.00\,\mathrm{m/s}$, $|q|=4.00\,\mu\mathrm C$, and $r=0.500\,\mathrm m$. Find $B$.
4. $r=0.400\,\mathrm m$, $|q|=5.00\,\mu\mathrm C$, $B=0.200\,\mathrm T$, and $v=2.00\,\mathrm{m/s}$. Find $m$.
5. $m=1.00\times10^{-6}\,\mathrm{kg}$, $v=4.00\,\mathrm{m/s}$, $B=0.500\,\mathrm T$, and $r=2.00\,\mathrm m$. Find $|q|$.

## 28. The $ILB\sin\theta$ formula: force on a straight wire

**Meaning:** This is the magnetic force on a straight wire segment carrying current in a uniform magnetic field.

$$
\mathbf F=I\mathbf L\times\mathbf B,\qquad F=ILB\sin\theta
$$

$L$ is the length of the segment in the field; $\theta$ is the angle between the conventional current direction and $\mathbf B$. This repeats the force relation from section 10 so you can practice it separately.

1. $I=4.00\,\mathrm A$, $L=0.500\,\mathrm m$, $B=0.200\,\mathrm T$, and $\theta=90^\circ$. Find $F$.
2. $F=0.600\,\mathrm N$, $L=0.300\,\mathrm m$, $B=0.500\,\mathrm T$, and $\theta=90^\circ$. Find $I$.
3. $F=0.120\,\mathrm N$, $I=3.00\,\mathrm A$, $B=0.200\,\mathrm T$, and $\theta=90^\circ$. Find $L$.
4. $F=0.150\,\mathrm N$, $I=2.00\,\mathrm A$, $L=0.300\,\mathrm m$, and $\theta=30^\circ$. Find $B$.
5. $I=5.00\,\mathrm A$, $L=0.400\,\mathrm m$, $B=0.300\,\mathrm T$, and $\theta=30^\circ$. Find $F$.

---

# Answer key

Answers follow the same section and question numbers. The rearranged relations below show which quantity each exercise isolates.

## Answers 1: Gauss's law for electricity

1. $\Phi_E=Q_{\mathrm{enc}}/\epsilon_0=1.00\,\mathrm{N\,m^2/C}$.
2. $Q_{\mathrm{enc}}=\epsilon_0\Phi_E=3.54\times10^{-11}\,\mathrm C$.
3. $\Phi_E=Q_{\mathrm{enc}}/\epsilon_0=-2.00\,\mathrm{N\,m^2/C}$.
4. $Q_{\mathrm{enc}}=\epsilon_0(0)=0\,\mathrm C$. Zero net enclosed charge does not require every individual charge inside to be zero.
5. $Q_{\mathrm{enc}}=\epsilon_0\Phi_E=-4.43\times10^{-11}\,\mathrm C$.

## Answers 2: Gauss's law for magnetism

1. $\Phi_2=-6.00\,\mathrm{mWb}$.
2. $\Phi_3=-(3.00-8.00)=+5.00\,\mathrm{mWb}$.
3. $\Phi_4=-(4.00+2.00-1.00)=-5.00\,\mathrm{mWb}$.
4. $\Phi_2=+0.0200\,\mathrm{Wb}$.
5. $\Phi_{B,\mathrm{net}}=0\,\mathrm{Wb}$. Closed-surface magnetic flux is zero regardless of field strength.

## Answers 3: Faraday's law

1. $\mathcal E=-N\Delta\Phi_B/\Delta t=-0.300\,\mathrm V$.
2. $\mathcal E=-N\Delta\Phi_B/\Delta t=+0.400\,\mathrm V$.
3. $\Delta\Phi_B=-\mathcal E\Delta t/N=+0.0500\,\mathrm{Wb}$.
4. $\Delta t=-N\Delta\Phi_B/\mathcal E=0.200\,\mathrm s$.
5. $N=-\mathcal E\Delta t/\Delta\Phi_B=20$ turns.

## Answers 4: Ampère–Maxwell law

1. $\mathcal C_B=\mu_0I_{\mathrm{enc}}=12\pi\times10^{-7}\,\mathrm{T\,m}\approx3.77\times10^{-6}\,\mathrm{T\,m}$.
2. $I_{\mathrm{enc}}=\mathcal C_B/\mu_0=2.00\,\mathrm A$.
3. $I_d=\epsilon_0\,d\Phi_E/dt=1.77\,\mathrm A$.
4. $d\Phi_E/dt=I_d/\epsilon_0=1.00\times10^{11}\,\mathrm{N\,m^2/(C\,s)}$.
5. $I_d=\mathcal C_B/\mu_0-I_{\mathrm{enc}}=3.00\,\mathrm A$.

## Answers 5: Biot–Savart law

1. $dB=2.00\times10^{-8}\,\mathrm T$.
2. $I=4\pi r^2dB/(\mu_0d\ell\sin\theta)=4.00\,\mathrm A$.
3. $d\ell=4\pi r^2dB/(\mu_0I\sin\theta)=1.00\times10^{-3}\,\mathrm m$.
4. $r=\sqrt{\mu_0I\,d\ell\sin\theta/(4\pi dB)}=0.200\,\mathrm m$.
5. $dB=3.00\times10^{-8}\,\mathrm T$.

## Answers 6: Magnetic force on a moving charge

1. $F_B=3.00\times10^{-4}\,\mathrm N$.
2. $|q|=F_B/(vB\sin\theta)=6.00\,\mu\mathrm C$.
3. $v=F_B/(|q|B\sin\theta)=2000\,\mathrm{m/s}$.
4. $B=F_B/(|q|v\sin\theta)=0.500\,\mathrm T$.
5. $F_B=1.00\times10^{-3}\,\mathrm N$.

## Answers 7: Electric dipole moment

1. $p=qd=6.00\times10^{-8}\,\mathrm{C\,m}$.
2. $q=p/d=4.00\,\mu\mathrm C$.
3. $d=p/q=0.0300\,\mathrm m$.
4. $p=qd=3.00\times10^{-10}\,\mathrm{C\,m}$.
5. $d=p/q=0.200\,\mathrm m$.

## Answers 8: Time constant

1. $\tau=RC=0.0100\,\mathrm s$.
2. $R=\tau/C=3000\,\Omega$.
3. $C=\tau/R=5.00\,\mu\mathrm F$.
4. $\tau=L/R=0.0200\,\mathrm s$.
5. $L=\tau R=0.800\,\mathrm H$.

## Answers 9: Magnetic dipole moment

1. $\mu=NIA=0.0600\,\mathrm{A\,m^2}$.
2. $I=\mu/(NA)=4.00\,\mathrm A$.
3. $A=\mu/(NI)=0.0150\,\mathrm{m^2}$.
4. $N=\mu/(IA)=20$ turns.
5. $\mu=NIA=0.100\,\mathrm{A\,m^2}$.

## Answers 10: Torque and force

1. $F=ILB\sin\alpha=0.300\,\mathrm N$.
2. $\tau=NIAB\sin\theta=0.300\,\mathrm{N\,m}$.
3. $I=\tau/(NAB\sin\theta)=2.00\,\mathrm A$.
4. $A=\tau/(NIB\sin\theta)=0.0100\,\mathrm{m^2}$.
5. $B=\tau/(\mu\sin\theta)=0.400\,\mathrm T$.

## Answers 11: Electric flux

1. $\Phi_E=EA\cos\theta=60.0\,\mathrm{N\,m^2/C}$.
2. $E=\Phi_E/(A\cos\theta)=200\,\mathrm{N/C}$.
3. $A=\Phi_E/(E\cos\theta)=0.300\,\mathrm{m^2}$.
4. $\Phi_E=50.0\,\mathrm{N\,m^2/C}$.
5. $\Phi_E=0\,\mathrm{N\,m^2/C}$ because $\cos90^\circ=0$.

## Answers 12: Magnetic flux

1. $\Phi_B=BA\cos\theta=0.0800\,\mathrm{Wb}$.
2. $B=\Phi_B/(A\cos\theta)=0.300\,\mathrm T$.
3. $A=\Phi_B/(B\cos\theta)=0.0800\,\mathrm{m^2}$.
4. $\Phi_B=0.0150\,\mathrm{Wb}$.
5. $\Phi_B=0\,\mathrm{Wb}$ because $\cos90^\circ=0$.

## Answers 13: Electric force

1. $F=k|q_1q_2|/r^2=0.600\,\mathrm N$.
2. $|q_1|=Fr^2/(k|q_2|)=1.00\,\mu\mathrm C$.
3. $|q_2|=Fr^2/(k|q_1|)=4.00\,\mu\mathrm C$.
4. $r=\sqrt{k|q_1q_2|/F}=0.200\,\mathrm m$.
5. $F=0.360\,\mathrm N$; the force is attractive.

## Answers 14: Electric field

1. $E=F/|q_{\mathrm{test}}|=3000\,\mathrm{N/C}$.
2. $F=|q_{\mathrm{test}}|E=0.00200\,\mathrm N$.
3. $|q_{\mathrm{test}}|=F/E=4.00\,\mu\mathrm C$.
4. $E=k|Q|/r^2=200\,\mathrm{N/C}$.
5. $|Q|=Er^2/k=4.00\,\mathrm{nC}$.

## Answers 15: Magnetic field

1. $B=\mu_0I/(2\pi r)=1.00\times10^{-5}\,\mathrm T$.
2. $I=2\pi rB/\mu_0=5.00\,\mathrm A$.
3. $r=\mu_0I/(2\pi B)=0.100\,\mathrm m$.
4. $B=\mu_0NI/(2R)=4\pi\times10^{-6}\,\mathrm T\approx1.26\times10^{-5}\,\mathrm T$.
5. $B=\mu_0nI=8\pi\times10^{-4}\,\mathrm T\approx2.51\times10^{-3}\,\mathrm T$.

## Answers 16: Capacitance

1. $C=Q/V=2.00\,\mu\mathrm F$.
2. $Q=CV=50.0\,\mu\mathrm C$.
3. $V=Q/C=8.00\,\mathrm V$.
4. $C=\epsilon_0A/d=1.77\times10^{-10}\,\mathrm F=177\,\mathrm{pF}$.
5. $A=Cd/\epsilon_0=0.0200\,\mathrm{m^2}$.

## Answers 17: Current

1. $I=\Delta Q/\Delta t=4.00\,\mathrm A$.
2. $\Delta Q=I\Delta t=4.00\,\mathrm C$.
3. $\Delta t=\Delta Q/I=6.00\,\mathrm s$.
4. $I=V/R=2.00\,\mathrm A$.
5. $R=V/I=30.0\,\Omega$.

## Answers 18: Charge

1. $Q=-Ne=-8.00\times10^{-7}\,\mathrm C$.
2. $N=Q/e=3.00\times10^{12}$ protons.
3. $N=|Q|/e=5.00\times10^{10}$ excess electrons.
4. $\Delta Q=I\Delta t=10.0\,\mathrm C$.
5. $I=\Delta Q/\Delta t=5.00\,\mathrm A$.

## Answers 19: Electric potential

1. $V=kQ/r=+60.0\,\mathrm V$.
2. $Q=Vr/k=+4.00\,\mathrm{nC}$.
3. $r=kQ/V=0.300\,\mathrm m$.
4. $V=U/q=+4000\,\mathrm V$.
5. $V=kQ/r=-180\,\mathrm V$.

## Answers 20: Electric potential energy

1. $U=qV=+6.00\times10^{-4}\,\mathrm J$.
2. $V=U/q=+800\,\mathrm V$.
3. $q=U/V=-3.00\,\mu\mathrm C$.
4. $U=kq_1q_2/r=+0.180\,\mathrm J$.
5. $U=kq_1q_2/r=-0.0900\,\mathrm J$.

## Answers 21: Inductive reactance

1. $X_L=2\pi fL=10\pi\,\Omega\approx31.4\,\Omega$.
2. $X_L=\omega L=60.0\,\Omega$.
3. $L=X_L/\omega=0.400\,\mathrm H$.
4. $\omega=X_L/L=200\,\mathrm{rad/s}$.
5. $f=X_L/(2\pi L)=50.0\,\mathrm{Hz}$.

## Answers 22: Capacitive reactance

1. $X_C=1/(\omega C)=100\,\Omega$.
2. $C=1/(\omega X_C)=10.0\,\mu\mathrm F$.
3. $\omega=1/(X_CC)=1000\,\mathrm{rad/s}$.
4. $X_C=1/(2\pi fC)=31.8\,\Omega$.
5. $f=1/(2\pi X_CC)=159\,\mathrm{Hz}$.

## Answers 23: RMS current

1. $I_{\mathrm{rms}}=I_{\mathrm{peak}}/\sqrt2=7.07\,\mathrm A$.
2. $I_{\mathrm{peak}}=\sqrt2 I_{\mathrm{rms}}=4.24\,\mathrm A$.
3. $I_{\mathrm{rms}}=2.00\,\mathrm A$.
4. $I_{\mathrm{peak}}=0.707\,\mathrm A$.
5. $I_{\mathrm{rms}}=84.9\,\mathrm{mA}$.

## Answers 24: RMS voltage

1. $V_{\mathrm{rms}}=V_{\mathrm{peak}}/\sqrt2=70.7\,\mathrm V$.
2. $V_{\mathrm{peak}}=\sqrt2 V_{\mathrm{rms}}=170\,\mathrm V$.
3. $V_{\mathrm{rms}}=12.0\,\mathrm V$.
4. $V_{\mathrm{peak}}=7.07\,\mathrm V$.
5. $V_{\mathrm{rms}}=0.566\,\mathrm V$.

## Answers 25: Impedance

1. $Z=\sqrt{3^2+(8-4)^2}=5.00\,\Omega$.
2. $Z=\sqrt{12^2+(5-10)^2}=13.0\,\Omega$.
3. $R=\sqrt{Z^2-(X_L-X_C)^2}=8.00\,\Omega$.
4. $I_{\mathrm{rms}}=V_{\mathrm{rms}}/Z=3.00\,\mathrm A$.
5. $Z=V_{\mathrm{rms}}/I_{\mathrm{rms}}=12.0\,\Omega$.

## Answers 26: Resonance

1. $f_0=1/(2\pi\sqrt{LC})=50.3\,\mathrm{Hz}$.
2. $\omega_0=1/\sqrt{LC}=500\,\mathrm{rad/s}$.
3. $L=1/(\omega_0^2C)=0.100\,\mathrm H$.
4. $C=1/(\omega_0^2L)=50.0\,\mu\mathrm F$.
5. $X_C=X_L=80.0\,\Omega$.

## Answers 27: Magnetic force equals centripetal force

1. $r=mv/(|q|B)=3.00\,\mathrm m$.
2. $v=r|q|B/m=0.200\,\mathrm{m/s}$.
3. $B=mv/(|q|r)=3.00\,\mathrm T$.
4. $m=r|q|B/v=2.00\times10^{-7}\,\mathrm{kg}$.
5. $|q|=mv/(Br)=4.00\,\mu\mathrm C$.

## Answers 28: Force on a straight wire

1. $F=ILB\sin\theta=0.400\,\mathrm N$.
2. $I=F/(LB\sin\theta)=4.00\,\mathrm A$.
3. $L=F/(IB\sin\theta)=0.200\,\mathrm m$.
4. $B=F/(IL\sin\theta)=0.500\,\mathrm T$.
5. $F=ILB\sin\theta=0.300\,\mathrm N$.
