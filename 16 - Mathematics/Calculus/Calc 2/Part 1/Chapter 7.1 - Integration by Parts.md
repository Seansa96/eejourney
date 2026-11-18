The Product rule for derivatives states

$$
\frac{d}{dx}[f(x)g(x)]=f'(x)g(x)+g'(x)f(x)
$$

For an indefinite integrals, this becomes

$$
\int f(x)g'(x)+g(x)f'(x)
$$

or

$$
\int f'(x)g(x)+\int g'(x)f(x)
$$

Put simply, and involving substitution, this becomes:

$$
\int udv = uv-\int vdu
$$

## Example 1

$\int xe^{2x}dx$

> [!answer]- Answer
> ![[Pasted image 20260517195528.png]]

# LIPET
**L** - Ln
**I** - Inverse Trig
**P** - Powers of x
**E** - Exponential 
**T** - Trig 

or

# LIATE

**L** - Logarithm
**I** - Inverse Trig
**A** - Algebraic Polynomial
**T** - Trig
**E** - Exponential


$$
\int x^2 \ln xdx
$$

So for this one, we would pick $\ln x$ instead of $x^2$.


# Tabular Integration by Parts

Doesn't always work, but when we have a polynomial multiplied by a basic trigonometric or exponential function, it is useful.

Something like

$$
\int t^5 \sin(kt)
$$

where sin could be cos or $e^x$.

You then create a column of **Derivatives** and **Integrals**. In the derivative column, differentiate until you reach 0. In the integration column, integrate until you reach the same row as the derivative.  
## Example 2 

$$
\int x \sin x dx
$$

> [!answer]- Answer
> ![[Pasted image 20260518101329.png]]

# Example 3

$$
\int \ln x dx
$$


# Example 4 

$$
\int t^2e^t dt
$$

> [!answer]- Answer
> ![[Pasted image 20260518120916.png]]

## Example 5

$$
\int e^x\sin x
$$

> [!answer]- Answer
> ![[Pasted image 20260524152543.png]]


# Example 6

$$
\int 3x \cos(5x)dx
$$

> [!answer]- Answer
> 

# Example 7 

$$
4ue^{-6u}du
$$


> [!answer]- Answer
> 

# Example 8

$$
p^2 \ln p dp
$$

> [!answer]- Answer
> ![[Scan from 2026-06-09 10_44_40 AM.pdf]]

# Example 9 

$$
\int \arcsin dx
$$

> [!answer]- Answer
> ![[Scan from 2026-06-09 11_01_21 AM.pdf]]


# Example 10


Assume K is constant

$$
\int t^2 \sin(kt)dt
$$

> [!answer]- Answer
> ![[Scan from 2026-06-09 11_15_45 AM.pdf]]


# Example 11 - Definite Integral

$$
\int_{0}^1 (x^2+1)e^{-x}dx
$$
> [!answer]- Answer
> 


# Harder Examples

## Example 12

$$
\int e^{2x}\sin(3x)dx
$$
> [!answer]- Answer
> 

To solve this, we require the use of a particular strategy which requires a double integration by parts and thus expresses the integral as a standalone component, known as some dummy variable.

## Example 13 - Requires Review

$$
\int9t\sec^2(2t)dt
$$
> [!answer]- Answer
> 


## Example 14

$$
\int 9x^{11} \cos(1-x^6)dx
$$

> [!answer]- Answer
> 

For this problem, consider the following:

Standard U-sub or Integration by parts cannot be done. The argument of cos is too complex. However, we can represent the integrand in terms of other values. The idea is to first reduce the complexity of the argument, then using what the argument then represents, we can cancel out factors of the polynomial in the integrand and represent them in terms of the argument.


# CIR — Cognitive Inquiry & Remediation



Welcome to the Cognitive Inquiry and Remediation section of this note.  Here you can evaluate your own progress on this topic and seek out recommendation for additional repair. Use the following rubric to score yourself for each question and add up the values at the end.

Your score will correspond to an appropriate remediation plan, but you may include other tasks as you see fit.
## Rubric

|Score|Meaning|
|---|---|
|1|Cannot explain or apply|
|2|Partial or unstable understanding|
|3|Functional understanding and standard application|
|4|Integrated understanding and transfer capability|



# CIR Assessment

## 1. Identity

What IS this concept?

Score: `/4`



## 2. Purpose

What problem does it solve, and why does it matter?

Score: `/4`



## 3. Application

When should this be used, and can I reliably recognize/apply it?

Score: `/4`



## 4. System Integration

What larger system does this belong to? What concepts does it connect to?

Score: `/4`



# Failure Analysis

## Primary Friction Type

- [ ]  Symbolic
    
- [ ]  Visual
    
- [ ]  Translation
    
- [ ]  Procedural
    
- [ ]  Memory
    
- [ ]  Abstraction
    
- [ ]  Pattern Recognition
    
- [ ]  Other:





## Common Failure Modes

- [x]  Forgetting steps
    
- [ ]  Misidentifying problem type
    
- [ ]  Weak algebra manipulation
    
- [ ]  Cannot visualize
    
- [ ]  Cannot connect equations to meaning
    
- [x]  Sign/notation errors
    
- [ ]  Understand concept but cannot execute
    
- [ ]  Slow recognition speed
    
- [ ]  Other:




# Remediation Plan

Based on your overall score, please follow the links below to access your remediation plan. Remember that these are only recommendations:

**1-6**: [[Mathematics CIR Remediation Protocol#Score Band 1–6|Shallow]]

**7-10**: [[Mathematics CIR Remediation Protocol#Score Band 7-10|Moderate]]

**11-14** [[Mathematics CIR Remediation Protocol#Score Band 11–14|Strong]]

**15-16**: [[Mathematics CIR Remediation Protocol#Score Band 15–16|Master]]





