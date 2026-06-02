Now, what if 12 bits isn't enough? That's why we are here to talk about long immediates, and RISC-V uses different instruction formats designed specifically for that:
- **U-type** (e.g., lui, auipc) → 20-bit immediate placed in the upper bits of a register.
- **J-type** (jal) → 20-bit PC-relative jump offset (much larger range than branch).

If far is outside the branch range, the assembler cannot encode it directly as a single beq. So it rewrites it into two instructions, invert the condition of the branching, and have an unconditional jump behind it.

![[Screenshot 2026-02-24 at 11.05.23 PM.png|500]]

That's one way, another way is use the U-Format long immediates.

![[Screenshot 2026-02-24 at 11.17.16 PM.png|500]]

- `imm[31:12]`(20 bits): Upper 20 bits of a large immediate value that will be shifted left by 12 before use.
- `rd` (5 bits) → Destination register where the result is written.
- `opcode` (7 bits): Determines whether the instruction is LUI (load upper immediate) or AUIPC (add upper immediate to PC).
- `LUI`: Loads the 20-bit immediate into the upper 20 bits of rd (lower 12 bits become zero).
- `AUIPC`: Adds the shifted 20-bit immediate to the current PC and stores the result in rd.

We'll look at LUI first, as it writes the upper 20 bits of the destination, combined with an `addi` that adds 12 bits, it can essentially create any 32 bit value.

![[Screenshot 2026-02-24 at 11.36.05 PM.png|500]]

As for AUIPC, AUIPC stands for: Add Upper Immediate to PC, So instead of writing just a shifted immediate into rd (like LUI), it adds that shifted immediate to the current program counter.

Why is that useful?

Because most large addresses in real programs are not absolute constants — they are **relative to where the code is loaded**.
