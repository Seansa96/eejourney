
# Chapter 5 - Using the Integers

Integers have quite a lot of interesting properties and uses. Math that involves the properties of integers is called **number theory**.

## 5.1 - Divisibility

An integer $n$ is divisible by a different integer $m$ if $n$ is an integral multiple of $m$.For example, $15$ is divisible by $3$ because $15=5*3$. Thus, the integers which divide a given integer are its **divisors**.

### Example 5.1 - Write Down all the divisors of 20.

> [!answer]- Answer
> 1, 2, 4, 5, 10, 20

**Primes** are integers which have no divisors except themselves and $1$. For example, $7$ is a prime but not $8$. Numbers that aren't prime, or that do have divisors other than themselves and 1 are called composite.

**Note that 1 is neither prime nor composite**.

The primes less than $10$ are 2, 3, 5, and 7.

### Exercise 5.2 - Write down all primes between 11 and 20 inclusive

> [!answer]- Answer
> 11, 13, 17, 19



### Exercise 5.3 - How many even primes are there?

> [!answer]- Answer
> Just the number $2$.

## 5.2 - Number Bases

We can write the integer $7965841$ as 

$7000000+900000+60000+5000+800+40+1$

This is a consequence of the fact that our usual number system is base 10, or that it has 10 digits. Each digit represents a multiple of a power of 10, based on its position.

The above could thus be represented as

$7*10^6+9*10^5+6*10^4+5*10^3+8*10^2+4*10^1+1*10^0$

To keep the notation clean we assume that the number $47$ in our base 10 system means $47_{10}$. Note that once we reach the number $10$, it is that way because we only have digits from $0$ to $9$, so once we we reach the tenths place, we reset the count and now begin counting in terms of the tens we have.

We can extend this train of thought to other base systems.

For example, in a base 8 system, we would have digits from $0$ to $7$, and then we would now start counting at the eighths place once we get to a value of 8.

### Example 5.1 - What is the base 7 number 3456 in base 10

> [!answer]- Answer
> $3*7^3+4*7^2+5*7^1+6*7^0=1266$

### Example 5.2 - Write the base 10 number 216 in base 4

> [!answer]- Answer
> ![[Pasted image 20260516232348.png]]


## The Last Digit

If we want to know the last digit of the sum or product of two numbers, all we have to do is find the sum or product of their last digits and take the last digit of that result.

### Example 5.10 - In base 10, what digits can the last digit of the square of an integer not be?

> [!answer]- Answer
> 2, 3, 7, 8

### Example 5.4 Find the units digit of $7^42$+$42^7$

> [!answer]- Answer
> ![[Pasted image 20260516233845.png]]


## 5.4 Modular Arithmetic

Let's say we want to do arithmetic in base 5. To make it easier, we'll just consider the last digits. All numbers which have the same last digit in base 5 will be considered equal.

So,

$$
2_{5}=12_{5}=22_{5}=32_{5}\dots
$$

In base 10, this would be like saying:

$$
2=7=12=17
$$

To show we're using such a system, we use the $\cong$ symbol and also append the suffix mod 5.

We would thus write

$$
12 \cong 7(mod 5)
$$

This makes actual computation way easier. Is is often useful to find the smallest nonnegative integer which is congruent to $xmody$. For example, the smallest integer congruent to $12$mod$5$ is $2$. 

This is a lot of words for just saying that the remainder of these numbers when divided by 5, is 2.

Doing this is  called "modding out" the $x$ value. 

When you do this, you use the base system as the multiplier for each digit like we did above, and basically check the mod against each digit by evaluating the remainder of the system's base, and using the smallest integer congruent to it instead, raised to the appropriate power,  then add them together. According to what we discovered earlier, this preserves the structure of the system.

So, for example, given $$4583_{10}\pmod{4}$$
> [!answer]- Answer
> ![[Pasted image 20260522213326.png]]

## Example 1 (gpt practice question)

