# Chapter 6 - User-Defined Functions

*C++ Programming: From Problem Analysis to Program Design* - D. S. Malik, 8th edition. The examples use the book's C++11-era baseline.

# Functions and the Flow of a Program

A **function** groups a particular task under a name. Instead of repeating the same calculation or input procedure throughout a program, we define it once and call it where needed.

It is useful to think about three separate things: what information goes into the function, what work it performs, and how its result reaches the caller. A returned value and a change to an argument are two different ways of sending information back.

```cpp
int larger(int first, int second) {
    return first > second ? first : second;
}
```

Here `int` before the name is the **return type**. The variables `first` and `second` are **formal parameters**, which name the incoming values inside the function.

When we write `larger(4, 9)`, the expressions `4` and `9` are the **arguments**, or actual parameters. Their positions determine which parameter receives which value. The names used by the caller do not need to match the parameter names.

That call evaluates to 9. Thus `int result = larger(4, 9);` stores the answer in `result`, while `larger(4, 9);` performs the call and discards its result. Returning a value does not automatically print it or assign it to a variable in the caller.

## Declaration Versus Definition

Before compiling a call, the compiler needs to know the function's interface. A **declaration**, also called a prototype here, provides that information without the body:

```cpp
int larger(int first, int second);
```

The earlier version with braces is the **definition**. We can place the prototype before `main` and the definition afterward. The declaration makes the call understandable; the definition supplies the work that will actually run.

Parameter names are optional in a prototype, so `int larger(int, int);` declares the same interface. The return type and parameter types must agree between declarations and the definition.

**DECLARING A FUNCTION DOES NOT IMPLEMENT IT.** A declaration can let compilation succeed, but calling the function without providing a linked definition usually produces a linker error.

Use parentheses to call even a parameterless function: `readCount()`. The expression `readCount` alone names the function. Ordinary named functions cannot be defined inside other functions; local lambdas are a separate facility.

For a predefined library function, include its header and use its declared interface, such as `<cmath>` and `std::sqrt`. A `using` statement does not supply a missing declaration or header.

# Returning a Value

When a `return` executes, the function stops immediately and control returns to its caller. Only one return statement is executed on that call, even when several appear in different branches.

```cpp
int absoluteSmall(int value) {
    if (value < 0) {
        return -value;
    }
    return value;
}
```

For `-5`, the first return sends back 5 and the second is never reached. For 5, the branch is skipped and the final return supplies the result. This example assumes the positive result is representable; negating the most negative `int` would overflow.

A non-`void` function must return a valid result on every normally completing path. Reaching its closing brace without a value is undefined behavior. `main` has a special rule: reaching its end is equivalent to returning 0.

## The Return Type Affects the Result

The returned expression is converted to the declared return type when that conversion is allowed. Returning `3.75` from an `int` function loses the fractional part.

Be careful about *when* a conversion happens:

```cpp
double average(int sum, int count) {
    return sum / static_cast<double>(count);
}
```

Assuming `count` is nonzero, converting the denominator makes the division floating-point. For `sum = 5` and `count = 2`, the answer is 2.5.

If we instead wrote `static_cast<double>(sum / count)`, integer division would happen first, producing 2. Converting that result gives 2.0. **A CONVERSION AFTER THE CALCULATION CANNOT RESTORE INFORMATION ALREADY DISCARDED.**

One return statement returns one value, but that value can be a composite object, such as a struct containing several related results. It need not be a single number.

## Void Functions

A `void` function supplies no result value. It can still perform work, print output, or change an object through a reference.

```cpp
void printPositive(int value) {
    if (value <= 0) {
        return;
    }
    std::cout << value << '\n';
}
```

The bare `return;` exits early. It does not return the integer 0. A void function can also finish by reaching its closing brace normally.

# Value Parameters: Working with a Copy

Suppose a function changes its parameter. Does that change the caller's variable?

```cpp
void changeCopy(int value) {
    value = 0;
}

void valueExample() {
    int number = 6;
    changeCopy(number);
    std::cout << number; // still 6
}
```

When the call begins, the value 6 is copied into the parameter `value`. The function then assigns 0 to that separate integer. The caller's `number` and the function's `value` started with equal contents, but they are different objects.

This is **passing by value**. A value parameter can receive a variable, literal, or expression as long as the type rules allow it. The function can change its own copy without changing the caller's stored value.

# Reference Parameters: Working with the Caller’s Object

Now change the parameter declaration:

```cpp
void changeOriginal(int& value) {
    value = 0;
}

void referenceExample() {
    int number = 6;
    changeOriginal(number);
    std::cout << number; // now 0
}
```

The `&` makes `value` a **reference parameter**. It is an alias for the caller's integer, so the assignment reaches `number` itself. We call the function in the same way; the difference is in the parameter declaration.

**A REFERENCE PARAMETER DOES NOT CREATE AN INDEPENDENT COPY OF THE ARGUMENT.** Assigning through the reference changes the referred object; it does not rebind the reference to another object.

