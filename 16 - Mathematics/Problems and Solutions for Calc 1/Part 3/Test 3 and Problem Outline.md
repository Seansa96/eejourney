
# Calc Test 3 – Targeted Practice Guide

---

## 1. Particle Motion Problems

**Subject:** Position, Velocity, Acceleration  
**Core Idea:** Derivatives describe motion layers

- ( s(t) ) → position
    
- ( v(t) = s'(t) ) → velocity
    
- ( a(t) = v'(t) = s''(t) ) → acceleration
    

**What they test:**

- When is particle at rest → ( v(t)=0 )
    
- Direction of motion → sign of ( v(t) )
    
- Speeding up/slowing down → compare signs of ( v(t) ) and ( a(t) )
    
- Total distance → integral of **|velocity|**
    
- Graph relationships between ( s, v, a )
    

**Drills:**

1. Given  $$s(t)=t^3-6t^2+9t $$
Find 

a. Velocity at time $t$
b. What is the velocity after 1 second?
c. When is the particle at rest?
d. When is the particle moving in the positive direction?
e. Find the total distance traveled during the first 6 seconds.
f Draw a diagram like Figure 2 to illustrate the motion of the particle.
g. Find the acceleration at time $t$ and after 1 second.
h. Graph the position, velocity, and acceleration function for $0 \leq t \leq 6$.
i. When is the particle speeding up? When is it slowing down?


> [!answer]- Answer
> ![[Pasted image 20260418194925.png]]





---

## 2. L’Hospital’s Rule

**Subject:** Limits & Indeterminate Forms

**Core Idea:** Only applies to:

- $$ \frac{0}{0} ,  \frac{\infty}{\infty} $$


**What they test:**

- Algebra BEFORE L’Hospital
    
- Multiple applications
    
- Recognizing hidden indeterminate forms
    

**Drills:**

Evaluate:  
$$\lim_{x\to 0} \frac{e^x - 1 - x}{x^2}  $$

> [!answer]- Answer
> ![[Pasted image 20260418195233.png]]


Rewrite then evaluate:  
$$\lim_{x\to \infty} \frac{\ln x}{x}  
    $$


> [!answer]- Answer
> ![[Pasted image 20260418195543.png]]


---

## 3. Mean Value Theorem (MVT)

**Subject:** Average vs Instantaneous Rate

**Core Idea:**  
If continuous + differentiable →  
there exists ( c ) such that:

$$
f'(c) = \frac{f(b)-f(a)}{b-a}  
$$

**What they test:**

- Checking conditions
    
- Solving for $c$
    
- Understanding geometric meaning
    

**Drills:**

1. Find all $c$ for $f(x)=x^2$ on $[1,5]$

> [!answer]- Answer
> ![[Pasted image 20260418203407.png]]



2. Verify MVT applies for $f(x)=\ln x$ on $[1,e]$
    
3. Interpret what $c$ means graphically
    
> [!answer]- Answer
> ![[Pasted image 20260418203726.png]]
> C means that there exists a point on the graph of the function where the slope at that point is equal to the slope of the overall function.



---

## 4. Given Graph of $f'(x)$, Describe $f(x)$

**Subject:** Derivative → Behavior

**What they test:**

- Increasing/decreasing → sign of ( f' )
    
- Concavity → slope of ( f' )
    
- Inflection points → where ( f' ) changes slope direction
    

**Drills:**

1. Given a sketch of ( f'(x) ), identify:
    
    - where ( f ) increases/decreases
        
2. Identify concavity from shape of $f'$
    
3. Mark relative extrema of $f$ from zeros of $f'$
    

---

## 5. Curve Sketching from Conditions

**Subject:** First & Second Derivative Analysis

**What they test:**

- Critical points
    
- Concavity
    
- Asymptotes
    
- End behavior
    

**Drills:**


   

---

## 6. Optimization

**Subject:** Max/Min Problems

**Core Idea:**

- Define variable
    
- Write constraint
    
- Reduce to ONE variable
    
- Differentiate and solve
    

**What they test:**

- Setup (most important)
    
- Correct constraint substitution
    
- Critical point + endpoints
    

**Drills:**

1. Maximize area of rectangle under curve
    
2. Minimize material for a box
    
3. Classic: fencing problem with fixed perimeter
    

---

## 7. Midpoint Rule (Definite Integral Approximation)

**Subject:** Riemann Sums

**Core Idea:**

- Use midpoint of each interval
    
- Multiply by $\Delta x$


**Drills:**

1. Approximate $$\int_0^4 x^2 dx$$ with 4 midpoints
    
2. Compare midpoint vs left sum
    
3. Practice quick interval splitting

> [!answer]- Answer
> ![[Pasted image 20260420230705.png]]


---

## 8. Table-Based Area / Distance Approximation

**Subject:** Numerical Integration

**What they test:**

- Left sum
    
- Right sum
    
- Midpoint sum
    
- Distance vs displacement distinction
    

**Drills:**

1. Given table, compute:
    
    - L4, R4, M4
        
2. Interpret whether over/under estimate
    
3. Convert velocity table → distance
    

---

## 9. Antiderivatives from Second Derivative

**Subject:** Reconstructing Functions

**Core Idea:**

- Integrate twice
    
- Use initial conditions to solve constants
    

**Drills:**

1. Given $f''(x)=6x$, $f'(0)=2$, $f(0)=1$, find $f(x)$
    
2. Practice constant tracking carefully
    
3. Verify by differentiating back
    

---

## 10. Trig + Sign Chart (Derivative Behavior)

**Subject:** Derivatives + Interval Analysis

**What they test:**

- Derivative of trig functions
    
- Sign charts
    
- Increasing/decreasing intervals
    

**Drills:**

1. For $f(x)=\sin x$ on $[0,2\pi]$:
    
    - find $f'(x)$
        
    - build sign chart


> [!answer]- Answer
> ![[Pasted image 20260421104603.png]]


2. Do same for cosine
    
3. Identify extrema from sign changes
    




# Second Set 

Alright—this is a **solid, exam-realistic set**. I’ll keep each one clean, but still at the level where you actually have to think a bit (like your tests). I’ll include **solutions right after each** so you can check yourself.

---

# **1. Particle Motion (multi-part)**

A particle moves along a line with position  
[  
s(t) = t^3 - 6t^2 + 9t  
]  
for (0 \le t \le 5).

### **Questions**

a) Find velocity and acceleration  
b) When is the particle at rest?  
c) When is it moving in the positive direction?  
d) When is it speeding up / slowing down?  
e) Find total distance traveled on ([0,5])  
f) Find (v(2))

