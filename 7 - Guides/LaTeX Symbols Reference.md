# LaTeX Symbols Reference — Math, Physics, EE, and Chemistry

An Obsidian reference with rendered examples beside copyable source. Unless delimiters are already shown, put commands inside `$...$` for inline math or `$$...$$` for display math.

## Contents

- [[#1. Writing math in Obsidian]]
- [[#2. Greek letters]]
- [[#3. Relations, logic, sets, and functions]]
- [[#4. Calculus and differential equations]]
- [[#5. Vectors and vector calculus]]
- [[#6. Linear algebra and tensors]]
- [[#7. Complex numbers and transforms]]
- [[#8. Probability and statistics]]
- [[#9. Physics and electromagnetism]]
- [[#10. Electrical engineering]]
- [[#11. Units and typography]]
- [[#12. Copyable equation layouts]]
- [[#13. Chemistry]]
- [[#14. Rendering fixes]]

## 1. Writing math in Obsidian

Obsidian uses MathJax for math rendering. Use dollar delimiters as shown in [Obsidian's math formatting guide](https://obsidian.md/help/advanced-syntax).

Inline source:

```markdown
The force is $\vec{F}=q\vec{E}$.
```

The force is $\vec{F}=q\vec{E}$.

Display source:

```latex
$$
\oint_S\vec{E}\cdot\mathrm{d}\vec{A}
=\frac{Q_{\mathrm{enc}}}{\varepsilon_0}
$$
```

$$
\oint_S\vec{E}\cdot\mathrm{d}\vec{A}
=\frac{Q_{\mathrm{enc}}}{\varepsilon_0}
$$

| Task | Rendered | Source |
|---|---|---|
| Subscript | $q_1$ | `q_1` |
| Grouped subscript | $V_{\mathrm{rms}}$ | `V_{\mathrm{rms}}` |
| Superscript | $r^2$ | `r^2` |
| Grouped exponent | $e^{-j\omega t}$ | `e^{-j\omega t}` |
| Fraction | $\frac{a+b}{c}$ | `\frac{a+b}{c}` |
| Square root | $\sqrt{x^2+y^2}$ | `\sqrt{x^2+y^2}` |
| General root | $\sqrt[n]{x}$ | `\sqrt[n]{x}` |
| Text in math | $E_{\text{inside}}=0$ | `E_{\text{inside}}=0` |
| Upright label | $Q_{\mathrm{enc}}$ | `Q_{\mathrm{enc}}` |
| Boxed result | $\boxed{E=mc^2}$ | `\boxed{E=mc^2}` |

Braces group input without printing braces. A backslash introduces a command. Use explicit arguments: `\vec{E}`, `\hat{r}`, and `\frac{a}{b}`.

## 2. Greek letters

Meanings depend on context; these are common uses, not fixed definitions. Uppercase Greek letters that resemble Latin letters are normally written with the corresponding Latin character.

| Letter | Source | Common uses |
|---|---|---|
| $\alpha,\beta,\gamma$ | `\alpha,\beta,\gamma` | Angles; attenuation, phase constant, propagation constant |
| $\delta,\Delta$ | `\delta,\Delta` | Variation, impulse, finite change, Laplacian |
| $\epsilon,\varepsilon$ | `\epsilon,\varepsilon` | Small parameter, tolerance, permittivity |
| $\zeta$ | `\zeta` | Damping ratio |
| $\eta$ | `\eta` | Efficiency, intrinsic wave impedance |
| $\theta,\vartheta,\Theta$ | `\theta,\vartheta,\Theta` | Angles; step function in some texts |
| $\iota$ | `\iota` | Index or inclusion notation in some mathematics |
| $\kappa$ | `\kappa` | Curvature, dielectric constant in some texts |
| $\lambda,\Lambda$ | `\lambda,\Lambda` | Wavelength, eigenvalue, line charge density |
| $\mu$ | `\mu` | Permeability, mean, mobility |
| $\nu$ | `\nu` | Frequency in physics, degrees of freedom |
| $\xi,\Xi$ | `\xi,\Xi` | Dummy variable, random variable, correlation length |
| $\pi,\Pi$ | `\pi,\Pi` | Circle constant; uppercase pi |
| $\rho$ | `\rho` | Volume charge density, mass density, resistivity |
| $\sigma,\Sigma$ | `\sigma,\Sigma` | Surface charge density, conductivity, standard deviation |
| $\tau$ | `\tau` | Torque magnitude, time constant, delay |
| $\upsilon,\Upsilon$ | `\upsilon,\Upsilon` | Less common parameters; distinct from Latin v |
| $\phi,\varphi,\Phi$ | `\phi,\varphi,\Phi` | Phase, angle, potential, flux |
| $\chi$ | `\chi` | Susceptibility |
| $\psi,\Psi$ | `\psi,\Psi` | Wavefunction, stream function, flux linkage |
| $\omega,\Omega$ | `\omega,\Omega` | Angular frequency, solid angle; ohm symbol as a unit |

$\epsilon$ and $\varepsilon$ are stylistic variants, as are $\phi$ and $\varphi$. Choose consistently unless your source assigns separate meanings. Latin $v$, Greek $\nu$, and Greek $\upsilon$ are different characters. Greek omicron is usually written as Latin `o`.

## 3. Relations, logic, sets, and functions

| Meaning | Rendered | Source |
|---|---|---|
| Multiplication | $a\cdot b,\quad a\times b$ | `a\cdot b,\quad a\times b` |
| Plus/minus; minus/plus | $\pm,\mp$ | `\pm,\mp` |
| Not equal | $a\ne b$ | `a\ne b` |
| Approximately equal | $a\approx b$ | `a\approx b` |
| Asymptotically equivalent | $f(x)\sim g(x)$ | `f(x)\sim g(x)` |
| Proportional to | $F\propto r^{-2}$ | `F\propto r^{-2}` |
| Inequalities | $a\le b,\quad a\ge b$ | `a\le b,\quad a\ge b` |
| Much less/greater than | $a\ll b,\quad a\gg b$ | `a\ll b,\quad a\gg b` |
| Identity/equivalence | $f\equiv g$ | `f\equiv g` |
| Definition | $f(x):=x^2$ | `f(x):=x^2` |
| Implication | $P\implies Q$ | `P\implies Q` |
| If and only if | $P\iff Q$ | `P\iff Q` |
| For all; exists | $\forall x,\quad\exists y$ | `\forall x,\quad\exists y` |
| Not; and; or | $\neg P,\quad P\land Q,\quad P\lor Q$ | `\neg P,\quad P\land Q,\quad P\lor Q` |
| Infinity | $\infty$ | `\infty` |
| Ellipses | $\ldots,\cdots,\vdots,\ddots$ | `\ldots,\cdots,\vdots,\ddots` |
| Degrees; angle | $90^\circ,\quad\angle ABC$ | `90^\circ,\quad\angle ABC` |
| Number sets | $\mathbb{N},\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C}$ | `\mathbb{N},\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C}` |
| Membership | $x\in A,\quad x\notin B$ | `x\in A,\quad x\notin B` |
| Subset; proper subset | $A\subseteq B,\quad A\subsetneq B$ | `A\subseteq B,\quad A\subsetneq B` |
| Union; intersection | $A\cup B,\quad A\cap B$ | `A\cup B,\quad A\cap B` |
| Set difference | $A\setminus B$ | `A\setminus B` |
| Empty set | $\emptyset$ | `\emptyset` |
| Set builder | $\{x\in\mathbb{R}:x>0\}$ | `\{x\in\mathbb{R}:x>0\}` |
| Mapping | $f:A\to B,\quad x\mapsto x^2$ | `f:A\to B,\quad x\mapsto x^2` |
| Composition | $(f\circ g)(x)$ | `(f\circ g)(x)` |
| Limit | $\lim_{x\to a}f(x)$ | `\lim_{x\to a}f(x)` |
| One-sided limit | $\lim_{x\to a^+}f(x)$ | `\lim_{x\to a^+}f(x)` |
| Supremum; infimum | $\sup A,\quad\inf A$ | `\sup A,\quad\inf A` |
| Absolute value | $\lvert x\rvert$ | `\lvert x\rvert` |
| Norm | $\lVert\vec{v}\rVert$ | `\lVert\vec{v}\rVert` |
| Inner product | $\langle u,v\rangle$ | `\langle u,v\rangle` |
| Big O; little o | $O(h^2),\quad o(h)$ | `O(h^2),\quad o(h)` |
| Named functions | $\sin x,\cos x,\tan x,\ln x,\exp x$ | `\sin x,\cos x,\tan x,\ln x,\exp x` |
| Inverse trig | $\arcsin x,\arccos x,\arctan x$ | `\arcsin x,\arccos x,\arctan x` |
| Hyperbolic functions | $\sinh x,\cosh x,\tanh x$ | `\sinh x,\cosh x,\tanh x` |
| Custom named operator | $\operatorname{sgn}(x)$ | `\operatorname{sgn}(x)` |
| Minimizing argument | $\underset{x}{\operatorname{arg\,min}}\,f(x)$ | `\underset{x}{\operatorname{arg\,min}}\,f(x)` |

Whether $0\in\mathbb{N}$ depends on the author. Use $\approx$ for approximation; $\sim$ has other meanings, including distributions. `\arcsin x` avoids the possible reciprocal ambiguity of `\sin^{-1}x`.

## 4. Calculus and differential equations

| Meaning | Rendered | Source |
|---|---|---|
| Ordinary derivative | $\frac{\mathrm{d}y}{\mathrm{d}x}$ | `\frac{\mathrm{d}y}{\mathrm{d}x}` |
| Second derivative | $\frac{\mathrm{d}^2y}{\mathrm{d}x^2}$ | `\frac{\mathrm{d}^2y}{\mathrm{d}x^2}` |
| Prime notation | $f'(x),f''(x)$ | `f'(x),f''(x)` |
| Time derivatives | $\dot{x},\ddot{x}$ | `\dot{x},\ddot{x}` |
| Partial derivative | $\frac{\partial f}{\partial x}$ | `\frac{\partial f}{\partial x}` |
| Mixed partial | $\frac{\partial^2 f}{\partial x\,\partial y}$ | `\frac{\partial^2 f}{\partial x\,\partial y}` |
| Evaluation at a point | $\left.\frac{\mathrm{d}f}{\mathrm{d}x}\right\rvert_{x=a}$ | `\left.\frac{\mathrm{d}f}{\mathrm{d}x}\right\rvert_{x=a}` |
| Indefinite integral | $\int f(x)\,\mathrm{d}x$ | `\int f(x)\,\mathrm{d}x` |
| Definite integral | $\int_a^b f(x)\,\mathrm{d}x$ | `\int_a^b f(x)\,\mathrm{d}x` |
| Double integral | $\iint_D f\,\mathrm{d}A$ | `\iint_D f\,\mathrm{d}A` |
| Triple integral | $\iiint_V\rho\,\mathrm{d}V$ | `\iiint_V\rho\,\mathrm{d}V` |
| Closed-path integral | $\oint_C\vec{F}\cdot\mathrm{d}\vec{l}$ | `\oint_C\vec{F}\cdot\mathrm{d}\vec{l}` |
| Closed-surface flux, physics shorthand | $\oint_S\vec{E}\cdot\mathrm{d}\vec{A}$ | `\oint_S\vec{E}\cdot\mathrm{d}\vec{A}` |
| Sum | $\sum_{n=0}^{\infty}a_n$ | `\sum_{n=0}^{\infty}a_n` |
| Product | $\prod_{k=1}^{n}a_k$ | `\prod_{k=1}^{n}a_k` |
| Variation | $\delta S=0$ | `\delta S=0` |
| Functional derivative | $\frac{\delta S}{\delta q(t)}$ | `\frac{\delta S}{\delta q(t)}` |
| Differential operator | $\mathcal{L}[y]=f$ | `\mathcal{L}[y]=f` |

Use `\,` before a differential for spacing. Upright `\mathrm{d}` distinguishes a differential from a variable named $d$; italic $d$ is also common. The domain label distinguishes a curve $C$ from a surface $S$: surface flux is a two-dimensional integral even when written with the physics shorthand `\oint_S`.

## 5. Vectors and vector calculus

| Meaning | Rendered | Source |
|---|---|---|
| Arrow vector | $\vec{v}$ | `\vec{v}` |
| Bold Latin vector | $\mathbf{v}$ | `\mathbf{v}` |
| Bold Greek vector | $\boldsymbol{\omega}$ | `\boldsymbol{\omega}` |
| Unit vector | $\hat{r},\hat{\mathbf{r}}$ | `\hat{r},\hat{\mathbf{r}}` |
| Cartesian basis | $\hat{\mathbf{x}},\hat{\mathbf{y}},\hat{\mathbf{z}}$ | `\hat{\mathbf{x}},\hat{\mathbf{y}},\hat{\mathbf{z}}` |
| Alternative Cartesian basis | $\hat{\imath},\hat{\jmath},\hat{k}$ | `\hat{\imath},\hat{\jmath},\hat{k}` |
| Cylindrical basis | $\hat{\rho},\hat{\phi},\hat{z}$ | `\hat{\rho},\hat{\phi},\hat{z}` |
| Spherical basis | $\hat{r},\hat{\theta},\hat{\phi}$ | `\hat{r},\hat{\theta},\hat{\phi}` |
| Magnitude | $v=\lVert\vec{v}\rVert$ | `v=\lVert\vec{v}\rVert` |
| Dot product | $\vec{a}\cdot\vec{b}$ | `\vec{a}\cdot\vec{b}` |
| Cross product | $\vec{a}\times\vec{b}$ | `\vec{a}\times\vec{b}` |
| Gradient | $\nabla f$ | `\nabla f` |
| Divergence | $\nabla\cdot\vec{F}$ | `\nabla\cdot\vec{F}` |
| Curl | $\nabla\times\vec{F}$ | `\nabla\times\vec{F}` |
| Laplacian | $\nabla^2f$ | `\nabla^2f` |
| Directional derivative | $D_{\hat{u}}f=\nabla f\cdot\hat{u}$ | `D_{\hat{u}}f=\nabla f\cdot\hat{u}` |
| Differential area vector | $\mathrm{d}\vec{A}=\hat{n}\,\mathrm{d}A$ | `\mathrm{d}\vec{A}=\hat{n}\,\mathrm{d}A` |
| Solid-angle element | $\mathrm{d}\Omega$ | `\mathrm{d}\Omega` |
| Boundary | $\partial V,\partial S$ | `\partial V,\partial S` |

In the common physics spherical convention, $\theta$ is the polar angle from $+z$ and $\phi$ is the azimuth. Some mathematics texts interchange the names.

Cartesian gradient:

$$
\nabla f=\frac{\partial f}{\partial x}\hat{\mathbf{x}}
+\frac{\partial f}{\partial y}\hat{\mathbf{y}}
+\frac{\partial f}{\partial z}\hat{\mathbf{z}}
$$

Source: `\nabla f=\frac{\partial f}{\partial x}\hat{\mathbf{x}}+\frac{\partial f}{\partial y}\hat{\mathbf{y}}+\frac{\partial f}{\partial z}\hat{\mathbf{z}}`

Divergence theorem, with outward normal:

$$
\iiint_V\nabla\cdot\vec{F}\,\mathrm{d}V
=\oint_{\partial V}\vec{F}\cdot\mathrm{d}\vec{A}
$$

Source: `\iiint_V\nabla\cdot\vec{F}\,\mathrm{d}V=\oint_{\partial V}\vec{F}\cdot\mathrm{d}\vec{A}`

Stokes's theorem, with compatible boundary orientation:

$$
\iint_S(\nabla\times\vec{F})\cdot\mathrm{d}\vec{A}
=\oint_{\partial S}\vec{F}\cdot\mathrm{d}\vec{l}
$$

Source: `\iint_S(\nabla\times\vec{F})\cdot\mathrm{d}\vec{A}=\oint_{\partial S}\vec{F}\cdot\mathrm{d}\vec{l}`

## 6. Linear algebra and tensors

| Meaning | Rendered | Source |
|---|---|---|
| Matrix-vector equation | $A\mathbf{x}=\mathbf{b}$ | `A\mathbf{x}=\mathbf{b}` |
| Matrix element | $A_{ij}$ | `A_{ij}` |
| Transpose | $A^{\mathsf{T}}$ | `A^{\mathsf{T}}` |
| Complex conjugate | $z^*,\overline{z}$ | `z^*,\overline{z}` |
| Conjugate transpose / adjoint | $A^{\dagger},A^{\mathsf{H}}$ | `A^{\dagger},A^{\mathsf{H}}` |
| Inverse | $A^{-1}$ | `A^{-1}` |
| Determinant | $\det A$ | `\det A` |
| Trace | $\operatorname{tr}(A)$ | `\operatorname{tr}(A)` |
| Rank; kernel | $\operatorname{rank}(A),\ker A$ | `\operatorname{rank}(A),\ker A` |
| Eigenvalue equation | $A\mathbf{v}=\lambda\mathbf{v}$ | `A\mathbf{v}=\lambda\mathbf{v}` |
| Identity matrix | $I_n$ | `I_n` |
| Kronecker delta | $\delta_{ij}$ | `\delta_{ij}` |
| Levi-Civita symbol | $\varepsilon_{ijk}$ | `\varepsilon_{ijk}` |
| Tensor / outer product | $\mathbf{a}\otimes\mathbf{b}$ | `\mathbf{a}\otimes\mathbf{b}` |
| Tensor indices | $T^{\mu\nu},T^{\mu}{}_{\nu}$ | `T^{\mu\nu},T^{\mu}{}_{\nu}` |
| Metric tensor | $g_{\mu\nu}$ | `g_{\mu\nu}` |
| Covariant derivative | $\nabla_\mu V^\nu$ | `\nabla_\mu V^\nu` |
| Jacobian | $J_{ij}=\frac{\partial f_i}{\partial x_j}$ | `J_{ij}=\frac{\partial f_i}{\partial x_j}` |
| Hessian | $H_{ij}=\frac{\partial^2f}{\partial x_i\partial x_j}$ | `H_{ij}=\frac{\partial^2f}{\partial x_i\partial x_j}` |

For complex inner products, state which argument is conjugated. Under Einstein summation, repeated upper/lower indices are summed, as in $a^\mu b_\mu$ (`a^\mu b_\mu`). Cartesian engineering notation often also sums repeated lower indices when that convention is declared.

## 7. Complex numbers and transforms

| Meaning | Rendered | Source |
|---|---|---|
| Imaginary unit | $i^2=-1,\quad j^2=-1$ | `i^2=-1,\quad j^2=-1` |
| Rectangular form | $z=a+jb$ | `z=a+jb` |
| Polar form | $z=re^{j\phi}$ | `z=re^{j\phi}` |
| Engineering angle notation | $Z=10\angle30^\circ\,\Omega$ | `Z=10\angle30^\circ\,\Omega` |
| Real/imaginary parts | $\operatorname{Re}(z),\operatorname{Im}(z)$ | `\operatorname{Re}(z),\operatorname{Im}(z)` |
| Alternate notation | $\Re z,\Im z$ | `\Re z,\Im z` |
| Argument | $\arg z$ | `\arg z` |
| Conjugation | $z^*=a-jb$ | `z^*=a-jb` |
| Complex frequency | $s=\sigma+j\omega$ | `s=\sigma+j\omega` |
| Transforms | $\mathcal{F}\{x(t)\},\mathcal{L}\{x(t)\}$ | `\mathcal{F}\{x(t)\},\mathcal{L}\{x(t)\}` |
| Inverse transform | $\mathcal{F}^{-1}\{X(\omega)\}$ | `\mathcal{F}^{-1}\{X(\omega)\}` |
| Transform pair | $x(t)\longleftrightarrow X(\omega)$ | `x(t)\longleftrightarrow X(\omega)` |
| Continuous convolution | $(x*h)(t)$ | `(x*h)(t)` |
| Discrete convolution | $(x*h)[n]$ | `(x*h)[n]` |
| Dirac impulse | $\delta(t)$ | `\delta(t)` |
| Unit step | $u(t)$ | `u(t)` |
| Discrete impulse | $\delta[n]$ | `\delta[n]` |

**Fourier convention here:** angular frequency $\omega$ in radians per second, forward kernel $e^{-j\omega t}$, inverse factor $1/(2\pi)$.

$$
\begin{aligned}
X(\omega)&=\int_{-\infty}^{\infty}x(t)e^{-j\omega t}\,\mathrm{d}t,\\
x(t)&=\frac{1}{2\pi}\int_{-\infty}^{\infty}X(\omega)e^{j\omega t}\,\mathrm{d}\omega.
\end{aligned}
$$

```latex
\begin{aligned}
X(\omega)&=\int_{-\infty}^{\infty}x(t)e^{-j\omega t}\,\mathrm{d}t,\\
x(t)&=\frac{1}{2\pi}\int_{-\infty}^{\infty}X(\omega)e^{j\omega t}\,\mathrm{d}\omega.
\end{aligned}
```

For frequency $f$ in hertz, use the forward kernel $e^{-j2\pi ft}$ and its matching inverse. The normalized sinc is $\operatorname{sinc}(x)=\sin(\pi x)/(\pi x)$; the unnormalized version is $\sin x/x$. Both take value $1$ at zero by continuity.

Unilateral Laplace transform for an ordinary causal signal:

$$
X(s)=\int_0^\infty x(t)e^{-st}\,\mathrm{d}t
$$

Source: `X(s)=\int_0^\infty x(t)e^{-st}\,\mathrm{d}t`

For impulses at the origin and initial-condition calculations, specify a lower limit of $0^-$ or $0^+$ as appropriate. Specify the region of convergence when relevant.

## 8. Probability and statistics

| Meaning | Rendered | Source |
|---|---|---|
| Probability | $\mathbb{P}(A)$ | `\mathbb{P}(A)` |
| Conditional probability | $\mathbb{P}(A\mid B)$ | `\mathbb{P}(A\mid B)` |
| Expectation | $\mathbb{E}[X]$ | `\mathbb{E}[X]` |
| Variance | $\operatorname{Var}(X)$ | `\operatorname{Var}(X)` |
| Covariance | $\operatorname{Cov}(X,Y)$ | `\operatorname{Cov}(X,Y)` |
| Mean; variance | $\mu,\sigma^2$ | `\mu,\sigma^2` |
| Sample mean | $\bar{x}$ | `\bar{x}` |
| Estimator | $\hat{\theta}$ | `\hat{\theta}` |
| Normal distribution | $X\sim\mathcal{N}(\mu,\sigma^2)$ | `X\sim\mathcal{N}(\mu,\sigma^2)` |
| Density; cumulative distribution | $f_X(x),F_X(x)$ | `f_X(x),F_X(x)` |
| Spectral density | $S_{xx}(\omega)$ | `S_{xx}(\omega)` |

For spectral densities, specify hertz versus radians per second and one-sided versus two-sided spectra.

## 9. Physics and electromagnetism

### Common quantities and equations

| Meaning | Rendered | Source |
|---|---|---|
| Electric field; force | $\vec{E},\quad\vec{F}=q\vec{E}$ | `\vec{E},\quad\vec{F}=q\vec{E}` |
| Magnetic flux density; field intensity | $\vec{B},\vec{H}$ | `\vec{B},\vec{H}` |
| Electric displacement; polarization; magnetization | $\vec{D},\vec{P},\vec{M}$ | `\vec{D},\vec{P},\vec{M}` |
| Current density | $\vec{J}$ | `\vec{J}` |
| Line, surface, volume charge density | $\lambda,\sigma,\rho$ | `\lambda,\sigma,\rho` |
| Electric potential | $V,\phi$ | `V,\phi` |
| Magnetic vector potential | $\vec{A}$ | `\vec{A}` |
| Electric/magnetic flux | $\Phi_E,\Phi_B$ | `\Phi_E,\Phi_B` |
| Permittivity; permeability | $\varepsilon,\mu$ | `\varepsilon,\mu` |
| Vacuum values | $\varepsilon_0,\mu_0$ | `\varepsilon_0,\mu_0` |
| Relative material properties | $\varepsilon_r,\mu_r$ | `\varepsilon_r,\mu_r` |
| Electric dipole moment | $\vec{p}$ | `\vec{p}` |
| Magnetic dipole moment | $\vec{m},\boldsymbol{\mu}$ | `\vec{m},\boldsymbol{\mu}` |
| Electromotive force | $\mathcal{E}$ | `\mathcal{E}` |
| Poynting vector | $\vec{S}=\vec{E}\times\vec{H}$ | `\vec{S}=\vec{E}\times\vec{H}` |
| Torque; angular momentum | $\boldsymbol{\tau},\vec{L}$ | `\boldsymbol{\tau},\vec{L}` |
| Lagrangian; Hamiltonian | $\mathcal{L},H$ | `\mathcal{L},H` |
| Coulomb force magnitude | $F=\frac{\lvert q_1q_2\rvert}{4\pi\varepsilon_0r^2}$ | `F=\frac{\lvert q_1q_2\rvert}{4\pi\varepsilon_0r^2}` |
| Electrostatic potential gradient | $\vec{E}=-\nabla V$ | `\vec{E}=-\nabla V` |
| General electric field from potentials | $\vec{E}=-\nabla V-\frac{\partial\vec{A}}{\partial t}$ | `\vec{E}=-\nabla V-\frac{\partial\vec{A}}{\partial t}` |
| Magnetic field from potential | $\vec{B}=\nabla\times\vec{A}$ | `\vec{B}=\nabla\times\vec{A}` |
| Lorentz force | $\vec{F}=q(\vec{E}+\vec{v}\times\vec{B})$ | `\vec{F}=q(\vec{E}+\vec{v}\times\vec{B})` |
| Electric dipole torque | $\boldsymbol{\tau}=\vec{p}\times\vec{E}$ | `\boldsymbol{\tau}=\vec{p}\times\vec{E}` |
| Plane wave, one convention | $E(z,t)=E_0\cos(\omega t-kz+\phi)$ | `E(z,t)=E_0\cos(\omega t-kz+\phi)` |
| Wavenumber; angular frequency | $k=2\pi/\lambda,\quad\omega=2\pi f$ | `k=2\pi/\lambda,\quad\omega=2\pi f` |

$\rho$ may mean charge density or resistivity; $\sigma$ may mean surface charge density or conductivity. Units and context identify the quantity. Distinguish $\vec{B}$ (tesla) from $\vec{H}$ (ampere per meter).

Maxwell's equations in SI, using free charge and current for the macroscopic $\vec{D},\vec{H}$ form:

$$
\begin{aligned}
\nabla\cdot\vec{D}&=\rho_{\mathrm{free}},
&\nabla\cdot\vec{B}&=0,\\
\nabla\times\vec{E}&=-\frac{\partial\vec{B}}{\partial t},
&\nabla\times\vec{H}&=\vec{J}_{\mathrm{free}}+\frac{\partial\vec{D}}{\partial t}.
\end{aligned}
$$

```latex
\begin{aligned}
\nabla\cdot\vec{D}&=\rho_{\mathrm{free}},
&\nabla\cdot\vec{B}&=0,\\
\nabla\times\vec{E}&=-\frac{\partial\vec{B}}{\partial t},
&\nabla\times\vec{H}&=\vec{J}_{\mathrm{free}}+\frac{\partial\vec{D}}{\partial t}.
\end{aligned}
```

### Quantum and statistical physics

| Meaning | Rendered | Source |
|---|---|---|
| Reduced Planck constant | $\hbar$ | `\hbar` |
| Wavefunction | $\psi(\vec{r},t)$ | `\psi(\vec{r},t)` |
| Ket; bra | $\lvert\psi\rangle,\langle\psi\rvert$ | `\lvert\psi\rangle,\langle\psi\rvert` |
| Bra-ket overlap | $\langle\phi\mid\psi\rangle$ | `\langle\phi\mid\psi\rangle` |
| Operator | $\hat{H}$ | `\hat{H}` |
| Expectation, normalized state | $\langle\psi\rvert\hat{A}\lvert\psi\rangle$ | `\langle\psi\rvert\hat{A}\lvert\psi\rangle` |
| Commutator | $[\hat{x},\hat{p}]=i\hbar$ | `[\hat{x},\hat{p}]=i\hbar` |
| Anticommutator | $\{\hat{A},\hat{B}\}$ | `\{\hat{A},\hat{B}\}` |
| Partition function | $Z=\sum_n e^{-\beta E_n}$ | `Z=\sum_n e^{-\beta E_n}` |
| Inverse thermal energy | $\beta=(k_{\mathrm{B}}T)^{-1}$ | `\beta=(k_{\mathrm{B}}T)^{-1}` |

Hats can denote unit vectors, operators, or estimators. The bra-ket commands above do not require a dedicated bra-ket extension.

## 10. Electrical engineering

### Circuits and devices

| Meaning | Rendered | Source |
|---|---|---|
| Instantaneous voltage/current | $v(t),i(t)$ | `v(t),i(t)` |
| DC or specified scalar values | $V,I$ | `V,I` |
| Phasors | $\tilde{V},\tilde{I}$ | `\tilde{V},\tilde{I}` |
| Impedance | $Z=R+jX$ | `Z=R+jX` |
| Admittance | $Y=G+jB$ | `Y=G+jB` |
| Resistor impedance | $Z_R=R$ | `Z_R=R` |
| Inductor impedance | $Z_L=j\omega L$ | `Z_L=j\omega L` |
| Capacitor impedance | $Z_C=1/(j\omega C)$ | `Z_C=1/(j\omega C)` |
| Phasor Ohm's law | $\tilde{V}=Z\tilde{I}$ | `\tilde{V}=Z\tilde{I}` |
| Kirchhoff current law | $\sum_k i_k=0$ | `\sum_k i_k=0` |
| Kirchhoff voltage law, lumped model | $\sum_k v_k=0$ | `\sum_k v_k=0` |
| Complex power, RMS phasors | $S=\tilde{V}\tilde{I}^*=P+jQ$ | `S=\tilde{V}\tilde{I}^*=P+jQ` |
| Apparent power | $\lvert S\rvert=V_{\mathrm{rms}}I_{\mathrm{rms}}$ | `\lvert S\rvert=V_{\mathrm{rms}}I_{\mathrm{rms}}` |
| Sinusoidal power factor | $\mathrm{pf}=\cos(\phi_v-\phi_i)$ | `\mathrm{pf}=\cos(\phi_v-\phi_i)` |
| Transfer function, zero initial conditions | $H(s)=Y(s)/X(s)$ | `H(s)=Y(s)/X(s)` |
| Ideal LC resonance | $\omega_0=1/\sqrt{LC}$ | `\omega_0=1/\sqrt{LC}` |
| RC time constant | $\tau=RC$ | `\tau=RC` |
| Device terminal voltages | $V_{\mathrm{GS}},V_{\mathrm{DS}}$ | `V_{\mathrm{GS}},V_{\mathrm{DS}}` |
| Transconductance at operating point | $g_m=\left.\frac{\partial I_D}{\partial V_{\mathrm{GS}}}\right\rvert_Q$ | `g_m=\left.\frac{\partial I_D}{\partial V_{\mathrm{GS}}}\right\rvert_Q` |

**Phasor convention here:** $j$ is the imaginary unit and time dependence is $e^{j\omega t}$. The reactive impedances above follow that choice; their signs reverse for $e^{-j\omega t}$. Phasors here have RMS magnitudes, so $v(t)=\sqrt{2}\operatorname{Re}\{\tilde{V}e^{j\omega t}\}$. With peak phasors, complex power includes a factor of $1/2$.

Use the passive sign convention for absorbed power: current enters the positive voltage terminal. In the small-signal derivative, $Q$ means the quiescent operating point, with other independent device variables fixed.

With waveform distortion, total power factor is $P/(V_{\mathrm{rms}}I_{\mathrm{rms}})$ and need not equal a single phase-angle cosine.

### Signals, control, and RF

| Meaning | Rendered | Source |
|---|---|---|
| Discrete-time signal | $x[n]$ | `x[n]` |
| Sampling interval/rate | $T_s,\quad f_s=1/T_s$ | `T_s,\quad f_s=1/T_s` |
| Digital angular frequency | $\Omega$ | `\Omega` — often radians per sample |
| Z-transform | $X(z)=\sum_{n=-\infty}^{\infty}x[n]z^{-n}$ | `X(z)=\sum_{n=-\infty}^{\infty}x[n]z^{-n}` |
| Power gain in decibels | $G_{\mathrm{dB}}=10\log_{10}(P_2/P_1)$ | `G_{\mathrm{dB}}=10\log_{10}(P_2/P_1)` |
| Voltage ratio in decibels | $20\log_{10}(\lvert V_2\rvert/\lvert V_1\rvert)$ | `20\log_{10}(\lvert V_2\rvert/\lvert V_1\rvert)` |
| Quality factor | $Q$ | `Q` |
| Propagation constant | $\gamma=\alpha+j\beta$ | `\gamma=\alpha+j\beta` |
| Characteristic impedance | $Z_0$ | `Z_0` |
| Voltage reflection coefficient | $\Gamma=\frac{Z_L-Z_0}{Z_L+Z_0}$ | `\Gamma=\frac{Z_L-Z_0}{Z_L+Z_0}` |
| Scattering parameters | $S_{11},S_{21}$ | `S_{11},S_{21}` |
| Natural frequency/damping ratio | $\omega_n,\zeta$ | `\omega_n,\zeta` |

The voltage-ratio dB expression equals the corresponding power-gain dB for equal real reference impedances. In RF, $Z_L$ often means **load impedance**; in element tables it may mean **inductor impedance**. Digital frequency is also often denoted by lowercase $\omega$.

## 11. Units and typography

Variables are usually italic; unit symbols and descriptive labels are upright. Put a thin space between a value and its unit. Unit symbols are case-sensitive.

| Example | Rendered | Source |
|---|---|---|
| Scientific notation | $1.602\times10^{-19}\,\mathrm{C}$ | `1.602\times10^{-19}\,\mathrm{C}` |
| Voltage | $12\,\mathrm{V}$ | `12\,\mathrm{V}` |
| Resistance | $4.7\,\mathrm{k}\Omega$ | `4.7\,\mathrm{k}\Omega` |
| Capacitance | $100\,\mu\mathrm{F}$ | `100\,\mu\mathrm{F}` |
| Inductance | $10\,\mathrm{mH}$ | `10\,\mathrm{mH}` |
| Conductance | $2\,\mathrm{mS}$ | `2\,\mathrm{mS}` |
| Electric field | $250\,\mathrm{V\,m^{-1}}$ | `250\,\mathrm{V\,m^{-1}}` |
| Electric flux unit | $\mathrm{N\,m^2\,C^{-1}}$ | `\mathrm{N\,m^2\,C^{-1}}` |
| Charge density unit | $\mathrm{C\,m^{-3}}$ | `\mathrm{C\,m^{-3}}` |
| Angular frequency | $100\,\mathrm{rad\,s^{-1}}$ | `100\,\mathrm{rad\,s^{-1}}` |
| Temperature | $298\,\mathrm{K},\quad25\,{}^\circ\mathrm{C}$ | `298\,\mathrm{K},\quad25\,{}^\circ\mathrm{C}` |
| Planck/Boltzmann constants | $h,\hbar,k_{\mathrm{B}}$ | `h,\hbar,k_{\mathrm{B}}` |
| Electron mass; Avogadro constant | $m_e,N_{\mathrm{A}}$ | `m_e,N_{\mathrm{A}}` |

Common prefixes: $\mathrm{p}$ (pico), $\mathrm{n}$ (nano), $\mu$ (micro), $\mathrm{m}$ (milli), $\mathrm{k}$ (kilo), $\mathrm{M}$ (mega), $\mathrm{G}$ (giga). Wrap Latin unit/prefix letters in `\mathrm{...}`. The micro glyph here uses the broadly supported `\mu`; upright Greek typography depends on renderer/package support.

## 12. Copyable equation layouts

### Aligned derivation

$$
\begin{aligned}
\Delta U&=q\Delta V,\\
W_{\mathrm{field}}&=-\Delta U\\
&=-q\Delta V.
\end{aligned}
$$

```latex
$$
\begin{aligned}
\Delta U&=q\Delta V,\\
W_{\mathrm{field}}&=-\Delta U\\
&=-q\Delta V.
\end{aligned}
$$
```

Use `&` for an alignment point and `\\` for a row break inside an appropriate environment.

### Piecewise function

$$
E(r)=\begin{cases}
0, & 0\le r<R,\\[6pt]
\dfrac{\lvert Q\rvert}{4\pi\varepsilon_0r^2}, & r>R.
\end{cases}
$$

```latex
$$
E(r)=\begin{cases}
0, & 0\le r<R,\\[6pt]
\dfrac{\lvert Q\rvert}{4\pi\varepsilon_0r^2}, & r>R.
\end{cases}
$$
```

This is the field magnitude for a charged spherical conducting shell with an empty cavity. The surface is excluded because the idealized field has different one-sided limits.

### Matrix and determinant

$$
A=\begin{bmatrix}a&b\\c&d\end{bmatrix},\qquad
\det A=\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc
$$

```latex
$$
A=\begin{bmatrix}a&b\\c&d\end{bmatrix},\qquad
\det A=\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc
$$
```

Use `pmatrix` for parentheses, `bmatrix` for square brackets, `vmatrix` for determinant bars, and `matrix` for no enclosing delimiters.

### Delimiters, annotations, and spacing

| Task | Rendered | Source |
|---|---|---|
| Automatic delimiter size | $\left(\frac{a}{b}\right)^2$ | `\left(\frac{a}{b}\right)^2` |
| Explicit size | $\Bigl(\frac{a}{b}\Bigr)$ | `\Bigl(\frac{a}{b}\Bigr)` |
| Underbrace | $\underbrace{R+j\omega L}_{Z}$ | `\underbrace{R+j\omega L}_{Z}` |
| Overbrace | $\overbrace{x_1+\cdots+x_n}^{n\text{ terms}}$ | `\overbrace{x_1+\cdots+x_n}^{n\text{ terms}}` |
| Labeled arrow | $A\xrightarrow{\text{transform}}B$ | `A\xrightarrow{\text{transform}}B` |
| Symbol over a relation | $a\overset{\text{def}}{=}b$ | `a\overset{\text{def}}{=}b` |
| Display style inside inline math | $\displaystyle\frac{a}{b}$ | `\displaystyle\frac{a}{b}` |
| Thin, medium, wide spaces | $a\,b\;c\quad d$ | `a\,b\;c\quad d` |

`\left` needs a matching `\right`. Use a dot for an invisible side: `\left.f(x)\right\rvert_a^b`. Commands `\,`, `\;`, `\quad`, and `\qquad` control spacing; ordinary source spaces usually do not.

## 13. Chemistry

### Portable standard math notation

Chemical element symbols are upright. Atom counts go in subscripts, ionic charges in superscripts, and isotope mass numbers at upper left. Group multi-character charges with braces: `^{2-}`.

| Meaning | Rendered | Source |
|---|---|---|
| Molecule | $\mathrm{H_2O}$ | `\mathrm{H_2O}` |
| Grouped formula | $\mathrm{Ca(OH)_2}$ | `\mathrm{Ca(OH)_2}` |
| Cation | $\mathrm{Na}^{+}$ | `\mathrm{Na}^{+}` |
| Polyatomic anion | $\mathrm{SO_4}^{2-}$ | `\mathrm{SO_4}^{2-}` |
| Isotope | ${}^{14}_{6}\mathrm{C}$ | `{}^{14}_{6}\mathrm{C}` |
| Electron | $\mathrm{e}^{-}$ | `\mathrm{e}^{-}` |
| Physical state | $\mathrm{H_2O(l)}$ | `\mathrm{H_2O(l)}` |
| Concentration | $[\mathrm{H}^{+}]$ | `[\mathrm{H}^{+}]` |
| Reaction arrow | $\mathrm{A}\rightarrow\mathrm{B}$ | `\mathrm{A}\rightarrow\mathrm{B}` |
| Equilibrium arrow | $\mathrm{A}\rightleftharpoons\mathrm{B}$ | `\mathrm{A}\rightleftharpoons\mathrm{B}` |
| Reaction enthalpy | $\Delta_{\mathrm{r}}H$ | `\Delta_{\mathrm{r}}H` |
| Standard Gibbs energy change | $\Delta_{\mathrm{r}}G^\circ$ | `\Delta_{\mathrm{r}}G^\circ` |
| Activation energy | $E_{\mathrm{a}}$ | `E_{\mathrm{a}}` |
| Acid dissociation constant | $K_{\mathrm{a}}$ | `K_{\mathrm{a}}` |
| Activity | $a_{\mathrm{H}^{+}}$ | `a_{\mathrm{H}^{+}}` |
| pH definition | $\mathrm{pH}=-\log_{10}a_{\mathrm{H}^{+}}$ | `\mathrm{pH}=-\log_{10}a_{\mathrm{H}^{+}}` |
| Molar concentration unit | $\mathrm{mol\,L^{-1}}$ | `\mathrm{mol\,L^{-1}}` |

Balanced reaction:

$$
2\,\mathrm{H_2(g)}+\mathrm{O_2(g)}\longrightarrow2\,\mathrm{H_2O(l)}
$$

Source: `2\,\mathrm{H_2(g)}+\mathrm{O_2(g)}\longrightarrow2\,\mathrm{H_2O(l)}`

The thermodynamic pH definition uses dimensionless activity; substituting a concentration ratio is an approximation. A standard-state superscript $\circ$ does not itself specify a temperature.

### Optional mhchem extension

MathJax provides `\ce{...}` through the `mhchem` extension. Availability depends on renderer configuration; see the [official extension documentation](https://docs.mathjax.org/en/latest/input/tex/extensions/mhchem.html). The standard examples above do not require it.

If supported, place these inputs inside math delimiters:

```latex
\ce{H2O}
\ce{SO4^2-}
\ce{^{14}_{6}C}
\ce{2 H2(g) + O2(g) -> 2 H2O(l)}
\ce{N2(g) + 3 H2(g) <=> 2 NH3(g)}
```

For a full LaTeX document, load `\usepackage[version=4]{mhchem}` in the preamble. That command does not belong inside an Obsidian math block.

## 14. Rendering fixes

| Problem | Fix |
|---|---|
| Plain commands instead of math | Wrap inline math in `$...$` and displays in `$$...$$`. |
| Source is shown literally | Remove backticks or code fences when rendering is wanted; this sheet deliberately shows source examples. |
| Only one character is superscripted | Use grouped exponents such as `e^{-j\omega t}`. Group subscripts too. |
| Command runs into following letters | Write `\rvert r`, not `\rvertr`. |
| Equation splits a Markdown table | Use `\lvert...\rvert`, `\lVert...\rVert`, or `\mid` instead of literal vertical bars, including in code columns. |
| Words look like multiplied variables | Use `\text{net force}`, `\mathrm{rms}`, and named functions such as `\sin`. |
| Line break fails | Use `\\` inside `aligned`, `cases`, or a matrix environment. |
| Alignment marker fails | Put `&` inside an alignment, cases, or matrix environment. |
| Braces are invisible | Use `\{` and `\}`; ordinary braces group input. |
| Delimiter error | Match `\left` with `\right`; `.` supplies an invisible side. |
| Shortcut is unsupported | Prefer explicit commands. `\ce`, `\qty`, `\dv`, `\pdv`, `\bra`, and `\ket` can depend on packages/extensions. |
| Greek vector is not bold | Use `\boldsymbol{\omega}`; `\mathbf` primarily targets Latin letters and digits. |
| Unit looks like a variable | Use upright symbols such as `\mathrm{V}` and `\mathrm{A}`. |

For standalone `.tex` documents, use document math delimiters such as `\(...\)` and `\[...\]`, and load required packages in the preamble. This sheet uses Obsidian's dollar delimiters. MathJax supports math typesetting rather than an entire LaTeX document; consult the [supported-command list](https://docs.mathjax.org/en/stable/input/tex/macros/) when a command fails.

# Other characters



### Official syntax references

- [Obsidian: advanced formatting and math](https://obsidian.md/help/advanced-syntax)
- [MathJax: supported TeX/LaTeX commands](https://docs.mathjax.org/en/stable/input/tex/macros/)
- [MathJax: mhchem extension](https://docs.mathjax.org/en/latest/input/tex/extensions/mhchem.html)
