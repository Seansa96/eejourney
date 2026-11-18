# Chapter 22: Gauss's Law

15 questions. Standardized prompts with original solutions; source numbering follows the 13th edition.

## Q22.1: Gauss's law

A balloon encloses a fixed point charge. Does its total electric flux depend on inflation?

**Solution:**
No, provided the charge stays inside. The outward net flux is $q/\epsilon_0$ regardless of the balloon's size or shape.

**Why it works:**
Gauss's law depends on enclosed net charge, not surface area alone.

**Grading key points:**

- No, provided the charge stays inside.
- The outward net flux is $q/\epsilon_0$ regardless of the balloon's size or shape.

Source: [PDF page 773](source-page-773.png); source question Q22.1.

## Q22.2: Enclosed charge accounting

In Figure 22.15 replace the negative charge with $+q$, leaving the other charge $+q$. Find flux through A, B, C, and D.

**Solution:**
A encloses the first positive charge and has flux $q/\epsilon_0$. B encloses the second, now positive charge and also has $q/\epsilon_0$. C encloses both and has $2q/\epsilon_0$. D encloses neither and has zero net flux.

**Why it works:**
For each closed surface, add the enclosed charges algebraically; the shape is irrelevant.

**Grading key points:**

- A encloses the first positive charge and has flux $q/\epsilon_0$.
- B encloses the second, now positive charge and also has $q/\epsilon_0$.
- C encloses both and has $2q/\epsilon_0$.
- D encloses neither and has zero net flux.

Source: [PDF page 773](source-page-773.png); source question Q22.2.

## Q22.3: External charge and net flux

Would adding a point charge outside surface C in Figure 22.15 change the net flux through A, B, C, or D?

**Solution:**
No. The new charge is outside C and therefore outside its contained surfaces A, B, and D. It can change the electric field locally on all these surfaces, but contributes zero net flux through each.

**Why it works:**
A charge outside a closed surface contributes equal inward and outward net flux.

**Grading key points:**

- No.
- The new charge is outside C and therefore outside its contained surfaces A, B, and D.
- It can change the electric field locally on all these surfaces, but contributes zero net flux through each.

Source: [PDF page 773](source-page-773.png); source question Q22.3.

## Q22.4: Zero flux versus zero field

If a closed region contains no charge, must the field vanish everywhere on its boundary? Under what conditions would it vanish?

**Solution:**
No. A uniform external field can pass through the region with zero net flux but nonzero boundary field. The boundary field is zero only if all source contributions cancel there, for example an empty cavity inside a closed conductor in electrostatic equilibrium with no charge in the cavity.

**Why it works:**
Zero enclosed charge requires zero total flux, not zero field at every surface point.

**Grading key points:**

- No.
- A uniform external field can pass through the region with zero net flux but nonzero boundary field.
- The boundary field is zero only if all source contributions cancel there, for example an empty cavity inside a closed conductor in electrostatic equilibrium with no charge in the cavity.

Source: [PDF page 773](source-page-773.png); source question Q22.4.

## Q22.5: Displacing an enclosed charge

Move a point charge from the center of a spherical Gaussian surface to another interior point. What happens to the surface field and total flux?

**Solution:**
The field at particular surface points generally changes in magnitude and direction because the source distances change. The integrated outward flux remains $q/\epsilon_0$.

**Why it works:**
Gauss's law survives the loss of spherical symmetry, although the shortcut $\Phi=EA$ generally does not.

**Grading key points:**

- The field at particular surface points generally changes in magnitude and direction because the source distances change.
- The integrated outward flux remains $q/\epsilon_0$.

Source: [PDF page 773](source-page-773.png); source question Q22.5.

## Q22.6: Measuring charge by flux

How can the net charge in a sealed box be found without opening it?

**Solution:**
Measure the normal electric-field component over a closed surface surrounding the box and compute $Q_{\rm encl}=\epsilon_0\oint\mathbf E\cdot d\mathbf A$. This yields total enclosed charge, including any charge on the box itself; subtract a known box charge if the desired quantity is only the contents.

**Why it works:**
External fields complicate local readings but cancel in the closed-surface integral.

**Grading key points:**

