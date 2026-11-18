# Chapter 7 - User-Defined Simple Data Types, Namespaces, and the string Type

*C++ Programming: From Problem Analysis to Program Design* - D. S. Malik, 8th edition. The examples use the book's C++11-era baseline.

# Enumeration Types

Suppose a program needs to record whether a task is ready, running, or finished. We could use the integers 0, 1, and 2, but then every reader must remember which number represents which state.

An **enumeration**, or enum, gives those values names and groups them under a distinct type:

```cpp
enum Status { READY, RUNNING, FINISHED };
Status state = READY;
```

`Status` is the type, `state` is a variable, and `READY`, `RUNNING`, and `FINISHED` are **enumerators**. They are named constants, not variables that we can assign new values to.

The first unspecified enumerator starts at 0, and each later unspecified value is the previous value plus 1. Thus these three codes are 0, 1, and 2.

We can supply explicit constant values instead:

```cpp
enum Code { OK = 0, RETRY = 10, FAILED = 11 };
```

This means declaration order does not always guarantee consecutive or increasing numerical values; explicit values can introduce gaps, duplicates, or a different order. Enumerators must be identifiers, not quoted characters or names beginning with a digit. The definition ends with a semicolon.

## Assignment and Arithmetic

The variable can hold a value of its own enum type:

```cpp
void enumExample() {
    Status state = READY;
    state = RUNNING;
    int followingCode = state + 1; // 2, with integer type
    std::cout << followingCode;
}
```

The arithmetic is allowed because an ordinary **unscoped enum** can undergo integral promotion. For this enum, `state + 1` produces an `int`; it does not produce a new `Status` value automatically.

That distinction explains the restriction:

| Expression | Meaning / result |
|---|---|
| `state = FINISHED` | Valid assignment of a `Status` value |
| `state = 1` | Invalid implicit integer-to-enum assignment |
| `state + 1` | Valid promoted integer arithmetic |
| `state = state + 1` | Invalid implicit conversion back to `Status` |
| `++state` | No built-in enum increment |
| `state == READY` | Valid value comparison |

**THE RESULT OF ENUM ARITHMETIC IS NOT AUTOMATICALLY AN ENUM VALUE.** The book's blanket statement that arithmetic is unavailable is too broad; the restriction is important when assigning the result back.

An explicit `static_cast<Status>(number)` requests that conversion, but does not check whether the number is one of the named states. For enums without a fixed underlying type, an out-of-range conversion can itself be undefined behavior. Read and validate input, then select a named enumerator. Do not treat a cast as validation.

Likewise, increment-and-cast code assumes consecutive values and an appropriate stopping point. It is not a general way to traverse every enum definition.

## Comparison, Input, and Output

Comparisons of values from the same enum use their numerical ordering. With the default `Status` values, `READY < FINISHED` is true. If explicit codes change the numerical order, comparisons follow those codes.

Unscoped enums can also be output through integer promotion: `std::cout << state` prints a number. It does not automatically print the word `RUNNING`.

Ordinary stream extraction does not directly parse an enum. Read text or an integer into another variable, check it, and map it to a named value. A small switch makes textual output explicit:

```cpp
const char* statusName(Status state) {
    switch (state) {
    case READY:    return "ready";
    case RUNNING:  return "running";
    case FINISHED: return "finished";
    }
    return "unknown";
}
```

Here the return values point to string literals, whose lifetime continues after the function returns. This differs from returning a pointer to an ordinary local character array.

Enums can be passed by value or reference and returned by value. Separate enum definitions remain distinct types even when their values look alike. A named enum also makes a clearer function interface than an anonymous one.

## Unscoped Versus Scoped Enums

The ordinary enum introduces its enumerator names into the surrounding scope. Two unscoped enums in that same scope cannot both declare a name such as `READY`.

A C++11 **scoped enum** keeps the names under the enum type:

```cpp
enum class Mode { read, write };
Mode mode = Mode::read;
int code = static_cast<int>(mode);
```

