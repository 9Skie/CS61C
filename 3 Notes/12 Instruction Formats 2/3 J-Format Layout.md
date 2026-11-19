Remember how in [[110 Learning/112 CS/112.2 SWE/2 What is a Computer/1 UCB CS61C/3 Notes/12 Instruction Formats 2/2 Long Immediates|Long Immediates]], how there was a `jump instruction`? That's what the J-Format layout is for.

If you recall, a jump in RISC-V either jumps to a PC-relative offset (using jal) or jumps to an address computed from a register plus a small immediate offset (using jalr).

The format of a J instruction looks like:

![[110 Learning/112 CS/112.2 SWE/2 What is a Computer/1 UCB CS61C/3 Notes/12 Instruction Formats 2/attachments/Screenshot 2026-02-25 at 10.09.49 AM.png|500]]

- `opcode`: Identifies this as a jal instruction (unconditional jump and link).
- `rd`: Destination register that receives the return address (usually x1 for function calls).
- `immediate`: Signed PC-relative jump offset used to compute the target address.

But, `jalr` doesn't use a J-Format, that's because it needs to have room for a destination register and a source register, so it uses the I-Format instead.

![[110 Learning/112 CS/112.2 SWE/2 What is a Computer/1 UCB CS61C/3 Notes/12 Instruction Formats 2/attachments/Screenshot 2026-02-25 at 10.25.37 AM.png|500]]

If you recall, `jalr` does:
1. write `pc + 4` to the return address `rd`
2. sets `pc` = `rs` + `immediate`