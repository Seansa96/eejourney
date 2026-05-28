2024-08-10 09:06

Status: #child

Tags: [[operating-systems]] [[process-management]] [[concurrency]] [[scheduling]] [[multitasking]]

# Processes

**A process is just an instance of an executing program**, including the current values of the program counter, registers, and variables.  Each core on a CPU can handle one process, at the most simple level, and each thread can handle a separate task within a process, allowing for parallelism of execution, speeding up the completion of a process.

## SMT or Simultaneous Multi-Threading (Known commonly as Hyper-threading) 
is true parallelism, where separate threads are scheduled tasks from individual processes to complete.  Single core CPUs and even multi-core CPUs may use apparent parallelism, which is the appearance of this execution scheme through rapid context-switching through multiple processes at once, allowing even a single core CPU to run multiple programs.  In this scheme, each process has its own virtual CPU, which the real CPU uses as a program counter at the macro level to know where to restart when it arrives back at that process again, the individual vCPUs inserting their program counters into the actual program counter. This is called multi-programming.

It is important to remember that this execution and scheduling is not uniform, and often dependent upon the type of process being run.  Real-time applications, with deadlines sensitive to scheduling, often require advanced algorithms and methods to meet the user's expectations.  It is important that the process does not experience an interrupt while running some critical task when working in tandem with another process, and so these scheduling parameters must be sophisticated enough to prioritize certain tasks above others.

There is also a difference between a program and a process.  A program is the total list of items necessary to execute the process, while the process is, well, the process of its execution.  If we were to use a simple analogy, straight from the book, 
"...the recipe is the program, that is, an algorithm expressed in some suitable notation, the computer scientist is the processor (CPU),
and the cake ingredients are the input data. The process is the activity consisting of our baker reading the recipe, fetching the ingredients, and baking the cake.

Now on the topic of interrupts, what are our options in regards to maintaining the state of our process in the unfortunate case it does experience an interrupt? Since not all processes are equal, this will invariably occur.  In most situations, it is common for the program counter, a pointer holding the address of the next instruction in the program; the stack pointer, which points to the top of the stack loaded into memory at that moment. The stack contains variables, functions and their parameters, return addresses, stack frames, saved register values, temporary data, exception handling information, stack canaries, environment variables, context data, and alignment padding. This, along with the status of currently associated open files, is saved to the Process Control Block (PCB).  This block essentially holds the total context for that process, and keeps it in a segregated data structure to help preserve its spot in its allocated virtual memory space, which is an abstraction of its true contiguous location in its saved location on disk.  The PCB is aided by various subsystems for Memory management, Heap management, File System management, and I/O management in order to restore the process totally when control is returned following an interrupt.

It is also worth noting that though a process may be invoked more than once, this does not mean that it is exactly similar in all respects to its sibling.  Two processes running the same program are still two distinct processes. This means they have their own stack, address space, and all the other relevant singular data structures.

2.1.2 - Process Creation

In simpler Operating Systems, it is possible for all applications necessary for the device's services to complete to be loaded and present when the system comes up. In more complex systems, the OS needs a way to create processes as needs arise. There are four principal ways to accomplish this.  System initialization, Execution of a process-creation system call by a running process, a manual request initiated by the user, and the initiation of a batch job.

Upon system initialization, several background processes are run while a few foreground processes run simultaneously. These foreground processes provide a layer of interaction for the user and the OS, while the background processes accomplish necessary tasks in the background.  These background processes are commonly referred to as daemons.  They range from accomplishing relatively simple tasks: opening sockets to listen for requests over the network, such as incoming e-mail, webserver related requests (such as GET requests to load a website's landing page), service advertisements from network devices, and so on.

Of course, after system initialization, we may need additional processes.  In Windows OS's, this is done with the CreateProcess system call, which takes in the .exe file, CLI arguments, process attributes, security attributes, etc. In Unix-based OS, like Linux, this is typically done through a combination of fork() and exec(). fork() is the ONLY way to create a new process, while exec allows for the substitution of a process. The initial system process, such as init or systemd is forked, beginning the process tree, with child processes being duplicated off of this init structure, inheriting its form but not its address space.  Thus, other calls like that of the exec family (execv, execl, execp) are used to replace the program with a new binary and start its execution to transform the process while retaining this newly abstracted memory space.

Users can of course start their own processes (and this is often a fundamental interaction in OS). The most common way is the classic double-clicking in GUIs or typing a command in a CLI.  The way that newly created processes choose to occupy this space varies with the OS.

Lastly, a batch job initiation, which typically applies to large mainframes owned by an enterprise entity, takes in some input queue and executes this batch at a specified point.  This is based off of the old model of batch jobs from the days when PCs did not exist, and is not applicable to most situations.

In Unix, the reasoning for the separation of process creation into two steps (fork then exec), is to allow the child process to manipulate its file descriptors (standard input, output, error) after the fork but before the exec call so that redirection may occur.




## Reference:

[[Modern Operating Systems - Andrew Tanenbaum]]