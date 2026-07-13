U-type instructions contain a 20-bit immediate and a destination register, with no source registers. The immediate becomes the upper 20 bits of the result; the lower 12 bits are zero.

It's used for 2 instructions:
- lui – Load Upper Immediate
- auipc – Add Upper Immediate to PC

Similar to JAL, the immediate generator must recognize the U-type instruction format and rearrange/sign-extend its immediate bits correctly.

![[Screenshot 2026-07-13 at 5.17.08 PM.jpg|500]]