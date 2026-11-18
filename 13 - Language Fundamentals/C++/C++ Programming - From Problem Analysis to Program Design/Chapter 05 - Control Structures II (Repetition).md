# Chapter 5 - Control Structures II (Repetition)

*C++ Programming: From Problem Analysis to Program Design* - D. S. Malik, 8th edition. Implementation notes using the book's C++11-era baseline.

# Choosing a Loop

| Loop | Condition checked | Minimum number of executions |
|---|---|---|
| `while` | Before the body | 0 |
| `for` | Before the body | 0 |
| `do ... while` | After the body | 1 |

Use `for` when initialization, a condition, and a regular update belong together. Use `while` when repetition is driven by input or another condition. Use `do ... while` only when the body should run at least once.

# while: Initialization, Test, Progress

```cpp
int sumFirst(int count) {
    int total = 0;
    int i = 0;
    while (i < count) {
        total += i;
        ++i;
    }
    return total;
}
```

Initialize the control state before testing it, and ensure each continuing path makes progress toward termination. A missing update, reversed condition, or update skipped by a branch can create an infinite loop.

The chapter's common control patterns are:

- **Counter-controlled:** stop after a known number of iterations.
- **Sentinel-controlled:** stop when a special data value appears; do not process the sentinel as ordinary data.
- **Flag-controlled:** stop when a boolean state changes, such as finding the requested item.
- **Input/EOF-controlled:** continue while the required extraction succeeds.

# for: The Order Matters

```cpp
int sumEvenBelow(int limit) {
    int total = 0;
    for (int i = 0; i < limit; ++i) {
        if (i % 2 != 0)
            continue;
        total += i;
    }
    return total;
}
```

The order is **initialize once → test → body → update → test again**. If the first test is false, the body never executes. A variable declared in the initializer, such as `i`, is scoped to the loop rather than available afterward.

`continue` skips the rest of this body but still executes the `for` update. `break` skips the update and leaves the loop immediately.

The initializer, condition, or update may be omitted, but the two semicolons remain. An omitted condition behaves as true: `for (;;) { ... }` requires some other exit if it should terminate.

# do ... while

```cpp
int decimalDigits(unsigned int value) {
    int digits = 0;
    do {
        ++digits;
        value /= 10;
    } while (value != 0);
    return digits;
}
```

The first execution counts the digit in 0 correctly. The trailing semicolon after `while (...)` is required. This differs from an accidental semicolon after the header of a `while` or `for`, which creates an empty body.

# Input and Sentinels

**TEST THE READ, NOT WHETHER EOF HAS ALREADY BEEN REPORTED.** A stream usually discovers the end only when a read attempts to reach it. `while (!in.eof())` can therefore enter the body when no new value was obtained.

```cpp
int sumUntilSentinel(std::istream& in) {
    int total = 0;
    int value = 0;
    while (in >> value && value != -1) {
        total += value;
    }
    return total;
}
```

The extraction happens first; only a successful read is tested against the sentinel. `-1` must be outside the ordinary data domain for this design. It is consumed but not added.

For records with several fields, test the complete read: `while (in >> id >> amount)`. Do not process a partially read record as complete. Input failure may mean malformed data or an I/O error, not just EOF.

To recover from a malformed line, clear the failure state and discard the unwanted characters before trying again. Clearing alone leaves the bad input waiting:

```cpp
void discardBadLine(std::istream& in) {
    in.clear();
    in.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}
```

Include `<limits>`. Use recovery only when retrying makes sense; stop at EOF rather than repeatedly clearing it in an endless retry loop.

# break, continue, and Nested Loops

`break` exits the innermost enclosing loop or switch. It does not exit every nested loop or return from the function. A `break` inside a switch nested in a loop exits the switch.

`continue` targets the innermost loop, even if it appears inside a switch within that loop:

- In `for`, it proceeds to the update, then the condition.
- In `while`, it proceeds directly to the condition.
- In `do ... while`, it proceeds to the condition at the bottom.

A manual counter update at the bottom of a `while` can therefore be skipped by `continue`. Nested counter loops need independent counters, and the inner counter must be reset for each outer iteration.

# Boundary and Lifetime Pitfalls

- For `n` items indexed from 0, use `i < n`; `i <= n` attempts one extra item.
- Initialize sums to 0 and products to 1. For a maximum/minimum, use the first actual value only after confirming one exists.
- Check for zero processed items before dividing to calculate an average.
- Avoid floating-point counters when an exact iteration count matters; repeated additions can round.
- An unsigned counter cannot become negative. `i >= 0` does not terminate a descending unsigned loop, and `size - 1` wraps when size is zero.
- Arithmetic must stay within the type's range. Signed overflow is undefined behavior; a counter overflowing is not a valid termination mechanism. The integer-sum examples here assume totals fit in `int`.

For reverse traversal of an unsigned size, decrement only after checking it is nonzero:

```cpp
for (std::size_t i = text.size(); i != 0;) {
    --i;
    std::cout << text[i];
}
```

Braces determine the body, not indentation. `while (condition);` and `for (...);` repeatedly execute an empty statement unless that is deliberately the design.

When debugging, trace the initial state, first iteration, last intended iteration, and first rejected iteration. Test empty input, one item, the sentinel immediately, and malformed input.
