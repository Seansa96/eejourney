# Chapter 12 - Pointers, Classes, Virtual Functions, and Abstract Classes

*C++ Programming: From Problem Analysis to Program Design* - D. S. Malik, 8th edition.

# Pointer Data Type and Pointer Variables

Recall that the set of values of a data type is called its domain. In addition to that, there is a set of operations, and a third property which is its name. To manipulate variables of a type, we declare it using its name such as with integers, we declare `int`. We now will work with the pointer data type.

The values that belong to this type are the memory addresses of the computer in which the program executes. There is no actual name for the pointer data type, which is typical in most languages which allow their use.

This means that its domain is the memory address. A pointer variable is thus said to "point" to that location.
## Declaring Pointer Variables

The general syntax is

`dataType *identifier`

You can see that in C++ we declare it by putting an asterisk between the data type and the name of the variable.  Pointers are bound to their declared data types and so can only contain the addresses of a variable of that data type.

So we can do

```cpp
int *p;
char *ch;
````

Note that the asterisk character may be at any point between the data type and the variable name, but for each variable name we need an asterisk.

`int *p, q`

for example will result in variable `p` becoming a pointer of type int, but `q` is just an int. To avoid confusion, the convention is usually to attach the asterisk to the variable name as we have seen rather than something like `int * p` or `int* p`.

So if we wanted multiple pointer variables, we'd do

`int *p, *q`.

To clear up some confusion:

**Pointer declaration:** `int* p`. This makes a pointer to an `int`.

**Reference declaration:** This makes a reference to an `int` identifier. `int& r = x;` `int& r;` is gibberish. A reference is a compiler level abstraction serving as an alias to an existing variable.


# Address of Operator (&)

Note that `&` used in this way differs from `&` as the unary operator that translates to "address of" its operand.

Applying the `&` operator to a pointer, like `p`, still gives you the pointer `p`’s address.

# Dereferencing Operator (*)

After declaration, we can use `*p` to get the value stored at the address `p` points to. Note that the pointer `p` exists in memory at `0x1000`. Its content is the address of an integer, so `*p` is equivalent to saying, "At address `0x2000`, give me what’s inside."


# Classes, Structs, and Pointer Variables

# Initializing Pointer Variables

## Initializing Pointer Variables Using nullptr

# Dynamic Variables

## Operator new

## Operator delete

# Operations on Pointer Variables

# Dynamic Arrays

## Arrays and Range-Based for Loops (Revisited)

## Functions and Pointers

Using `*&` in a function heading is like using it in a type declaration. Thus, we read `int*& pointer` as a reference to a pointer to an `int`, named `pointer`.

## Pointers and Function Return Values

## Dynamic Two-Dimensional Arrays

When we want to do some things with pointers, here's a reference.

```
twoDarray[0]   // The pointer stored in the first slot
&twoDarray[0]  // The address of that pointer slot
*twoDarray[0]  // The integer it points to, IF the pointer is valid
```

The proper sequence looks like this:

```
int number = 52;
int* pointer = &number;  // First, point to an existing integer.
std::cout << *pointer;  // Then, dereference to print 52.
```
# Shallow versus Deep Copy and Pointers

# Classes and Pointers: Some Peculiarities

## Destructor

## Assignment Operator

## Copy Constructor

# Inheritance, Pointers, and Virtual Functions

## Classes and Virtual Destructors

# Abstract Classes and Pure Virtual Functions

# Address of Operator and Classes

# Quick Review

# Exercises

# Programming Exercises