An `int&` parameter needs a suitable modifiable lvalue. `changeOriginal(6)` and `changeOriginal(number + 1)` are invalid because the function is asking for a modifiable integer object, not a temporary result.

If two reference arguments name the same object, writes through one are immediately visible through the other. Do not assume your parameters refer to distinct objects unless the interface requires that.

## Const Reference Parameters

What if we want to avoid copying a large object, but do not want the function to change it?

```cpp
std::size_t nameLength(const std::string& name) {
    return name.size();
}
```

The reference provides access to the existing string, and `const` prevents modifying it through `name`. This is useful for read-only access to larger objects. Unlike a non-const lvalue reference, a const reference can also bind to a temporary, such as the string created for `nameLength("Mira")`.

| Parameter | Main purpose |
|---|---|
| `int value` | Read or change an independent local value |
| `int& value` | Intentionally modify the caller's integer |
| `const std::string& value` | Read a string without making a parameter copy |

Pass stream objects such as `std::istream` by reference because they cannot be copied.

There is an important limit to the copy explanation: copying a pointer copies its address, not the object at that address. A by-value pointer can still provide access to shared data. Ordinary built-in array parameters also follow pointer-adjustment rules, rather than copying all the elements; see Chapter 8.

## Argument Evaluation

Arguments must be evaluated before the function body uses the resulting parameters, but this does not generally mean they are evaluated left to right.

In C++11, `f(i++, i++)` has unsequenced modifications and undefined behavior. Put required changes in separate statements before the call. Later standards improve some sequencing rules, but still do not generally promise left-to-right argument order.

# Scope Versus Lifetime

**Scope** tells us where a name is visible. **Lifetime** tells us when its object exists.

A parameter belongs to its function, and a block-local name is available from its declaration within that scope and appropriate nested scopes. It is not available to unrelated functions merely because those functions are called from there.

An inner declaration can hide an outer name. `::count` can select a visible global `count`, while `settings::count` selects a namespace member. Reusing a name does not merge the objects.

## Automatic and Static Variables

Ordinary automatic locals are created as execution reaches their declarations and destroyed when their scope exits. Each function call has its own ordinary parameters and locals. Uninitialized local scalar values must not be read.

A local `static` behaves differently:

```cpp
int nextTicket() {
    static int ticket = 0;
    return ++ticket;
}
```

The first call returns 1, the next 2, and the next 3, as long as the counter remains representable. The object retains its stored value between calls, even though its name remains local to the function.

So a local static demonstrates why scope and lifetime are separate ideas: other functions cannot directly use that local name, but the object continues to exist after the call ends. A dynamic local-static initializer runs once when execution first reaches it. Scalar objects with static storage duration are zero-initialized if no other initialization supplies their value; this is guaranteed, not merely a compiler habit.

Globals also have static storage duration. Prefer explicit inputs and outputs over mutable globals, since hidden changes make calls harder to reason about. `extern int count;` declares an object defined elsewhere; it does not create a separate local integer.

**DO NOT RETURN A POINTER OR REFERENCE TO AN ORDINARY LOCAL OBJECT.** That object is destroyed when the function returns. Returning the object by value is different: the caller receives a result object whose lifetime can continue independently.

# Function Overloading

Overloading gives related operations the same name while distinguishing their parameter lists.

```cpp
int twice(int value) { return value * 2; }
double twice(double value) { return value * 2.0; }
```

`twice(3)` selects the integer version; `twice(3.0)` selects the double version. The argument types determine which overload is selected, rather than the type of the variable receiving the result.

Changing only parameter names or only the return type cannot distinguish overloads. Likewise, `f(int)` and `f(const int)` declare the same function: top-level const on a by-value parameter does not make a separate overload. References to const and non-const objects are different cases.

Conversions can make a call ambiguous when neither candidate is better. More overloads do not automatically make an interface easier to use.

# Default Arguments

```cpp
int scale(int value, int factor = 2);

int scale(int value, int factor) {
    return value * factor;
}
```

`scale(5)` behaves as a call with factor 2, while `scale(5, 3)` supplies 3 instead. The caller can omit an argument because the visible declaration supplies it; the function still has two parameters.

For ordinary functions, once a parameter has a default, the parameters to its right must also have defaults available. Arguments are omitted from the right; an empty middle comma slot does not mean “use the default.”

Put defaults in the declaration visible to callers and do not repeat them in the later definition, even with the same value. Combining overloads with defaults can make a call ambiguous. A non-const reference cannot use an integer literal as its default, because the literal cannot bind to that reference.

# Testing Functions

A **driver** calls a function with selected test inputs. A **stub** stands in for an unfinished dependency so the surrounding program can be developed.

Check boundary cases as well as ordinary ones: zero, negative values when permitted, empty strings, and repeated calls when state is retained. A stub returning a plausible constant can hide unfinished work, so label it clearly and replace it before relying on the program's results.

Technical clarification: [C++ working draft — default arguments](https://eel.is/c++draft/dcl.fct.default).
