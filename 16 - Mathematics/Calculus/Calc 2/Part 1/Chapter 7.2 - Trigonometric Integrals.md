

# Integrals of Powers of Sine and Cosine

These will be integrals in which the integrand is a power of sine, a power of cosine, or a product of these.

## Example 1

Evaluate 

$$
\int \cos^3xdx
$$

Trying to substitute $u=cosx$ doesn't really work, since $du$ would then be $-sinxdx$. In order to integrate powers of cosine, we'd need an extra $sinx$ factor.  Conversely, a power of sine would need a $cosx$ factor.  So, we can separate one of the cosine factors and turn the remaining $cos^2x$ to an expression that involves sine using the fundamental pythagorean identity ($\sin^2x+\cos^2x=1$).

This works specifically in the case where one of the powers of the trig functions is odd, as this allows the use of this strategy wherein a spare factor can be reduced, thus allowing simple substitution and algebraic manipulation to express the integrand in terms of one factor, thus allowing the substitution variable to express the entire form.

Tl;dr - Odd powers good, allows you to then use identities.


> [!answer]- Answer
> ![[Pasted image 20260524174215.png]]


# Example 2 

Find

$$
\int \sin^5x\cos^2xdx
$$
You might be tempted to convert the cosine factor here, but then we would be left with an expression in terms of $sinx$ with no extra $cosx$ factor.  Instead, separate a single sine factor and rewrite the remaining $sin^4 x$ factor in terms of $cosx$.

> [!answer]- Answer
> 

# If both trig functions are even

If both are even, then you want to rewrite in terms of cosine specifically through use of reduction identities. 

# Tan and secant

# Integrals Involving Powers of $\tan(x)$ and $\sec(x)$

For integrals of the form

$$
\int \tan^m(x)\sec^n(x)\,dx
$$

use the following decision tree.

---

## Case 1: The Power of $\sec(x)$ is Even

If $n$ is even:

1. Save a factor of

$$
\sec^2(x)\,dx
$$

2. Convert the remaining secants using

$$
\sec^2(x)=1+\tan^2(x)
$$

3. Let

$$
u=\tan(x)
$$

so that

$$
du=\sec^2(x)\,dx
$$

---

## Case 2: The Power of $\tan(x)$ is Odd

If $m$ is odd:

1. Save a factor of

$$
\sec(x)\tan(x)\,dx
$$

2. Convert the remaining tangents using

$$
\tan^2(x)=\sec^2(x)-1
$$

3. Let

$$
u=\sec(x)
$$

so that

$$
du=\sec(x)\tan(x)\,dx
$$

---

# Example

Evaluate

$$
\int \tan^8(x)\sec^4(x)\,dx
$$

Since the power of $\sec(x)$ is even, save a factor of

$$
\sec^2(x)\,dx
$$

Rewrite

$$
\sec^4(x)=\sec^2(x)\sec^2(x)
$$

and keep one factor of $\sec^2(x)\,dx$.

Convert the remaining secant factor:

$$
\sec^2(x)=1+\tan^2(x)
$$

giving

$$
\int \tan^8(x)\sec^4(x)\,dx
=
\int \tan^8(x)(1+\tan^2(x))\sec^2(x)\,dx
$$

Now let

$$
u=\tan(x)
$$

so that

$$
du=\sec^2(x)\,dx
$$

The integral becomes

$$
\int u^8(1+u^2)\,du
$$

Expand:

$$
\int (u^8+u^{10})\,du
$$

and integrate normally.

---

## Identities to Memorize

$$
\sec^2(x)=1+\tan^2(x)
$$

$$
\tan^2(x)=\sec^2(x)-1
$$

$$
\frac{d}{dx}[\tan(x)]
=
\sec^2(x)
$$

$$
\frac{d}{dx}[\sec(x)]
=
\sec(x)\tan(x)
$$
# Example 3

$$
\int\sin^2x\cos^5xdx
$$

> [!answer]- Answer
  ![[Scan from 2026-06-10 10_38_15 AM.pdf]]


# Example 4


$$
\int \cos^4tdt
$$


> [!answer]- Answer
> 

# Example 5

$$
\int \tan^2(t)\sec^4(t)dt
$$

> [!answer]- Answer
> 


# Example 6

$$
\int \sec^3xdx
$$

> [!answer]- Answer
> ![[Pasted image 20260614155404.png]]

# CIR — Cognitive Inquiry & Remediation



Welcome to the Cognitive Inquiry and Remediation section of this note.  Here you can evaluate your own progress on this topic and seek out recommendation for additional repair. Use the following rubric to score yourself for each question and add up the values at the end.

Your score will correspond to an appropriate remediation plan, but you may include other tasks as you see fit.
## Rubric

| Score | Meaning                                           |
| ----- | ------------------------------------------------- |
| 1     | Cannot explain or apply                           |
| 2     | Partial or unstable understanding                 |
| 3     | Functional understanding and standard application |
| 4     | Integrated understanding and transfer capability  |



# CIR Assessment

## 1. Identity

What IS this concept?

Score: `1/4`



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

- [ ]  Forgetting steps
    
- [ ]  Misidentifying problem type
    
- [ ]  Weak algebra manipulation
    
- [ ]  Cannot visualize
    
- [ ]  Cannot connect equations to meaning
    
- [ ]  Sign/notation errors
    
- [ ]  Understand concept but cannot execute
    
- [ ]  Slow recognition speed
    
- [ ]  Other:




# Remediation Plan

Based on your overall score, please follow the links below to access your remediation plan:

**1-6**: [[Mathematics CIR Remediation Protocol#Score Band 1–6|Shallow]]

**7-10**: [[Mathematics CIR Remediation Protocol#Score Band 7-10|Moderate]]

**11-14** [[Mathematics CIR Remediation Protocol#Score Band 11–14|Strong]]

**15-16**: [[Mathematics CIR Remediation Protocol#Score Band 15–16|Master]]





