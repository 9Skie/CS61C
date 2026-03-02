Uh, I did kinda give an example of an R instruction last time, you've also probably seen something similar in Nand2Tetris.

Here's how the 32 bit R-format instruction is divided into.

![[Screenshot 2026-02-24 at 1.44.22 PM.png|500]]

Now, what do each of these fields mean?
- `opcode`: this let's the CPU know it's a R-instruction (0110011), and control signals will route toward the ALU datapath rather than memory or branch hardware.
- `rd`: destination register, these 5 bits go directly to the write-address input of the register file. After the ALU finishes, the result will be written into this register.
- `rs1`: source register 1. These bits select which register’s value is placed on the first ALU input bus.
- `rs2`: source register 2. These bits select the second ALU input.
- `funct3`: This narrows the operation type. For R-type, funct3 distinguishes between add/sub, shift, set-less-than, AND, OR, XOR, etc. These bits go into the ALU control logic.
- `funct7`: This further distinguishes operations that otherwise look identical. As for example, ADD and SUB share the same opcode and funct3, they differ in funct7.

Let's look at a real example again:

```
add x18, x19, x10
```

This is the R-format of it:

![[Screenshot 2026-02-24 at 1.58.18 PM.png|500]]

Let's break this down step by step:

- The opcode is 0110011, indicating a R-instruction
- rd is 10010, which is 18, which corresponds to x18, the register where we will put the result into
- rs1 is 10011, which is 19, so that's one of the registers which we are taking the data from
- rs2 is 01010, which is 10, again where we will read data from
- func3 and func7 helps identify that this operation is `add`.

Here's a big table of all the (common) R-format instructions.

![[Screenshot 2026-02-24 at 2.18.28 PM.png|500]]
