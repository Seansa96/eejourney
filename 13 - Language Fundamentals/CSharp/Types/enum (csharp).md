Tags: [[csharp]] 

An enum is declared with the `enum` keyword, and associates a given type with a constant value. By default, this is an int, but by use of the [[Colon Operator|:]] , you can specify a desired type, such as `ushort`.

Here's a simple implementation:

```
 public enum Colors
 {
     Blue = 0,
     Red = 1,
     Green = 2,
 }
```

By default, operations on individual `enums` such as `Colors.Blue` work on the enum type itself, so doing something like:

`Console.WriteLine(Colors.Blue)` would print `Blue`.

You need to cast that element to the underlying type to access it.

`Console.WriteLine((int)Colors.Blue)`

But what's the point of the first print statement? Not much. However, if we can cast the `enum` type to an int, couldn't we do the reverse to access the enum?

`Console.WriteLine((Colors)1)` would thus print `Red`.  

Utilizing this paradigm, we can perform a variety of far more efficient, and more importantly, simpler operations when working with constant values such as this.