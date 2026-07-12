Lets go! How to actually build hardware that runs RISC-V code!!!

![[Screenshot 2026-07-06 at 3.49.53 PM.png|500]]

One side note, however, as I have personally started to look into parallel computing in [[1 Why Parallelism? Why Efficiency?]] from Stanford CS 144, there is need to acknowledge that at the moment, we are looking at the simplest level of a CPU, just parallelism at the gates level.

![[Screenshot 2026-07-06 at 3.48.49 PM.png|500]]

But now, back to the CPU, there are 2 main parts that make up a CPU:
- Datapath: where data flows and gets operated on (the brawn: registers, ALU, muxes, memory)
- Control: decides what the datapath should do, based on the instruction (the brain: sets the ALU operation, write enables, mux selects)


We already built intuition for the _what_ when we studied instruction formats: what each instruction does, what its fields mean. 

And we just covered the _how_ at the hardware level with combinational circuits. 

Now it's time to combine the two: to see how instructions are physically executed, by building the data path that carries them out and the control that directs it.