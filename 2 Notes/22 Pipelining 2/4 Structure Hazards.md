This is uh... very similar to PH reading 4.5 as well, we did already a detailed talk on them there, so this is like a mini recap.

When you pipeline, you encounter problems, as you are running multiple instructions simultaneously.

It's always a situation that prevents starting a new instruction when there is another instruction that is in execution.

Structural hazard happens when two or more instructions in the pipeline compete for the same resources, like both needing to do a reading/writing of memory, or using the ALU.

As we recall, each instruction:
- Can read up to two operands in decode stage
- Can write one value in write back stage

We can avoid structural hazard by having separate “ports”,  two independent read ports and one independent write port, so three accesses per cycle can happen simultaneously.

![[Screenshot 2026-07-27 at 10.53.15 PM.jpg|500]]

