# Chapter 5.1 - Double Integrals over Rectangular Regions Solutions

# Problem 3

Here $\Delta A=\pi^2/4$. The lower-left samples are $(0,0),(\pi/2,0),(0,\pi/2),(\pi/2,\pi/2)$, whose function values sum to $-2$. Thus

$$
\iint_R f\,dA\approx-\frac{\pi^2}{2}.
$$

# Problem 4

Here $\Delta A=\pi^2/8$. The four lower-left values sum to $2$, so

$$
\iint_R f\,dA\approx\frac{\pi^2}{4}.
$$

# Problem 6

The upper-right samples are $9.75,7.83,9.63,8.21$, and $\Delta A=1$. Therefore

$$
\iint_R f\,dA\approx9.75+7.83+9.63+8.21=35.42.
$$

# Problem 8a

Each subrectangle has area $1$. The upper-left samples sum to

$$
6.5+6.4+6+7+7.5+6.5+6.7+6.5+6=59.1.
$$

The estimated excavated volume is $59.1\text{ ft}^3$.

# Problem 13

The reversed integral is

$$
\int_{-2}^{2}\int_{-1}^{1}(2x+3y+5)\,dy\,dx.
$$

The odd terms integrate to zero over their symmetric intervals, leaving $5(4)(2)=40$.

# Problem 14

Reversing gives

$$
\int_0^1\int_0^2(x+2e^y-3)\,dy\,dx
=2e^2-7.
$$

# Problem 15

Reverse the order:

$$
\int_1^2\int_1^{27}\left(x^{1/3}+y^{1/3}\right)\,dx\,dy
=60+\frac{39}{2}\left(2^{4/3}-1\right).
$$

# Problem 16

After reversing,

$$
\int_1^8\int_1^{16}\left(x^{1/4}+2y^{1/3}\right)\,dx\,dy
=\frac{5111}{10}.
$$

# Problem 17

Reversing gives

$$
\int_0^1\int_{\ln2}^{\ln3}e^{x+y}\,dx\,dy
=(e-1)(3-2)=e-1.
$$

# Problem 18

The integrand separates:

$$
\left(\int_0^2 3^x\,dx\right)\left(\int_0^1 3^y\,dy\right)
=\frac{8}{\ln3}\cdot\frac2{\ln3}
=\frac{16}{(\ln3)^2}.
$$

# Problem 19

$$
\left(\int_1^6x^{-2}\,dx\right)\left(\int_2^9\sqrt y\,dy\right)
=\frac56\cdot\frac23(27-2\sqrt2)
=15-\frac{10\sqrt2}{9}.
$$

# Problem 20

The reversed $y$-limits introduce a negative sign:

$$
\left(\int_1^9\sqrt x\,dx\right)\left(\int_4^2y^{-2}\,dy\right)
=\frac{52}{3}\left(-\frac14\right)
=-\frac{13}{3}.
$$

# Problem 21

$$
\left(\int_0^{\pi/2}\sin(2x)\,dx\right)
\left(\int_0^\pi\cos(3y)\,dy\right)
$$

is a product; the second factor is $0$. Hence the integral is $0$.

# Problem 22

Integrating each term over its natural variable gives two equal contributions:

$$
\frac{\pi}{24}\ln\sqrt{\frac32}
+\frac{\pi}{24}\ln\sqrt{\frac32}
=\frac{\pi}{24}\ln\frac32.
$$

# Problem 25

Separate the two terms:

$$
=(\ln2)^2+\frac34\ln\frac53.
(\ln2)^2+\left(\int_1^2x\,dx\right)
\cdot\left(\int_1^2\frac{dy}{2y+1}\right)
=(\ln2)^2+\frac34\ln\frac53.
=(\ln2)^2+\frac34\ln\frac53.
$$

# Problem 26

The inner integral contributes a factor of $1$:

$$
\int_1^e x^2\ln x\,dx
=\left[\frac{x^3}{3}\ln x-\frac{x^3}{9}\right]_1^e
=\frac{2e^3+1}{9}.
$$

# Problem 27

First integrate $y$:

$$
\frac32\int_1^{\sqrt3}\arctan(1/x)\,dx.
$$

Using $\int\arctan(1/x)\,dx=x\arctan(1/x)+\tfrac12\ln(x^2+1)$ yields

$$
\frac{\sqrt3\pi}{4}-\frac{3\pi}{8}+\frac34\ln2.
$$

# Problem 28

Split the sum and use $\int\arcsin u\,du=u\arcsin u+\sqrt{1-u^2}$:

$$
\frac12\left(\frac\pi2-1\right)
+\left(\frac\pi{12}+\frac{\sqrt3}{2}-1\right)
=\frac\pi3+\frac{\sqrt3}{2}-\frac32.
$$

# Problem 29

The integral separates:

$$
=1\cdot\frac{e^8-e^4}{4}.
\left(\int_0^1xe^x\,dx\right)
\cdot\left(\int_1^2e^{4y}\,dy\right)
=1\cdot\frac{e^8-e^4}{4}.
=1\cdot\frac{e^8-e^4}{4}.
$$

# Problem 30

$$
\left(\int_1^2xe^x\,dx\right)\left(\int_0^1e^{-y}\,dy\right)
=e^2(1-e^{-1})
=e^2-e.
$$

# Problem 36

Since $\operatorname{Area}(R)=1$,

$$
f_{\mathrm{ave}}
=\int_1^2\int_2^3(x^4+2y^3)\,dy\,dx
=\frac{31}{5}+\frac{65}{2}
=\frac{387}{10}.
$$
