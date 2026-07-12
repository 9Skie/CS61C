Designing a CPU is like designing a finite state machine, we know the inputs, we know the outputs, we know the logic of each instruction, but we just don't know what combinational logic makes them up.

We know the CPU contains these things in a state:
- program counter
- other registers
- memory

And at every tick's rising edge, the current state elements would go through the combinational logic, and present it's outputs back to the state elements.

On the next tick's rising edge, we actually do the write back to the new state elements.

![[Screenshot 2026-07-06 at 4.13.00 PM.png|200]]


But... as we know, it's not as simple as a single step, there are phases of this execution, as we know like fetch, decode... etc, this can be divided into 5 stages.
- We didn't really have to explicitly divide them into 5 stages, as we have felt this division when we were looking at logic of instructions before.

![[Screenshot 2026-07-06 at 4.38.17 PM.png|400]]


And from the textbook, we have already built a simplified logical model of this data path (so I won't repeat myself):

![[Screenshot 2026-07-06 at 4.42.28 PM.png|500]]

There's a few things to take note from this image:
- the physical memory we've logically divided into instruction memory & data memory
- the 5 stages happen in 1 clock cycle

As we've already learnt about these combinational circuits, we won't go over them again, we will instead turn towards the state keeping data path elements.

A register is simple, as we know we can either read/write from/to it, in the form of 32 bit inputs/outputs.

![[Screenshot 2026-07-06 at 10.00.05 PM.png|200]]

Then a collection of registers we call a register file, it holds all the registers in our architecture (32 of the), and it has 2 output busses, bus A and bus B, and 1 input bus, bus W, all which are 32 bit.

Register selection uses three 5-bit inputs (5 bits since 2⁵ = 32):
- **RA** → picks the register output on busA
- **RB** → picks the register output on busB
- **RW** → picks the register written from busW, only when Write Enable is 1

![[Screenshot 2026-07-06 at 10.04.29 PM.png|300]]


The other thing is the memory, it works similarly to the register file, we have a clock, a data in bus, a data out bus, and an address to which data goes into/out from.

- Read: address selects the word (32 bits) to put on data out
- Write: set write enable to 1, then address selects the word (32 bits) to be written from data in bus

![[Screenshot 2026-07-06 at 10.09.57 PM.png|300]]


**Each instruction during execution reads and updates the state of**: 
- (1) Registers
- (2) Program counter
- (3) Memory
