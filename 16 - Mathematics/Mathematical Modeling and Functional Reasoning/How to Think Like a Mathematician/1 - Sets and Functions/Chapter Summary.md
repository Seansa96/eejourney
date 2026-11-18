We'll define some common tools here that the book uses to determine a base foundation.

The first two items are that of sets and functions. These are basic mathematical objects but can be sufficiently abstracted.

A s**et** is a collection of objects, and a **function** is an association of members of one set to members of another.

Most high level mathematics deals with sets and the functions between them.

Calculus for example is the study of functions from the set of real numbers to the set of real numbers that have the property that we can differentiate them.

So in effect, these are our "building blocks".
# Sets

**Definition**.


> [!textbook]
> A set is a well defined collection of objects

Usually, this is done by making a list of its elements between brackets. Note that the proper definition is far more complicated.

To note that a given number or value is a **member** of a set, such as $X$, we use
$$
x \in X
$$
which is read as $x$ belongs to $X$, is in $X$, or is a member of $X$.  If w wish to indicate that it is **not** a member, then we dash a line through it. 

$$
x \notin X
$$

The set containing the numbers 1,2,3,4, and 5 for example, is written as
$$
\{1,2,3,4,5\}
$$

The number 3 here is an element of the set, so we say that $3 \in \{1,2,3,4,5\}$.  But note that $6 \notin \{1,2,3,4,5\}$. We can also write it as 

$$
\{1,4,3,2,5\}
$$
The order is unimportant.

We may represent any defined values as belonging to a set, such as the set $\{dog, cat, mouse\}$.

Sets can have sets as members, and we may combine sets together.  The set

$$
\{1,2,5,12 \{dog,cat\},\{5,72\}\}
$$
for example, contains the set $\{dog,cat\}$ and $\{5,72\}$.  

We must note that $\{5\}$ and $5$ are not equivalent. One is a set, while another is an element of a set. But as we saw, $\{5\}$ itself *can* then be an element of a set, so we have to be careful.

Looking at another example, we see that we can have $\{3,4\} \in X$, but $3$ and $4$ $\notin X$. Only the set $\{3,4\}$. 

## Important Sets

### Natural Numbers
**The Natural Numbers** $\{1,2,3,4,5...\}$ and is denoted by $\mathbb{N}$. The dots just mean that we go on forever and can be read as 'and so on'. 

Some mathematicians, particularly logicians, like to include $0$ as a natural number. Other s argue that the natural numbers are the counting numbers and that you don't start counting with $0$.

On the other hand, some theorems make more sense if we take that $0 \in \mathbb{N}$. One can get around the argument by specifying that we are only dealing with non-negative integers or positive integers, defined as....

### Integers

The set of integers is $\{...,-4,-3,-2,0,1,2,3,4\}$ and is denoted by $\mathbb{Z}$. From this set it is easy to define the non-negative integers, $\{0,1,2,3,4,5...\}$ which are often denoted by $\mathbb{Z^+}$. Similarly, we could denote the negative integers as $\{...,-3,-2,-1\}$. Note that we *cannot* say that $\mathbb{N} \in \mathbb{Z}$, and to express it correctly we have to learn a different expression.

### Rational Numbers

The set of **rational numbers** is denoted by $\mathbb{Q}$ and consists of all fractional numbers. If $x \in \mathbb{Q}$, then $x$ has to be able to be written in the form $p/q$ where $p$ and $q$ are integers that are nonzero. 

Examples are one-half, $6/1$, $80/5$. These representations do not need to be unique, since these can also be re-written as different expressions.

Note that all integers are rational numbers, since if $x \in \mathbb{Z}$, we can write this as $x/1$, showing that $x \in \mathbb{Q}$ also.

### Real Numbers

The real numbers, denoted by $\mathbb{R}$, are difficult to define rigorously. We will take them to be any number that can be given as a decimal representation, finite or otherwise, or as tbeing represented by a point on an infinitely long number line.

The real numbers include all rational numbers (which means the integers, and natural numbers). $\pi$ and $e$ are also real numbers, even though they are not rational numbers, at least rigorously so.  The number $\sqrt{ 2 }$ is not a rational number either. The set of real numbers that are not rational are called the **irrational** numbers.

### Complex Numbers

Going further, we introduce the **complex** numbers, denoted $\mathbb{C}$. We do this by pretending that the square root of $-1$ exists.  

## More on Sets

### The Empty Set

The most fundamental set in mathematics is the set with no elements, called the **empty set**.


> [!textbook]
> The set with no elements is called the empty set and is denoted $\emptyset$.

What use is this? Well, it allows us to build up ideas about counting. To explore this concept further, we must investigate a high level book on Set Theory or Logic.

We can say that $\emptyset \in \{\emptyset\}$, but we CANNOT say that $\emptyset \in \emptyset$, since the empty set has no elements.


> [!textbook]
> Two sets are equal if they have the same elements. If set $X$ equal set $Y$, then we write $X=Y$. If not, we write $X\ne Y$ 

### Finite Sets and Cardinality


> [!textbook]
>If the set $X$ has a finite number of elements, then we say that $X$ is a finite set, and if a set is finite, we can define the number of elements it has as its **cardinality**. The cardinality of $X$ is denoted as $|X|$. 

If $X$ has an infinite number of sets it becomes difficult to define its cardinality, because there are different sizes of infinity. For now, we'll just say that the cardinality of an infinite set is undefined.

As an example, the set

$$
\{1,2,3,4\}
$$
has a cardinality of $4$.

### Cardinality Practice

![[Pasted image 20261026234947.png]]

> [!answer]- Answer
> ![[Pasted image 20261026235006.png]]


### Subsets

This is an important definition and way of expressing elements or corresponding quantities of sets.


