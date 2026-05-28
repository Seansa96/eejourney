Tags: [[regex]] 


# Metacharacters

| Metacharacter | Name                      | Meaning                                                            | Example                                  | Matches                                |      |                  |
| ------------- | ------------------------- | ------------------------------------------------------------------ | ---------------------------------------- | -------------------------------------- | ---- | ---------------- |
| `.`           | Dot                       | Matches any character **except newline**                           | `a.c`                                    | `'abc'`, `'a1c'`, not `'ac'`           |      |                  |
| `^`           | Caret (start anchor)      | Anchors pattern to **start** of string                             | `^The`                                   | `'The cat'`, not `'A The cat'`         |      |                  |
| `$`           | Dollar (end anchor)       | Anchors pattern to **end** of string                               | `cat$`                                   | `'black cat'`, not `'cat food'`        |      |                  |
| `*`           | Asterisk (zero or more)   | Matches **0 or more** of the previous element                      | `lo*l`                                   | `'ll'`, `'lol'`, `'lool'`              |      |                  |
| `+`           | Plus (one or more)        | Matches **1 or more** of the previous element                      | `lo+l`                                   | `'lol'`, `'lool'`, not `'ll'`          |      |                  |
| `?`           | Question (zero or one)    | Matches **0 or 1** of the previous element                         | `lo?l`                                   | `'ll'`, `'lol'`, not `'lool'`          |      |                  |
| `{}`          | Curly braces (quantifier) | Matches a **specific number** of repetitions (e.g. `{m}`, `{m,n}`) | `a{2,3}`                                 | `'aa'`, `'aaa'`, not `'a'` or `'aaaa'` |      |                  |
| `[]`          | Square brackets (class)   | Matches **any one character** in the set                           | `[aeiou]`                                | `'a'`, `'e'`, etc.                     |      |                  |
| `\`           | Backslash (escape)        | Escapes a metacharacter or introduces a **special sequence**       | `\.` or `\d`                             | Literal `.` or a digit                 |      |                  |
| `             | `                         | Pipe (alternation)                                                 | Matches **either** left or right pattern | `cat                                   | dog` | `'cat'`, `'dog'` |
| `()`          | Parentheses (grouping)    | Groups patterns, captures match                                    | `(ab)+`                                  | `'ab'`, `'abab'`, etc.                 |      |                  |
| Sequence | Matches                        | Example       | Matches              |
|----------|--------------------------------|---------------|-----------------------|
| `\d`     | Any digit (`0–9`)              | `\d+`         | `'123'`, `'0'`        |
| `\w`     | Word char (`[a-zA-Z0-9_]`)     | `\w+`         | `'abc123'`, `'x_'`    |
| `\s`     | Whitespace (`space`, `\n`, etc)| `\s+`         | `' '`, `'\t'`         |
| `\b`     | Word boundary                  | `\bcat\b`     | `'the cat'` not `'catalog'` |
| `\\`     | Literal backslash              | `'\\\\'`      | `'\'`                 |

# Pattern Rules

**Literal Match**: Done simply by encapsulating the chosen characters in a literal string. This is case sensitive, although usually you can pass `re.IGNORECASE` as an argument if you desire.
	Example: `re.findall("a", "Goat")` prints  a.
A literal match may also use a range of character, such as `a-c`, which would match all characters within that range. This is equivalent to `abc`.

You may also use a **Character Class**. This is simply a set of characters that you wish to match, encapsulated within `[]`.

* **Character Class Example:*** `[abc]`

The main difference between a character class and a string literal is that **metacharacters** are not active within a character class.


You can also match characters not listed within a class by **complementing** the set. This is done with the carat character, `^`.
	**Complement Example:** `[^5]` would match every character *except* for 5. 
		`"".join(re.findall('[^5]', "The number 5 is invisible"`). would print out "The number is invisible".
# Most useful methods