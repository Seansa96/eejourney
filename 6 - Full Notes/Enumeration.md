Tags: [[programming concept]]

Enumeration is the act of structuring a relationship of a given type to a constant value.

What the hell does that mean?

It means, if I'm given something--say a `string blue`, and I want that to be mapped to a value and thus also be able to represent that `string blue` by that value, then most likely it would make sense to perform enumeration.

Typically, in most languages, this is done with a special keyword that implements this, done in say, [[enum (csharp)|Csharp]].  This keyword creates a new type that the compiler (or language-equivalent arbitrator and executor) recognizes as the same as a value type that represents, by default, an int, although this is subject to that specific instance's declaration.

But how does this differ from a regular variable, say `int x = 1`?

Well, for one, unless specified as `readonly` or `private`, a regular variable would be subject to mutation. An `enum` is a fixed relationship that remains constant.  An `enum` also has built-in bounds checking.  An `enum` cannot be a value outside of the definition of that `enum type` unless you do some buggery with casting.

An `enum` also has built-in explanation/documentation.  With an `enum` of, say, `Days`, you know 0 is `Monday`, and so on, because that's the mapped, fixed relationship that's enforced by the compiler or language equivalent abstraction.
# Example of Enumeration (Pseudocode)

```
public enum Colors //can specify the underlying type binding, like long, ushort, etc

{
	Blue = 0,
	Red = 1,
	Green = 2
}

print((int)Colors.Blue); //prints 0
```

