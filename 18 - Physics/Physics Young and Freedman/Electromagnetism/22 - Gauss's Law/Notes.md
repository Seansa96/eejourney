# Charge and Electric Flux

Previously, we started with a distribution of charge and determined the electric field it produced. We could treat that distribution as many individual point charges, calculate their fields, and then add those fields as vectors.

But can we work backward? If we know the electric field in a region, what can it tell us about the charge inside?

Imagine a box that may or may not contain electric charge. We can move a small positive test charge around it and measure the force at different positions, which tells us the electric field through $\vec F=q_0\vec E$.

The box is just an **imaginary closed surface**, meaning that it completely encloses a volume. It doesn't interfere with the field or need to be made of any particular material.

It turns out that examining the field over this surface is enough to determine the **net charge enclosed**. We don't need to open the box.

## Electric Flux and Enclosed Charge

Suppose the box contains a single positive charge. Its electric field points outward, so the field passes outward through the box's surface. If we replace it with a negative charge, the field points inward instead.

We describe this using **electric flux**, represented by $\Phi_E$. We can loosely imagine the field “flowing” through the surface, with outward flux taken as positive and inward flux as negative.

This is only an analogy. The electric field isn't actually a substance flowing through the box.

The important quantity here is the **net flux**, which accounts for both the inward and outward contributions over the entire surface.

So what happens when the enclosed charge is zero?

There are several ways this can occur:

1. **An empty box with no electric field.** There is no field passing through the surface, so the flux is zero.
2. **A box containing equal positive and negative charges.** There is an electric field, but the total inward and outward flux cancel.
3. **An empty box placed in a uniform electric field produced by charges outside it.** The field enters through one end and leaves through the other. Along the sides, it runs parallel to the surface and contributes no flux.

All three have zero net flux, but their electric fields are quite different.

**ZERO NET FLUX DOES NOT MEAN THE ELECTRIC FIELD IS ZERO, OR EVEN THAT THERE ARE NO CHARGES INSIDE.**

It tells us that the _net enclosed charge_ is zero. Equal amounts of positive and negative charge can still be present.

Likewise, an external charge can affect the field on the surface without contributing any net flux through that closed surface. Its inward and outward contributions cancel.

## What Determines the Amount of Flux?

If we double a single enclosed point charge while keeping its position and the box unchanged, the electric field doubles everywhere on the surface. The net flux therefore doubles as well.

So the net flux is directly proportional to the net enclosed charge.

But what if we keep the charge unchanged and make the box larger?

The field becomes weaker farther from the charge, but there is also more surface area through which it passes. For a uniformly enlarged box around the same point charge, these effects compensate, leaving the net flux unchanged.

> **needs expansion — Inverse-Square Field and Surface-Area Scaling:** Explain why doubling every distance from the point charge reduces the field to one quarter, while doubling the box's linear dimensions increases each face's area fourfold. Include why we use the component of the field perpendicular to each face.

## Connection to Gauss's Law

These observations give us the qualitative idea behind **Gauss's Law**:

- Positive net enclosed charge gives net outward flux; negative net enclosed charge gives net inward flux.
- Charges outside the surface contribute zero net flux through it.
- Net flux depends on the net enclosed charge, rather than the size of the enclosing surface.

We introduced these ideas using boxes and simple charge arrangements, but the relationship also holds for closed surfaces of other shapes.

To state it precisely, we first need a mathematical definition of electric flux, which is what the next section develops.


