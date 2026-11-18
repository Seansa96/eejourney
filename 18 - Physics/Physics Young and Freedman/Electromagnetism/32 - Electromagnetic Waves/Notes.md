# Maxwell's Equations and Electromagnetic Waves

Importantly, our previous studies concerned fields that don't vary with time, only space.  This is so we can analyze just the independent field in question without considering any interactions between them.

But we see that when we DO allow these to vary in time, then we must account for these interactions, because by definition they are no longer independent. **Farday's Law** told us that a time-varying magnetic field acts like a source of an electric field (it is said to induce a circulating electric field). Similarly, Ampere-Maxwell's Law tells us that a changing electric field acts like a source for a magnetic field (remember that Maxwell's displacement current is included here).

So when *either* an electric or a magnetic field changes with time, then a field of the other kind is induced in an adjacent region of space.  So what do we call this? Likely, the propagation of a disturbance in a unified electromagnetic field. But we already have a way to express the propagation of a disturbance in some medium, that being a wave! 

Thus,


> [!textbook]
> The propagation of a disturbance in the time-varying electromagnetic field is an electromagnetic wave.

Note that in terms of an actual, physical medium--none is needed. Electromagnetic waves can and may propagate through vacuum.

## Electricity, Magnetism, and Light

Maxwell was the pioneer of this front. Though he is not solely responsible for all of the discoveries, he was the first to formalize them and interpret their greater meaning. He saw that if electromagnetic disturbances can propagate through space, then they should do so with a speed equal to that of light, implying that light waves themselves were electromagnetic.

The principles of electromagnetism can be summed in his equations, which we studied previously:

1. Gauss's Law for Electric Fields - Electric field lines begin and end on charges of opposite signs.
2. Gauss's Law for Magnetic Fields - Magnetic monopoles do not exist because magnetic field lines are a closed loop, terminating on themselves.
3. Ampere's Law - A changing magnetic field induces a circulating electric field.
4. Faraday's Law - A changing electric field induces a circulating magnetic field.

These apply specifically only to vacuum. If a material is present, then the permittivity $\epsilon_0$ and $\mu_0$ permeability of free space are replaced by the permittivity and permeability of that material. If the values of these are different at different points throughout, then we must also integrate these variables and thus they need be transferred to the left side of the equations within the integrand.

Maxwell's equations tell us that a point charge at rest produces a static $\vec E$ field but no $\vec B$ field; a point charge moving with a constant velocity produces both fields. These equations when manipulated, also show and tell us that electromagnetic waves are produced when a point charge accelerates.

In fact, we see that in general, every accelerated charge radiates electromagnetic energy.

## Generating Electromagnetic Radiation

One way to accelerate a point charge is through simple harmonic motion, where it accelerates at every instant except at the equilibrium. *Why can't it do this with constant velocity?*

Field lines are not material objects, but we can imagine them like a piece of string that we oscillate up and down. Doing so makes waves that propagate outward from the charge along these "strings". Note that the charge doesn't emit these waves equally in all directions, as the waves are strongest at $90 \degree$ to the motion of the charge. This is while there are *no* waves along this axis. *What does this mean? Need geometric visualization*

![[Pasted image 20261027145531.png]]
This is just what the "string" picture would lead you to conclude. There is also a magnetic disturbance that radiates outward from the charge. Because both have this "radiating" behavior, electromagnetic waves are also interchangeable with **electromagnetic radiation**.

They were first produced by [[Heinrich Hertz]], who confirmed Maxwell's theory in a groundbreaking experiment in his laboratory in 1887.

For his source of waves, he used the charges oscillating in an LC circuit. He detected the waves with other circuits tuned to the same frequency. *Why did this work? Because they interfered constructively, being in phase?*

He also produced standing electromagnetic waves and measured the distance between adjacent nodes (one half-wavelength) to determine the wavelength. Since he knew the resonant frequency of his circuits, he found the speed of the waves from the wavelength-frequency relationship, $v=\lambda f$. This allowed him to establish that their speed was equal to that of light, which verified Maxwell's predictions directly. The SI unit of frequency is Hertz in his honor.

We find that the modern value of the speed of light is exactly 

$$
299,792,458 \frac{m}{s}
$$
One meter is defined to be the distance that light travels in the above value as a fraction. $c=3.0 \times 10^8$ is sufficient however for most purposes.

Hertz did not immediately see the use of his discovery, that being left to Marconi and other inventors. In such a radio **transmitter**, electric charges oscillate along the length of the antenna, a conducting material, and these field disturbances propagate like we see in the figure above. Since these charges oscillate together, their disturbances are far greater than that of a single charge, and can be detected at much greater distances.

In a radio **receiver**, the antenna is also a conductor. The fields of the waves from the distant transmitter exert forces on the free charges within the receiver antenna, which produces an oscillating current that is detected and then amplified by the receiver circuitry. *Does the frequency determine how the receiver translates this induced emf in the receiver?*

## The Electromagnetic Spectrum

This encompasses waves of all frequencies and wavelengths.  Despite the differences in their uses and means of production, they all have the same propagation speed (in vacuum) of $c$. They may differ in frequency $f$ and wavelength $\lambda$, but the relationship $c=\lambda f$ holds for each (in vacuum).

Our sight can only detect a small segment of this spectrum, called **visible light**. This ranges from about $380$ to $750$ nm, with frequencies of $790 to 400$ THz. Different parts of the spectrum evoke in humans the sensations of different colors.

| Color | Approximate wavelength $\lambda$ (nm) |
| --- | --- |
| Violet | 380–450 |
| Blue | 450–495 |
| Green | 495–570 |
| Yellow | 570–590 |
| Orange | 590–620 |
| Red | 620–750 |

These boundaries are approximate; the colors blend continuously into one another. Wavelength increases from violet to red, while frequency decreases according to $f=c/\lambda$. Recall that $1\text{ nm}=10^{-9}\text{ m}$.

Ordinary white light includes all the visible wavelengths. By using special sources or filters, we can select a narrow band of wavelengths within the range of a few nanometers. Such light is called *monochromatic*., or single-color, light.  We cannot obtain absolutely monochromatic light, of course, as this is just an idealization.  So expressions such as "monochromatic light with $\lambda = 550nm$", this really just means a small band about that value.

![[Pasted image 20261027151509.png]]

Light from a laser is much closer to this idea of monochromatic than light obtainable any other way.

However, even those forms of electromagnetic radiation which are not visible are vitally important to understand.  Global communication for example depends on radio waves: AM uses waves with frequencies from $5.4 \times 10^5$ Hz to $1.6 \times 10^6$ Hz, while FM radio broadcasts are at frequencies from $8.8 \times 10^7$ Hz to $1.08 \times 10^8$ Hz. Television broadcasts often use frequencies that bracket the FM band.

Microwaves also are used for communication, like by cellular phones and wireless networks, and for weather radars, around $3 \times 10^9$ Hz. Many cameras also have a device that can emit a beam of infrared radiation. By analyzing the properties of the waves reflected from the subject, the camera can determine the distance to the subject an automatically adjust the focus.  X rays can penetrate through flesh but not as deeply through bone, which is why scans with them reveal skeletal structures. Gamma rays, the shortest and highest energy wavelengths, are often used in chemotherapy to destroy cancer cells.

### Test Your Understanding 32.1

Is it possible to have a purely electric wave propagate through empty space? What about a purely magnetic wave?

*Both shouldn't be possible if time is relevant, but if only space/position is relevant, then it is possible.*. 


# Plane Electromagnetic Waves and the Speed of Light

We will assume a model where an $\vec E$ field has only a y-component and a magnetic field $\vec B$ only has a z-component.  We will assume that both fields move together in the positive-x direction with a speed $c$ that is initially unknown.  

![[Pasted image 20261027152301.png]]


# Sinusoidal Electromagnetic Waves

# Energy and Momentum in Electromagnetic Waves

# Standing Electromagnetic Waves

