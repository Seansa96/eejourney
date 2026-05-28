2024-08-10 14:49

Status: #child

Tags: [[compiler]] [[lexical-analysis]] [[syntax-analysis]] [[code-generation]] [[low-level]] [[language-processing]]
See also: [[Interpreter]]
# Compiler Basic Structure

A compiler is simply a program that translates a source language to a target language.
When compared to an interpreter, it is important to note that because a compiler actually completes the translation ahead of time in the form of the program, and then takes in inputs, it is much faster at mapping those inputs to outputs.  However, a compiler may give more nebulous feedback (although the feedback usually is quite good in modern compilers) than an interpreter, since an interpreter executes the code line-by-line.

Language Processing System -

There are four parts to it. The Preprocessor, Compiler, Assembler, and Linker/Loader

The Preprocessor takes in as input the High-Level Language(HLL) and expands it/modifies it accordingly in order to produce "pure" High-Level Language. It outputs this modified source code to the Compiler.

The Compiler takes in as input the pure source code, modified by the preprocessor, and compiles it into the target assembly language for that machine's CPU architecture. It may also optimize the code as per its initial configuration where it deems necessary.

The Assembler is responsible for converting the Assembly into binary. This is an object file, but it is now prepared to be linked together by the Linker/Loader to be made fully executable.

The Linker/Loader is responsible for converting the Assembly into pure machine code (a binary file) and linking it to the necessary dependencies required for execution of the program, as well as loading it into memory. The memory it occupies may be main memory or registers within the CPU, depending upon the machine the code is executed upon.


Regions of the Compiler -

Front End (Analysis): Machine Independent, Language Dependent. Involves Lexical Analysis, Syntax analysis, Semantic Analysis, and Intermediate Code Generation.  It is machine independent because the architecture of the processor does not matter here, only the language (which is why it is language dependent).  

Back End (Synthesis): Machine Dependent, Language Independent.  Involves Code Optimization and Code Generation.  Here, we generate the target assembly language based on the processor's architecture. 


Design of Compiler Phases:

Lexical Analysis - Involves parsing the HLL input to output tokens, which are

Syntax Analysis - Takes the tokens as input and outputs a Parse Tree.

Semantic Analysis - Takes the Parse Tree as input and outputs an Annotated Parser Tree

Intermediate Code Generation - Takes the APT as input and outputs TAC/Postfix notation

Code Optimization - Takes TAC as input and outputs 2-Address Code

Code Generation - Takes the 2AC as input and outputs Assembly Language

Each phase needs to have error handling. For example, if one tries to execute c = a + b in the C language, the Syntax Analysis will raise an error as the semicolon was omitted. Or, if a is a char where b is an int, and we rectify the semicolon omittance, then the semantic analysis might raise an error.

Each phase will also use a symbol table as reference for the definition of things such as variable names, function names, data types, scope levels, identifiers, and memory address references.  This keeps definitions consistent throughout each phase and also helps to expose other information that can aid in optimization. Aids in managing scope and name resolution/conflicts, tracking variable declaration, relative/absolute memory location, and other useful attributes.




## Reference:

[[Compilers Principles Techniques and Tools (2nd Edition)]]
