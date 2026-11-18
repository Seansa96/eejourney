# Right-Hand Rules — Electricity & Magnetism

## 1. Right-Hand Rule Reference Table

|Application|Right-Hand Rule|Direction Determined|Governing Equation|
|---|---|---|---|
|**Magnetic force on a moving charge**|Index = velocity $\vec v$; middle = magnetic field $\vec B$; thumb = force $\vec F_B$ on positive charge|Force perpendicular to $\vec v$ and $\vec B$|$\vec F_B=q(\vec v\times\vec B)$|
|**Magnetic force on a current-carrying wire**|Index = conventional current $I$; middle = $\vec B$; thumb = $\vec F_B$|Force on the conductor|$\vec F_B=I\vec L\times\vec B$|
|**Magnetic field around a straight wire**|Thumb = conventional current $I$; curled fingers = $\vec B$|Circulation of magnetic field around wire|$B=\frac{\mu_0I}{2\pi r}$|
|**Magnetic field through a current loop**|Curl fingers along conventional current; thumb = $\vec B$ through center|Direction of magnetic field along loop axis|$\vec\mu=NI A\hat n$|
|**Solenoid magnetic field**|Curl fingers along winding's conventional current; thumb = internal $\vec B$|Direction of magnetic field inside solenoid|$B=\mu_0nI$|
|**Magnetic dipole moment**|Curl fingers along conventional current; thumb = $\vec\mu$|Direction of magnetic dipole moment|$\vec\mu=NI A\hat n$|
|**Torque on a magnetic dipole**|Index = $\vec\mu$; middle = $\vec B$; thumb = $\vec\tau$|Torque vector along rotation axis|$\vec\tau=\vec\mu\times\vec B$|
|**Torque on an electric dipole**|Index = electric dipole moment $\vec p$; middle = $\vec E$; thumb = $\vec\tau$|Torque vector along rotation axis|$\vec\tau=\vec p\times\vec E$|
|**Biot–Savart law**|Index = current element $d\vec\ell$; middle = displacement direction $\hat r$; thumb = $d\vec B$|Magnetic field contribution from a current element|$d\vec B=\frac{\mu_0I}{4\pi}\frac{d\vec\ell\times\hat r}{r^2}$|
|**Motional charge separation / emf**|Index = conductor velocity $\vec v$; middle = $\vec B$; thumb = force on positive charge|Which end becomes positive|$\vec F_B=q(\vec v\times\vec B)$|
|**Ampère's law orientation**|Curl fingers along positive integration direction; thumb = positive surface normal|Sign of current crossing surface|$\oint\vec B\cdot d\vec\ell=\mu_0I_{\mathrm{enc}}$ (steady currents)|
|**Faraday / induced current direction**|First use Lenz's law to determine induced $\vec B$; point thumb along induced $\vec B$; curled fingers = conventional induced current|Clockwise or counterclockwise induced current|$\mathcal E=-\frac{d\Phi_B}{dt}$|

**Finger assignment convention:** This table uses the three-finger right-hand rule: **index = first vector, middle = second vector, thumb = cross-product result**.

Other textbooks use different finger assignments. The cross-product order must remain unchanged.

---

## 2. The Three Main Hand Rules

### A. Three-Finger Rule — Cross Products

Use whenever the equation contains $\times$.

For:

$\vec A\times\vec B=\vec C$

- **Index finger:** $\vec A$ (first vector).
    
- **Middle finger:** $\vec B$ (second vector).
    
- **Thumb:** $\vec C$ (result).
    

**Important:**

- The vectors are mutually perpendicular in the nonzero perpendicular-vector case.
    
- Rotate your entire hand as necessary.
    
- Reversing the order reverses the result: $\vec A\times\vec B=-(\vec B\times\vec A)$.
    
- For a negative charge, reverse the force direction.
    

### B. Right-Hand Grip Rule — Straight Wire

- **Thumb:** Direction of conventional current.
    
- **Curled fingers:** Direction of magnetic field circulation.
    

Viewed with current coming toward you (•), the magnetic field is counterclockwise.

Viewed with current going away from you (×), the magnetic field is clockwise.

### C. Right-Hand Grip Rule — Current Loop / Solenoid

- **Curled fingers:** Direction of conventional current around the loop or windings.
    
- **Thumb:** Direction of magnetic field through the center and magnetic dipole moment.
    

Viewed face-on:

|Current direction|Magnetic field through center|
|---|---|
|Counterclockwise|Out of page (•)|
|Clockwise|Into page (×)|

---

## 3. Directional Rules That Do NOT Require a Right-Hand Rule

|Phenomenon|Direction Rule|Equation|
|---|---|---|
|**Electric field from positive charge**|Points away from positive charge|$\vec E=\vec F/q_+$|
|**Electric field from negative charge**|Points toward negative charge|$\vec E=\vec F/q_+$|
|**Electric force on positive charge**|Same direction as $\vec E$|$\vec F_E=q\vec E$|
|**Electric force on negative charge**|Opposite direction to $\vec E$|$\vec F_E=q\vec E$|
|**Conventional current**|Direction positive charges would flow|$I=dQ/dt$|
|**Electron drift**|Opposite to conventional current|$\vec F_E=q\vec E$, $q<0$|
|**Electric dipole moment**|Points from negative to positive charge|$\vec p=q\vec d$|
|**Electrostatic potential**|Electric field points toward decreasing potential|$\vec E=-\nabla V$|
|**Induced electric field**|Circulates according to Faraday's law and Lenz's law|$\oint\vec E\cdot d\vec\ell=-d\Phi_B/dt$|
|**Lenz's law**|Induced magnetic field opposes the _change_ in magnetic flux|$\mathcal E=-d\Phi_B/dt$|
|**Magnetic flux**|Determined by field component along the chosen area normal|$\Phi_B=\int\vec B\cdot d\vec A$|
|**Electric flux**|Determined by field component along the chosen area normal|$\Phi_E=\int\vec E\cdot d\vec A$|

**Flux sign convention:**

- Field aligned with chosen area normal → positive flux.
    
- Field opposite chosen area normal → negative flux.
    
- Field perpendicular to area normal → zero flux.
    

For closed surfaces, area normals conventionally point outward.

---

## 4. Into and Out of the Page

|Symbol|Meaning|Mnemonic|
|---|---|---|
|$\odot$ or •|Vector comes **out of the page**, toward you|Arrowhead approaching you|
|$\otimes$ or ×|Vector goes **into the page**, away from you|Tail feathers of departing arrow|

These symbols can represent $\vec E$, $\vec B$, $\vec v$, $\vec F$, current, or any other vector.

They do not uniquely represent magnetic fields.

### Quick Cross-Product Reference

Take:

- Right = $+\hat x$
    
- Up = $+\hat y$
    
- Out of page = $+\hat z$
    

|First vector|Second vector|Cross-product direction|
|---|---|---|
|Right|Up|Out of page|
|Up|Right|Into page|
|Right|Out of page|Down|
|Right|Into page|Up|
|Up|Out of page|Right|
|Up|Into page|Left|
|Out of page|Right|Up|
|Into page|Right|Down|
|Forward|Up|Right (aircraft-relative coordinates)|

**Mnemonic:** $,\hat x\times\hat y=\hat z,\quad\hat y\times\hat z=\hat x,\quad\hat z\times\hat x=\hat y$.

Reverse any pair to reverse the result.

---

## 5. Induction — Direction-Finding Procedure

For Faraday's law / Lenz's law problems:

1. **Identify the source magnetic field:** Determine the direction of $\vec B$ through the affected loop.
    
2. **Determine the flux change:** Is the flux into or out of the page increasing or decreasing?
    
3. **Apply Lenz's law:** The induced field opposes the change in flux.
    
4. **Apply the loop grip rule:** Thumb = induced $\vec B$; fingers = induced conventional current.
    

|Original magnetic flux|Induced $\vec B$|Induced current|
|---|---|---|
|Increasing into page|Out of page|Counterclockwise|
|Decreasing into page|Into page|Clockwise|
|Increasing out of page|Into page|Clockwise|
|Decreasing out of page|Out of page|Counterclockwise|

**Crucial:** The induced magnetic field opposes the change in flux, not necessarily the original magnetic field or source current.

If the magnetic flux through a stationary loop does not change, its induced emf from Faraday's law is zero, even when the surrounding magnetic field changes in magnitude.

---

## 6. Which Rule Do I Use?

|Problem asks...|Start with...|
|---|---|
|Which way does a charged particle deflect?|Magnetic-force three-finger rule|
|Which end of a moving rod becomes positive?|$\vec v\times\vec B$|
|Which way does a current-carrying wire move?|$I\vec L\times\vec B$|
|Which way does $\vec B$ circulate around a wire?|Straight-wire grip rule|
|Which direction is $\vec B$ inside a solenoid?|Solenoid grip rule|
|Which direction is the magnetic dipole moment?|Current-loop grip rule|
|Which way will a dipole rotate?|$\vec p\times\vec E$ or $\vec\mu\times\vec B$|
|Which direction is the induced current?|Lenz's law → loop grip rule|
|Is magnetic or electric flux positive or negative?|Compare field vector with area normal|
|What direction is a Biot–Savart field contribution?|$d\vec\ell\times\hat r$|
|What is the sign of enclosed current in Ampère's law?|Path-normal right-hand orientation|
|Which way does an electric field point?|Charge signs / Coulomb's law, not a right-hand rule|

---

## 7. Essential Reminders

- **Magnetic force is perpendicular to both velocity and magnetic field.**
    
- **A negative charge reverses the magnetic-force direction.**
    
- **Conventional current follows positive-charge motion, not electron drift.**
    
- **A cross product is order-sensitive.**
    
- **Magnetic field around a straight wire forms concentric circles.**
    
- **Magnetic dipole moment follows the loop's area-normal direction selected by current.**
    
- **Magnetic flux depends on field orientation relative to a surface normal.**
    
- **An induced current responds to changing flux, not simply the existence of a magnetic field.**
    
- **Torque vectors specify an axis and rotation sense, not a linear force direction.**
    

### Master Decision Rule

**If you see a cross product → three-finger rule.**

**If you see a straight wire or current loop → right-hand grip rule.**

**If you see induced current → Lenz's law first, then right-hand grip rule.**

**If you see electric force or flux → use charge signs or vector orientation, not automatically a right-hand rule.**

