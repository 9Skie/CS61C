Remember these guys? Loads in RISC-V is just about loading data from registers to memory, but we don't need new instructions to call them, as they are just simply I-type instructions formatted.

But, they do get their own operand name despite being an I-instruction format.

![[Screenshot 2026-02-24 at 4.06.14 PM.png|500]]

- **opcode (7 bits)** → Identifies this as a load instruction (e.g., 0000011).
- **rd (5 bits)** → Destination register that will receive the loaded value.
- **funct3 (3 bits)** → Specifies load width and type (lb, lh, lw, ld, sign vs zero extend).
- **rs1 (5 bits)** → Base register containing the starting memory address.
- **imm[11:0] (12 bits)** → Signed offset added to rs1 to compute the effective memory address.

The most important part of this is probably `funct3`, which indicates what data type we are loading, as different data types have different lengths.

![[Screenshot 2026-02-24 at 4.14.43 PM.png|500]]