- Measure the normal electric-field component over a closed surface surrounding the box and compute $Q_{\rm encl}=\epsilon_0\oint\mathbf E\cdot d\mathbf A$.
- This yields total enclosed charge, including any charge on the box itself; subtract a known box charge if the desired quantity is only the contents.

Source: [PDF page 773](source-page-773.png); source question Q22.6.

## Q22.7: Induced surface charge

A positively charged solid copper sphere initially has uniform surface charge. Bring a negative point charge near it. Where is its excess charge, how is it distributed, and what is the interior field?

**Solution:**
In electrostatic equilibrium all excess net charge remains on the outer surface and the field inside the metal is zero. The surface distribution becomes nonuniform, with enhanced positive charge on the side facing the negative source. The far side becomes less positive and may even be locally negative if induction is strong enough.

**Why it works:**
Mobile charges redistribute until the conductor is equipotential and its internal field vanishes.

**Grading key points:**

- In electrostatic equilibrium all excess net charge remains on the outer surface and the field inside the metal is zero.
- The surface distribution becomes nonuniform, with enhanced positive charge on the side facing the negative source.
- The far side becomes less positive and may even be locally negative if induction is strong enough.

Source: [PDF page 773](source-page-773.png); source question Q22.7.

## Q22.8: Inverse-square dependence of Gauss's law

Would the usual Gauss law hold if a point-charge field varied as $1/r^3$ instead of $1/r^2$?

**Solution:**
No. For a centered spherical surface, $\Phi=4\pi r^2E\propto1/r$, which changes with radius despite unchanged enclosed charge. It therefore cannot equal the same $q/\epsilon_0$ on every sphere.

**Why it works:**
Area growth cancels an inverse-square field exactly, but not an inverse-cube field.

**Grading key points:**

- No.
- For a centered spherical surface, $\Phi=4\pi r^2E\propto1/r$, which changes with radius despite unchanged enclosed charge.
- It therefore cannot equal the same $q/\epsilon_0$ on every sphere.

Source: [PDF page 773](source-page-773.png); source question Q22.8.

## Q22.9: Mobile electrons versus excess charge

Does the existence of mobile electrons throughout a metal contradict the statement that excess charge resides on its surface?

**Solution:**
No. The bulk contains mobile electrons together with compensating positive ion charge. Surface localization refers to the small imbalance between positive and negative charge in electrostatic equilibrium, not to the locations of all electrons.

**Why it works:**
Charge carriers and net excess charge are different quantities.

**Grading key points:**

- No.
- The bulk contains mobile electrons together with compensating positive ion charge.
- Surface localization refers to the small imbalance between positive and negative charge in electrostatic equilibrium, not to the locations of all electrons.

Source: [PDF page 773](source-page-773.png); source question Q22.9.

## Q22.10: Polarization of a hollow conductor

A charged van de Graaff dome approaches an uncharged, closed hollow conducting sphere without contact. Describe the induced charges, net flux, and interior field.

**Solution:**
The near exterior surface acquires charge opposite to the dome, and the far exterior surface acquires like charge, with equal total induced amounts. The sphere's net charge and outward net flux are zero. The field in its metal and its empty closed cavity is zero in electrostatic equilibrium.

**Why it works:**
Induction redistributes surface charge without changing the sphere's total charge, and electrostatic shielding protects the empty interior.

**Grading key points:**

- The near exterior surface acquires charge opposite to the dome, and the far exterior surface acquires like charge, with equal total induced amounts.
- The sphere's net charge and outward net flux are zero.
- The field in its metal and its empty closed cavity is zero in electrostatic equilibrium.

Source: [PDF page 774](source-page-774.png); source question Q22.10.

## Q22.11: Lightning conductors and surface curvature

Why does a grounded copper lightning rod divert current from a building, and why round its end?

**Solution:**
The thick copper path has low impedance and is intended to carry the discharge to earth with less heating and voltage rise in the building. Rounding reduces extreme surface-field concentration and premature corona discharge compared with a sharp tip. Actual lightning performance also depends on grounding and the transient inductance of the installation.

**Why it works:**
Current divides according to electrical impedance, while small curvature radii concentrate surface fields.

**Grading key points:**

