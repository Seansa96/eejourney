2025-04-29 18:58

Status: #child 

Tags: [[programming concept]] [[scheduling]]

# basics of a polling function


Polling is an important concept in regards to scheduling and event-driven programming.  It refers to the simple concept of alternating periods of actively listening for an action, then waiting until that action occurs again, or otherwise some scheduling logic wakes the listener for a direct read of the stream they are monitoring.

In general, the simple implementation can be thought of as such, in the case of a polling function dictated by time and blocking.

```
deadline = 3 seconds //this is so that upon first running the system, a poll is conducted straight away

current time = 3 seconds

function poller()

	current time = method to obtain the current time
	if deadline < current time then
		print("Polling...")
		deadline = get new current time and add interval to it, say 1 second
	end
	else
		print("Not ready yet...")
		sleep(2 seconds)
	end
	return true
end

loop(poller())

the first iteration it will poll immediately, then block on the next frame for 2 seconds and repeat.

```

The basic idea here is to define the original schedule and current time variables outside of the polling function.  Then, when you enter it, have the system do a refresh to see what the system time is, and compare that to the deadline that was set.  If the deadline has been passed, then we'll run the associated logic and schedule the next event. If it hasn't passed, then we'll block for an arbitrary interval, exit the function, and poll again.

There's literal hundreds of ways to optimize and improve this, but this is the basic idea.  You can obviously do things like encapsulation, event-driven polling, abstract away the scheduling to a separate interface, so on and so forth--it really just depends on what your aim is.
## Reference:
