# Chapter 8 - Arrays and Strings

*C++ Programming: From Problem Analysis to Program Design* - D. S. Malik, 8th edition. Focus: built-in arrays and C-strings, using the book's C++11-era baseline.

# Arrays

An array is a collection of a fixed number of components, also called elements. All elements have the same type and occupy contiguous memory. A one-dimensional array arranges them in list form.

```cpp
const int SIZE = 4;
int values[SIZE] = {8, 3, 6, 1};
```

The general declaration is `dataType arrayName[size];`. The bound must be a positive compile-time integer constant expression. An ordinary runtime variable is not a valid bound in standard C++, even if a compiler accepts variable-length arrays as an extension.

```cpp
int inferred[] = {8, 3, 6}; // size inferred as 3
int zeros[4] = {};          // all four integers are 0
int partial[4] = {8, 3};    // remaining integers are 0
int uninitialized[4];       // local integers have no initialized values
```

You may omit the bound when an initializer determines it, but not simply write `int values[];` as a standalone local definition. You cannot supply too many initializers or leave an empty slot such as `{8, , 6}`. For numeric elements, unspecified trailing values in a brace initializer become zero.

An array's bound stays fixed for that object's lifetime. Reassignment cannot resize it. This does not mean a local array exists for the entire program; an ordinary local array ends when its scope ends. For a runtime-sized collection, `std::vector` is usually simpler than managing a dynamic array manually.

# Accessing Array Components

Use `arrayName[index]`. The `[]` operator is the **array subscripting operator**. Indices begin at 0, so a four-element array has valid indices `0` through `3`.

```cpp
values[0] = 12;
values[2] = values[0] + values[1];
```

An element supports the operations of its own type. Integer elements support arithmetic and comparisons; a `std::string` element supports string operations.

**THE ARRAY BOUND IS NOT A VALID ELEMENT INDEX.** Accessing `values[4]` or `values[-1]` is undefined behavior. Built-in subscripting does not check bounds, and an error need not produce a crash or warning. Do not read uninitialized numeric elements either.

```cpp
for (int i = 0; i < SIZE; ++i) // < SIZE, not <= SIZE
    std::cout << values[i] << ' ';
```

# Processing One-Dimensional Arrays

The operations on one element do not automatically become operations on the entire array.

| Operation | Built-in array behavior |
|---|---|
| `a = b` | Invalid: no whole-array assignment |
| `int a[4] = b;` | Invalid: cannot initialize this way from another array |
| `a + b`, `a * 2` | No element-wise arithmetic |
| `a == b`, `a < b` | Do not compare contents; ordinary expressions use pointer comparisons |
| `std::cin >> a` for an integer array | Invalid; read elements individually |
| `std::cout << a` for an integer array | Outputs an address, not the elements |

Copy, compare, and process the contents one element at a time or use an appropriate library algorithm. Define what a comparison means: equal contents, equal sums, lexicographic ordering, and so on are different questions.

```cpp
int copy[SIZE] = {};
bool same = true;
for (int i = 0; i < SIZE; ++i) {
    copy[i] = values[i];
    if (copy[i] != values[i])
        same = false;
}
```

For minimum/maximum searches, do not start from element 0 unless the occupied portion is nonempty. Track **capacity** separately from the number of elements containing useful data: `0 <= used <= capacity`.

## Array Names, Addresses, and Arithmetic

In most expressions, an array converts to a pointer to its first element. This is why printing its name or comparing two names does not process its values. The array object itself is not a pointer variable.

```cpp
int* p = values;      // points to values[0]
int second = *(p+1);  // same element as values[1]
// values = p;        // invalid: cannot rebind an array
```

Adding an integer to a pointer moves by that many **elements**, not bytes. Pointer addition/subtraction is not array arithmetic. Pointer subtraction requires positions within the same array, including its one-past position. Do not use ordering comparisons between unrelated arrays to order their contents.

You may form `values + SIZE`, the one-past pointer, for an end marker, but must not dereference it. Do not form pointers farther outside the array.

Where `values` is still an actual array, `sizeof(values)` is its total size in bytes and `sizeof(values) / sizeof(values[0])` gives its element count. That formula does not recover an array length from a pointer.

## Range-Based Loops

```cpp
for (auto item : values)    // item is a copy
    std::cout << item << ' ';

for (auto& item : values)   // item refers to the actual element
    item = 0;
```

Use `const auto&` when reading larger elements without copying them. A range-based loop traverses the whole array, not just its occupied prefix.

# Arrays and Functions

```cpp
int sum(const int list[], int used) {
    int total = 0;
    for (int i = 0; i < used; ++i)
        total += list[i];
    return total;
}

void clear(int list[], int used) {
    for (int i = 0; i < used; ++i)
        list[i] = 0;
}
```

Call these with the array name and its valid element count: `clear(values, SIZE);`.

The book calls this “passing by reference,” meaning that changes reach the caller's elements. More precisely, a parameter declared `int list[]` is adjusted to `int* list`: the pointer is passed by value, and the elements are not copied.

