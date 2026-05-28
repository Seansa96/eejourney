
# Project Functionality

The program should ask the user for their name, then print the user's name as well as the date and time.

# Project Structure

It should have three functions:

* Main: This calls two functions, `print_name` and `print_time`
* print_time
* print_name

The other two functions that are not main should also be in their own source file, and you will need to include a header for each file. The project will also use a precompiled header. 

In total, three headers and four source files will be used.

# Creating a precompiled header

The C++ Standard Library will be used to handle input and output via streams, meaning the `<iostream>` header will be used. It will also use strings, so the `<strings>` header will be needed. Lastly, it needs the C runtime date and time functions in `<ctime>`.

To do so, you'll need a C++ header file with:

```
#include <iostream>
#include <string>
#include <ctime>
```

