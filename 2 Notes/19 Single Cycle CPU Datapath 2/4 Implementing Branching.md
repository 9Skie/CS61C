If we recall branching, it looks similar to the store instruction's format, just using the 2 source registers for comparison, but uses them for comparison.
``
`beq rs1, rs2, label`
- Read `rs1` and `rs2`.
- If their values are equal, set `PC` to the address of `label` (`PC + offset`).
- Otherwise, continue normally with the next instruction (`PC + 4`).

![[Screenshot 2026-07-13 at 4.10.58 PM.jpg|500]]

To add branching to the data path, we need the ability to change the program counter through a mux of either taking `pc + 4` or `pc + offset`.

We need to compute `pc + offset` and to compare the values of `rs1` and `rs2`, but we only have 1 ALU, so we need to add another piece of hardware, 'branch comp' for the comparison.

![[Screenshot 2026-07-13 at 4.13.32 PM.jpg|500]]