- `int list[100]` in a parameter list does **not** enforce a length of 100.
- Pass the count separately and ensure it does not exceed the actual array's capacity.
- `const int list[]` prevents modification of the integers through that parameter.
- `sizeof(list)` inside these functions measures a pointer. A range-based loop cannot infer the range from this pointer alone.
- Passing `values[i]` to an `int` parameter passes one integer by value, not the whole array.

A real array-reference parameter preserves the bound:

```cpp
void clearExactlyFour(int (&list)[4]) {
    for (int& item : list)
        item = 0;
}
```

Functions cannot return a built-in array **by value**. Return a struct containing the array, use `std::array`/`std::vector`, or let the caller provide output storage. Returning a pointer to an ordinary local array is invalid to use after return because the array has been destroyed.

# C-Strings: Character Arrays

A `char` array becomes a **C-string** when a `\0` character terminates the text. A character array is not automatically a valid C-string.

```cpp
char word[] = "code";          // 5 elements, including '\0'
char buffer[12] = "code";      // capacity 12; text length 4
char letters[4] = {'c','o','d','e'}; // not null-terminated
```

**RESERVE ONE EXTRA CHARACTER FOR THE TERMINATOR.** A buffer of capacity 12 holds at most 11 text characters as a C-string. `'A'` is one character; `"A"` is an array containing `'A'` and `'\0'`. The first null terminates the text even if more characters follow in the buffer.

Include `<cstring>` for these operations:

| Function | Critical behavior |
|---|---|
| `std::strlen(s)` | Counts characters before `\0`, excluding the terminator |
| `std::strcpy(dest, src)` | Copies through the terminator; destination must have enough space |
| `std::strncpy(dest, src, n)` | Copies at most `n` source characters; may leave the result unterminated |
| `std::strcmp(a, b)` | Negative / zero / positive for lexicographic less / equal / greater |
| `std::strncmp(a, b, n)` | Compares at most `n` characters, stopping earlier at a null |

`buffer = "new";` is invalid after declaration. `std::strcpy(buffer, "new");` works here because the destination is large enough. C-string copy functions require nonoverlapping source and destination regions. Do not assume they allocate more space or check the capacity. For `strncpy`, `n` must fit the destination; shorter strings are padded with nulls up to `n`, while truncated strings need explicit termination.

Use `std::strcmp(a, b) == 0` to test equal C-string contents. `a == b` compares pointers instead, and `strcmp` is not required to return exactly `-1` or `1` for unequal strings.

## Input and Output

`std::cout << buffer` prints characters up to `\0`. It does not print the buffer's capacity. Using a nonterminated array as a C-string can cause reads beyond its bounds.

```cpp
// C++11-compatible token input: <iostream>, <iomanip>
std::cin >> std::setw(12) >> buffer; // at most 11 characters
```

Token extraction skips leading whitespace and stops at the next whitespace. `std::setw` applies to the next extraction; reapply it for each buffer read. A longer token can leave characters pending in the stream.

`std::cin.get(buffer, 12)` reads up to 11 characters, includes spaces, and leaves the newline pending. `std::cin.getline(buffer, 12)` consumes the newline when it reaches it; an overlong line can set the stream's failure state. After numeric `>>`, handle the pending newline before reading a full line. An uncleared failure state prevents subsequent input from proceeding normally.

`std::string` is a different type: it supports assignment, content comparisons, and resizing. `std::getline(std::cin, text)` reads a line into a `std::string` without managing a fixed character buffer yourself.

# Two- and Multidimensional Arrays

```cpp
int grid[2][3] = {{1, 2, 3}, {4, 5, 6}};
grid[1][2] = 9; // second row, third column
```

Each dimension has its own bound. Storage is **row-major**: one complete row comes before the next. `grid` is an array of two rows, each row being an array of three integers. A row's `grid[r][3]` is out of bounds even if another row follows in memory.

With initializers, the first bound may be inferred: `int grid[][3] = {{1,2,3}, {4,5,6}};`. The later bounds still determine each row's shape.

```cpp
int sumRows(const int grid[][3], int rows) {
    int total = 0;
    for (int r = 0; r < rows; ++r)
        for (int c = 0; c < 3; ++c)
            total += grid[r][c];
    return total;
}
```

In this parameter form, omit only the first bound; the column count must match the argument. For higher dimensions, all bounds after the first are needed. The adjusted parameter is a pointer to a row, not `int**`; a rectangular built-in array and an array of pointers have different layouts.

Parallel arrays associate data by matching indices. If you reorder one, reorder the others identically or their records no longer correspond. An array of structs can keep each record together instead.

For a fixed-size collection that needs whole-object copying and content comparison, `std::array` is a separate library type that supports those operations. These restrictions concern **built-in arrays**.

Technical clarifications checked against the C++ working draft: [array declarations](https://eel.is/c++draft/dcl.array) and [array parameter adjustment](https://eel.is/c++draft/dcl.fct#5).
