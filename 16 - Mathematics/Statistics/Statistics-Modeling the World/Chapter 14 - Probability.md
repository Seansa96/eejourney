# General Addition rule

This rule states that for any two events, $A$ and $B$, $P(A\cup B)$ is $P(A)+P(B)-P(A \cap B)$. It does not require disjoint events.

## Example

Suppose that 32% of people have a dog, 18% have a cat, and 8% own both.  What's the probability of someone owning a dog or a cat?

**Step 1**:
Find the probability of each event.

Dog - .32
Cat - .18
Both - .08

**Step 2**
Determine what represents $P(A \cap B)$

This would be "Both", so .08


**Step 4**
Plug the values into the Formula

$$
.32+.18 - .08 = .42
$$

So $P(A \cup B) = .42$

# Conditional Probability Formula

$$
P(B|A)=\frac{P(A \cap B)}{P(A)}
$$

# General Multiplication rule

$$
P(A \cap B) = P(B) \times P(A|B)
$$

# Independence and Disjointedness

An event is said to be disjoint when it is mutually exclusive with another.  This means that it cannot occur simultaneously with another event, or that it prevents the occurrence of another.

This can also be expressed by:
$$
P(A \cap B)=0
$$
An example of such an event would be the probability of someone being a freshmen and sophomore at the same time.

Independence is almost the opposite, where the event of one event does not influence the other.  Thus, disjoint events can be said to generally (where $P(A \cap B)>0$) **dependent**.


