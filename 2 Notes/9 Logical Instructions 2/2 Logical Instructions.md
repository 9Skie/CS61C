
## Logical Comparisons

Again we are at RISC-V instructions, logical instructions like `and`, `or` etc.

![[Screenshot 2026-02-13 at 9.22.19 PM.png|500]]

There are 2 variants to them, like:
- `add`: adds the content of 2 registers
- `addi`: adds the content of a register and a constant

And there's no `not` instruction in RISC! Simply because 


## Shifting

Shifting bits is done through commands like `sll` (shift left logical) or `srl` (shift right logical).

![[Pasted image 20260213212940.png|500]]

A logical shift simply inserts 0s at the end where values are being pushed from, while an 
arithmetic shifts inserts copies of the sign bit (MSB).

![[Pasted image 20260213213321.png|500]]

Why have this difference? Well:
- Arithmetic right shift ≈ signed division by 2
- Logical right shift ≈ unsigned division by 2