2025-02-15 01:57

Status: #baby

Tags: [[webdev]] [[config]]


# tsconfig.json


This is just a configuration file that contains objects which to inherit from, almost like header files.  Editing the `extends` field allows you to determine what subset of typescript to inherit from. Possible extensions can be located at `astro/tsconfigs`.

Example:

{
	"extends": "astro/tsconfigs/strictest"
}

Can be followed in VScode to see the specific directives inherited.  General config options in a base, starter project are `base`, `strict`, and `strictest`.



## Reference:
