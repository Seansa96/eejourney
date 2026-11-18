# Chapter 22 — Gauss's Law

## Chapter objectives

By the end of this chapter, you should be able to:

1. Explain electric flux and how it describes the electric field passing through a surface.
    
2. Calculate electric flux through flat, curved, open, and closed surfaces.
    
3. Explain Gauss's law conceptually and mathematically, including why it works.
    
4. Recognize spherical, cylindrical, and planar symmetry and select appropriate Gaussian surfaces.
    
5. Apply Gauss's law to calculate electric fields from symmetric charge distributions.
    
6. Explain how electric charges redistribute themselves on conductors in electrostatic equilibrium.
    
7. Distinguish situations where Gauss's law simplifies an electric-field calculation from situations where it does not.
    

## 22.1 — Charge and Electric Flux

Core question: What is electric flux, and what does it tell us about an electric field passing through a surface?

### Conceptual questions

- What is electric flux, and how is it different from electric field strength?
    
- What does it mean physically for electric field lines to pass through a surface?
    
- Why does the orientation of a surface affect the electric flux through it?
    
- What is an area vector, and why is its direction perpendicular to the surface?
    
- Why do we use the dot product to calculate electric flux?
    
- Under what conditions is the electric flux positive, negative, or zero?
    
- What is the difference between an open surface and a closed surface?
    
- Why do the area vectors of a closed surface always point outward by convention?
    
- Can a surface have zero net electric flux even when the electric field is nonzero everywhere on it?
    
- What are the SI units of electric flux?
    

### Mathematical relationships

For a uniform electric field passing through a flat surface:

$$
\Phi_E=\vec E\cdot\vec A=EA\cos\theta
$$

For a nonuniform electric field or curved surface:

$$
\Phi_E=\int_S\vec E\cdot d\vec A
$$

For a closed surface:

$$
\Phi_E=\oint_S\vec E\cdot d\vec A
$$

Understand the distinction between an ordinary surface integral and a closed-surface integral.

### Problem-solving checklist

- Calculate flux through a flat surface for an arbitrary angle between the field and the surface normal.
    
- Determine the flux through a tilted rectangular or circular surface.
    
- Calculate flux through multiple faces of a cube placed in a uniform electric field.
    
- Determine the total flux through a closed surface in a uniform electric field.
    
- Evaluate the flux through a surface where the electric field varies with position.
    
- Determine the sign of the flux using the electric field direction and outward normal.
    
- Explain why changing a surface's orientation can change the flux without changing the field magnitude.
    

Teaching challenge: Explain why rotating a rectangular surface in a uniform electric field changes the electric flux, even though both the surface area and electric field strength remain constant.

## 22.2 — Calculating Electric Flux

Core question: How do we mathematically determine the total electric flux through a surface when the electric field, surface geometry, or orientation varies?

### Conceptual questions

- Why do we divide a surface into infinitesimal area elements when calculating flux?
    
- What does the differential area vector $d\vec A$ represent?
    
- Why is the electric flux through a curved surface generally calculated using an integral?
    
- How do you determine the correct surface normal for a curved surface?
    
- Why can we sometimes take the electric field outside the integral?
    
- How can symmetry simplify flux calculations?
    
- What is the difference between calculating flux directly and using Gauss's law to determine total flux?
    
- Why can electric field lines enter and exit the same closed surface without producing net flux?
    

### Mathematical relationships

The general electric flux integral is

$$
\Phi_E=\int_S \vec E\cdot d\vec A
$$

For a closed surface consisting of multiple parts:

$$
\Phi_{E,\text{total}}=\sum_i\Phi_{E,i}
$$

The integral simplifies when the field magnitude is constant and the angle between $\vec E$ and $d\vec A$ is fixed:

$$
\Phi_E=EA\cos\theta
$$

### Problem-solving checklist

- Calculate electric flux through all six faces of a cube.
    
- Find the flux through an open hemisphere in a uniform electric field.
    
- Calculate flux through a cylinder's curved surface and end caps.
    
- Determine which parts of a composite surface contribute zero flux.
    
- Set up a surface integral when the electric field depends on position.
    
- Use symmetry to evaluate flux without integrating over every individual surface element.
    
- Determine the net flux through a closed surface when field lines enter and leave through different faces.
    

Teaching challenge: A cylinder is placed in a uniform electric field parallel to its central axis. Explain why the curved surface contributes zero flux, while the two end caps have equal and opposite flux.

## 22.3 — Gauss's Law

Core question: How is the electric flux through a closed surface related to the total electric charge enclosed by that surface?

