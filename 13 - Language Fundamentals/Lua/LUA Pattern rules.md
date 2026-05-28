tags: [[lua]] [[lua scripts]][[regex]]

Lua Patterns are not technically regex, as they do not allow for some features, although they serve much of the same purpose.  A pattern is encapsulated within quote characters, like `" "`.

The `^` character can be used to denote the beginning of some sequence, ending with the `$` character. Note that the $ character serves as an anchor, so it assumes that the pattern ends with the most recently filtered part of the expression.

Example: If you are trying to match some letter (such as with (%d+)), then the `$` character will be expecting the pattern to end with a character. This can also serve as a form of validation.

You can do exact matching of a string by simply typing that string.

An exact match for "shark", would be `"shark"`, for example.

What you actually capture, if wanting to return a specific string (and remember, WHAT IS RETURNED IN TERMS OF TYPE IS ENTIRELY DEPENDENT UPON THE FUNCTION YOU USE, NOT THE PATTERN EXPRESSION.)

There are several character classes, which are items in a pattern that can match any character in a specific set.  Each instance of a character class is itself mapped to a single instance of what that class represents.

So, if you have some string `aaron`, and you want to capture the 2nd `a` character, you could do `"a(%a)r"`. 

It is also probably a good time to note that exact matching can also serve as the way to finish the expression as well as begin it.  Informally, this can be referred to as a "separator".

That being said, here is the list of character classes available:

# Character Classes

| Class | Representation                      |
| ----- | ----------------------------------- |
| `.`   | all characters                      |
| `%a`  | letters                             |
| `%c`  | control characters                  |
| `%d`  | digits                              |
| `%l`  | lower case letters                  |
| `%p`  | punctuation characters              |
| `%s`  | space characters                    |
| `%u`  | upper case letters                  |
| `%w`  | alphanumeric characters             |
| `%x`  | hexadecimal digits                  |
| `%z`  | the character with representation 0 |



