So far, the data path we have looked at do not have the ability to read/write from/to memory.

![[Screenshot 2026-07-13 at 10.23.02 AM.png|500]]

A quick review on how the instruction format for loading data from memory:

![[Screenshot 2026-07-13 at 10.33.17 AM.jpg|500]]

Say for an instruction `lw x14, 8(x2)`, it means to:
1.  Read the base address stored in register `x2`.
2. Add the immediate `8` to it to form the memory address.
3. Read the 4-byte word at that address and store it in `x14`.

Honestly, this part looks very similar to how we gotten instruction memory, as instruction memory address is accessed by program counter + offset value, data memory address is also accessed by some value in a register + some offset value.

![[Screenshot 2026-07-13 at 10.40.42 AM.jpg|500]]

Do notice there is another select signal, indicating we either select from the ALU's output, or from the value we gotten back from the data memory address.

funct3 determines the data type which is being loaded for the load.

![[Screenshot 2026-07-13 at 3.39.10 PM.jpg|500]]