### Conceptual questions

- What does Gauss's law state in plain English?
    
- How is Gauss's law related to Coulomb's law?
    
- Why does only the enclosed charge determine the net electric flux through a closed surface?
    
- Why can charges outside a Gaussian surface affect the electric field on that surface without changing its net flux?
    
- What happens to electric flux if you change the shape or size of a Gaussian surface without changing its enclosed charge?
    
- What happens when a Gaussian surface encloses multiple positive and negative charges?
    
- Why can a Gaussian surface have zero net flux even when it contains charges?
    
- Why does zero net flux not imply that the electric field is zero?
    
- What is the difference between the physical surface of an object and a Gaussian surface?
    
- What is the relationship between Gauss's law and the inverse-square dependence of the electric field of a point charge?
    
- Does Gauss's law require symmetry to be valid, or only to be useful for calculating electric fields?
    

### Mathematical relationships

Gauss's law in integral form:

$$
\boxed{\oint_S\vec E\cdot d\vec A=\frac{Q_{\text{enc}}}{\varepsilon_0}}
$$

For multiple discrete charges:

$$
Q_{\text{enc}}=\sum_i q_i
$$

For a continuous charge distribution:

$$
Q_{\text{enc}}=\int_V\rho\,dV
$$

Gauss's law in differential form (optional extension):

$$
\nabla\cdot\vec E=\frac{\rho}{\varepsilon_0}
$$

Be able to explain that the integral form relates the total outward electric flux to the enclosed charge, while the differential form relates the local divergence of the electric field to the local charge density.

### Problem-solving checklist

- Calculate net electric flux through a closed surface containing a known charge.
    
- Determine the enclosed charge from the measured net electric flux.
    
- Calculate the net flux through a Gaussian surface containing several positive and negative charges.
    
- Determine how flux changes when a charge crosses a Gaussian surface.
    
- Explain why an external charge changes the field distribution on a Gaussian surface but not its net flux.
    
- Use Gauss's law to find the total flux through a closed surface without calculating the electric field.
    
- Distinguish problems that ask for electric flux from those that ask for electric field magnitude.
    

Teaching challenge: A point charge is enclosed by a sphere. You then deform the sphere into an irregular shape without moving the charge outside it. Explain why the net electric flux remains unchanged even though the electric field strength and its angle relative to the surface normal vary across the new surface.

## 22.4 — Applications of Gauss's Law

Core question: How do we use symmetry to calculate electric fields from charge distributions that would otherwise require difficult integration?

This is probably the most important problem-solving section of the chapter.

### Conceptual questions

- What types of symmetry make Gauss's law useful for calculating electric fields?
    
- Why do point charges and spherically symmetric charge distributions naturally suggest spherical Gaussian surfaces?
    
- Why do infinitely long lines of charge suggest cylindrical Gaussian surfaces?
    
- Why do infinite planes of charge suggest pillbox Gaussian surfaces?
    
- What conditions allow the electric field to be taken outside the flux integral?
    
- How do you determine which parts of a Gaussian surface contribute zero flux?
    
- Why must the electric field be perpendicular or parallel to the relevant surface normals for common simplifications?
    
- How does the enclosed charge change as the Gaussian surface grows?
    
- Why do different charge geometries produce different dependencies of electric field strength on distance?
    
- Why can an infinite sheet produce a constant electric field, while the field of a point charge decreases as $1/r^2$?
    
- Why is Gauss's law generally not sufficient by itself to determine the electric field of an arbitrary asymmetric charge distribution?
    

### Mathematical relationships

For a spherically symmetric distribution:

$$
E(4\pi r^2)=\frac{Q_{\text{enc}}}{\varepsilon_0}
$$

For an infinitely long, uniformly charged line:

$$
E(2\pi rL)=\frac{\lambda L}{\varepsilon_0}
$$

For an infinite, uniformly charged nonconducting sheet:

$$
2EA=\frac{\sigma A}{\varepsilon_0}
$$

These yield the standard results:

|Charge geometry|Electric field magnitude|
|---|---|
|Point charge / outside spherical distribution|$\displaystyle E=\frac{1}{4\pi\varepsilon_0}\frac{\lvert Q \rvert}{r^2}$|
|Inside uniform solid sphere|$\displaystyle E=\frac{\lvert \rho \rvert r}{3\varepsilon_0}$|
|Infinite line of charge|$\displaystyle E=\frac{\lvert \lambda \rvert}{2\pi\varepsilon_0r}$|
|Infinite nonconducting sheet|$\displaystyle E=\frac{\lvert \sigma \rvert}{2\varepsilon_0}$|

The solid-sphere result assumes uniform volume charge density. These equations give magnitudes; charge signs determine directions.

### Problem-solving checklist

#### Spherical symmetry

- Calculate the electric field outside a uniformly charged solid sphere.
    
- Calculate the electric field inside a uniformly charged solid sphere.
    
- Calculate the electric field inside and outside a uniformly charged spherical shell.
    
- Determine the electric field at the surface of a spherical charge distribution.
    
- Construct a piecewise expression for $E(r)$ inside and outside a sphere.
    
- Sketch the electric field magnitude as a function of radial distance.
    

#### Cylindrical symmetry

- Calculate the electric field from an infinitely long uniformly charged line.
    
- Calculate the electric field inside and outside a uniformly charged solid infinite cylinder.
    
- Calculate the electric field inside and outside a uniformly charged infinite cylindrical shell.
    
- Identify why the cylinder's end caps contribute zero flux for a radial field.
    
- Determine how the electric field scales with distance from the axis.
    

#### Planar symmetry

- Calculate the electric field produced by an infinite uniformly charged nonconducting sheet.
    
- Calculate the field between two infinite oppositely charged sheets.
    
- Determine the electric field outside two infinite oppositely charged sheets.
    
- Apply superposition to multiple parallel charged sheets.
    
- Explain why a pillbox Gaussian surface simplifies flux calculations.
    

#### Mixed reasoning

- Select an appropriate Gaussian surface for an unfamiliar symmetric charge distribution.
    
- Determine $Q_{\text{enc}}$ as a function of Gaussian surface size.
    
- Recognize when Gauss's law is valid but cannot directly isolate $E$.
    
- Check an electric-field result using units, limiting behavior, and physical intuition.
    

### Symmetry visualization

A useful way to understand these problems is to compare Gaussian surfaces that match a charge distribution's symmetry with ones that do not.

Try switching the source geometry and observing which Gaussian surface allows the flux integral to simplify.

$\oint \vec E \cdot d\vec A = \frac{Q_{\mathrm{enc}}}{\varepsilon_0}$

$\oint \vec E\cdot d\vec A = E(4\pi r^2)$

source

pointinfinite lineinfinite sheet

surface

centered sphereoff-center sphere

+

Give feedback

Teaching challenge: Explain why an isolated point charge produces an electric field proportional to $1/r^2$, an infinite line charge produces a field proportional to $1/r$, and an infinite sheet produces a field independent of distance.

Your explanation should connect the different dependencies to the geometry of the corresponding Gaussian surfaces.

## 22.5 — Charges on Conductors

Core question: How does Gauss's law explain the distribution of charge and electric fields in conductors at electrostatic equilibrium?

### Conceptual questions

- What does electrostatic equilibrium mean for a conductor?
    
- Why must the electric field inside the conducting material be zero in electrostatic equilibrium?
    
- Why does excess charge reside on the surface of a conductor?
    
- Why is the electric field immediately outside a conductor perpendicular to its surface?
    
- What would happen if the electric field had a tangential component along the conductor's surface?
    
- How does Gauss's law determine the electric field immediately outside a conductor?
    
- Why can excess charge concentrate near sharply curved regions of a conductor?
    
- What happens to the electric field inside an empty cavity surrounded by a conductor?
    
- How does placing a charge inside a cavity affect the charge distribution on the inner and outer surfaces?
    
- What is electrostatic shielding, and how does a Faraday cage work?
    
- Why can the net charge on a conductor be nonzero even though the electric field inside its material is zero?
    

### Mathematical relationships

Inside conducting material in electrostatic equilibrium:

$$
\boxed{\vec E=0}
$$

Immediately outside the surface of a conductor:

$$
\vec E_{\text{outside}}=\frac{\sigma}{\varepsilon_0}\hat n
$$

where $\sigma$ is the local signed surface charge density and $\hat n$ is the outward surface normal.

For a spherical conducting shell with no charge inside its cavity:

$$
E(r)= \begin{cases} 0, & r<R\\[6pt] \displaystyle \frac{1}{4\pi\varepsilon_0}\frac{|Q|}{r^2}, & r>R \end{cases}
$$

Here $R$ is the shell radius, and the expression gives electric field magnitude.

### Problem-solving checklist

- Determine the electric field inside and outside a charged conducting sphere.
    
- Calculate the surface charge density of a spherical conductor.
    
- Find the electric field immediately outside a conductor given its surface charge density.
    
