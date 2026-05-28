2024-08-06 11:42

Status: #child 

Tags: [[guide]] [[linux]] [[C_programming]] 



How to set up C development in Linux


1. **Make sure gcc is installed**. This should already be the case on most Linux distros, but you can check if it isn't with a quick 
	`gcc --version` 
2. **Get the dependencies for C development**. build-essential should contain them. You can grab them with this:
    `sudo apt install build-essentials`  Just remember to update your repo before this command.
3. **Then you'll need a build system generator. We'll use cmake for this.**
    `sudo apt install cmake`
4. **Then we'll need to tell cmake where everything is with a CMakeLists.txt file**. Here's what it looks like:
	`cmake_minimum_required(VERSION 3.0)`
	`project()`
	`add_executable()`

The above functions take in arguments as follows (cmake_minimum_required being self-explanatory):
- project() will take in the name of the project and the programming language it is written in. This has no real bearing on the output of your makefiles, it's more of metadata for steps involved in the process itself and for logging. More information can be found in [[cmake]]. 
  Ex: `project(hello_world C)`
- add_executable() takes in the name of the executable that will be output, and the name of the main C file related to the project.
  Ex: `add_executable(hello_world main.c)`
  This of course can be expanded further in a larger project, with directories being defined relative to the cmakelists.txt's location.
- If necessary, you may also include directives such as find_packages() and target_link_libraries. These are used for external libraries not included in the C99 Standard library. You must first find them with find_packages(), then link them with target_link_libraries like so:
	`find_packages(Boost REQUIRED)`
	`target_link_libraries(hello_world Boost::Boost)`
	
5. **Next, we'll make a build directory**. This is not necessary, but it is good practice to do so in the vein of attempting to keep things tidy. Just do:
   `mkdir build`
   and `cd` into it.
6. Now, we'll go ahead and generate all the makefiles and build scripts (as well as other things like caches for optimization on further calls and checking for dependencies). We do this by running `cmake`  in the same directory as the CMakeLists.txt file. By this I mean, the command itself needs to target the CMakeLists.txt file, so this can be run from anywhere, and the output will be ran in the location you invoked the command from.
   Example:
   Project directory hierarchy - root/cmakelists.txt, root/main.c, root/build
   I cd into build and am now at root/build. If I run cmake .., this will successfully invoke cmake to generate the build files, but because I am in root/build, they will be generated there, instead of root/.
6. Now that the makefiles have been generated, you can actually build your program. Just run
   `make` and your target .exe file will be generated (in the directory you run the call from, so in this case it should be the /build directory). Then just run the program like you would anything else (aka ./programname)
   

## References:
https://github.com/Seansa96/Setting-up-VS-Code-for-C/blob/main/CMakeLists.txt