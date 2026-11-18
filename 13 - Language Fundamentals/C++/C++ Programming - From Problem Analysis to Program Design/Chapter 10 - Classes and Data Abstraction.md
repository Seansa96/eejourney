# Chapter 10 - Classes and Data Abstraction

*C++ Programming: From Problem Analysis to Program Design* - D. S. Malik, 8th edition. Examples use the book's C++11-era baseline.

# Classes

Recall that a `struct` groups related values under one type. A **class** can group both those values and the operations that work on them. The values describe an object's state; the member functions provide ways to inspect or change that state.

The class defines the type. An **object**, or instance, is a particular variable of that type. Two clocks have the same available operations, but each stores its own time.

The following declaration will serve as `Clock.h` for the examples. The member function definitions appear in the later sections.

```cpp


class clockType {
public:
    void setTime(int, int, int);
    void getTime(int&, int&, int&) const;
    void printTime() const;
    void incrementSeconds();
    void incrementMinutes();
    void incrementHours();
    bool equalTime(const clockType&) const;

private:
    int hr = 0;
    int min = 0;
    int sec = 0;
}; // required semicolon


```

`public` members form the interface available to client code. `private` members are implementation details that ordinary client code cannot access directly. A member function can itself be private if it is only an internal helper. `protected` is another access category, developed with inheritance in the next chapter.

**PRIVATE DATA LETS THE CLASS CONTROL ITS VALID STATES.** For a time of day, the class can maintain `0 <= hr < 24` and `0 <= min, sec < 60` instead of relying on every caller to remember those limits. Such a condition is a **class invariant**.

Defining a class does not create an object or allocate a separate set of instance data. Constructing an object creates its own non-static members; member function code is not duplicated inside each object.

## Unified Modeling Language Class Diagrams

A UML class diagram summarizes the interface and stored data in three compartments: class name, attributes, and operations.

| Symbol | Access |
| --- | --- |
| `+` | Public |
| `-` | Private |
| `#` | Protected |

For example, `- hr: int` describes a private integer, while `+ hours(): int` describes a public operation returning an integer. UML places the type after a colon; this is diagram notation, not literal C++ syntax. A constructor has no return type.

## Variable (Object) Declaration

```cpp
Clock first;                  // default construction: midnight
Clock second(9, 15, 0);        // construction with arguments
Clock third{18, 30, 0};        // C++11 direct-list initialization
```

Each object has its own `hr`, `min`, and `sec`. Changing `first` does not automatically change `second`. The class definition must be available before declaring an object that needs its complete type.

The zero values above come from **this class's member initializers**. Merely using `class` does not guarantee that ordinary local numeric members start at zero.

A class variable is called a **class object** or **class instance**. Although, typically we just say **object**.

In the above example, we have 10 members in each object: seven member functions, and then three member variables. Each object gets its own memory allocated for each of its member variables.

All objects of the same class will use one physical copy of the member functions of that class.

## Accessing Class Members

Use the object name, the **member access operator** `.`, and the member name:

```cpp
first.setTime(8, 20, 0);
int hour = first.hours();
bool equal = first.sameTime(second);
// first.hr = 8;              // error: hr is private
```

The parentheses call the function. In `first.sameTime(second)`, `first` is the object whose member function runs; `second` is the explicit argument. The function therefore needs only one parameter to compare two clocks.

**Access control applies to the code doing the accessing.** A member of `Clock` may inspect another `Clock` object's private members. Ordinary code in `main` may not, even when it holds that object.

Or, in plain English, if we declared an object in the definition of a member function, then it can access both public and private members--not the case if declared in a place like main.

## Built-in Operations on Classes

A new class does not automatically acquire meaningful arithmetic, ordering, or stream operations just because its members support them.

Below shows a table of operators you can use. Note that arithmetic and relational operators do not work.

| Operation on this `Clock` | Available? |
| --- | --- |
| `a.hours()` | Yes, through the public interface |
| `Clock b = a;` | Yes, copy initialization |
| `b = a;` | Yes, generated memberwise assignment |
| `a + b`, `a++` | No matching operators defined |
| `a == b`, `a < b` | No matching operators defined |
| `std::cout << a`, `std::cin >> a` | No matching stream operators defined |

