Tags: [[low-level]] [[memory]]

The General-Purpose Registers are a set of specialized Registers within the [[CPU]] that handle the vast majority of operations relating to logical and arithmetic operands, address calculation operands, and Memory pointers.

There are 3 main types of GPRs. Some of these can also be referenced by their MSB or LSB, which slightly alters the presentation of their reference, changing it from (Z)X (where Z is the affiliated name of that register), to (Z)H or (Z)L, where 'H' refers to the MSB portion, and 'L' refers to the LSB portion. 32-bit architecture expanded the naming scheme as well, as it introduced new GPRs. Registers within this space attach an "E' (for extra). The 64-bit extension similarly attaches 'R' (for Register...yeah, not sure why that happened).

Thus, in the 32-bit space, the Accumulator Register (AX) becomes EAX. In the 64-bit space, it becomes RAX.

* Data Registers
	1. AX: The Accumulator Register. It is used in arithmetic, logic, and data transfer instructions. 
	2. BX: The Base Register. Used to hold a byte that is a pointer to the start of a memory address, and thus can be used in addition to an offset to calculate the exact memory address of an item.
	3. CX: The Count Register. This is used primarily for holding the bits or bytes specifying the amount of iterations a loop might have, or the amount of bits to shift or rotate in instructions where this is necessary. It can also be used to store data just like any other register, when needed, although this is less necessary in 32 and 64 bit architecture, where extra registers exist for this purpose.
	4. DX: The Data Register. It is used in input/output operations, as well as in tandem with the Accumulator for multiply and divide operations.
* Index Registers
	1. SI: Source Index. This register is used to identify the source of a data transfer stream with a pointer to the address of the start of its address block.  
	2. DI: Destination Index. This register's function is identical to that of the SI, just with the destination address. String operations and their related instructions typically employ this register.