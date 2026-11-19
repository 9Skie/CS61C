
## Logical Comparisons

Again we are at RISC-V instructions, logical instructions like `and`, `or` etc.

![[110 Learning/112 CS/112.2 SWE/2 What is a Computer/1 UCB CS61C/3 Notes/9 Logical Instructions 2/attachments/Screenshot 2026-02-13 at 9.22.19 PM.png|500]]

There are 2 variants to them, like:
- `add`: adds the content of 2 registers
- `addi`: adds the content of a register and a constant

And there's no `not` instruction in RISC! Simply because 


## Shifting

Shifting bits is done through commands like `sll` (shift left logical) or `srl` (shift right logical).

![[110 Learning/112 CS/112.2 SWE/2 What is a Computer/1 UCB CS61C/3 Notes/9 Logical Instructions 2/attachments/Pasted image 20260213212940.png|500]]

A logical shift simply inserts 0s at the end where values are being pushed from, while an 
arithmetic shifts inserts copies of the sign bit (MSB).

![[110 Learning/112 CS/112.2 SWE/2 What is a Computer/1 UCB CS61C/3 Notes/9 Logical Instructions 2/attachments/Pasted image 20260213213321.png|500]]

Why have this difference? Well:
- Arithmetic right shift ≈ signed division by 2
- Logical right shift ≈ unsigned division by 2