- Determine the charge induced on the inner surface of a conducting shell containing a point charge.
    
- Determine the total charge on the outer surface of a conducting shell.
    
- Analyze nested concentric conducting spherical shells.
    
- Determine the electric field in each region of a system containing spherical conducting shells.
    
- Use Gaussian surfaces within the conducting material to infer enclosed charge.
    
- Explain which regions are shielded from external electrostatic fields.
    
- Distinguish conductor problems from uniformly charged insulating sphere problems.
    

Teaching challenge: Consider a neutral conducting spherical shell surrounding a positively charged point charge. Explain why negative charge appears on the inner surface, positive charge appears on the outer surface, and the electric field inside the conducting material remains zero.

# Final Chapter Mastery Assessment

After completing the individual sections, test your understanding with these eight integrated problems.

|#|Problem|Primary concepts|
|---|---|---|
|1|A point charge enclosed by an irregular closed surface|Enclosed charge, flux, Gauss's law|
|2|A cube in a uniform electric field at an arbitrary orientation|Dot products, surface normals, flux|
|3|A uniformly charged solid insulating sphere|Spherical symmetry, piecewise electric fields|
|4|A uniformly charged infinite solid cylinder|Cylindrical symmetry, enclosed charge|
|5|Two infinite parallel sheets with equal and opposite surface charge densities|Planar symmetry, superposition|
|6|A conducting shell surrounding an off-center point charge|Induced surface charges, equilibrium, limits of symmetry|
|7|Two concentric conducting spherical shells carrying different net charges|Multiple Gaussian surfaces, charge redistribution|
|8|An irregular charge distribution inside a spherical Gaussian surface|Distinguishing total flux from local electric field|

## Five questions that demonstrate deeper understanding

These are questions I'd especially recommend answering verbally without consulting notes.

1. Why does Gauss's law always work, but not always help us calculate electric fields? Explain the difference between the law's validity and the symmetry conditions required to extract $E$ from the integral.

2. Why can the net electric flux through a closed surface be zero even though the electric field is nonzero at every point on it? Connect your explanation to the dot product and signed flux.

3. Why does the enclosed charge determine net flux, but not necessarily the electric field at an individual point on the surface? Explain how external charges can contribute to local electric fields while leaving total flux unchanged.

4. Why do the electric fields of point, line, and planar charge distributions have different distance dependencies? Derive the dependencies using symmetry and Gaussian surface geometry.

5. Why must electric fields vanish inside conducting material at electrostatic equilibrium? Explain the connection between free charge motion, charge redistribution, and Gauss's law.

# Suggested Teach-Back Video Structure

For this chapter, I'd divide the material into four videos rather than attempting to cover each textbook section independently.

|Video|Topic|Main objective|
|---|---|---|
|1|Understanding Electric Flux|Explain the dot product, surface normals, and what flux physically measures|
|2|Gauss's Law and Its Meaning|Derive or motivate the flux–charge relationship and distinguish net flux from local field|
|3|Calculating Electric Fields with Symmetry|Work through spherical, cylindrical, and planar distributions|
|4|Conductors and Electrostatic Equilibrium|Explain surface charge, shielding, cavities, and induced charges|

## A standard problem-solving procedure

One particularly valuable skill for Gauss's law is developing a consistent strategy that you can apply to unfamiliar geometries.

1. Identify the symmetry. Is the charge distribution spherical, cylindrical, planar, or something else?

2. Determine the electric field's direction. Use the symmetry of the entire source distribution to infer the field orientation.

3. Choose a Gaussian surface. Select one on which the field's magnitude is constant over contributing portions and its orientation relative to $d\vec A$ is known.

4. Calculate the enclosed charge. Determine whether it is best expressed using $Q$, $\lambda$, $\sigma$, or $\rho$.

5. Apply Gauss's law. Evaluate the flux integral using the geometry and symmetry.

6. Solve for the electric field. Express the result in terms of position and identify any separate regions requiring piecewise expressions.

7. Check the physics. Verify units, directions, continuity where appropriate, and limiting behavior.

My main recommendation: Put extra emphasis on the connection between symmetry, geometry, and electric-field behavior. Memorizing the electric fields of spheres, cylinders, and sheets is useful for exams, but being able to derive those expressions from geometric reasoning is what will make the knowledge transferable to more advanced electromagnetism.

For this chapter, I'd consider your understanding genuinely solid once you can look at a previously unseen charge distribution and explain whether Gauss's law alone can determine its electric field—and justify your answer before doing any calculations.