$$
7631_{10}\pmod{9}
$$

> [!answer]- Answer
> ![[Pasted image 20260522212928.png]]

## Example 2 (gpt practice question)

$$
17^{23}
$$
Find the last digit.

Things to consider:

This is a very large number. 17 is also a difficult base to work with in terms of raising exponents. You should find a number congruent to 17 to work with.

The behavior of exponents can work in cycles. The modulus operation exposes cycles, but you need to know how long the cycle is. Remember we want the last digit. If the exponents will have cyclical behavior, and you want to know the last digit, and we know the last digit is always just the last digit multiplied or added to a number, then think about how that can be obtained relative to powers.

This is a difficult question but being able to solve it will lock in these concepts!

> [!answer]- Answer
> ![[Pasted image 20260522203732.png]]

## Example 5-11 

Write down some numbers which are congruent to $3\pmod{5}$. 

> [!answer]- Answer
> ![[Pasted image 20260522204117.png]]

## Example 5-12 

What is the largest integer less than $100$ which is congruent to $3\pmod{5}$

> [!answer]- Answer
> ![[Pasted image 20260522204646.png]]

## Exercise 5-13 

How many integers are there between $50$ and $250$ inclusive which are congruent to $1\pmod{7}$

> [!answer]- Answer
> 


## Exercise 5-14 Which numbers are congruent to $0\pmod{5}$?

> [!answer]- Answer
> All multiples of $5$, since those are the numbers with remainders of $0$ when divided by $5$.



# 5.5 Tricks

We can tell using congruency if one number $y$, divides another number $x$.

It is obvious to tell that a number is divisible by $10$ if and only if the last digit is $0$ through experience, but why is this the case in terms of congruency? Well, think of the Exercise 5-14 in this chapter.

A number $k$ is a multiple of a number $y$ if $k\cong0\pmod{y}$

Look at the number $15$, for example. It is a multiple of $5$. Let's plug these in to the above.

$$
15\cong 0\pmod{5}
$$
Which, in English, just means that when $15$ is divided by $5$, it has a remainder of $3$.

So if we want to check divisibility of a number $x$ by a number $y$, we just need to see if it's congruent to $0\pmod{5}$.

Let's take $45376$, and see if it's divisible by $4$.
![[Pasted image 20260522213834.png]]

We simply break up each piece into much simpler slices, then evaluate their divisibility. We get to replace anything that is congruent to $0\pmod{4}$ with $0$, since that would be the same effective value.  At that point, it's simple arithmetic. Since we finish with a value of $0$, then the whole thing is $\pmod{4}$, or in other words, divisible by $4$. 

# 5.6 - Primes


Primes are the most important integers. This is simply because they are the building blocks of every other number. In a way, they can be considered atomic in this regard.  The splitting up of numbers into prime factors is called **prime factorization**, is extremely useful because each number has only one distinct prime factorization. 

Finding prime factorization of small numbers is very easy using only trial and error. For large numbers however, we need to be a bit more systematic. An important trick is the divisibility tricks we have derived. It's pretty easy to factor out all $5$s and $2$s for example. We then test for $3$s and $11$s. Most numbers are easily handled with just those.

This does not always work however, requiring going through each prime to check if it works. One way to limit the amount of searching required is to think about what the largest primes involved can be.

Let the number to be factored be called $N$. There cannot be more than one factor greater than $\sqrt{ N }$, since if there were more than one, their product would exceed $N$. Likewise, if $N$ is not prime, there must be at least one factor less than or equal to $\sqrt{ N }$. This is because since $N$ is not prime, it must have at least two factors other than itself and $1$. So either both are greater than $\sqrt{ N }$ , which we have shown is impossible, or at least one is less than or equal to $\sqrt{ N }$. Hence if we cannot find a prime less than $\sqrt{ N }$ which divides $N$, we know $N$ is prime.

![[Pasted image 20260523192600.png]]