Use a named operation such as `sameTime`, process accessible values, or define suitable overloaded operators later. In particular, **assignment support does not imply equality support**. This C++11-style class does not receive an automatic content comparison.

## Assignment Operator and Classes

```cpp
Clock original(7, 45, 0);
Clock copy = original;       // initializes a new object
Clock assigned;
assigned = original;        // replaces an existing object's state
copy.tick();               // original is unchanged
```

For this class, we see that the assignment operator does a **member-wise** copy. That is, it copies each private member variable and nothing else, because nothing else is needed to be copied. Recall that each object has its own memory allocated only for these variables, while they both share each member function.

Copying a pointer member would copy its address, rather than duplicate the pointed-to object. Also, some definitions, including those with `const` or reference data members, cannot use generated copy assignment. **Memberwise copying is not automatically a complete resource-ownership policy.** The later pointer chapters develop that issue.

Assignment does not invoke an ordinary constructor to construct the destination again, and it does not necessarily call your setters. Any validation needed by a custom assignment operation must be part of its design.

## Class Scope

Members belong to the class's scope. Inside a non-static member function, unqualified member names normally refer to the object on which the function was called. Outside the class, access members through the appropriate object or qualified class name.

A class object can be **automatic**, which is when control reaches its declaration it is created, and then destroyed when control exits the surrounding block.  You may also do similar things as we did with structs, such as declaring an array of class objects.

`Clock::hours` identifies a member in class scope. `first.hours()` calls it on a particular object. These uses of `::` and `.` serve different purposes.

An object also has the usual variable scope and storage duration. An ordinary local object is destroyed when its block exits; a function-local `static Clock saved;` persists across calls and is initialized the first time execution reaches its declaration. **An object's lifetime and access to its members are separate issues.**

## Functions and Classes

Class objects can be function parameters and return values. They can also be passed by value or by reference.

```cpp
Clock noon() {
    return Clock(12, 0, 0);
}

void advanceCopy(Clock value) {
    value.tick();             // changes only the parameter object
}
```

For an ordinary lvalue argument, passing by value creates a separate parameter using copying. Returning by value is valid; the compiler can often avoid intermediate copies. Do not return a reference to an ordinary local object, whose lifetime ends on return.

A free function does not gain access to private data merely because a parameter has that class type. It uses the public interface unless special access has been granted.

## Reference Parameters and Class Objects (Variables)

Suppose we have some class that has several member variables that take up a large amount of memory. When we pass by value, we have to copy those member variables into the formal parameters, which can take up not only a large amount of space, but a large amount of compute.

Thus, we may in this case choose to pass by reference, only providing the address of the actual parameter. Of course, we may not want the function to change those member variable values. In this case, we can use the keyword const in the formal

| Parameter | Purpose |
| --- | --- |
| `Clock value` | Separate value; local changes do not change the caller's directly stored data. |
| `Clock& value` | Reference to the caller's object; permits changes. |
| `const Clock& value` | Read-only access through the reference, without copying the object. |

```cpp
void advance(Clock& value) {
    value.tick();
}

int inspect(const Clock& value) {
    return value.hours();
}
```

Use `const&` when read-only access should avoid copying, especially for larger objects. It is not interchangeable with a value parameter when the function needs a disposable local copy.

`const` restricts operations through that reference. It does not freeze other references to the object, or automatically make externally pointed-to data const if the class contains pointers.

## Implementation of Member Functions

For a definition outside the class, qualify the function name with `ClassName::`. Without it, you would define an unrelated free function.

These definitions belong in `Clock.cpp`, which begins with `#include "Clock.h"`:

```cpp
void Clock::setTime(int hours, int minutes, int seconds) {
    hr  = (0 <= hours   && hours   < 24) ? hours   : 0;
    min = (0 <= minutes && minutes < 60) ? minutes : 0;
    sec = (0 <= seconds && seconds < 60) ? seconds : 0;
}

int Clock::hours() const {
    return hr;
}

bool Clock::sameTime(const Clock& other) const {
    return hr == other.hr && min == other.min && sec == other.sec;
}

void Clock::tick() {
    if (++sec < 60) return;
    sec = 0;
    if (++min < 60) return;
    min = 0;
    hr = (hr + 1) % 24;
}
```

