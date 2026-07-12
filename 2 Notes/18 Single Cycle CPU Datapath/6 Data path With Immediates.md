This is still just simple data path of ALU operations! But, except with data coming from 2 registers, we have data coming from 1 register and 1 immediate.

As we recall the format of how immediate instructions look like:

| Field     |  Bits | Width | Span          |
| ----------| ----: | ----: | ------------- |
| opcode    |   6:0 |     7 | [x : x+7)     |
| rd        |  11:7 |     5 | [x+7 : x+12)  |
| funct3    | 14:12 |     3 | [x+12 : x+15) |
| rs1       | 19:15 |     5 | [x+15 : x+20) |
| imm[11:0] | 31:20 |    12 | [x+20 : x+32) |

![[Screenshot 2026-07-08 at 11.41.24 AM.png|500]]

So, all that we need to add is the ability to replace the value passed from the 2nd register, as an immediate value that we passed in!

![[Screenshot 2026-07-08 at 11.54.03 AM.png|500]]

But how would we achieve it? Well, it's simple! We would use 1 bit to toggle from a generated immediate value or the 2nd register's value!

![[Screenshot 2026-07-08 at 11.57.25 AM.png|500]]

And we would need an immediate generator to turn the 12 bits in the instruction for the immediate and extend it to 32 bits.

![[Screenshot 2026-07-08 at 11.58.36 AM.png|500]]

Now, there will also be a control here for the immediate generator, as there's different types of immediate we need to extend and generate, integers, longs, floats... who knows? 

As a quick recap of generating I-type immediates:
- Copy the instruction's upper 12 bits (`inst[31:20]`) into the lower 12 bits of the immediate (`imm[11:0]`).
- Use `inst[31]` as the sign bit of the immediate.
- Fill the upper 20 bits (`imm[31:12]`) by replicating `inst[31]` (sign extension).
- The result is a 32-bit signed immediate that can be used directly by the ALU.

![[Screenshot 2026-07-08 at 12.02.29 PM.png|500]]

