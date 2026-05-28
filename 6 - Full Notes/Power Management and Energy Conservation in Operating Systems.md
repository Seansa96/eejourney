2024-08-10 09:14

Status: #child

Tags: [[operating-systems]] [[power-management]] [[batteries]] [[memory]]

# Power Management and Energy Conservation in Operating Systems

5.8.1 - Batteries

Batteries are either rechargeable or disposable

Disposable typically used for handhelds (A, AAA, D)

Nickel cadmium at first, then Nickel metal hydride. Now Lithium Ion batteries dominate and don't have to fully deplete to be recharged.

NiCd
Nickel(III) oxide-hydroxide (NiOOH) - Positive Electrode
Negative Electrode - Cadmium 
Electrolyte - Potassium Hydroxide (KOH) 

Good in a wide range of temperatures, good life cycle, high density discharge currents, high energy density.  Good for power tools,
photography equipment, emergency lighting. Suffers from memory effect (eventual erosion of battery life due to recharging at partial
capacity).

NiMH

Nickel(III) Oxide-Hydroxide (NiOOH) - Positive Electrode
Hydrogen absorbing alloy - Negative Electrode
Potassium Hydroxide - Electrolyte

Memory effect is less pronounced, higher capacity than NiCd due to hydrogen absorbing alloy, less toxic due to absence of Cd, better energy
density. Does suffer from a higher self-discharge rate.

Good for high-capacity AA and AAA batteries for consumer electronics, hybrid vehicles, and other applications where moderate energy density and environmental concerns are important.

Lithium-Ion

Lithium compound - Positive Electrode
Graphite (or other forms of carbon + silicon) - Negative Electrode
Lithium salt mixed with organic compound - Electrolyte

Highest energy density, little to no memory effect, lower self discharge rate and no use of heavy metals (better for environment).  Is sensitive to high temperatures so not as good in extreme climates and can result in lower lifespan, and requires more complex circuitry.


Approach to battery conservation in a macro sense focuses on states of function, as in being on, off, sleeping, or hibernating.  Sleeping reduces power consumption, hibernating further reduces this consumption in return for a higher energy cost to re-instate active function.
Usually, software handles the flow control between these states. There may be buttons that send signals to the OS, telling it what state to be put into. Some countries require hardware circuitry in place to fully break the circuit.

The highest energy consumers tends to be the display, CPU, and hard disk. The display is far and away the greatest consumer of power.

5.8.2 - OS Issues

As the OS controls all devices, it must make decisions in regards to what states devices may be put into in order to conserve energy.  This requires appropriate algorithms to make the best decision possible based on user preference.

The display requires so much power due to needed backlighting for a sharper image.  At the same time, the display is a good candidate for draining power away from on demand, offering the user intervals in which inactivity can cause the display to power off.  This is because VRAM (video ram) can instantly regenerate the picture to the display.

Hard disks in particular consume far more power than their counterpart, the SSD. This is largely due to the need to rotate the spinning platters and move the read/write head.  This motion, as well as the relatively large power required, also results in a higher temperature, which interacts negatively with Li-Ion batteries, as you might recall, reducing battery life.  It also takes physically longer to complete I/O, meaning that it can take longer to return to a lower power state, compared to the near-instantaneous operations of an SSD.  THis can be alleviated with a larger main memory as well as more sophisticated state signaling between the processes and the disk.  If writing/disk access can be scheduled to specific intervals, then disk restarts can be optimized accordingly, reducing unnecessary starting and stopping of the disk.

The CPU can also be a pain point of power consumption.  There are various methods to improve the efficiency of power usage here. The most popular way is to simply reduce the voltage being supplied to the CPU.  This will linearly reduce the clock cycles by a proportional amount, to the square of the voltage.  This property can be exploited with proper scheduling.  

There is also something to be said for the efficiency of CPU process scheduling in relation to the utilization of multiple cores.  It can happen that, due to the speed of one core performing one task, it might perform so well that it spends much of its time waiting on another core that is computing a task that simply takes longer (such as a network stack communicating with some program reading from a slow HDD).

In this situation, it is not efficient to remain idle and awake, polling the still-busy core while the finished core sits there waiting. In this situation, it is more efficient to simply sleep until it is awakened by some interrupt, but it requires a non-trivial amount of energy to perform this wake action.  In this case, it would be overall better for the core to perform worse, receiving overall less voltage to match the performance of the slower operation, never sleeping and thus fully optimizing power.

5.8.3 - Memory

Saving power with Memory, if you recall, comes from setting the system to various different states.  This is done by flushing the L-caches in the CPU, then switching the CPU off. Main memory thus stores this data, and it can be reloaded from dynamically.  This is sleeping.

Hibernation flushes main memory itself to disk, then shuts off main memory.  Because the cache and main memory are empty, the CPU must be interrupted and told to jump to ROM in order to reload that journaled data. This can put the system in a state of low power consumption while not taking minutes to restart the system.  





## Reference:

[[Modern Operating Systems - Andrew Tanenbaum]]