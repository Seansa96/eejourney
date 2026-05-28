Tags: [[low-level]]

There are two definitions of runtime that get used in the modern literature.  

A runtime, in the first respect, can refer to the period in which your program is running. This is also what a "runtime error" typically refers to, as it is an error that occurs while your program is running, and that may or may not cause it to crash.

The second refers to the platform or underlying program that actually executes the code you have written.  This can be, in the case of compiled code, the operating system itself, various libraries, frameworks, an [[Interpreter]], or some other program built to run that code.

Scripting languages often are made to be executed directly, line-by-line, by some abstraction of the Operating System, which is why they can be much more simply interacted with.

# Further Thoughts

From what I understand now, runtime is mapped to two more distinct and strict definitions that are some variation of "runtime environment" and "runtime library". The first is just defining the scope of a program's current execution step. Like, if an error occurs while you're in the program's runtime environment, then that's a runtime error. 

A program may be said to be performing its task when the runtime environment is active and being used. Whereas a runtime library or runtime platform would be the actual external program, framework, API or what have you that is actually used to execute the source code. The JVM is a runtime library/platform in this sense, or python's VM, or a browser running compiled javascript, or a shell running bash or windows batch or whatever. Although this term feels a bit awkward to use in that sense as it kind of crosses over to the idea of a runtime environment.