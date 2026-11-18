# Chapter 11 - Inheritance and Composition

*C++ Programming: From Problem Analysis to Program Design* - D. S. Malik, 8th edition.

# Inheritance

Sometimes we want to re-use or extend a class that we've already implemented. Suppose we have some class `personType`, and it has some member variables and functions like `firstName, lastName` and some basic getters, setters, and printing functionality.

We want to then implement a new class called `partTimeEmployee`. Well, `personType` already has some of the basic things we would want. So, we want to be able to extend this definition without changing the original implementation.

This is the principle of inheritance, which is referred to as an "is-a" relationship, as in "every employee **is a** person".

Creating a new class from an existing class results in a **derived class**, while the existing class is referred to as the **base class**. As the name suggests, it inherits the properties from the base class.

Each derived class can itself become a base class for a future derived class. We can thus have multiple inheritance as well as this single inheritance.

We will only talk about single inheritance in this chapter.

Inheritance is often seen as a tree-like structure
![[Pasted image 20261102175209.png]]

Shape here being the base class, with circle and rectangle being derived classes. We can see that a square is a derived class of rectangle as well.


The syntax of a derived class is:
> [!textbook]
> ```cpp
> class className: memberAccessSpecifier baseClassName
> {
> member List
> };
> ```

where `memberAccessSpecifier` is public, protected, or private. When no specifier is provided, just as a regular class, it is assumed private by default.

Say we defined some class `shape`. The following declares a derived class `circle` from `shape` with public inheritance.
```cpp
class circle: public shape
{
}
```

We can similarly do private inheritance with
```cpp
class circle: private shape
```

In private inheritance, the public members of shape become private members of circle. This stops any other objects of type circle from accessing these now private members of `circle`, and no object may access the private members of `shape` beside `shape` objects.

Public members of a base class can become either public or private.

The derived class may include additional members as either data or functions.

The derived class may also redefine the public member functions of the base class. You can have member functions with the same name, number, and types of parameters, but with different code in the function body. This of course **only applies to the derived class**.

All member variables of the base class are also member variables of the derived class. So too are the member functions, unless redefined.
## Redefining (Overriding) Member Functions of the Base Class

Redefining a member function of a base class requires that you use the same name, number, and type of parameters. In other words, the function header and the parameters must be the same. 

If you use the same name, but different parameters, this is also legal of course, it is just overloading.

When a public member function of a base class is overridden in this way, then calling it is a little different.

For example, instead of 

```cpp
derivedClass.print();
```

we should see

```cpp
derivedClass.baseClass::print();
```

If we don't override the baseClass's member function however, we can just do

```cpp
derivedClass.print();
```


## Constructors of Derived and Base Classes

Constructors go from base->derived. Basically, if you use inheritance for the derived class, then the derived class constructor will invoke the base class constructor.
## Destructors in a Derived Class

Destructors are basically the opposite. When a derived class destructor is invoked, it will first destroy the derived class, then the base class.
## Multiple Inclusions of a Header File

You have to be careful when including various files, and it is often helpful to use a few preprocessor directives to protect against misuse in this regard. 

The directives `ifndef`, `define`, and `endif` are using to achieve this. An example of such is

```cpp
#ifndef primeFactorization_H
#define primeFactorization_H

#include "integerManipulation.h"

class primeFactorization: public integerManipulation
{
public:
.
.
.

private:
.
.
.
};
#endif
```

This work as you might expect. If the primeFactorization_H identifier is not defined, then the compiler allows the statements in between `ifndef` and `endif` to pass.

If it is already defined, perhaps from multiple inclusions, then of course the statement will not be true so the compiler will skip over it.
## C++ Stream Classes

In earlier chapters and even now, we used members from the header file `iostream` , members like cin and cout, the extraction and insertion operators and more to compile file I/O and general input and output.

This header file includes the definitions for the classes `istream` and `ostream`.  For specifically file I/O, the program includes the header file `fstream` which has objects of type `ifstream` for the input with `ostream` and `ofstream` for file output.  

We can represent this with a simple tree,

![[Pasted image 20261113104812.png]]


## Protected Members of a Class

This exists between public and private. This member access identifier allows you to generally treat the member variables of the base class as private to everything outside the derived class, but the derived class can access the base class's member variables as if they were public, to it. You define it like you would a `public` or `private` inheritance.

```cpp
class derivedClass : protected baseClass
{
};
```


## Inheritance as public, protected, or private

Inheritance of all levels breaks down to this:

Public Inheritance - Public members of the base class stay public, protected stays protected, private becomes inaccessible. Basically, everything keeps its access level.

Protected Inheritance - Public members of base become protected of derived, protected stays protected, private becomes inaccessible.

Private Inheritance - Public and Protected of base become private of derived. Private of base still is inaccessible.

When we say inaccessible, we mean that it requires a getter/accessor to access instead of direct access through the member access operator `'.'`. 


### Accessing protected Members in the Derived Class

Note that these member access specifiers are purely a compiler level construct. The CPU when executing the program doesn't utilize any of this information: it just loads the addresses it's told to load using offsets and what-have-you and executes the code.  It'll use pointers and whatnot but otherwise these access protections don't exist, effectively.

What the compiler does here is just enforces what you've told it, essentially.

When you say something is protected, the compiler recognizes that and goes, "Ok, you can access this in your member definitions and whatnot, but if you try to access it in an external function or something like main, I'm going to stop you."

### Parameterized Constructors and Member Initializer Lists

We can be more concise and also guard against situations where we need to declare objects first before initializing them using parameterized constructors, and their accompanying **Member Initializer Lists**.

A simple example is:

````cpp
class A {
int val;

A(int initialVal) : val(initialVal) {}
}
````


The first part, `A(int initialVal)`, is basically the function heading for the constructor. Since constructors have no type, this is acceptable. The part after the `:` character is the member initializer list, which treats the member variable almost like a function instead of using typical assignment. If we don't want any side effects, we leave the body empty.

A more common and useful example is

````cpp
#include <iostream>

class bClass {
public:
    // This default constructor lets dClass omit an explicit base constructor call.
    bClass() {
        value = 0;
    }

    // TODO: Initialize value in a member initializer list instead of assigning here.
    
    bClass(int initialValue, int initialId, std::string initialName ) : value(initialValue), id(initialId), name(initialName) {}

    void print() const {
        std::cout << "Value: " << value << '\n';
        std::cout << "Id: " << id << std::endl;
        std::cout << "Name: " << name << std::endl;
    }

protected:
    int value; // Accessible inside bClass and its derived classes.
    int id;
    std::string name;
};

class dClass : public bClass {
public:
    // TODO: Call the parameterized bClass constructor in an initializer list,
    // then remove the assignment from this body.
    dClass(int initialValue, int initialId, std::string name, int initExtra_val) : bClass(initialValue, initialId, name), extra_val(initExtra_val) {}

    void add(int amount) {
        value += amount; // dClass can directly access the inherited protected member.
    }

    void print() const
    {
        bClass::print();
        std::cout << "Extra Value: " << extra_val << std::endl;
    }
protected: 
    int extra_val;
};

int main() {
    // Keep the output the same after refactoring the constructors.
    dClass Example(3, 5, "first", 10);
    
    Example.print();
}

````


# Composition (Aggregation)

This is a "has a" relationship and utilizes similar principles as composite functions from mathematics. Basically, we can let a member be an object of another class.


# Object-Oriented Design (OOD) and Object-Oriented Programming (OOP)

## Identifying Classes, Objects, and Operations

# Programming Example: Grade Report

# Quick Review

# Exercises

# Programming Exercises
