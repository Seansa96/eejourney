# Mutual Inductance

## Error

Thought Lenz's Law meant that the induced effect, that being the current, must oppose the cause, so that its sign should be opposite of the current cause, which was positive. This is not correct. The cause here is **changing magnetic flux**, so the current flows in whatever way the magnetic field that would oppose that changing flux. This means it is possible for the inducing effect to have the same sign as the induced current.

# Flux Orientation

## Error

Thought that magnetic field lines and thus flux had to be linear at all points for a linear geometry.  Not true. Use the right grip rule: point your thumb in the way the current travels (doesn't matter technically), then grip your hand around the wire. How you curl it determines the circulation of the magnetic field--clockwise or counterclockwise.

# Plane flying through an upward magnetic field

## Error

Didn't understand how to apply the right hand rule for this problem. Upward magnetic field, plane flying horizontally. Point index in the direction of the velocity, then curl in the direction of the field. Have to have palm facing up to curl towards it, so thumb should point right. For negative charge, you'd reverse. So you get right wingtip having positive charge accumulate, left tip have negative charge accumulate. Electric field goes towards decreasing potential, so all the potential is at the wingtip, driving a current through it ala Hall Effect.

# Square loop and Induced EMF

## Error

Identify the quality the problem is asking for, and identify the axis of rotation's relation to the magnetic field first, which will then explain the relation between it and the plane of the loop face. If the hinge is parallel with the field, then it "skims" the surface, whereas if it is perpendicular to the hinge, then it goes "into" the surface, and with a changing angle the amount of field lines through the loop face changes, which dictates the flux's rate of change

# Nonconservative Electrical Work

## Error

It is actually meaningful to talk about the work done on the electron, but note that the magnetic field itself does no work. While the source of the induced electric field is the changing magnetic flux, it is the induced electric field itself which is what does work. And then because this induced EMF is what drives the current, there is no "potential difference" endpoint that is meaningful to work. 


# Slidewire Circuit Break

> Misconception: Assuming an open circuit means zero resistance or that current continues without decreasing.
> 
> Correct principle: An open circuit has effectively infinite resistance, preventing sustained current. Motional emf can still exist, but without sustained current, there is no sustained magnetic braking force.
> 
> Procedure: Determine whether the circuit is open or closed before calculating current or magnetic force.

The most transferable lesson: An emf is not the same thing as a current. An emf can exist even when no current flows.


# Scaling Induced EMF and Field

### Q29.13 — Induced EMF and Electric Field Scaling

**Errors:**

- Didn't expand the area term $A=\pi r^2$ when evaluating how radius affects magnetic flux.
    
- Assumed the induced electric field decreases with circumference without accounting for the changing emf.
    

**Corrective Procedure:**

1. Identify which quantities change and which remain constant.
    
2. Expand geometric variables ($A=\pi r^2$, $C=2\pi r$).
    
3. Substitute into the governing equations before determining proportionality.
    
4. Compare how numerator and denominator scale.
    

**Key Relationships:**

- $|\mathcal E|=\pi r^2|dB/dt|$ → emf scales as $r^2$.
    
- $E=|\mathcal E|/(2\pi r)$ → tangential electric field scales as $r$.
    

**Transferable Rule:** Never assume how a physical quantity scales until all geometry-dependent variables have been substituted into the governing equation.