Unlike an unscoped enum, `Mode` does not implicitly convert to an integer. The explicit qualification prevents name collisions, and the lack of implicit conversion prevents many accidental mixed-type operations. Use the rules of the form actually declared; the book's unscoped-enum promotion rules do not carry over to `enum class`.

# typedef and Type Aliases

An enum creates a distinct type. A type alias only gives an existing type another name:

```cpp
typedef unsigned int Count;
using ItemCount = unsigned int; // C++11 alternative syntax
```

`Count`, `ItemCount`, and `unsigned int` still name the same underlying type. These declarations do not allocate an ordinary variable or add range checking.

This also means `Count` and `unsigned int` cannot distinguish two function overloads. The names look different, but the compiler is seeing the same parameter type.

# Namespaces

What if two libraries both define a function named `print`? The problem is not with either function individually; it is that the unqualified name no longer clearly identifies which one we mean.

A **namespace** groups names so they can be qualified:

```cpp
namespace settings {
    const int limit = 10;
    int doubled(int value) { return value * 2; }
}

int readLimit() {
    return settings::limit;
}
```

The `::` is the **scope resolution operator**. `settings::doubled(3)` identifies the function inside `settings`. This is different from `.` on an object: a namespace is a scope of names, not an instance of a struct.

Namespaces can be reopened and can contain other namespaces. Their definitions belong at namespace scope, rather than inside a function.

## The Two Forms of using

`using settings::limit;` makes one particular name available unqualified. `using namespace settings;` makes the namespace's names available for unqualified lookup.

Neither creates copies of the objects. Both affect how names can be found, and a broad using-directive can make a previously clear name ambiguous when another namespace supplies the same one.

This is why explicit qualification is useful in shared headers. A header-level `using namespace std;` affects every source file that includes it. Bringing in one needed name, or writing its namespace explicitly, makes the dependency easier to see.

**A USING STATEMENT DOES NOT INCLUDE A HEADER.** We still need `<string>` before using `std::string`, and `<iostream>` before using `std::cout`.

# The string Type

A built-in character array has fixed capacity and special rules for null-terminated text. `std::string` is a library type that owns its character storage and supports changing the text's length.

```cpp
std::string name = "Mira";
std::string copy = name;
name += " Chen";
bool same = (name == copy); // false
```

The assignment to `copy` creates an independent string value. Appending to `name` changes `name` to `"Mira Chen"`, while `copy` stays `"Mira"`. The two variables began with equal contents; they did not become the same string object.

## Assignment, Concatenation, and Comparison

The `+` operator concatenates when an appropriate `std::string` operand is present. `name + " Chen"` produces a new string, while `name += " Chen"` modifies the existing one.

`"Mira" + " Chen"` does not work because both operands are character arrays, not `std::string` objects. Adjacent literals, `"Mira" " Chen"`, instead join at compile time without `+`.

String comparisons are **lexicographic**: compare the first differing character, or treat the shorter string as less if it is a prefix of the other. They are case-sensitive, rather than natural-language alphabetical comparisons. String length alone does not determine the order.

`compare()` reports the same kind of ordering using a negative value, zero, or a positive value. Do not require exactly `-1` or `1`, despite the book's simplified table.

# String Size and Character Positions

The length tells us how many characters are stored. An index identifies one position within that text. These are related, but they are not the same thing:

```cpp
std::string text = "code";
text[0] = 'C';
char last = text.at(text.size() - 1); // 'e'
```

The string has size 4, with text characters at positions 0, 1, 2, and 3. Thus the last character is at `size() - 1`, provided the string is not empty. `size()` and `length()` report the same count.

**THE SIZE IS NOT THE INDEX OF THE LAST TEXT CHARACTER.** In C++11, `s[s.size()]` exposes the null terminator used for C-string interoperability. It is not spare room in which to place another non-null character. Use append operations to grow the string.

`s[i]` does not provide checked access to an existing character. Keep text indices below `s.size()`. `s.at(i)` instead checks and throws `std::out_of_range` when `i >= s.size()`. `front()` and `back()` also require nonempty text.

