# Terms
Alternating Current

Phasors

Phasor Diagrams


# Equations


# Phasors and Alternating Currents

Alternating Current is defined as sinusoidally varying voltages and currents. Transformers utilize this to step the voltage up and down with AC but not with DC, because high voltages and low currents are best for long-distance power transmission to minimize $i^2 R$ losses in cables.

For an alternating current to be supplied to a circuit, a source of alternating EMF or voltage is required. This would be a coil of wire rotating with constant angular velocity in a magnetic field.  This is the foundation for the commercial alternating-current generator known as an alternator.

We use the term AC source for any device that supplies a sinusoidally varying voltage $v$ or current $i$. The image for this is

![[Pasted image 20261013151937.png]]

This voltage is described by the function

$$
v = V\cos(\omega t)
$$
Where $v$ is the instantaneous potential difference, $V$ is the maximum potential difference (called the **Voltage Amplitude**) and $w$ is the *angular frequency*, which is equal to $2\pi$ times the frequency *f*. 

In the US and Canada, commercial electric-power distribution systems use a frequency of $60Hz$ which corresponds to $120\pi$ rads/s while the rest of the world largely uses $50Hz$. 

A sinusoidal current can be described as:

$$
i=I\cos(\omega t)
$$
Where i is the instantaneous current and $l$ is the maximum current or current amplitude.

## Phasor Diagrams

To represent these voltages and currents, we use rotating vector diagrams, where the instantaneous value of a quantity which varies with time is represented by the projection onto a horizontal axis of a vector with a length equal to its amplitude.

The vector rotates counterclockwise with constant angular speed, $w$. This is called a phasor, and diagrams containing them are phasor diagrams.

![[Pasted image 20261013153207.png]]

Note that a phasor is not a real physical quantity. It is a geometric entity that helps describe and analyze quantities that vary sinusoidally with time.

## Rectified Alternating Current

A d'Arsonval galvanometer is used to measure steady current, but passing a sinusoidal current through such a meter is fruitless since it operates on the deflection due to the magnetic field, and as the current is reversing sign with time, the average deflection cancels out to zero.

The needle may wiggle at low enough frequencies, but again, that average deflection will be zero.  To get a measurable current through that meter, we need a *diode*. This is a device that conducts better in one direction that the other; an ideal diode has zero resistance for one direction of current and infinite resistance for the other.

![[Pasted image 20261013153836.png]]

Because the diode only allows current to pass in one direction, it can be used to control the flow of current though the sign of it alternates.

The **G** represents the position of the **Galvanometer**, and because it lies where the current can only go in one direction, regardless of its source, then the average deflection cannot be zero.

Current restrained in this way is said to be **rectified**, and thus it measures the **rectified average current**
$$
I_{rav}
$$
which is defined so that during any whole number of cycles, the total charge that flows is the same as though the current were constant with a value equal to $I_rav$. 

Note that this is NOT the average of the original sinusoidal current. The total charge that flows in time $t$ corresponds to the expression
$$
i=\frac{dq}{dt}
$$
, the instantaneous current, integrated over some interval of time. Thus, the area under the curve of i vs t gives us the total charge, which the area of must equal the rectangular area with height $I_rav$. But $I_rav$ is less than the maximum current, so the two are related by

$$
I_{rav} = \frac{2}{\pi}I = 0.637I
$$
The factor of $2/\pi$ is the average value of $cos(\omega t)$ or of $sin(\omega t)$. The galvanometer deflection is proportional to the rectified current's average. Such a meter can be calibrated to read $I$, $I_rav$, or $I_rms$.

## Root-Mean-Square Values

A useful way to describe a quantity that can be either positive or negative is the **root-mean-square value**, (rms). By squaring the instantaneous current $i$, and taking its average, then square rooting that average, we get the RMS current, denoted as $I_{rms}$. 

Even when $i$ is negative, $i^2$ is always positive, so the $I_{rms}$ can never be negative or 0, except when the current is 0.

