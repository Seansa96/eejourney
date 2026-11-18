# Chapter 4 - Control Structures I (Selection)

*C++ Programming: From Problem Analysis to Program Design* - D. S. Malik, 8th edition. Implementation notes using the book's C++11-era baseline.

# Conditions and Comparisons

Selection changes which statements execute. A condition is converted to `bool`: zero is false, and a nonzero number is true. A comparison such as `score >= 60` produces a `bool` directly.

| Operator | Meaning |
|---|---|
| `==`, `!=` | Equal, not equal |
| `<`, `<=`, `>`, `>=` | Ordering comparisons |
| `!condition` | Logical negation |
| `a && b` | Both conditions must be true |
| `a || b` | At least one condition must be true |

`=` assigns; `==` compares. `if (score = 60)` can compile, but assigns 60 and then treats that nonzero value as true. It does not test the old score.

**WRITE BOTH COMPARISONS IN A RANGE TEST.** `0 <= score <= 100` compares the boolean result of `0 <= score` with 100, so it does not implement the mathematical inequality.

```cpp
bool validScore(int score) {
    return 0 <= score && score <= 100;
}
```

Arithmetic is grouped before ordering comparisons, then equality comparisons, then `&&`, then `||`. Unary `!` binds more tightly than comparisons: `!x == y` means `(!x) == y`. Use parentheses to express the intended grouping rather than relying on a long precedence chain.

## Short-Circuit Evaluation

Built-in `&&` evaluates its right operand only if the left is true. Built-in `||` evaluates its right operand only if the left is false. The left operand is evaluated first.

```cpp
bool dividesExactly(int numerator, int denominator) {
    return denominator != 0 && numerator % denominator == 0;
}
```

This guard checks zero before using `%` (assuming values for which the division itself is representable). Reversing the operands loses that protection. Do not put a required update or function call in a right operand that might be skipped. `&` and `|` are bitwise operators, not replacements for short-circuit `&&` and `||`.

# if, else, and Blocks

```cpp
char grade(int score) {
    if (score >= 90) {
        return 'A';
    } else if (score >= 80) {
        return 'B';
    } else {
        return 'C'; // simplified example
    }
}
```

An `if` controls one statement; braces group several statements into one block. Indentation alone has no effect. An `else` belongs to the nearest unmatched `if`, so braces also make nested decisions unambiguous.

- An `if`/`else if` chain executes only the first matching branch. Order overlapping tests carefully.
- Separate `if` statements are independent; several bodies can execute.
- `if (condition);` has an empty controlled statement. The following block then executes independently.
- There is no standalone `else`. Do not place an unrelated statement between an `if` body and its `else`.

## Conditional Operator

`condition ? trueExpression : falseExpression` produces a value. Only the selected branch is evaluated, but both branches still must satisfy the language's type rules.

```cpp
int smaller(int a, int b) {
    return a < b ? a : b;
}
```

The result type is determined from both alternatives. Mixing types can introduce conversions even when only one branch executes. Use `if` for more involved branching instead of deeply nested conditional expressions.

# switch

A `switch` evaluates its selector once and jumps to a matching constant label.

```cpp
int menuCode(char choice) {
    switch (choice) {
    case 'a':
    case 'A':
        return 1;
    case 'b': {
        int code = 2; // braces give this case a scope
        return code;
    }
    default:
        return 0;
    }
}
```

The selector must be integral or an enum in these examples; `double` and `std::string` are not supported selectors. Each `case` needs a compile-time constant value, with no duplicates after conversion. There may be at most one `default`, and it is optional.

**CASE LABELS DO NOT STOP EXECUTION.** Once a case is entered, execution continues through later labels unless a `break`, `return`, or other control transfer stops it. Several labels can intentionally share one body.

`break` exits the innermost enclosing switch or loop. `return` exits the function. Give a case its own braces when declaring initialized local variables; another case must not jump past their initialization into their scope.

# Comparison Pitfalls

- Floating-point computations can round. Exact `==` is often unsuitable for approximate computed values; choose a tolerance appropriate to the units and magnitude. A single arbitrary epsilon is not a universal solution.
- Character ordering follows the execution character encoding. Do not assume all character ranges or uppercase/lowercase relationships are portable ASCII arithmetic.
- `std::string` comparisons are case-sensitive and lexicographic, not comparisons of length or natural-language alphabetical order. C-string pointers follow different rules; see Chapter 8.
- Mixed signed and unsigned comparisons can convert a negative integer to a large unsigned value. Avoid comparing an unchecked signed index with an unsigned size.

# Input Checks and assert

```cpp
int readOrDefault(std::istream& in) {
    int value = 0;
    if (in >> value) {
        return value;
    }
    return -1;
}
```

Test the extraction itself before using the value. A failed stream needs appropriate recovery before further reads; testing an old variable does not validate the latest input.

`assert(condition)` from `<cassert>` aborts when an enabled assertion fails. Defining `NDEBUG` disables the check, so assertions are not a substitute for required input validation. Never put work that must happen, such as `++count`, inside an assertion.

Technical clarification: [C++ working draft — switch rules](https://eel.is/c++draft/stmt.switch).
