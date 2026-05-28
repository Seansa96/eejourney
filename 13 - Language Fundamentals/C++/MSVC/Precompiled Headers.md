In large builds, it's common to have large header files. A way to speed up builds and testing is to build the headers once, save their state, and reuse that for future builds. This is known as precompiling.

You can do this with the following command:

```
cl /EHsc /c utils.cpp /Ycutils.h
```

`cl` is the command-line driver for MSVC.

The option `/EHSC` specifies the exception handling, and this is the most common variety. It tells the compiler to generate proper stack unwinding code for standard C++ exceptions (*needs elaboration)*.

The option `c` just means don't link, only compile, which is ideal for reducing overhead.

And `/Yc` is where it's actually precompiled.

Typically, the main build target (like, for the main.obj) line of the makefile will include `/Yu` which means to use the precompiled header, like so:

```
main.obj : main.cpp name.h time.h utils.pch
	cl /EHsc /c main.cpp /Yuutils.h
```