The setter follows the book's policy of replacing each out-of-range component with zero. It does not normalize an input such as 90 minutes into one hour and 30 minutes. **Validation behavior is part of the interface contract; choose and document it.**

In `sameTime`, `hr` belongs to the receiving object and `other.hr` belongs to the argument. Both accesses are legal because the function is a member of `Clock`. Basically, if we recall how classes and objects work in memory, it becomes obvious why this happens. They both share the function, and thus the scope of the function, so when calling that function, one instance of a class can access another instance's private members.

Declarations and definitions must agree on parameter types and any trailing `const`. `int hours()` and `int hours() const` declare different member functions.

A **client** is any software or program that manipulates objects of a class.

## Accessor and Mutator Functions

An **accessor** observes the object's state. A **mutator** changes it. In this example, `hours` and `sameTime` are accessors; `setTime` and `tick` are mutators.

Place `const` after an accessor's parameter list to express that it does not modify the object's ordinary non-static data members. This makes the function a **constant** function.

```cpp
const Clock fixed(6, 0, 0);
int h = fixed.hours();       // allowed: const member function
// fixed.tick();             // error: non-const member function
```

An accessor needs that qualification to be callable through a `const` object or `const` reference. A const member function cannot call a non-const member function on the same object. It may still work with a separate non-const object.

The two uses of `const` in `bool sameTime(const Clock& other) const` protect different objects: the first restricts access through `other`; the trailing one restricts changes to the receiving clock.

Const does not mean “no observable effects anywhere.” For example, a const printing function can write to a stream without modifying the clock's stored time.

## Order of public and private Members of a Class

Access sections may appear in either order and may repeat. Each access label applies until the next one. Before the first label, a `class` is **private by default**.

Putting the public interface first helps a reader see how to use the type. That is a convention, not a syntax requirement. Also distinguish access-section order from **data member declaration order**, which determines member initialization order.

Placing either label ensures that the rest of the class falls under that access class. If you do:

```cpp
class clockType {
public:
	void setTime();
}
````

Then any other variables or functions you implement will be public. You need to specifically delineate the access boundaries.

## Constructors

A **constructor** initializes an object as it is created. It has the class's name and **no return type**, including no `void`, so it literally has no type.

Classes can overload constructors using different parameter lists. Construction selects a matching accessible overload; it does not call every constructor in the class.

Add this definition to `Clock.cpp`:

```cpp
Clock::Clock(int hours, int minutes, int seconds) {
    setTime(hours, minutes, seconds);
}
```

Here the member initializers first provide zeros, then the constructor body applies the validated input. The opening declaration's `Clock() = default;` requests a compiler-generated default constructor, which also uses those initializers.

**A CONSTRUCTOR IS ONLY AS COMPLETE AS ITS INITIALIZATION.** An empty body does not, by itself, zero an ordinary local object's numeric members.

For direct initialization of members, a constructor may instead use a **member initializer list**. This separate example assumes its arguments are already valid:

```cpp
class Reading {
public:
    Reading(int code, double value) : id(code), amount(value) {}
private:
    int id;
    double amount;
};
```

Members initialize in their **declaration order**, regardless of their order after the colon. Class-type members are constructed before the constructor body; a later assignment in the body is not their initial construction. `const` and reference members must be initialized appropriately rather than assigned afterward.

## Invoking a Constructor

Construction happens when an object is initialized. Supply arguments in the object declaration, rather than trying to invoke the constructor as an ordinary member function.

```cpp
Clock alarm(6, 30, 0);
// alarm.Clock(7, 0, 0);     // error: not an ordinary callable member
alarm.setTime(7, 0, 0);      // modifies the existing object
alarm = Clock(8, 0, 0);      // constructs a temporary, then assigns
```

The last two statements can lead to the same stored time, but they are different operations.

## Invoking the Default Constructor

A **default constructor** is a constructor callable without arguments. It can have no parameters, or parameters that all have defaults.

```cpp
Clock a;
Clock b{};
Clock c();                  // declares a function, NOT an object
```

`Clock c();` declares a function named `c` returning `Clock` and taking no arguments. It is not the syntax for constructing an empty local clock.

Both `a` and `b` are safely initialized for our class. **Do not assume `T{}` repairs an incomplete user-provided constructor for every class.** Initialize the data explicitly or provide default member initializers.

## Invoking a Constructor with Parameters

```cpp
Clock meeting(14, 10, 0);
Clock departure{17, 45, 0};
```

Arguments match parameters by position. Their number and types must select a viable, unambiguous constructor; allowed conversions may participate. Brace initialization additionally rejects narrowing conversions, such as a non-integral `double` supplied to an `int` parameter.

For a one-argument constructor, consider `explicit` when implicit conversion to the class should not be allowed:

```cpp
class Radius {
public:
    explicit Radius(double value) : r(value) {}
private:
    double r;
};

