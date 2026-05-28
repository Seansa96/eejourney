2024-08-12 19:16

Status: #baby

Tags: [[language-processing]] [[low-level]] 
See also: [[Compiler Basic Structure]]
# Interpreter

An interpreter can take the source program and execute it directly without compiling it to machine code. The source code is supplied along with the input to produce the output, as below:

![[Pasted image 20240812191905.png]]

Because the interpreter executes the code directly, line by line, it can usually offer enhanced feedback compared to a compiler.  However, because it is executing this code directly, the interpreter also must translate the source code to machine code while processing the input, so it is naturally slower at producing an output (depending on the program).


## Reference:

[[Compilers Principles Techniques and Tools (2nd Edition)]]