## Unsigned Positions

String sizes and positions use `std::string::size_type`, an unsigned integer type. `auto` is convenient when storing a result without guessing its exact type.

An empty string's size is 0, so subtracting 1 from that unsigned value wraps to a large positive number. Check for emptiness before using `size() - 1`, and do not expect an unsigned reverse counter to become negative.

Also, a `std::string` stores `char` units. With UTF-8 text, several of those units can represent one visible character, so `size()` is not necessarily a count of displayed letters.

# Finding and Changing Text

| Operation | Effect |
|---|---|
| `s.empty()` | Tests whether there is any text |
| `s.clear()` | Removes all the text |
| `s.append(part)` | Adds text at the end |
| `s.substr(pos, count)` | Returns a new substring; leaves `s` unchanged |
| `s.erase(pos, count)` | Removes text in place |
| `s.insert(pos, part)` | Inserts text before `pos` |
| `s.replace(pos, count, part)` | Replaces existing text with `part` |
| `s.find(part, pos)` | Finds a substring or character at or after `pos` |
| `s.find_first_of(chars, pos)` | Finds a character belonging to the supplied set |
| `s.find_first_not_of(chars, pos)` | Finds a character outside the supplied set |
| `s.swap(other)` | Exchanges the two strings' contents |

For the positional substring and modifying operations listed here, a starting position greater than size throws `std::out_of_range`; a starting position equal to size is allowed. An oversized removal or substring count reaches only to the end. Replacing a short section with longer text can increase the string's size.

## Why npos Needs an Explicit Check

A failed search returns `std::string::npos`, rather than a valid character position:

```cpp
void enlargeFirstO(std::string& text) {
    auto pos = text.find('o');
    if (pos != std::string::npos) {
        text.replace(pos, 1, "OO");
    }
}
```

For `"code"`, `pos` is 1. The function replaces one character there with two, producing `"cOOde"`. If there is no `o`, the test prevents us from using the failure marker as a position.

`if (text.find('o'))` would be wrong for two reasons: a match at index 0 converts to false, while the large unsigned failure value converts to true. Thus **TEST FOR SEARCH SUCCESS, NOT WHETHER THE RETURNED NUMBER IS NONZERO**.

Do not add 1 to a result before checking it either. Arithmetic on `npos` can wrap and produce an ordinary-looking index.

## Storage Can Change

String operations that grow or otherwise modify the text can invalidate pointers, references, or iterators into its storage. An earlier character pointer is not guaranteed to keep referring to the current text after such a change.

`reserve()` requests storage capacity; it does not add text characters. `resize()` changes the text's size. Extra capacity is not permission to index beyond the existing text.

# Input, Output, and Functions

`std::cin >> text` skips leading whitespace and reads a token. `std::getline(std::cin, text)` reads a line, consumes its delimiter, and leaves that delimiter out of the string.

If numeric extraction leaves a newline pending, the next `getline` can immediately consume it and return an empty line. Discard the rest of the preceding line when that matches the input format. `std::getline(std::cin >> std::ws, text)` is another option, but it removes leading whitespace and skips blank lines; it changes what input is preserved.

The parameter rules from Chapter 6 still apply. Pass a string by value when you need an independent parameter object, by `std::string&` when changing the caller's text, and by `const std::string&` for read-only access without copying. Returning a string by value is supported.

## Interacting with C-Strings

`text.c_str()` provides a null-terminated, read-only character pointer for an API expecting a C-string. It is access to the string's storage, not a separately owned copy. Do not write through it, keep it after the string is destroyed, or rely on it surviving an invalidating modification.

A `std::string` can contain embedded null characters. Its own size still counts them, but a C-string API sees only the prefix before the first null. The two representations therefore do not always describe the same apparent text.

Technical clarifications: [C++ working draft — enums](https://eel.is/c++draft/dcl.enum) and [string element access](https://eel.is/c++draft/string.access).