Radius direct(2.5);          // allowed
// Radius implicit = 2.5;    // error: explicit constructor
```

`explicit` controls implicit conversion; it does not validate the argument.

## Constructors and Default Parameters

The book shows how one constructor with default arguments can replace several overloads. As an **alternative** to our two constructor declarations, the declaration could be:

```cpp
Clock(int hours = 0, int minutes = 0, int seconds = 0);
```

This permits zero, one, two, or three arguments. Omitted values come from the right: `Clock(9)` means hour 9, minute 0, second 0. Defaults follow the same trailing-parameter rule as ordinary functions.

Put the defaults in the declaration visible to callers and do not repeat them in the out-of-class definition. **Do not keep a separate `Clock()` alongside this all-defaulted overload:** calling with no arguments would be ambiguous.

## Classes and Constructors: A Precaution

If no constructor is user-declared, the compiler can implicitly declare a default constructor. Once you declare a constructor, it does not automatically add a separate no-argument constructor for you.

```cpp
class Required {
public:
    explicit Required(int value) : number(value) {}
private:
    int number;
};

Required valid(3);
// Required missing;        // error: no default constructor
```

Provide a default constructor when a meaningful default state is needed. It is also valid to require arguments deliberately. Adding a meaningless default state merely to make a declaration compile can weaken the design.

An implicitly generated default constructor does **not** mean all members are left untouched, nor that all members become zero: class-type members run their constructors and default member initializers apply. Uninitialized scalar members in an ordinary local object remain a hazard. Reading an indeterminate `int` is not a reliable way to obtain a “random default.”

## In-Class Initialization of Data Members and the Default Constructor

C++11 allows default initializers for non-static data members, as in `int hr = 0;`. These provide initial values when a constructor does not initialize those members in its member initializer list.

```cpp
class Setting {
public:
    Setting() = default;
    explicit Setting(int value) : level(value) {}
    int getLevel() const { return level; }
private:
    int level = 5;
};
```

`Setting a;` uses 5. `Setting b(8);` uses 8 because its member initializer overrides the default. Initializing `level` in the class definition does not itself restore a missing default constructor after a different constructor has been declared.

## Arrays of Class Objects (Variables) and Constructors

```cpp
Clock arrivals[100];         // default-constructs every element
arrivals[49].setTime(8, 5, 0);

