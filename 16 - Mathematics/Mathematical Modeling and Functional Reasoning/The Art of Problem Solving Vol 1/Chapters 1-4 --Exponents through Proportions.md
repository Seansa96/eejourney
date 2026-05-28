# Chapter 1 - Exponents and Logarithms

Negative numbers raised to odd powers are negative. Positive numbers raised to odd powers are positive. So it can be said that raising a number to an odd power retains the sign of the base. 

For notation, pertaining to negatives and roots, the inclusion or exclusion of parentheses controls the evaluation order here and is needed for precision.

For example,

$$
-1^{1/2} \neq (-1)^{1/2}
$$

The first is $-\sqrt{1}$ while the second is $\sqrt{ -1 }$ which is an imaginary number.

## Example Exercises

Find all real $x$ for the following.

$$
x=(-2)^5
$$

$$
x^6=64
$$

$$
x=(-27)^{2/3}
$$

$$
x=\sqrt[3]{ -\frac{1}{8} }
$$

$$
x^3=64
$$


$$
x^{5/3}=243
$$

## Simplifying Radical Expressions

When presented with a radical with a radicand that has no apparent root for the power of the radical, you can "factor" the radical to an extent to find factors that do have a root for the power of the radical.

$$
\sqrt{ 8 }= \sqrt{ 4*2 }=2\sqrt{ 2 }
$$

So, for the square root of $\sqrt{ 96 }$

we would want to find a factor within it that has a square root.  The smallest square is $4$, so let's try that

$$
\sqrt{ 96 }=\sqrt{ 4*24 }
$$

So we can factor out the 4 from the radicand

$$
2\sqrt{ 24 }
$$

And we know $24$ is just $4*6$, so

$$
2\sqrt{ 4*6 }=4\sqrt{ 6 }
$$

And we're done. No further square roots.  You can also see that by factoring out a $4$ from the radicand, that means there was a factor of $16$ as well, so we could have done it in one operation instead.

$$
\sqrt{ 96 }=\sqrt{ 16*6 }=4\sqrt{ 6 }
$$

Another way that takes longer, but never fails is to re-express the radical in exponent notation, then, separate the factors into values that have integer powers and fractional powers. Then, evaluate the integer exponents, multiply them, and place all the fractional exponents into the same grouping.

For the above:

$$
\sqrt{ 96 }=\sqrt{ 2^5*3 }=(2^5*3)^{1/2}=2^{5^{1/2}} * 3^{1/2}=2^2*2^{1/2}*3^{1/2}=4(2*3)^{1/2}
$$
$$
=4(6)^{1/2}=4\sqrt{ 6 }
$$


# Chapter 2 - Complex Numbers

The root (heh) of complex numbers and the theorem surrounding it comes from the simple question of this

What is:

$$
\sqrt{ -1 }
$$
?

For this, the answer is determined to be a number that is not real, but imaginary. That being the number $i$. Multiplying a real number by $i$ results in a **pure imaginary number**, such as $2i$. 

In this, it is important to remember that **IMAGINARY IS A PURELY MATHEMATICAL DEFINITION.**  These numbers are just as *real* as actual real numbers ($\in\{ 1,2,3\dots \}$ ), as in having some sort of assigned value and being able to be compared and computed. 

Keep in mind that you cannot combine the radical, so to speak, when manipulating $i$.

This is allowed:

$$
\sqrt{ -1 }*\sqrt{ -1 }=-1
$$


But this is not:

$$
\sqrt{ -1 }*\sqrt{ -1 }=\sqrt{ -1^2 }=\sqrt{ 1 }=1
$$

The powers of $i$ go in cycles of 4, that is $i, -1, -i, 1$, and it is important to keep in mind the very simple fact that $i$ is just representative of $\sqrt{ -1 }$.

So the cycle can be re-expressed as such.

$$
\sqrt{ -1 }, \sqrt{ -1 }*\sqrt{ -1 }, \sqrt{ -1 }*-1, -1*-1
$$
## Complex Number Operations

These are the numbers you get when you add a real to an imaginary number, such as in

$$
2+i
$$

Every real number is also a complex number, with the imaginary component assumed to be $0$. So, a real number can be re-expressed in its complex form as

$$
2 + 0i
$$

To add two complex numbers together, you just add their real and imaginary parts separately.

### Example 1

$$
(3+4i)+(-3+8i)= 12i
$$

What is:
$$
\left( -\frac{1}{4}+i \right) + \left( 2-\frac{3}{4}i \right)
$$
> [!answer]- Answer
> $\frac{7}{4}+\frac{1}{4}i$

Find the general formula for the sum $(z_{i}+z_{2}i)+(w_{1}+w_{2}i)$

> [!answer]- Answer
> $(z_{i}+w_{i})+(z_{2}i+w_{2}i)$
> 


### Example 2

For multiplication, one can simply employ use of the distributive property.
$$
(3+4i)(-3+8i)=3(-3+8i)+4i(-3+8i)
$$
$$
3*-3 + 3*8i + 4i*-3 + 4i*8i
$$

$$
-9+24i + -12i -32 = 12i-41
$$

Remember that $i$ is just $\sqrt{ -1 }$! So when we do $8i*4i$, we get $32*-1$, not $32i^2$.



### Example 3


When we divide two complex numbers, we clear all instances of $i$ from the denominator in exactly the same way as rationalizing a denominator which contains square roots.  So, you just employ the conjugate method.

