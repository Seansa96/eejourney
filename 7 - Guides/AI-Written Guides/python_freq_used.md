For learning Calc II, Physics, and numerical methods, I'd recommend **learning Python's math syntax directly** rather than relying on a LaTeX-to-Python layer. You'll end up reading and writing far more Python than LaTeX in computational work.

That said, there _are_ tools like SymPy that can parse some mathematical expressions from strings, and Jupyter notebooks render LaTeX beautifully in Markdown cells.

# Python Math Cheat Sheet

## Basic Arithmetic

|Math|Python|
|---|---|
|(a+b)|`a + b`|
|(a-b)|`a - b`|
|(ab)|`a * b`|
|(\frac{a}{b})|`a / b`|
|(a^b)|`a ** b`|
|(\sqrt{a})|`a**0.5` or `sqrt(a)`|
|(|a|

```python
2 + 3
2 * 3
2 ** 5
25 ** 0.5
abs(-17)
```

---
## Conversions

Converting between a decimal and fraction can be handled by the **Fractions** module.
```
from fractions import Fraction
```

And then use the limit denominator function. You can specify to what place you'd like to truncate it to as well, but by default it tries to find the smallest one typically.

```
Fraction(0.333333333333).limit_denominator() //output = 1/3
```
## Importing Math Functions

```python
from math import *
```

or (usually preferred)

```python
import math
```

then:

```python
math.sin(x)
math.cos(x)
```

---

## Constants

```python
from math import pi, e
```

|Math|Python|
|---|---|
|(\pi)|`pi`|
|(e)|`e`|

---

## Trigonometry

Assumes **radians**.

|Math|Python|
|---|---|
|(\sin(x))|`sin(x)`|
|(\cos(x))|`cos(x)`|
|(\tan(x))|`tan(x)`|
|(\sin^{-1}(x))|`asin(x)`|
|(\cos^{-1}(x))|`acos(x)`|
|(\tan^{-1}(x))|`atan(x)`|

```python
from math import *

sin(pi/2)
cos(pi)
```

---

## Degrees ↔ Radians

```python
degrees(pi)
```

```python
radians(90)
```

---

## Logs and Exponentials

|Math|Python|
|---|---|
|(e^x)|`exp(x)`|
|(\ln(x))|`log(x)`|
|(\log_{10}(x))|`log10(x)`|
|(\log_b(x))|`log(x,b)`|

```python
log(10)
exp(3)
```

---

## Useful Calc Expressions

### (x^2 \sin(x))

```python
x**2 * sin(x)
```

### (\frac{x^2+1}{x-3})

```python
(x**2 + 1) / (x - 3)
```

### (e^{-x^2})

```python
exp(-x**2)
```

Notice:

```python
-x**2
```

means:

[  
-(x^2)  
]

not

[  
(-x)^2  
]

---

## Defining Functions

### Standard

```python
def f(x):
    return x**2 + 3*x - 7
```

### Quick Lambda

```python
f = lambda x: x**2 + 3*x - 7
```

Very common for numerical integration.

---

## Summation

Mathematical:

[  
\sum_{i=1}^{n} i^2  
]

Python:

```python
sum(i**2 for i in range(1, n+1))
```

---

## Products

[  
\prod_{i=1}^{n} i  
]

```python
from math import prod

prod(i for i in range(1, n+1))
```

---

## Numerical Derivative

```python
def derivative(f, x, h=1e-5):
    return (f(x+h)-f(x))/h
```

---

## Numerical Integral

Using your midpoint rule:

```python
midpoint_rule(f, 0, 3, 1000)
```

---

# NumPy Syntax

Once you start graphing:

```python
import numpy as np
```

Use:

```python
np.sin(x)
np.cos(x)
np.exp(x)
np.log(x)
```

instead of the `math` versions.

The `math` versions work on one number.

The NumPy versions work on entire arrays.

---

# Jupyter Math Workflow

### Markdown Cell

Write:

```markdown
$$
\int_0^1 x^2\,dx
$$
```

and Jupyter renders it.

### Code Cell

```python
from math import *

f = lambda x: x**2
midpoint_rule(f, 0, 1, 100)
```

This is how most scientists, engineers, and mathematicians work.

---

# Closest Thing to "LaTeX Input"

With SymPy:

```python
from sympy import *

x = symbols('x')
expr = sympify("x**2*sin(x)")
```

or

```python
from sympy.parsing.latex import parse_latex

expr = parse_latex(r"\frac{x^2+1}{x-3}")
```

However:

- It's slower.
    
- It occasionally misparses.
    
- Most tutorials and libraries use standard Python syntax.
    

So I'd treat LaTeX parsing as a convenience feature, not your primary workflow.

# The 20 Expressions You'll Type Constantly

```python
x**2
x**3
sqrt(x)
sin(x)
cos(x)
tan(x)
asin(x)
acos(x)
atan(x)
exp(x)
log(x)
pi
e
abs(x)
sum(...)
max(...)
min(...)
f = lambda x: ...
def f(x):
return ...
```

Once those become muscle memory, you'll be able to translate almost any Calc II or Physics equation into Python in a few seconds.