---

### **Solution**

a)  
[  
v(t)=s'(t)=3t^2-12t+9  
]  
[  
a(t)=v'(t)=6t-12  
]

---

b) At rest when (v(t)=0):  
[  
3t^2-12t+9=0 \Rightarrow t^2-4t+3=0  
\Rightarrow (t-1)(t-3)=0  
]  
[  
t=1,3  
]

---

c) Moving positive when (v(t)>0)

Test intervals:

- (t<1): positive
    
- (1<t<3): negative
    
- (t>3): positive
    

So:  
[  
(0,1)\cup(3,5)  
]

---

d) Speeding up when (v) and (a) same sign

- (a(t)=0) at (t=2)
    

Check intervals:

|Interval|v|a|Behavior|
|---|---|---|---|
|(0,1)|+|-|slowing|
|(1,2)|-|-|speeding|
|(2,3)|-|+|slowing|
|(3,5)|+|+|speeding|

---

e) Total distance

Find position at key points:

[  
s(0)=0,\quad s(1)=4,\quad s(3)=0,\quad s(5)=20  
]

Distance:  
[  
|4-0| + |0-4| + |20-0| = 4+4+20 = 28  
]

---

f)  
[  
v(2)=3(4)-24+9=12-24+9=-3  
]

---

# **2. L'Hôpital's Rule**