Clock appointments[2] = {
    Clock(9, 0, 0),
    Clock(13, 30, 0)
};
```

Every element is an object, and indexing selects that object before `.` selects its member. For an array declared without element initializers, each element must be default-constructible.

A default constructor is **not required for every possible array declaration**: a class requiring arguments can still be used if every element is initialized appropriately. If some trailing elements are omitted from an initializer list, those elements must also be initializable from the omitted initializers.

Built-in array bounds are still unchecked. A class element does not make `arrivals[100]` valid, or allow whole-array assignment such as `arrivals = otherArrivals`.

## Destructors

A **destructor** runs when an object's lifetime ends. Its name is `~ClassName`; it has no return type and takes no parameters. A class has one destructor, which cannot be overloaded.

```cpp
class Plain {
public:
    ~Plain() = default;
};
```

Ordinary local objects are destroyed when their block exits, in reverse construction order. Array elements are destroyed in reverse element order. Dynamically allocated objects require the appropriate lifetime management, covered later.

For simple classes holding numbers and library-managed values, the generated destructor usually suffices; member objects are destroyed automatically. A destructor is not a replacement for understanding who owns an external resource. **Do not manually invoke a destructor on an ordinary local object and then continue using it.**

# Data Abstraction, Classes, and Abstract Data Types

**Data abstraction** separates what a type represents and what its operations mean from how it stores and processes the data. An **abstract data type**, or ADT, describes a set of values and operations independently of a particular representation.

For our clock, a client needs to understand “time of day,” setting the time, reading the hour, comparing times, and advancing a second. It does not need to manipulate three integers directly. The implementation could later store seconds since midnight while preserving those meanings.

A C++ class is a mechanism for implementing an ADT. A class declaration alone does not guarantee a useful abstraction: the operations must preserve the type's rules and have clear behavior.

## A struct versus a class

Both can contain data, member functions, constructors, destructors, and access sections. The relevant language differences are the defaults:

| Default | `struct` | `class` |
| --- | --- | --- |
| Member access | Public | Private |
| Base-class access when inheriting | Public | Private |

The book uses structs mainly for simple public records and classes for controlled interfaces. This is a design convention, not a restriction preventing structs from having functions.

# Information Hiding

The interface should tell callers what an operation does, what it requires, and what it guarantees. The implementation supplies the storage choices and algorithms.

- **Precondition:** something that must be true before the operation.
- **Postcondition:** something guaranteed after successful completion, assuming its preconditions.
- **Invariant:** a rule maintained for the object's valid state across operations.

For example, a sale operation may require positive stock and guarantee one fewer item. Alternatively, it can check stock itself and report failure. State which policy applies; the existence of a setter does not automatically make every update safe.

The usual file arrangement is:

| File        | Contents                                                    |
| ----------- | ----------------------------------------------------------- |
| `Clock.h`   | Class definition and interface declarations; include guard. |
| `Clock.cpp` | Out-of-class member definitions; includes `Clock.h`.        |
| `main.cpp`  | Client code; includes `Clock.h`.                            |

Use `#include "Clock.h"` for the project header. An include guard prevents repeated inclusion from redefining the class within one translation unit.

**PRIVATE IS AN ACCESS RULE, NOT ENCRYPTION.** Private declarations can still be visible in a header. Likewise, putting code in a separate file does not by itself change access permissions. The benefit is reducing client dependence on implementation details.

# Executable Code

The first code block provides `Clock.h`. Put the four out-of-class member definitions and the parameterized constructor definition into `Clock.cpp`, preceded by `#include "Clock.h"`. A client can then be:

```cpp
// main.cpp
#include <iostream>
#include "Clock.h"

int main() {
    Clock current(23, 59, 59);
    current.tick();
    const Clock midnight;
    std::cout << current.hours() << '\n';          // 0
    std::cout << current.sameTime(midnight) << '\n'; // 1
}
```

For a GCC-style compiler, compile and link both source files:

```sh
g++ -std=c++11 -Wall -Wextra -pedantic main.cpp Clock.cpp -o clock_demo
```

`#include` makes declarations available; it does not automatically link a separate `.cpp` file. A declared function without its needed definition can compile at the call site and still fail at link time. Keep ordinary non-inline definitions in one implementation file, and provide only one `main` for this executable.

# More Examples of Classes

The book develops a circle, a die, a person, and an integer-processing object. Their useful design lessons are:

| Example | State and operations | Implementation concern |
| --- | --- | --- |
| Circle | Radius; set/read radius, calculate area and circumference. | Validate radius and calculate derived values from the current radius. |
| Die | Current face; roll and read the result. | Each die has its own face value; random-number generation is an implementation detail. |
| Person | First and last names; set, retrieve, and print names. | Class-type members such as `std::string` manage their own stored values. |
| Integer manipulation | Number, digit counts, reversed number. | Cached results must correspond to the current number; recompute or invalidate them when it changes. |

The common idea is to store enough state to represent the object, then expose operations with clear meanings. Avoid storing redundant results unless the class also keeps them consistent.

# Inline Functions

A member function defined inside the class definition is implicitly **inline** in the ordinary header-based setting used here:

```cpp
class Switch {
public:
    bool isOn() const { return on; }
    void toggle() { on = !on; }
private:
    bool on = false;
};
```

