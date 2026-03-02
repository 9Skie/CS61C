The format of a store instruction looks like this:

![[Screenshot 2026-02-24 at 4.27.53 PM.png|500]]

- `rs1`: This is the base _address_. It holds a memory address (a pointer).
- `rs2`: This holds the _data_ that will be written into memory.
- `imm[11:0]`: This is a single 12-bit signed offset.
- `funct3` → Specifies the width/type of store
- `opcode` → Identifies this instruction as a store.

If you see the code, don't be confused in that it seems that we have 2 offsets, it is 1 offset split into two parts (imm[11:5] and imm[4:0]) only because of encoding constraints.

And again, we'll give an example of a store instruction:

![[Screenshot 2026-02-24 at 4.32.34 PM.png|500]]