> [!textbook]
>Suppose $X$ is a set. A set $Y$ is a **subset** of $X$ if every element of $Y$ is an element of $X$. We denote this as $Y \subseteq X$. 
>This is the same as saying that if $x \in Y$, then $x \in X$.

The set of even numbers is a subset of $\mathbb{N}$. 

For any set $X$, we have $X \subseteq X$.

For any set $X$, we have $\emptyset \subseteq X$.

### Caution!

It is important to distinguish an **element** vs a **subset** of a set. These are easy to get confused.

For example, if $x \in X$, then $\{x\} \subseteq X$. Again, it is important to know how to read these. We say that if $x$ is in $X$, then the set containing only the element $x$, or $\{x\}$, is a **SUBSET** of $X$.

However, it is NOT the case, typically (there are exceptions), where

If $x \in X$, then $\{x\} \notin X$.

A special example where this is not the case, is

$$
X= \{x, \{x\}\}
$$
See here that $x \in X$, and $\{x\} \subseteq X$. 

This prevents us from writing rules that affirm the consequent.

### Proper Subset

A proper subset is defined as


> [!textbook]
> A subset $Y$ of $X$ is called a **proper subset** of $X$ if $Y$ is not equal to $X$. This is denoted by $Y \subsetneq X$. The other notation just don't have the bar below the "C" at all.

### Defining Sets

We can define sets with different notation:

$\{x |x$ satisfies property $P\}$

The symbol "|" is read as 'such that'. Sometimes the colon character is used in place of '|'.

An example of this would be

$\{x|x \in \mathbb{N}$ and $x<5\}$ 

We read this as "the set x, such that x is in the set of natural numbers, and is all numbers less than 5".

The set of numbers that qualifies then would be $\{1,2,3,4\}$. Because the natural numbers are all numbers $\{1,2,3,4...\}$, and the set must be numbers less than $5$. 

We may also apply restrictions on the set before the "|" character, as below.

$\{x \in \mathbb{N}|5 \leq x \leq 10\}$ 

It is common to use the notation $[a,b]$ to represent $\{x \in \mathbb{R}|a \leq x \leq b\}$ 

$(a,b)$ is similarly representative of $\{x \in \mathbb{R} | a < x < b\}$ 

We could also say $\{x^2 | x \in \mathbb{N}\}$ which would indicate a set $\{1,4,9,16...\}$.

*How do we actually read the expression before the bar character, and for the above how does expressing it involve the natural numbers exactly? Are we just saying that $x^2$ is not actually $x^2$ but $1 \times 1$, $2 \times 2$, etc*.


## Operations on Sets

In mathematics, we often make a definition of some object, like a set, and then we find ways to create new kinds of objects from old ones.

For example, subsets of sets.  We can then do two new operations by finding the union and intersection of sets.

### Union Definition

> [!textbook]
>Suppose that $X$ and $Y$ are two sets. The **union** of $X$ and $Y$, denoted $X \cup Y$ is the set consisting of elements that are in $X$ or in $Y$ or in both. We can define the set as $X \cup Y$. This is equal to $\{x|x \in X$ or $x \in Y\}$.


#### Union Practice

![[Pasted image 20261027003902.png]]
### Intersection Definition


> [!textbook]
>Suppose that $X$ and $Y$ are two sets. The **intersection** of $X$ and $Y$ denoted $X \cap Y$ is the set consisting of elements that are in $X$ and in $Y$. We can define the set as $X \cap Y$, which is equal to $\{x | x \in X$ and $x \in Y\}$.

#### Intersection Practice

![[Pasted image 20261027003933.png]]

### Difference of Sets

> [!textbook]
> **Definition 1.25 — Set Difference**
The **difference** of $X$ and $Y$, denoted $X \setminus Y$, is the set of elements that are in $X$ but not in $Y$. That is, we take elements of $X$ and discard those that are also in $Y$.
We do not require that $Y$ is a subset of $X$. If $Y$ is defined as a subset of $X$, then we often call $X \setminus Y$ the **complement** of $Y$ in $X$ and denote this by $Y^c$.

#### Difference Practice

![[Pasted image 20261027004210.png]]

### Products of Sets


> [!textbook]
> Let $X$ and $Y$ be two sets. THe **product** of $X$ and $Y$, denoted by $X \times Y$ is the set of all possible pairs $(x,y)$ where $x \in X$ and $y \in Y$, i.e.
> 
$X \times Y = \{(x,y)|x \in Y$ and $y \in Y\}$

Here, $(x,y)$ just denotes a pair and isn't related to our set notation we used earlier.

#### Product of sets practice

![[Pasted image 20261027004718.png]]




# Maps and Functions

To relate elements of sets to elements of other sets, we use functions.


> [!textbook]
> Suppose that $X$ and $Y$ are sets. A **function** or **map** from $X$ to $Y$ is an association between the members of the sets. More precisely, for every element of $X$ there is a unique element of $Y$.

If $f$ is a function from $X$ to $Y$, then we write that $f:X->Y$, and the unique element in $Y$ associated to $x$ is denoted $f(x)$. This element is subsequently called the **value** of $x$ **under** $f$ or called a **value** of $f$. The set $X$ is called the **source** or the **domain** of $f$ and $Y$ is called the **target** or **codomain**, of $f$.

To describe a function $f$ we usually use a formula to define $f(x)$ for every $x$ and talk about applying $f$ to elements of a set, or to a set.

Note that an element of $X$ must be associated to an element of $Y$, but two distinct elements of $X$ may map to the same element in $Y$. However, you cannot have two elements of $Y$ map to the same element in $X$.

## Function Practice Examples

![[Pasted image 20261027005230.png]]

![[Pasted image 20261027005242.png]]


