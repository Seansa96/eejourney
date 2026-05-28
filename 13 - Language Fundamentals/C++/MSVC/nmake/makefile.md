A makefile is the file that actually tells the compiler how to structure a project and defines build targets.

Typically ran with the make (GNU) or nmake (windows). 

The core idea is around targets and dependencies. Each one of these is defined in a **rule.**

```
target : dependencies
	command
```

# Example of a simple rule

```
main.obj: main.cpp utils.h
	cl /c main.cpp
```

This basically means "create main.obj, it depends on main.cpp and utils.h. Then, run this command to build it."

With several of these in a file, now it is possible for the make utility to look and check the timestamps of each file, and then only recompile a file if it has actually been changed. Without this, you would need to recompile each file individually every time you make a single change to one file.

# Linking

A simple linking rule would be something like:

```
time_test.exe: main.obj name.h time.h utils.obj
	link /out:$@ $^
```
`$**` is also fine and what the textbook says, but apparently the one used above is more modern.

# Cleaning

It is good practice to provide a way to remove all of the files created by the compile process and leave the project clean, with only the source files.

You do this with the `clean` pseudo-target. Because it's not a real target, no file is actually made and thus there are no dependencies, only commands. Make certain it is formatted as such. If you include anything on the same line as the pseudo target, clean, it will be interpreted as a dependency. Commands must be suitable to the scripting environment you are using.

```
clean : 
	@echo Cleaning the project...
	del main.obj time.obj name.obj utils.obj utils.pch
	del time_test.exe
```

The `@` symbol just means to run quietly, and then the other two commands are self-explanatory. You can then run this with `nmake clean`.