For an out-of-class definition placed in a header, write `inline` explicitly when appropriate. It permits identical definitions in multiple translation units under the language's definition rules.

**INLINE DOES NOT FORCE THE COMPILER TO SUBSTITUTE THE FUNCTION BODY AT EVERY CALL.** The compiler decides whether to perform that optimization, and can optimize a function without the keyword. Short accessors are common inline definitions because keeping them in the header is convenient.

# Static Members of a Class

A non-static data member belongs to each object. A **static data member** is one shared member associated with the class, and can exist even when no objects of that class exist.

```cpp
class SharedCounter {
public:
    void incrementLocal() { ++local; }
    int localValue() const { return local; }
    static void recordEvent() { ++events; }
    static int eventCount() { return events; }
private:
    int local = 0;
    static int events;       // declaration, not the storage definition
};

// In exactly one .cpp file for this C++11 example:
int SharedCounter::events = 0;
```

`SharedCounter::recordEvent()` changes the shared event count. `a.incrementLocal()` changes only `a`'s local count. `SharedCounter::eventCount()` can be called without constructing any counter objects.

A **static member function has no receiving object**. It cannot directly access a particular object's non-static data; it would need an object or reference explicitly. It can access private static members, as above, and cannot have a trailing member-function `const`.

Use `static` in the member declaration, not again on an out-of-class member definition. Access control still applies: a private static member is not directly accessible to ordinary client code through `ClassName::member`.

The shared count is not automatically the number of live objects. To represent that, construction, copying, and destruction would all need a consistent counting policy. C++17 inline static variables are a later alternative to the separate definition shown here.

# Programming Example: Juice Machine

The example separates the machine's responsibilities into a **cash register**, which tracks money, and **product dispensers**, which track price and available stock. Client code coordinates a purchase using their public operations.

The important sequence is: check availability, obtain payment, check sufficiency, then update the register and stock only if the sale succeeds. Prices and payments are represented in integer cents.

Both objects must be passed by non-const reference to an operation that changes them:

```cpp
void sellProduct(Dispenser& product, CashRegister& registerBox);
```

This signature assumes those types have been declared. Passing either object by value would update a copy, leaving the actual dispenser or register unchanged.

The textbook program allows an initial deposit and one additional deposit. On a successful sale, it records the **entire amount deposited** and does not calculate change. That is the example's policy, not a consequence of using classes. A fuller implementation needs explicit behavior for change, invalid input, and unsuccessful transactions.

# Quick Review

| Question | Rule to remember |
| --- | --- |
| Does defining a class create an instance? | No; declare an object to create its instance data. |
| Can client code access private data through an object? | No; use the public interface. |
| Can a member inspect another instance's private data? | Yes, for the same class. |
| Does copying make two objects aliases? | No; ordinary memberwise copies create separate stored state. Pointer targets can still be shared. |
| Which parameter avoids copying for read-only access? | Usually `const T&`; value semantics remain useful when a separate copy is intended. |
| What makes a member callable on a const object? | An appropriate trailing-`const` member function declaration. |
| Does any constructor guarantee zeroed numbers? | No; initialize every member appropriately. |
| Does `T object();` create a default object? | No; it declares a function. |
| Is a default constructor always supplied? | No; user-declared constructors affect its implicit declaration. |
| Does `static` data belong to each object? | No; it is shared class-level state. |
| Does `inline` guarantee faster execution? | No; call substitution is an optimization decision. |

# Exercises

Useful checks when reviewing this chapter:

- Explain why `sameTime` takes one clock argument, and identify which object each `const` protects.
- Predict which constructor a declaration selects, including omitted default arguments and the `T object();` trap.
- Distinguish a compile-time access error from a missing-definition linker error.
- Trace a value parameter, a reference parameter, and a shared static member across two objects.

# Programming Exercises

For implementation practice, extend the examples without exposing their private state:

- Add read-only minute and second accessors, then verify second, minute, hour, and midnight rollover.
- Implement the circle interface with a documented invalid-radius policy and const calculation functions.
- Extend the juice-machine transaction to calculate change while preserving stock and cash when a purchase fails.

For each extension, state the invariant, the arguments required, the result returned, and which existing objects may change. These decisions determine the interface before the function bodies are written.