$$
\frac{3+4i}{-3+8i}= \frac{3+4i}{-3+8i}* \frac{-3-8i}{-3-8i}= \frac{23-36i}{73}
$$


## Complex Variables

These are usually designated as $z$ or $w$ since $x$ and $y$ are usually used for reals and linear-polynomial equations.

# Chapter 3 - Linear Equations

The degree of a term is the sum of the powers of the variables in that term, including dissimilar variables.

For example, in 

$$
xy^3
$$
The degree of this term is $4$, not $1$ for $x$ and $3$ for $y$.

And similarly, when the degree of an equation is $1$, it is called a **linear equation.** There can also be no variables raised to fractional powers.

**Linear Equations**:

$$
2x+1=y, x+y=1, 5y+4x=0
$$

**Non-linear Equations**

$$
xy=1, x^2+y=5, 3^x+y=0, x+\sqrt{ x }=3
$$

## Word Problems

To solve a word problem, interpret the words as a set of equations and then solve them. Utilize these steps as a framework.

1.  Define all the variables.
2. Write the equations described by the problem.
3. Solve the equations.

### Example 1


Johnny is twice as old as Gina. Johnny is five years older than Gina. How old is Johnny?

**First step is to define all the variables.**

Let $J=$Johnny.
Let $G=$Gina.

**Then, we'll write the equations described here.**


Johnny is twice as old as Gina, so:

$2G=J$

Johnny is five years older than Gina.

$J-5=G$.

I would personally next prefer to just solve through reducing the variables to one kind and then solving that way, so:

$$
2(J-5)=J;2J-10=J;J-10=0;J=10
$$

$$
J-5=G;10-5=G=5
$$

If Gina is $5$, and Johnny is $10$, is Johnny twice as old as Gina while also being only five years older than her?

$$
\frac{10}{2}=5;10-5=5
$$
We see that the equations hold true with these values, so we can conclude that Johnny is $10$ and Gina is $5$.


### Example 2

The units digit in a two-digit number is three times the tens digit. If the digits are reversed, the resulting number is 54 more than the original number. Find the original number.


Let $u=$units digit
Let $t=$tens digit
Let $n=$the number.

$u$ can be expressed as $u=3t$ 
$n$ can be expressed as $10t+u$, since a two-digit number can be expressed as a unit such as $1$ to $9$, added to another unit multiplied by 10.

So, $53$ would decompose to $10(5)+3$, for example.

To find the reverse of $n$, you would just swap the variables around, because a given number $n$ is just $xt + u$, so the reverse of $n$, $n_r$, is just $xu+t$.

We know also that the reverse must be $54$ more than the original number, which can be expressed as

$$
n_{r}-n=54
$$

Substituting in the equations we then get:

$$
(10u+t)-(10t+u)=54
$$

Simplifying this, we get

$$
9u-9t=54
$$

Since we know the equation of $u$, it's best to solve for that to reduce computation time.  So we get.

$$
9u-9t=54;9u=54+9t;u=6+t
$$

Then we just substitute in the expression for $u$

$$
(3t)=6+t
$$

And then solve for t

$$
3t=6+t;2t=6;t=3
$$
Now plug this in to the equation for $u$

$$
u=3t;u=3(3);u=9
$$

And then plug it in to our equation for $n$.

$$
n=10t+u;n=10(3)+(9);30+9=39
$$

And then check to see if this satisfies the earlier equation that asks if $n_r-n=54$.

$$
93-39=54
$$

It does, so we're done.  Our number is $39$.


### Example 3

Jim drives to his mother's house, which is $40$ miles away, and then drives back.
On the way there he drives $40$ miles an hour, but on the way back he drives only $20$ mph. What is
his average speed for the whole trip?


> [!answer]- Answer
> ![[Pasted image 20260506205436.png]]

### Example 4

Jim drives 40 mph to his mother's house and $20$ mph on the way back. Show that
his average speed for the trip is $26.67$ mph regardless of the distance to his mother's house.

> [!answer]- Answer
> ![[Pasted image 20260506220503.png]]

A bit more elegant approach would be like this:

> [!answer]- Answer
> ![[Pasted image 20260506220647.png]]


### Example 5

A frog swims 8 miles downstream in 2 hours. She returns upstream in 14 hours.
How fast does the frog swim in still water?


> [!answer]- Answer
> ![[Pasted image 20260506223005.png]]


# Chapter 4 - Proportions


In a directly proportional relationship, the quotient of the two quantities is a constant, so as one increases so must the other.

### Example 1

A ten foot pole casts an eight foot shadow. How long is a pole which casts a twelve
foot shadow?

> [!answer]- Answer
> ![[Pasted image 20260506224010.png]]


### Example 2

The ratio of boys to girls in a class is 3 : 2. If there are 35 students in the class, how
many girls are there?

> [!answer]- Answer
> ![[Pasted image 20260506224544.png]]


### Example 3

In 4 games, Michael Jordan scores 124 points. If he continues scoring at this rate,
how many points will he score in the next 6 games?

## Proportion Manipulation

When $\frac{a}{b}=\frac{c}{d}$, then the following inequalities hold:

![[Pasted image 20260507002608.png]]

Another common type is proportion multiplication.  This can be seen in the following:

$$
\frac{x}{y}=\frac{4}{5}, \frac{z}{y}=\frac{4}{3}
$$
Then $$\frac{x}{z}=\frac{x}{y} *\frac{y}{z}$$
So

$$
\frac{4}{5}* \frac{3}{4}=\frac{3}{5}
$$


