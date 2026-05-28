Tags: [[low-level]] [[memory]]
See also: [[stack]]

A region of RAM used by a program's runtime for memory allocation. If there is not enough RAM, typically in most modern OS's you'd be able to page out to secondary/external memory.  

This is where the compiler (through an interface with the Operating System) will allocate resources on in order to supply your program with enough volatile memory to complete its operations.  Typically, whether managed or unmanaged (GC vs Manual Memory Management) by the developer, the issuing runtime, after running an allocation call of whatever flavor, is returned a pointer to the virtual address of that memory.

This is the main difference between the heap and the [[stack]]. A program will need a page table of pointers to the various resources used to store the global variables, objects, and dynamic variables used by the program.