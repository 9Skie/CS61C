The idea is very simple to R-Format instructions, the only difference between them is instead of two source registers, you have **one register plus an immediate constant**.

And, as a result, it's format looks really similar to R-format instructions, we simply discard rs2 (as we aren't loading another register anymore) and funct7, so we can put a larger constant in the instruction.

R instruction:
![[Screenshot 2026-02-24 at 2.43.25 PM.png|500]]

I-Instruction:
![[Screenshot 2026-02-24 at 2.46.14 PM.png|500]]
- imm: The immediate constant. This is the critical difference from R-type, and being 12 bits long, it can be a value in a range of (-2048, 2048)

And so, it's instruction is pretty intuitive to understand as it doesn't differ much from R-instructions.

![[Screenshot 2026-02-24 at 2.51.00 PM.png|500]]