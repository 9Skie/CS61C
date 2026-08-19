Again just PH 4.5 stuff...

A data hazard happens when an instruction needs a value that a previous instruction has not written back yet, like here, does `sw` in the example fetch the old or new value in the register?

![[Screenshot 2026-07-27 at 11.03.43 PM.jpg|500]]

Due to the nature of the high speed of reading & writing to a register being only 100ps, and the clock cycle being 200ps, the order goes as:
1. write back updates value
2. instruction decode reads new value

But this is still not a solution to the nature of data hazards, as shown below, where `sub` and `or` will calculate wrong results due to the write back from add being too late before the execution of sub and or.

![[Screenshot 2026-07-27 at 11.10.43 PM.jpg|500]]


The first solution is stalling, where we just add additional 'empty' instructions between dependent instructions.

![[Screenshot 2026-07-27 at 11.16.26 PM.jpg|500]]

But this reduces performance, and that's not preferred, is there some way to directly grab the value from the pipeline stage and 'move' it to those previous instructions that need it?

Basically, we directly use the result when it's computed, and don't wait for it to be stored inside a register, this requires however, more communication in the datapath.

![[Screenshot 2026-07-27 at 11.18.51 PM.jpg|500]]

![[Screenshot 2026-07-27 at 11.23.33 PM.jpg|500]]