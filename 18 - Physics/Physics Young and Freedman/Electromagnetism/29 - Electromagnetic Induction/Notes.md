# Terms

**Induced Current** - Current produced by the motion of charged particles which produces a changing magnetic field.

**Induced EMF** - The EMF required to cause an Induced Current.
# Induction Experiments

The first is to place two circuits near each other, one with an Inductor. Upon switching the current on in the first circuit, it induces a voltage spike in the other (these are DC Circuits), and when it is switched off, it also induces a voltage spike.

![[Pasted image 20261016140743.png]]

We can also squeeze a coil, jerk it, and generally move in in space at varying speeds.  We see in all cases that the induced EMF is only dependent upon the geometry, speed, and deformation (which decreases cross-sectional area).

# Faraday's Law


![[Pasted image 20261016141441.png]]The common factor in all electromagnetic induction effects is changing magnetic flux through a circuit.

We find that the magnetic flux is similar to the electric flux, in that

$$
d \phi_{B} = \vec B \cdot dA - \vec B \perp dA = \vec B \cos dA
$$
Which states that the magnetic flux is equal to the magnetic field dot some infinitesimal area, which is then the perpendicular component projected onto that surface, which is equal to the magnetic field times the cosine of the angle between the field line through the surfae and the surface itself.

![[Pasted image 20261016141917.png]]

We see here that this visual demonstrates this: when the angle coming out of the face of the surface is parallel to the field line, we achieve maximum flux, whereas when it differs, we have some lesser flux, and when the surface angle is perpendicular to the magnetic field, flux is 0.

![[Pasted image 20261016142353.png]]


Be careful when defining the direction of the vector area $dA$ or $\vec A$. There are always two directions that are perpendicular to a given area, so the sign of the flux depends on which we choose ot be positive.

## Faraday's Law of Induction

This states that:

**THE INDUCED EMF IN A CLOSED LOOP EQUALS THE NEGATIVE OF THE TIME RATE OF CHANGE OF MAGNETIC FLUX THROUGH THE LOOP**

Or:

$$
\mathcal{E} = -\frac{d\Phi_{B}}{dt}
$$
To understand the negative sign, we need to look into **Lenz's Law**.


## Direction of Induced EMF

Guidelines:

1. Define a positive direction for vector area $A$.
2. From that direction, determine the sign of the flux and its rate of change
3. Determine the sign of the induced EMF or current. If flux is increasing, then its positive, so induced EMF or current is negative, and vice versa.
4. Then, use the right hand rule to determine the direction. Curl the fingers of your right hand around the $A$ vector, with your right thumb in the direction of the $A$ vector. If it's positive, its the same direction as your curled fingers.
![[Pasted image 20261016152248.png]]

Induced EMFs are caused by changes in flux. Since magnetic flux plays a critical role in Faraday's Law, it's tempting to think that the flux is the cause of the induced EMF, but its the change in flux through a circuit that causes the induced EMF.

If we have a coil with $N$ identical turns, and the flux varies at the same rate, then the total rate of change through all the turns is going to be $N$ times as large, so the induced EMF through a coal with $N$ turns is

$$
\mathcal{E} = -N\frac{d\Phi_{B}}{dt}
$$
## Generators as Energy Converters

The slidewire generator doesn't produce electric energy out of nowhere; the energy is supplied by whatever body exerts the force that keeps the rod moving.  What the generator does is convert that mechanical energy into a different form.

This equality holds--that being the rate at which the mechanical energy is supplied to the electric energy generated--for all types of generators.

This is true especially for the alternator described in [[18 - Physics/Physics Young and Freedman/Electromagnetism/29 - Electromagnetic Induction/Examples#Example 29.3 - Generator 1 A simple Alternator|Example 29.3]]

Earlier, we claimed that the magnetic force on moving charges can never do work. This holds here. The work done is zero, because the moving charges that make up the current in the rod have a vertical component of velocity, causing a horizontal component of force on these charges.

As a result, there is a horizontal displacement of charge within the rod, the left side acquiring a net positive charge while the right side a net negative charge. The result being a horizontal component of electric field, perpendicular to the length of the road. The field is what does work on the charges in the rod in the direction of the motion of the rod.

# Lenz's Law

This is a convenient alternative method for determining the direction of an induced current or emf. It's not an independent principle and can be derived directly from Faraday's Law. It always gives the same results as the sign rules we introduced in connection with Faraday's Law, but it is often easier to use. It also gives us understanding of various induction effects and the role of energy conservation.

**Lenz's Law states that:**

**THE DIRECTION OF ANY MAGNETIC INDUCTION EFFECT IS SUCH AS TO OPPOSE THE CAUSE OF THE EFFECT**.

The cause could be changing flux through a stationary circuit due to a varying magnetic field, changing flux due to the motion of the conductors that make up the circuit, or any combination. 

If the flux in a stationary circuit changes, then the induced current sets up a magnetic field of its own.

Within the area bounded by the circuit, this field is opposite to the original field if the original field is increasing, but is in the same direction as the original field if the latter is decreasing.

So, the induced current opposes the change in the flux, but not the flux itself.

If the flux change is due to the motion of the conductors, then the direction of the induced current in the moving conductor is such that the direction of the magnetic-field force on the conductor is opposite in direction to its motion.

It can be said then that the induced current tries to preserve the status quoe y opposition motion or changes in flux.

This law directly relates energy conservation. If the induced current is in the direction opposite to that given by Lenz's law, then the magnetic force on the rod would accelerate to ever-increasing speeds without an external energy source, even though the electric energy is being dissipated in the circuit, which would be a violation.

## Lenz's Law and the Response to Flux Changes

So if the induced current always opposes any change in magnetic flux, then how is it possible for the flux to change at all?  This is because this law only gives the *direction* of the induced current. The *magnitude* depends on the resistance of the circuit, following from Ohm's Law.

The greater the circuit resistance, the less the induced current appears to oppose any change in flux and the easier it is for a flux change to take effect.

So if we have an induced effect, it will create a magnetic field in response that opposes the changing magnetic flux, and the resulting current flows in that direction.

# Motional Electromotive Force

The example we use is

![[Pasted image 20261016164733.png]]

A conducting rod is moving with a magnetic field pointing into the page. The motion causes induced EMF in the rod which creates charge separation: at $a$, we have positive charge, and at $b$, we have negative charge. Charge accumulates until the electric force by the field is equal to the magnetic force, or:

$$
qE=qvB
$$
To find the magnitude of the force, we use the differential in potential between the two points or

$$
V_{ab}=V_{a}-V_{b}
$$
and then we multiply it by the rod length, assuming the rod is uniform, so

$$
V_{ab}=EL
$$

But we know that
$$
E=vB
$$
from earlier, so

$$
V_{ab}=vBL
$$
What this then tells us is that as long as velocity is non-zero, the induced EMF will be proportional to the magnetic field magnitude times the length.

Using this by attaching the rod to a stationary U-conductor circuit:

![[Pasted image 20261016165143.png]]

While the rod is moving, it functions like a battery: charge moves from the "terminals" through the circuit since it not functions as an EMF source, in conventional current flow from the positive end towards the negative end, the strength of the current being proportional to how fast the rod is moving.

## Motional EMF: General Form

We can generalize this concept for any shape, moving in any uniform or not magnetic field.

For an element $d\vec l$ of the conductor, the contribution $d\mathcal{E}$ is the magnitude $dl$ multiplied by the component of $\vec v \times \vec B$ parallel to the conductor element $d\vec l$ or:

$$
d\mathcal{E} = (\vec v \times \vec B) \cdot d\vec l
$$
So then for any closed conducting loop, the total emf is

$$
\mathcal{E} = \oint \vec v \times \vec B) \cdot d\vec l
$$
This and Faraday's Law expression for the EMF are equivalent, but when the conductor is stationary, we must use Faraday's expression.
# Induced Electric Fields

So what pushes charges around the circuit in a stationary conductor, exactly?

We see that when we change the magnetic flux, or the rate of change of the flux is nonzero, there is an induced electric field in the conductor.  However, this is different from a regular **electrostatic field**. This is a **nonelectrostatic field**, and the differing factor is that this field is non-conservative. This is because the closed integral around this path is equal to the total work done by the electric field, which is $q$ times this induced EMF, which is nonzero.  

So we say that:

$$
\oint \vec E \cdot d\vec l = \frac{-d \Phi_{B}}{dt}
$$

So, basically a changing magnetic field acts as a source of electric field that is not possible with a static charge distribution, and a changing electric field can act as a source of magnetic field.
# Eddy Currents
![[Pasted image 20261016171602.png]]



In many pieces of electrical equipment, there are masses of metal moving in magnetic fields or located in changing magnetic fields.  In situations like these, we get induced currents that circulate throughout the volume of a material much like the swirling eddies in a river, and so we call them **eddy currents**.

Being induced, these opposite the motion of the force that caused them, typically giving downward components such as in the above, and the return path is given by nearby conducting paths for the charges displaced by the induced effect, resulting in a circulation.

This can be used for practical purposes and also can be unwanted, depending on the application.

Detectors like metal detectors observe the interaction of these eddy currents from a generated or alternating magnetic/electric field. Meters use this same principle to estimate power usage, magnetic heating can be achieved in cases where contamination is not acceptable by the resistive heating caused by the opposition of these eddy currents, and transformers must minimize the effect of these eddy currents by narrowing the size of their return paths.
# Displacement Current and Maxwell's Equations


## Generalizing Ampere's Law

Looking at Ampere's Law

$$
\oint \vec B \cdot d\vec l = \mu_{0}I_{encl}
$$
Or the closed surface integral of the magnitude of the magnetic field is equal to the magnetic constant by the current enclosed in a surface.

We see that this form is incomplete, by analyzing a charging capacitor.

We see that  in the picture below

![[Pasted image 20261016194454.png]]

we have the conduction current $i_c$. We saw earlier that the closed line integral of the surface is equal to the permeability of free space times the current enclosed.


## 1. First, identify the three geometric objects


- The black oval on the left: This is the circular Amperian path, \(C\), around which we calculate the magnetic field's circulation.
    
- The gray plane surface: This is the flat circular surface bounded by that black oval. The conducting wire passes through it.
    
- The gray bulging surface: This is a different, curved surface with the exact same black oval as its boundary. It extends to the right, between the capacitor plates, without intersecting the wire.
    

The yellow disks are the actual capacitor plates, which are separate physical objects.

The two gray surfaces are imaginary mathematical surfaces, not physical objects.

Think of the black circular path as a rigid wire hoop. You could stretch a flat sheet of rubber across it, or you could stretch the rubber into a bulging dome.

Both sheets have the same circular boundary, but they occupy different regions of space.

## 2. Why does Ampère's law give two answers?

The original Ampère's law for steady currents states:

\[ \boxed{\oint_C\vec B\cdot d\vec l=\mu_0 I_{\text{enclosed}}} \]

The left-hand side measures the circulation of the magnetic field around the black circular path.

Crucially, it depends on the path, not on which imaginary surface you choose to span that path.

Now consider the two possible surfaces.

Surface 1: Flat disk

The wire passes through the surface, so the enclosed conduction current is \(i_C\).

Surface 2: Bulging dome

The surface passes through the gap between the plates, where no conduction current crosses it.

For the flat surface:

\[ I_{\text{enclosed}}=i_C \]

Therefore:

\[ \boxed{\oint_C\vec B\cdot d\vec l=\mu_0 i_C} \]

But for the bulging surface:

\[ I_{\text{enclosed}}=0 \]

Therefore, applying the same original equation would give:

\[ \boxed{\oint_C\vec B\cdot d\vec l=0} \]

See the contradiction?

We're integrating the same magnetic field around the same black circular path, yet the equation appears to produce two different answers:

\[ \mu_0 i_C\neq 0 \]

The magnetic field circulation cannot simultaneously equal both quantities.

## 3. Why is this a problem with Ampère's law rather than the surfaces?

Because the original version of Ampère's law was derived for steady currents.

But here, the capacitor is charging, so the electric field between its plates is changing with time.

Maxwell recognized that the original equation was missing a term accounting for that changing electric field.

He introduced what we call the displacement current:

\[ I_D=\varepsilon_0\frac{d\Phi_E}{dt} \]

The corrected Ampère–Maxwell law becomes:

\[ \boxed{\oint_C\vec B\cdot d\vec l =\mu_0\left(I_C+\varepsilon_0\frac{d\Phi_E}{dt}\right)} \]

Now reconsider the two surfaces.

|Quantity|Flat surface|Bulging surface|
|---|---|---|
|Conduction current \(I_C\)|\(i_C\)|\(0\)|
|Displacement current \(I_D\)|\(0\) in the idealized setup|\(i_C\)|
|Total effective current|\(i_C\)|\(i_C\)|
|Magnetic circulation|\(\mu_0 i_C\)|\(\mu_0 i_C\)|

Both surfaces now produce the same answer.

The contradiction disappears.

## 4. What is physically happening between the plates?

The conduction current delivers charge to the capacitor plates.

As charge accumulates, the electric field between the plates increases:

$$E=\frac{Q}{\varepsilon_0 A}$$ 

For ideal parallel plates, the electric flux through the gap is:

$$ \Phi_E=EA=\frac{Q}{\varepsilon_0}$$ 

Differentiate with respect to time:

$$ \varepsilon_0\frac{d\Phi_E}{dt} =\frac{dQ}{dt}$$

But the rate of charge accumulation is precisely the conduction current:

$$ \frac{dQ}{dt}=i_C$$ 

Therefore:

$$ \boxed{I_D=i_C}$$

So the displacement current between the capacitor plates is equal in magnitude to the conduction current in the wires.

This doesn't mean electrons are physically crossing the insulating gap. It means the changing electric field contributes to the magnetic field in the same way that an equivalent current would in Ampère's law.

## 5. The deeper mathematical idea

The point Maxwell was making is that the magnetic field circulation around a closed curve must be independent of which surface we mathematically construct across that curve.

The flat surface and the bulging surface can intersect completely different physical regions, but they share the same boundary.

That's the crucial geometric relationship.

It also connects to the distinction between line integrals and surface integrals that you've been studying in vector calculus:

- The left side, \(\oint_C\vec B\cdot d\vec l\), is a closed line integral around a boundary.
    
- The enclosed conduction current is determined by the current flowing through a surface bounded by that curve.
    
- Maxwell's correction ensures that the law remains consistent regardless of which spanning surface is chosen.
    
So what do we need to understand?

1. Tow things can produce a magnetic field. Movement of electric charges (conduction current), and the displacement current, $I_D$, which is from changing electric flux.
2. Ampere-Maxwell Law $$\oint \vec B \cdot d\vec l = \mu_{0}(I_{c}+I_{d}) $$ and $$I_{d}=\varepsilon_{0}\frac{d\Phi_{E}}{dt}$$
3. Calculating displacement current: For a uniform electric field perpendicular to a constant area: $$\Phi_{E}=EA, \qquad I_{D}=\varepsilon_{0}A\frac{d\Phi_{E}}{dt} $$ Also note that for an ideal charging capacitor, $I_D=I_C$. 
4. Understand why Maxwell introduced it. He did this because of the contradiction of the integral both equating to $\mu_0I_{encl}$ and zero, which made no sense. This mixing term fixed the expression and made obvious the intertwining of the electric field and the magnetic field.

## Maxwell's Equations

While the equations themselves in simplified form are utilized for solving situations, let's explore what they're really saying:


Gauss's Law for electric flux states that electric charges produce electric fields.

For magnetic fields, Gauss's Law simply states they have no beginning or end and because the flux in equals flux out.

Ampere's and Faraday's Laws shows us as we have seen that a changing magnetic field produces a circulating electric field, and a changing electric field also produces circulating magnetic fields.

The symmetry of Ampere's and Faraday's Laws in particular explain how electromagnetic waves are able to propagate through space.

![[Pasted image 20261019201005.png]]
# Superconductivity



## Superconductivity — Essential Notes

1. Zero electrical resistance: Below a critical temperature \(T_c\), a material can enter a superconducting state with zero DC electrical resistance. A persistent current can flow without continuous energy input to overcome resistance.

2. Meissner effect: When a material transitions into the superconducting state, it expels magnetic flux from its interior (apart from a thin surface region, in the ideal case). This is what distinguishes a superconductor from a hypothetical perfect conductor.

3. Critical limits: Superconductivity can be destroyed if the temperature, magnetic field, or current exceeds certain critical values. These limits depend on the material and conditions.

4. Cooper pairs: In conventional superconductors, electrons form correlated pairs called Cooper pairs. These participate in a collective quantum state that permits superconducting current without ordinary electrical resistance.

5. Magnetic levitation: Superconductors can levitate above magnets because of magnetic interactions associated with the Meissner effect and, in some superconductors, magnetic flux pinning. These forces can balance gravity.

## One distinction worth remembering

A superconductor is not simply a conductor with zero resistance.

The Meissner effect is a separate defining property.

![Superconductivity CDT - Oxford Open Day 2025 | University of Oxford Department of Physics](https://images.openai.com/static-rsc-4/GLIfsXZjXdp4J8oB8RsEDPrh4W0QZOHJybv7AbecK8o7c0PCqzL4dYt8Jwl8p96Kp-HdtnLLvlCng04V1C2xOUo7s9JlR6MNwJDS_3_0mUgCwM-1zp0V17Lf38ztG5dvZjsgtfd86XN8RNSwQOdDiL7jjntkkn-GIF5146C59xg?purpose=inline)

Meissner effect

Magnetic flux is expelled from the superconducting interior.

![Science project - Quantum Levitation](https://images.openai.com/static-rsc-4/hps1cr7EEqt-d_Haf08XDaJKBa2bWlsokMUy146onuAKcS1FxtbKBwNJ6_2c-3htREIlnXyDRvkmYvebcNJRqzaTST_JwdoX1quWivKjSLGDa-iq0Fj8aL7r2CeHrJd4-mdi3yYQUl4BsmhcJdxiNoP0lhmeua5e_6Zn4AzXgDs?purpose=inline)

Flux pinning

Magnetic vortices become pinned, helping stabilize the superconductor's position.

You also mentioned sustaining current without an active electric field. That's essentially right for a steady persistent current, but superconductors can still experience electric fields during transients, such as when their current is changing.

## What I'd actually memorize


> Superconductivity is a quantum state of matter occurring below a critical temperature, characterized by zero DC resistance and the Meissner effect. It allows persistent currents without resistive energy loss, but is constrained by critical temperature, current, and magnetic field. Conventional superconductivity involves Cooper pairs.



# Diagrams and Worksheets


# Faraday's Law

![[faradays_law_anddiagrams.pdf]]


## Lenz's Law

![[lenz_law.pdf]]



## Induced Electric Fields

![[induced-electric-fields.pdf]]


## Maxwell's Equations


![[maxwells-eqn.pdf]]


## General Form of Faraday's Law - Moving Conductors (Plus Disk Dynamo)

![[general-form-of-faraday-moving-conductor.pdf]]


## Displacement Currents

![[displacement-current.pdf]]


