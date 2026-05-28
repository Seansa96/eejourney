The tangent line to the curve $y = f(x)$ at the point $P(a,f(a))$ is the line through $P$ with slope:

$$
m = \lim_{x \to a}\frac{f(x)-f(a)}{x-a}
$$

as long as the limit exists.

However, to take the limit of that point, we need remember that slope is $$\frac{y^2 -y^1}{x^2 - x^1}$$
However, you can't take the slope of a curve like $y=f(x)$. So, we need a secant line, which is just a way to cut between two points on a curve.

![[Pasted image 20260129201727.png]]

If we wanted to then use a tangent line, well, it'll skim off the point A, but then there's no other point within the domain of the curve function that we'll touch.

![[Pasted image 20260129202033.png]]

# Example 1 - Equation of a tangent line

Find the equation of the tangent line to the parabola $y=x^2$ at the point $P(1,1)$.

Recall the formula for above, then plug in the values that we know:

* $f(x)$ is $x^2$
* $x$ is $1$
* $a$ would have to be whatever value would be necessary to approach to calculate the limit.

![[Pasted image 20260129204726.png]]

So, $a$ would have to be $1$.

then,

$$\lim_{x \to a}\frac{x^2 - (1)^2}{x-1}$$

Now, this is in a form we're pretty familiar in dealing with. So we just factor and cancel out the $x-1$.

$$lim_{x \to 1} x+1$$
Then, just plug in the $1$, and we get $\lim_{x \to 1} = 2$. Remember, **this is the slope of the tangent line, or** $m$. 

Now, we need to show the equation of the line. We can do this with point-slope form or slope-intercept form.

We'll use **point-slope**, which is:

$$
y-y_1 = m(x-x_1)$$

So,

$$
y-1 = 2(x-1)
$$

Simplify and we get

$$
y = 2x - 1
$$
Answer:
	So, the equation of the line for the parabola $y=x^2$ at point $P(1,1)$ is $y=2x-1$.

# The second expression for the slope of a secant line

$$m_{pq} = \frac{f(a+h)-f(a)}{h}$$
Note that with this expression, $h$ approaches $0$, since we are trying to compress $a+h$ by $a$, and as we get closer to $x$, $h$ will approach $0$.
# Example 2: Equation of a tangent line using the second expression

Find an equation of the tangent line to the hyperbola $y=3/x$ at the point $(3,1)$.

* $f(x) = 3/x$
* $x$ = $3$
* $a$ = $3$

So,

$$\lim_{h \to 0}\frac{f(3+h)-\frac{3}{3}}{h}$$

$$\lim_{h \to 0}\frac{\frac{3}{3+h}-1}{h}
$$
**NOTE THAT WE CAN ONLY SUBSTITUTE 3 FOR A BECAUSE WE HAVE BEEN GIVEN THE POINT. YOU WILL SEE QUESTIONS LATER THAT DO NOT PROVIDE THIS VALUE AND THUS YOU SHOULD SIMPLY REPLACE IT WITH A+H**

We basically take whatever equation $f(x)$ represents and evaluate it for $a$ for $f(a)$, and plug in $3$ for $a$ here since we know $a$'s value.  Then we just use the LCD and simplify down.

**Work for solution:**
	![[Pasted image 20260201025630.png]]

$$
\lim_{h \to 0}\frac{-h}{h(3+h)}$$
$$
\lim_{h \to 0}\frac{-1}{3} = m
$$
Apply point-slope or slope-intercept:

$$
y-y_1 = m(x-x_1)
$$

$$
y-1 = -\frac{1}{3}(x-3)
$$
Which turns into $y=-\frac{1}{3}x + 2.$

Answer:
	So, the equation of the line is $y=-\frac{1}{3}x + 2$.

# Instantaneous Velocity

We define the instantaneous velocity of an object with position function $f(t)$ at time $t = a$ is:

$$
v(a) = \lim_{h \to 0}\frac{f(a+h)-f(a)}{h}
$$
so long as the limit exists.

# Example 3

Suppose that a ball is dropped from the upper observation deck of the CN Tower, 450 $m$ above ground. $f(x)$ is defined as $4.9t^2$.

a) What is the velocity of the ball after 5 seconds?
b) How fast is the ball traveling when it hits the ground?

First, we'd want to find the general velocity as it relates to time, which will allow us to determine a function that can be evaluated for the purpose of determining its velocity at point $t$, where $t$ is equal to $a$.

That basically is just asking what the slope of the secant line would be, so:

![[Pasted image 20260129222513.png]]

Now that we have the function for determining the general velocity, we just plug in time $t$, which is equal to $a$, so:

$9.8(5) = 49m/s$.

So the velocity of the ball after 5 seconds is $49m/s$.

For b, we want to determine how fast the ball is going when it hits the ground.  We could calculate the velocity for each interval of time and add up the distance traveled at each point, but for a simpler way we can just solve the original motion equation $4.9t^2$ for $450m$. 

$$
4.9t^2=450
$$
$$t^2=91.8367$$
$$t=\sqrt{91.8367}$$
$$
t = ~9.6
$$
# Example 4

Use expression 2 for the definition of the slope of the secant line to find the derivative of the function $f(x) = x^2 -8x + 9$ at the number $2$ and at $a$.

![[Pasted image 20260129232115.png]]