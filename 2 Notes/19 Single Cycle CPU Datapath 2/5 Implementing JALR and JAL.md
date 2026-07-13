## JALR

crying, wailing, hating, (yes, there are most instruction types than what I'd expect).

anyways, JALR are the jump instructions, which `jalr rd, offset(rs1)` means:
- compute the target address `rs1 + offset`.
- save the address of the next instruction (`PC + 4`) into `rd`.
- Set `PC` to the target address (with its lowest bit cleared).

These only change the program counter and update a register, which... our existing data path is all able to handle! Except writing this address of the next instruction (`PC + 4`) into `rd`.

![[Screenshot 2026-07-13 at 4.37.07 PM.jpg|500]]

---
## JAL

`jal` differs from `jalr` as it does not read a target address from a register. Instead, it jumps to a PC-relative target encoded as an immediate.

`jal rd, label`
- The assembler converts `label` into a PC-relative offset.
- The CPU writes the return address, `PC + 4`, into `rd`.
- The CPU sets `PC` to `PC + offset`.

The immediate generator must recognize the J-type instruction format and rearrange/sign-extend its immediate bits correctly.

![[Screenshot 2026-07-13 at 5.10.53 PM.jpg|500]]