Evaluate:  
$$
\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}  
$$

---

### **Solution**

Plug in:  
[  
\frac{0}{0} \Rightarrow \text{use L'Hôpital}  
]

First derivative:  
[  
\frac{e^x -1}{2x}  
]

Still (0/0), again:

[  
\frac{e^x}{2}  
]

Evaluate:  
[  
= \frac{1}{2}  
]

---

# **3. Mean Value Theorem**

Let $f(x)=x^2+2x) on ([1,4])$

Find (c) such that:  

$f'(c)=\frac{f(4)-f(1)}{4-1}$

---

### **Solution**

[  
f(4)=16+8=24,\quad f(1)=1+2=3  
]

Slope:  
[  
\frac{24-3}{3}=7  
]

Derivative:  
[  
f'(x)=2x+2  
]

Set equal:  
[  
2c+2=7 \Rightarrow c=\frac{5}{2}  
]

---

# **4. Given (f'(x)), describe (f)**

Suppose:

- (f'(x) > 0) on ((0,2))
    
- (f'(x) < 0) on ((2,5))
    
- (f'(2)=0)
    

---

### **Solution**

- Increasing on ((0,2))
    
- Decreasing on ((2,5))
    
- Local max at (x=2)
    

---

# **5. Sketch Based on Conditions**

Sketch a function where:

- (f'(x)>0) for all x
    
- (f''(x)<0) for all x
    

---

### **Solution**

- Increasing everywhere
    
- Concave down everywhere
    

Think:  
[  
f(x)=\ln(x+5)  
]

---

# **6. Optimization**

A rectangle has perimeter 20. Maximize area.

---

### **Solution**

Constraint:  
[  
2x+2y=20 \Rightarrow y=10-x  
]

Area:  
[  
A=x(10-x)=10x-x^2  
]

[  
A'=10-2x=0 \Rightarrow x=5  
]

[  
y=5  
]

Max area:  
[  
25  
]

---

# **7. Midpoint Approximation**

Approximate:  

$$\int_0^4 x^2 dx$$  
using 4 midpoints.

---

### **Solution**

[  
\Delta x=1  
]

Midpoints:  
0.5, 1.5, 2.5, 3.5

[  
f(x)=x^2  
]

[  
= (0.25 + 2.25 + 6.25 + 12.25)  
=21  
]

---

# **8. Table Approximation**

|x|0|1|2|3|
|---|---|---|---|---|
|f(x)|2|4|6|8|

Approximate using:

- Left
    
- Right
    
- Midpoint
    

---

### **Solution**

[  
\Delta x=1  
]

Left:  
[  
2+4+6=12  
]

Right:  
[  
4+6+8=18  
]

Midpoint (avg):  
[  
(12+18)/2=15  
]

---

# **9. Antiderivative from (f'')**

Given:  
[  
$$f''(x)=6x,\quad f'(0)=2,\quad f(0)=1$$

---

### **Solution**

Integrate:  
[  
f'(x)=3x^2 + C  
]

Use (f'(0)=2):  
[  
C=2  
]

[  
f'(x)=3x^2+2  
]

Integrate again:  
[  
f(x)=x^3+2x + C  
]

Use (f(0)=1):  
[  
C=1  
]

Final:  
[  
f(x)=x^3+2x+1  
]

---

# **10. Trig + Sign Chart**

Let:  
[  
$$f(x)=\sin x \quad \text{on } [0,2\pi]$$

---

### **Solution**

[  
f'(x)=\cos x  
]

Sign chart:

|Interval|cos(x)|Behavior|
|---|---|---|
|(0, π/2)|+|increasing|
|(π/2, 3π/2)|-|decreasing|
|(3π/2, 2π)|+|increasing|

Critical points:  
[  
x=\frac{\pi}{2},\frac{3\pi}{2}  
]

---

---

If you want, next step I’d recommend (based on your test style):

👉 I can turn this into a **mock exam** where you solve first and I grade it like your professor (including catching those tiny algebra slips you mentioned).
