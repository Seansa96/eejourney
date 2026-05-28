$$
\int^{0}_{\pi} \frac{2x^3-3\pi x^2}{(1+\sin x)^2} dx
$$

Questions:

## Question 1

Why is he allowed to substitute x=$pi$-t? Is this FTC part 1 being used? Where is $\pi-t$ coming from though?

## Question 2

He says we'll use the symmetry of the integral. What exactly does that mean? Is he referring to splitting the integral, or is he referring to the bounds of the integral (0,$\pi$)?

## Question 3

What rule or theorem allows him to represent the entire integral as just $I$?

He then transforms the original Integral and then adds them. Why does he do so, and why is he allowed to do so? What is this a measurement of accumulation of?

> [!answer]- Answer
> You can just represent an integral as a simple variable. This is still an accumulation of the original integral, just re-expressed.

## Question 4

Why does he let

$$
u=\tan \left( \frac{x}{2} \right)
$$
instead of

$$
u=1-\sin(x)
$$
?

> [!answer]- Answer
> This is called the **Weierstrass substitution**. It gives
> $$
> \sin x=\frac{2u}{1+u^2}, dx=\frac{2}{1+u^2}du
> $$

## Question 5

What is the idea as well behind every step he has made thus far? I get that it's to make it easier to work with, but what patterns should I see and look to shift a problem to, in order to make it easier to work with here?

Like, for the symmetry and splitting it, then re-adding it again...I get that it cancels out a lot of terms and then let's us do an easy factoring out of the -\pi^3 that's in the numerator, but what made him choose to go that way?

> [!answer]- Answer
> Regarding the rewrite of the denominator into $$\frac{(1-\sin x)^2}{(1-\sin^{2}x)^2}$$
> 
> This is a setup move to make use of the identity
> 
> $$1-\sin^2x=\cos^2x$$
> 
> Regarding the adding of integrals, yes, this is to get rid of a lot of messy terms. So that instinct is correct. Then, his goal is to get rid of trig functions, but that requires him to first prepare them in the way that best fits with the Weierstrauss substitution.
> 
> In general, the idea is to use symmetry to simplify the numerator so it can be factored out, leaving us with the denominator which is trig, and then turn the function into a rational function in terms of u which is much easier to work with.
> 
> What allowed him to use symmetry, and why he chose it, was due to the bounds being $[0,\pi]$, seeing the trig functions, and the polynomials in terms of $x$.
> 



## Question 6

Later, why use the substitution rule? What is the form he's looking for when he changes u to = $tan\frac{pi}{2}$?


> [!answer]- Answer
> He's looking to turn everything into pure algebra (rational functions). By doing this he can utilize the aforementioned Weierstrauss substitution and eliminate the trig function forms which don't play nicely with integrals.



## Question 7

Why can he treat $$
\sin(\pi-x)
$$
as

$$
\sin(x)
$$

> [!answer]- Answer
> This is because $sin$ is a function that is symmetric about $\frac{\pi}{2}$. An example would be 
> $$x=0$$
> $$\sin(\pi-0)=\sin(0)$$
> The $sin$ of $0$ and the $sin$ of $pi$ are the same, both being $0$. If it were $cos$, we know that $cos$ is symmetric about $0$, so we'd need a different value to subtract from, but we'd see similar results if our bounds fit appropriately.
> 
> Knowing this, we can simply treat $sin(\pi-x)=\sin(x)$