- The thick copper path has low impedance and is intended to carry the discharge to earth with less heating and voltage rise in the building.
- Rounding reduces extreme surface-field concentration and premature corona discharge compared with a sharp tip.
- Actual lightning performance also depends on grounding and the transient inductance of the installation.

Source: [PDF page 774](source-page-774.png); source question Q22.11.

## Q22.12: Cavity shielding and grounding

Does a charge in a conducting cavity affect the external field? Does a charge outside the conductor affect the field in its empty cavity?

**Solution:**
For an isolated conductor of fixed total charge Q, a cavity charge q induces $-q$ on the inner surface and leaves $Q+q$ on the outer surface, so it generally affects the exterior. An external charge cannot create a field inside an otherwise empty closed cavity in electrostatic equilibrium. If the conductor is grounded, charge can flow to earth and the internal charge need not change the exterior field.

**Why it works:**
Electrostatic shielding acts inward; outward effects depend on the conductor's net charge constraint and grounding.

**Grading key points:**

- For an isolated conductor of fixed total charge Q, a cavity charge q induces $-q$ on the inner surface and leaves $Q+q$ on the outer surface, so it generally affects the exterior.
- An external charge cannot create a field inside an otherwise empty closed cavity in electrostatic equilibrium.
- If the conductor is grounded, charge can flow to earth and the internal charge need not change the exterior field.

Source: [PDF page 774](source-page-774.png); source question Q22.12.

## Q22.13: Tangential electrostatic field

Why must the tangential field vanish at a conductor's electrostatic surface, and must it vanish at an insulator's surface?

**Solution:**
A nonzero tangential field would move mobile surface charges, contradicting equilibrium. In an insulator the charges are bound and need not move freely along the surface, so a tangential field may persist.

**Why it works:**
The conductor condition follows from charge mobility; it is not a universal boundary condition for every material.

**Grading key points:**

- A nonzero tangential field would move mobile surface charges, contradicting equilibrium.
- In an insulator the charges are bound and need not move freely along the surface, so a tangential field may persist.

Source: [PDF page 774](source-page-774.png); source question Q22.13.

## Q22.14: Divergence and charge density

Show that a uniform electric field implies zero volume charge density. Does zero volume charge density imply a uniform field?

**Solution:**
For a constant vector field, $\oint\mathbf E\cdot d\mathbf A=\mathbf E\cdot\oint d\mathbf A=0$ for every small closed surface. Gauss's law gives zero enclosed charge, hence $\rho=0$. The converse fails: a point charge's field varies with position in every surrounding region that excludes the source.

**Why it works:**
Zero divergence constrains net outward flow, not all spatial derivatives of the field.

**Grading key points:**

- For a constant vector field, $\oint\mathbf E\cdot d\mathbf A=\mathbf E\cdot\oint d\mathbf A=0$ for every small closed surface.
- Gauss's law gives zero enclosed charge, hence $\rho=0$.
- The converse fails: a point charge's field varies with position in every surrounding region that excludes the source.

Source: [PDF page 774](source-page-774.png); source question Q22.14.

## Q22.15: Uniform charge and a charge-free bubble

Can a uniform positive volume charge density have a uniform field? Can a charge-free bubble within it have a uniform field?

**Solution:**
A uniform field cannot exist throughout the charged region because $\nabla\cdot\mathbf E=\rho/\epsilon_0>0$. A charge-free bubble can have a uniform field, but need not. For a spherical cavity centered at displacement $\mathbf a$ inside a uniformly charged sphere, superposing a negative-density sphere gives the constant cavity field $\mathbf E=\rho\mathbf a/(3\epsilon_0)$.

**Why it works:**
Subtracting the missing charge distribution cancels the position-dependent parts inside the cavity.

**Grading key points:**

- A uniform field cannot exist throughout the charged region because $\nabla\cdot\mathbf E=\rho/\epsilon_0>0$.
- A charge-free bubble can have a uniform field, but need not.
- For a spherical cavity centered at displacement $\mathbf a$ inside a uniformly charged sphere, superposing a negative-density sphere gives the constant cavity field $\mathbf E=\rho\mathbf a/(3\epsilon_0)$.

Source: [PDF page 774](source-page-774.png); source question Q22.15.