For the earlier expression of instantaneous current, its RMS is

![[Pasted image 20261013155446.png]]

We can derive a similar expression for an RMS voltage:

$$
V_{r m s}=\frac{V}{\sqrt{ 2 }}
$$
Converting a rectifying ammeter into a voltmeter is done by adding a series resistor. Voltages and currents in power distribution systems are always described in terms of their RMS values. The voltage amplitude (recall, maximum) for a 120-V AC power supply is 170V.


# Resistance and Reactance

For a resistor in an AC circuit, with resistance $R$, there is a counterclockwise current in the positive direction, and the current amplitude is given by $I$. From Ohm's Law, the instantaneous potential $V_R$ of point $a$ with respect to point $b$ across the resistor is

$$
V_{R}=IR\cos(\omega t)
$$

![[Pasted image 20261013161116.png]]

The maximum voltage or the voltage amplitude is the coefficient of the cosine function, or $V=IR$.

So an expression sometimes used is:

$$
v_{r}=V_{R}\cos(\omega t)
$$
where $v_r$ is the voltage drop across the resistor and $V_R$ is the voltage amplitude.

Current and voltage are both proportional to the cosine function, so the current is said to be **in phase** with the voltage.

![[Pasted image 20261013161350.png]]

Because they are in phase, their phasors rotate together and are thus parallel at any instant. Projection them onto the horizontal axis represent the instantaneous current and voltage respectively.

![[Pasted image 20261013161609.png]]

## Inductor in an AC Circuit

Replacing the resistor with a pure inductor with self-inductance $L$ and zero resistance



# RLC Series Circuit

# Power in Alternating Current Circuits

# Resonance in Alternating Current Circuits

# Transformers

![[Pasted image 20261022152758.png]]

A **transformer** is a passive electrical device that transfers electrical energy between two or more circuits through electromagnetic induction. It can do this through **stepping up** or **stepping down** voltage levels of an AC current, without changing the frequency.

This is significantly more efficient in long distance power transmission due to reducing power losses from resistive heating from higher voltages. It accomplishes this by reducing the resistance that the *source* observes.

This is down through the components of transformers, called *windings*, which are electrically insulated from each other, but wound on the same core.  The core is typically made of a material like iron with a large relative permeability, $K_m$. This orients the magnetic field lines from one winding's current nearly completely within the core, and so all the field lines pass through the other winding which maximizes their mutual inductance.

The winding to which power is supplied to is called the **primary winding**, while the winding in which power is delivered to is the **secondary winding**.  The circuit symbol for a transformer with an iron core is

![[Pasted image 20261022154345.png]]

The AC source causes an AC current in primary winding, which then sets up a changing flux in the core which of course through electromagnetic induction induces an EMF in each winding, just like we would predict from Faraday's Law:

$$
\varepsilon = -\frac{d\Phi_{b}}{dt}
$$

The induced EMF in that secondary winding then gives rise to an alternating current in the secondary, (due to self inductance?), and then this delivers energy to the device to which the secondary is connected.  All currents and EMFs have the same frequency as the AC source, so frequency remains constant.


![[Pasted image 20261022155526.png]]

By choosing an appropriate turns ratio, we can then get any desired secondary voltage from a given primary voltage.

So if 
$$
N_{2} > N_{1}
$$
then our voltage in the secondary goes up, so we have that **step-up** transformer.

Likewise, if

$$
N_{1} > N_{2}
$$
then our voltage in the secondary goes down, so we have a **step-dwon** transformer.

We typically step up for long-line transmission, and then step-down to enter commercial and residential power networks.

This is also what AC adapters do--such as what you use to recharge a mobile phone o laptop computer from line voltage. Even the low voltage used in household wall sockets is too high for many electronic devices, so this adapter contains a step-down transformer to convert the line voltage to a low value like 3-12 volts.

## Energy consideration for Transformers


# Diagrams and Worksheets

