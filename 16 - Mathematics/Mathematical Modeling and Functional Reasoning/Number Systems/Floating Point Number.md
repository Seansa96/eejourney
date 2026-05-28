Tags: 

A floating point number is a set of real numbers formed by a signed sequence of a fixed number of digits (this is referred to as the **significand**), multiplied by an integer power of that set's base.

The significand is sometimes referred to as the "**Mantissa**", although this is not precisely correct, as the formal definition of the mantissa is the fractional part of a [[Logarithm]]. This was typically the part that was used to lookup the computation of some logarithm on a log table.

Typically a floating point's significand will have a **radix point**, which gives the term its name.  The radix point is defined as a point or comma used to indicate the integer power's exponent. This is a key part of how scientific notation is used.  This can be interpreted as such:

$1.456 \times 10^{-3}$
 ^This is the radix point.

And just as easily, the same value could be represented as:

$14.56 \times 10^{-2}$ . Because the radix point can easily "float" to the left or right and still be represented by adjusting the exponent, this is where the name is derived.

In computing, floating point arithmetic is done by specialized FPUs (floating point units) due to the complexity of the operation, as floats are stored in scientific notation, which becomes unwieldy and difficult to represent in binary.