If we take a look at a general computer system, we can see:

- processor-memory interface
	- the processor can choose to read/write from/to the memory through addresses
	- all read data from memory go to registers
	- all write data from registers go to memory

- IO interface
	- inputs devices's inputs get mapped to memory
	- outputs devices's output get mapped from memory 

![[Screenshot 2026-02-12 at 3.05.14 PM.png|500]]

Assembly works on registers, small pieces of memory directly inside a chips's hardware, and since they are inside the hardware, there is a fixed number of them in a chip.

By default, as we saw from the book, there are 32 registers, each of 8 bytes in a RISC-V chip by default.
- For some reason, they are teaching the variant which has 4 bytes per register, don't know why

A few facts about the registers:
- The registers have names x0 - x31 respectively
- x0 always holds 0
- each register can be refereed to by name or number
- they don't have data types, the operations applied to the bits stored by them determines what the contents are
- each instruction (1 line of assembly code) can contain at most just 1 instruction.

