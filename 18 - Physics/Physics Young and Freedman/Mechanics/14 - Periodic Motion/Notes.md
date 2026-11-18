


# Damped Oscillations

Idealized oscillating systems are generally frictionless, so there are no non-conservative forces. Thus, total mechanical energy is constant, and so a system that is set into motion will continue oscillating forever, and without decrease in amplitude.

But real-world systems always have some dissipative forces, and so oscillations die out in time, unless that dissipated mechanical energy is replaced.  A mechanical pendulum clock will continue to run because the potential energy stored in the spring or a hanging weight system replaces that lost mechanical energy due to friction in the pivot and the gears.

Still, eventually the spring runs down or the weights reach the bottom of their path.  At that point, no more energy is available so the pendulum swings decrease in amplitude and stop.

This decrease in amplitude caused by dissipative forces is called **damping**, and the corresponding motion is called **damped oscillation.** The simplest case to is a simple harmonic oscillator with a frictional damping force which is directly proportional to the *velocity* of the oscillating body.  

This occurs usually in friction involving viscous fluid flow like in shock absorbers or sliding between oil-lubricated surfaces.  There is then an additional force on the body due to friction,
$$
F_{x}=-bv_{x}
$$
where

$$
v_{x}=\frac{dx}{dt}
$$
which is of course the velocity, and $b$ is the constant that describes the strength of a damping force. An example of such a force would be the viscosity of the fluid in which the oscillation occurs.

$$
x=Ae^{-(b/2m)t}\cos(w't+\phi)
$$
**Oscillator with little damping**

## Graph of Displacement vs Time

![[Pasted image 20261025033217.png]]

And then we can see that the angular frequency of oscillation, $w'$, is given by

$$
w' = \sqrt{ \frac {k}{m} - \frac{b^2}{4m^2} }
$$
And note that this is the case for **little damping**.

The motion that is described by the previous two equations differs from an undamped case in two ways:

First, the amplitude, $Ae^{-b/2m)t}$ is not constant, but varies (decreasing) with time because of the decreasing exponential factor.  The above graph shows for when the angle is 0, that the larger the value of $b$, then the more quickly the amplitude decreases, which makes sense: a greater damping constant means it'll damp faster.

Secondly, the angular frequency of oscillation equation shows that it's no longer equal to just the square root of $k$ over $m$, but is lessened by the secondary term.  It becomes zero when $b$ becomes so large that

$$
\frac{k}{m} - \frac{b^2}{4m^2}=0
$$
or

$$
b=2\sqrt{ km }
$$
When this is the case, in that the inside terms cancel, this is called **critical damping**. The system no longer oscillates and instead returns to its equilibrium position without oscillation when it is displaced and subsequently released.

If $b$ is greater than the second term, this is called **overdamping**. There is no oscillation, but the system returns to equilibrium more slowly than with critical damping.  

The solutions of this case possess the form
$$
x = C_{1}e^{-a_{1}t} + C_{2}e^{-a_{2}t}
$$
where $C_1$ and $C_2$ are constants that depend on the initial conditions, and $a_1$ and $a_2$ are constants determined by $m$, $k$, and $b$.

When $b$ is less than $2\sqrt{ km }$, this is called **underdamping**. The system does oscillate, just with steadily decreasing amplitude.

In a system like a tuning fork or guitar string, it is desirable to have as little damping as possible.  

In an automobile, you'd want it be slightly underdamped or critically damped for passenger comfort. However, if you damp too much, the springs in the suspension will still be compressed and thus not ready to reduce the shock of another bump if encountered.

## Energy in Damped Oscillations



# Forced Oscillations and Resonance

A damped oscillator that is left to itself will eventually cease moving altogether. However, we can maintain a constant amplitude oscillation by applying a force that varies with time in a periodic or cyclic way. It must have a definite period and frequency.  By providing what is called a **driving force**, once each cycle, we maintain the oscillation against damping.

## Damped Oscillation with a Periodic Driving Force

By applying a periodically varying driving force with angular frequency $w_d$ to a damped harmonic oscillator, the resulting motion is called a **forced oscillation** or a **driven oscillation**.

## Resonance and Its Consequences

