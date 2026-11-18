# Chapter 9 - Records (structs)

*C++ Programming: From Problem Analysis to Program Design* - D. S. Malik, 8th edition. Focus: the book's simple record-style structs.

# Declaring a Struct

A **struct** groups related values under one type. Unlike an array, its members can have different types and are selected by name rather than position.

```cpp
#include <string>

struct Student {
    std::string name;
    int scores[3];
    double gpa;
}; // the semicolon is required
```

This defines the type; it does not create a `Student` object. Declare objects separately, or place their names after the closing brace before the semicolon. Define the type before creating objects that need its complete layout.

Members have their own types and must have distinct names within the same struct. Different struct types can reuse a member name. Members are **public by default**; a `struct` in C++ can also have functions, constructors, and access controls, though the chapter uses simple data records.

Two separately defined struct types remain different types even if their member lists are identical. Matching field layouts do not make one implicitly assignable to the other.

## Initialization

```cpp
Student empty{};                          // empty name, zero scores and gpa
Student first{"Mira", {84, 91, 88}, 3.7}; // declaration order
Student other;                           // name constructed; numbers uninitialized
```

For this simple aggregate form, brace initializers follow the order of member declarations, not an arbitrary order. Missing trailing members are initialized from empty initializers; scalar numbers become zero. Too many initializers or narrowing conversions in brace initialization are errors.

An ordinary local `Student other;` does not automatically initialize its numeric members. The `std::string` member constructs an empty string, but that does not zero the neighboring integers or `double`. Prefer `{}` when you want an initialized empty record.

## Accessing Members

Use the **member access operator**, `.`:

```cpp
first.gpa = 3.8;
first.scores[1] = 95;
bool passed = first.scores[1] >= 60;
```

Select the member first, then apply that member's type rules. `first.scores` is still a built-in array; putting it inside a struct does not make direct array assignment or content comparison valid.

# Assignment and Other Operations

For a simple record whose members support copying, whole-struct assignment is allowed:

```cpp
Student second = first; // initializes a new object from first
second = first;         // assigns to an existing object
second.scores[0] = 100; // does not change first.scores[0]
```

The generated operations copy members. Built-in array members are copied **element by element**, even though an array by itself cannot be assigned with `=`. Nested structs and `std::string` members are copied using their own copy operations.

**COPYING A STRUCT DOES NOT MAKE TWO VARIABLES THE SAME OBJECT.** Its directly stored array elements are independent after copying. However, if you add a pointer member, copying that pointer copies the address, not the pointed-to data. Both copies can then refer to the same external object; ownership is not automatically duplicated.

| Whole-record operation | Available automatically for the simple struct above? |
|---|---|
| Copy initialization and `=` | Yes, between the same struct type |
| `+`, `-`, `*`, `/`, `++` | No |
| `==`, `!=`, `<`, `>` | No automatic content comparison in this C++11-style definition |
| `std::cin >> object` | No |
| `std::cout << object` | No |

Process members or define suitable operators/functions yourself. A C++20 explicitly defaulted comparison is a later feature, not something a plain record receives automatically.

```cpp
bool sameName(const Student& a, const Student& b) {
    return a.name == b.name;
}
```

This compares names, not complete records. If equality should include every score and GPA, compare those too. The programmer decides which fields define identity or ordering.

Likewise, read and write members individually: `std::cin >> first.gpa;`. Use `std::getline(std::cin, first.name)` for a name containing spaces, accounting for a newline left by previous formatted input.

Copy assignment can be unavailable for other struct definitions. For example, a `const` or reference data member, or a member that cannot be copied, can cause the generated assignment operator to be deleted. Do not assume every possible struct is assignable.

# Passing and Returning Structs

```cpp
void modifyCopy(Student s) { s.gpa = 0.0; }
void reset(Student& s)     { s.gpa = 0.0; }
double readGpa(const Student& s) { return s.gpa; }

Student makeStudent() {
    Student s{};
    s.name = "Mira";
    return s;
}
```

- **By value**, `Student s`: creates a separate parameter object. For an ordinary lvalue argument, its members are copied, including array members. Changes to those stored values do not change the caller's record.
- **By reference**, `Student& s`: operates on the caller's object. Use it when the function should modify that object.
- **By const reference**, `const Student& s`: avoids copying the record and prevents modifying its members through this reference. Useful for read-only access to larger records.
- **Return by value**, `Student`: supported. The returned object survives independently of the local variable; the compiler can often avoid an intermediate copy.

Do not return a reference or pointer to an ordinary local record: its lifetime ends when the function returns. Returning the record **by value** is different and is valid.

If a record contains pointers, passing it by value still permits changes to shared pointed-to data through those pointers. Likewise, a const reference does not automatically make externally pointed-to objects const.

# Combining Arrays and Structs

```cpp
struct Group {
    Student members[10];
    int used;
};

Group group{};
group.used = 1;
group.members[0] = first;
group.members[0].scores[2] = 90;
```

Use `[]` to select a record, `.` to select its member, and another `[]` if that member is an array. Keep `0 <= used <= 10`; the struct does not enforce this invariant for you.

`Group copy = group;` copies the embedded array as part of the record. Passing `Group` by value copies the record's stored contents. Passing just `group.members` to an ordinary array parameter instead follows the array-to-pointer rules from Chapter 8.

A nested struct works similarly: if `employee.hireDate` is a date record, use `employee.hireDate.year` to reach its year. A by-value nested type must already be complete. A struct cannot contain an object of its own type directly, because that would require an endlessly nested object; a pointer to its own type is allowed.

# Memory and Lifetime Quirks

The implementation can insert **padding** between members or after the last member for alignment. `sizeof(Student)` therefore need not equal the sum of the apparent member sizes. An array of structs places each complete object, including its padding, after the previous one.

Do not compare records with `std::memcmp` to decide whether their values are equal: padding and member representations do not define semantic equality. Do not serialize a record containing `std::string` or pointers by blindly dumping its raw bytes. Save the meaningful member values instead.

The struct owns its directly stored members. When an ordinary local record is destroyed, its embedded arrays and nested objects end their lifetimes too, and `std::string` handles its own resources. A raw pointer member does **not** automatically free the external object it points to.

Technical clarification: the C++ working draft specifies [member-wise generated assignment, including array members](https://eel.is/c++draft/class.copy.assign).
