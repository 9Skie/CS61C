B stands for branching in the format, if you recall:

```
beq, x1, x2, Label
```

In this case, if the value stored in x1 is equal to x2, then we jump to Label, or else we just keep going to the next instruction as normal.

But... how do you know where the label is? The label is some 32 (or 64 bit) address, and there's no way that's being stored fully in the instruction, so what does the instruction store instead?

It stores a relative 'offset' from the current instruction, `beq`. 

The idea is when the assembler sees this line, it knows the address of this `beq` and the address of `loop`, and therefore can compute the `offset`, the distance between `beq` and `loop`, and store that as the Label.

```
offset = address(loop) − address(beq)
```

That offset is a signed number, typically small, because branches are usually nearby. That signed offset is what gets encoded into the 12-bit immediate field of the branch instruction.

You can simply understand it as a signed displacement relative to the current PC, with the possible range of ($-2^{11}$ to $+2^{11}$ bytes).

And then the logic is simple:

![[Screenshot 2026-02-24 at 10.14.47 PM.png|500]]

However... we are going to complicate things a bit, RISC-V does **not** treat that number as a byte offset, so that multiply by 4 is wrong up there, it treats it as a halfword offset, so multiply by 2 instead.

Why?

Because RISC-V supports 16-bit compressed instructions. That means instruction addresses are guaranteed to be aligned to **2 bytes**, not necessarily 4 bytes, so the reach branch up there should be:

```
PC = PC + immediate * 2
```

This is achieved by bit shifting the immediate value right by 1 byte, as that is equilvant to dividing 2.


---

Now, with all that explanation, we can finally go look at the B-Format for Branches. It looks a bit scary with that `imm[]` everywhere.

![[Screenshot 2026-02-24 at 10.30.35 PM.png|500]]

It's actually very similarly structured to a S-Function. For **B-type (branch) instructions**:

- `opcode` (7 bits) - Identifies this as a branch instruction (1100011).
- `funct3` (3 bits) - Specifies branch type (beq, bne, blt, bge, etc.).
- `rs1` (5 bits) → First register to compare.
- `rs2` (5 bits) → Second register to compare.
- `immediate` (split across fields) - Signed PC-relative offset used to compute branch target

---

Example:

![[Screenshot 2026-02-24 at 10.42.31 PM.png|500]]

In this case, as the offset is 16 bytes, the immediate should be 8 (000000001000).

But what if sometimes these immediate offset values need to be extra large? Well, that's for the next note.