Tags: [[linux]] [[sudo]]



# How to Solve

add user to sudo group. can do this with adduser, but may need to enter root to do so.

so, enter root via:

`sudo su root

At this point you'll be asked for the root password, whatever that is. If you never made a password when setting up the OS, it should just be `root.

then, do an `adduser <user-goes-here> sudo

and then you need to **SWITCH BACK TO YOUR USER. DON'T JUST TYPE EXIT OR CLOSE THE TERMINAL.**

Not sure why this is necessary. Maybe the buffer that completes the action disappears with the root shell process.
	`