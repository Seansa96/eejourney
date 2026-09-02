# Calculus II - Unit 2 Cheat Sheet (Obsidian)

# Area Between Curves

## Vertical Slices ((dx))

Use when the region is easiest described as:

- Top function
    
- Bottom function
    

$$  
A=\int_a^b \left(f(x)-g(x)\right),dx  
$$

where

$$  
f(x)=\text{Top}  
$$

$$  
g(x)=\text{Bottom}  
$$

---

## Horizontal Slices ((dy))

Use when the region is easier described as:

- Right function
    
- Left function
    

$$  
A=\int_c^d \left(x_{\text{right}}-x_{\text{left}}\right),dy  
$$

---

# Volumes of Revolution

## Disk Method

Used when there is **no hole**.

### About the x-axis

$$  
V=\pi\int_a^b R(x)^2,dx  
$$

### About the y-axis

$$  
V=\pi\int_c^d R(y)^2,dy  
$$

---

## Washer Method

Used when there **is a hole**.

### About the x-axis

$$  
V=\pi\int_a^b\left(R(x)^2-r(x)^2\right),dx  
$$

### About the y-axis

$$  
V=\pi\int_c^d\left(R(y)^2-r(y)^2\right),dy  
$$

---

## Shell Method

Used when slices are **parallel** to the axis of rotation.

$$  
V=2\pi\int (\text{radius})(\text{height}),d(\text{variable})  
$$

Examples

About the y-axis

$$  
V=2\pi\int_a^b x\left(f(x)-g(x)\right),dx  
$$

About the x-axis

$$  
V=2\pi\int_c^d y\left(x_{\text{right}}-x_{\text{left}}\right),dy  
$$

---

# Volumes by Cross Sections

General Formula

$$  
V=\int A(x),dx  
$$

or

$$  
V=\int A(y),dy  
$$

where

$$  
A=\text{Area of one cross section}  
$$

---

## Square

If side length is (s)

$$  
A=s^2  
$$

---

## Rectangle

If dimensions are (b) and (h)

$$  
A=bh  
$$

---

## Semicircle

If diameter is (d)

$$  
A=\frac{\pi}{8}d^2  
$$

If radius is (r)

$$  
A=\frac12\pi r^2  
$$

---

## Circle

$$  
A=\pi r^2  
$$

---

## Equilateral Triangle

If side length is (s)

$$  
A=\frac{\sqrt3}{4}s^2  
$$

---

## Right Isosceles Triangle

### If the leg is given

$$  
A=\frac12L^2  
$$

### If the hypotenuse is given

$$  
A=\frac14H^2  
$$

---

# Arc Length

For

$$  
y=f(x)  
$$

$$  
L=\int_a^b\sqrt{1+\left(f'(x)\right)^2},dx  
$$

For

$$  
x=g(y)  
$$

$$  
L=\int_c^d\sqrt{1+\left(g'(y)\right)^2},dy  
$$

---

# Surface Area of Revolution

About the x-axis

$$  
S=2\pi\int_a^b y\sqrt{1+\left(y'\right)^2},dx  
$$

About the y-axis

$$  
S=2\pi\int_a^b x\sqrt{1+\left(y'\right)^2},dx  
$$

If integrating with respect to (y)

About the y-axis

$$  
S=2\pi\int_c^d x\sqrt{1+\left(x'\right)^2},dy  
$$

About the x-axis

$$  
S=2\pi\int_c^d y\sqrt{1+\left(x'\right)^2},dy  
$$

---

# Center of Mass (Uniform Density)

Area

$$  
A=\int (Top-Bottom),dx  
$$

Centroid

$$  
\bar{x}=\frac{M_y}{A}  
$$

$$  
\bar{y}=\frac{M_x}{A}  
$$

Moments

$$  
M_y=\int x(Top-Bottom),dx  
$$

$$  
M_x=\frac12\int\left(f(x)^2-g(x)^2\right),dx  
$$

---

# Center of Mass (Variable Density)

Mass

$$  
m=\int\rho(x)(Top-Bottom),dx  
$$

Centroid

$$  
\bar{x}=\frac{M_y}{m}  
$$

$$  
\bar{y}=\frac{M_x}{m}  
$$

Moments

$$  
M_y=\int x,\rho(x)(Top-Bottom),dx  
$$

$$  
M_x=\frac12\int\rho(x)\left(f(x)^2-g(x)^2\right),dx  
$$

---

# Average Value

# $$  
f_{\text{avg}}

\frac1{b-a}  
\int_a^b f(x),dx  
$$

Mean Value Theorem for Integrals

Find

$$  
c  
$$

such that

$$  
f(c)=f_{\text{avg}}  
$$

---

# Quick Decision Checklist

## Should I use (dx) or (dy)?

### Use (dx) if

- Vertical slices
    
- Top − Bottom
    
- Functions are already (y=f(x))
    
- Simpler algebra
    

### Use (dy) if

- Horizontal slices
    
- Right − Left
    
- Functions are (x=f(y))
    
- Avoid solving for (x)
    

---

## Disk or Washer?

Ask:

> Does the solid have a hole?

No

→ Disk

Yes

→ Washer

---

## Shells?

Ask:

> Are my slices parallel to the axis of rotation?

Yes

→ Shells

Remember

$$  
2\pi(\text{radius})(\text{height})  
$$

---

## Cross Sections?

1. Find the base length.
    
2. Determine what that length represents.
    
3. Apply the correct area formula.
    
4. Integrate the slice area.
    

---

## Surface Area?

Always remember

- Radius
    
- Arc Length
    

$$  
2\pi(\text{radius}),ds  
$$

where

$$  
ds=\sqrt{1+\left(f'(x)\right)^2},dx  
$$

---

# Universal Problem-Solving Order

1. Sketch the region.
    
2. Determine bounds.
    
3. Decide (dx) or (dy).
    
4. Identify the geometric quantity.
    
5. Determine slice dimensions.
    
6. Write the integrand.
    
7. Check units.
    
8. Integrate (or use calculator if permitted).