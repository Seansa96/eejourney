2024-08-06 14:54

Status: #adult

Tags: [[C_programming]] [[functions]] [[stdio.h]]

# snprintf

This function is used to format and write a string to a buffer, requiring a specified max length.  This is good for creating safely formatted strings to avoid buffer overflows.

`int snprintf(char *str, size_t size, const char *format, ...)`

First, it's of type int, so it will return a value describing the size of the characters written to the target buffer if the buffer was large enough. Even if the string is truncated due to buffer constraints, it will return the amount of characters that you wanted to write.

Example: I want to write 30 characters to the buffer, and it's of size 31 (we have to account for the null-terminator as well in terms of the space needed, but the null terminator is excluded from the return value calculation). snprintf will return 30 characters.

Example 2: I want to write 30 characters to the buffer, but the buffer is only 25 characters long. My string will be truncated and snprintf will return 30. 

The first parameter is a pointer to the location (aka buffer) that the string will be written to. Subject to pointer arithmetic so you could do some clever things with that.  Be cognizant of the buffer's size.

Next is the maximum number of bytes that is allowed to be written to the buffer. If the string exceeds whatever length is defined here in `size_t size`, then it will be truncated and terminated with the null-terminator.

Then, `const char *format`. This is a format string used to indicate the type essentially of the following arguments. This is similar to how printf works, where you may declare a format specifier like `%d` followed by the name of an int, like in printf("%d", number), and of course you may include as many arguments as you like and thus as many format specifiers as you need.
## Reference:

C99 Standard Library, <stdio.h>