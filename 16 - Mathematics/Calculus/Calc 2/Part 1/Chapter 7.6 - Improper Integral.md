
# Improper Integrals: Convergence and Divergence Tests

## Definition

An improper integral is an integral in which:

1. One or both limits of integration are infinite.
2. The integrand becomes unbounded at one or more points in the interval.

Examples:

$$
\int_1^\infty \frac{1}{x^2}\,dx
$$

$$
\int_0^1 \frac{1}{\sqrt{x}}\,dx
$$

---

# Infinite Intervals

## Type I Improper Integrals

Integrals extending to infinity:

$$
\int_a^\infty f(x)\,dx
=
\lim_{t\to\infty}
\int_a^t f(x)\,dx
$$

Converges if the limit exists and is finite.

Similarly,

$$
\int_{-\infty}^a f(x)\,dx
=
\lim_{t\to-\infty}
\int_t^a f(x)\,dx
$$

For both sides infinite:

$$
\int_{-\infty}^{\infty} f(x)\,dx
=
\int_{-\infty}^c f(x)\,dx
+
\int_c^\infty f(x)\,dx
$$

Both pieces must converge.

---

# Vertical Asymptotes

## Type II Improper Integrals

If \(f(x)\) is unbounded at \(x=a\):

$$
\int_a^b f(x)\,dx
=
\lim_{t\to a^+}
\int_t^b f(x)\,dx
$$

If unbounded at \(x=b\):

$$
\int_a^b f(x)\,dx
=
\lim_{t\to b^-}
\int_a^t f(x)\,dx
$$

If the asymptote occurs inside the interval:

$$
\int_a^b f(x)\,dx
=
\int_a^c f(x)\,dx
+
\int_c^b f(x)\,dx
$$

Both pieces must converge.

---

# p-Integral Test

The most important convergence result.

## Infinite Tail

Consider

$$
\int_1^\infty \frac{1}{x^p}\,dx
$$

Converges when:

$$
p > 1
$$

Diverges when:

$$
p \le 1
$$

### Examples

Converges:

$$
\int_1^\infty \frac{1}{x^2}\,dx
$$

$$
\int_1^\infty \frac{1}{x^{3/2}}\,dx
$$

Diverges:

$$
\int_1^\infty \frac{1}{x}\,dx
$$

$$
\int_1^\infty \frac{1}{\sqrt{x}}\,dx
$$

---

## Near Zero

Consider

$$
\int_0^1 \frac{1}{x^p}\,dx
$$

Converges when:

$$
p < 1
$$

Diverges when:

$$
p \ge 1
$$

### Examples

Converges:

$$
\int_0^1 \frac{1}{\sqrt{x}}\,dx
$$

Diverges:

$$
\int_0^1 \frac{1}{x}\,dx
$$

$$
\int_0^1 \frac{1}{x^2}\,dx
$$

---

# Tail Behavior Cheat Sheet

For large \(x\):

| Function        | Behavior                 |
| --------------- | ------------------------ |
| \(1/x^2\)       | Converges                |
| \(1/x^{1.1}\)   | Converges                |
| $(1/x$          | Diverges                 |
| \(1/\sqrt{x}\)  | Diverges                 |
| $1$)            | Diverges                 |
| $(ln(x)/x^2$    | Converges                |
| \(\sin(x)/x^2\) | Converges                |
| \(\sin(x)/x\)   | Conditionally convergent |
| \(e^{-x}\)      | Converges                |

---

# Comparison Test

Suppose

$$
0 \le f(x) \le g(x)
$$

for sufficiently large \(x\).

## Convergence

If

$$
\int_a^\infty g(x)\,dx
$$

converges, then

$$
\int_a^\infty f(x)\,dx
$$

also converges.

---

## Divergence

If

$$
0 \le g(x) \le f(x)
$$

and

$$
\int_a^\infty g(x)\,dx
$$

diverges, then

$$
\int_a^\infty f(x)\,dx
$$

also diverges.

---

# Limit Comparison Test

If

$$
f(x),g(x) > 0
$$

and

$$
\lim_{x\to\infty}
\frac{f(x)}{g(x)}
=
L
$$

where

$$
0 < L < \infty,
$$

then

$$
\int_a^\infty f(x)\,dx
$$

and

$$
\int_a^\infty g(x)\,dx
$$

have the same convergence behavior.

---

# Common Comparison Targets

When \(x\to\infty\):

### Rational Functions

$$
\frac{x^m}{x^n}
\sim
\frac{1}{x^{n-m}}
$$

Only highest powers matter.

Example:

$$
\frac{5x^2+1}{3x^5-7}
\sim
\frac{5}{3x^3}
$$

---

### Logarithms

Logs grow extremely slowly.

For large \(x\):

$$
\ln(x) \ll x^k
$$

for any \(k>0\).

Useful comparisons:

$$
\frac{\ln x}{x^2}
\sim
\frac{1}{x^2}
$$

---

### Exponentials

Exponentials dominate powers.

For large \(x\):

$$
e^x \gg x^n
$$

Therefore:

$$
\frac{x^5}{e^x}
$$

behaves like an exponentially decaying function and converges.

---

# Quick Recognition Rules

## Infinite Tails

### Usually Converges

$$
\frac{1}{x^p}
\quad (p>1)
$$

$$
e^{-x}
$$

$$
\frac{\ln x}{x^2}
$$

---

### Usually Diverges

$$
\frac{1}{x}
$$

$$
\frac{1}{x^p}
\quad (p\le1)
$$

$$
\ln x
$$

$$
1
$$

---

# Memory Rules

## Infinity

For

$$
\int_1^\infty \frac{1}{x^p}\,dx
$$

- Big powers converge.
- Small powers diverge.

$$
p>1 \Rightarrow \text{Converges}
$$

---

## Near Zero

For

$$
\int_0^1 \frac{1}{x^p}\,dx
$$

the rule flips:

$$
p<1 \Rightarrow \text{Converges}
$$

---

## Mnemonic

At infinity:

> "Need more than \(1/x\)."

Near zero:

> "Need less singular than \(1/x\)."


# Examples

## Example 1 - Simple p of 1 for infinite tail

$$
\int_{1}^{\infty} \frac{1}{t}dx
$$

> [!answer]- Answer
> ![[improperint1.pdf]]
> Divergent



## Example 2 - 