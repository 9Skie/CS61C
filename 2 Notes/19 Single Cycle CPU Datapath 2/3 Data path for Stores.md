Yep, more functionality!

If we recall what a store function is in RISC-V.... it's the same idea as a store, `sw x14, 8(x2)` means:

1. Read the base address in `x2`.
2. Add `8` to get the memory address.
3. Write the 4-byte word in `x14` to that memory address.

![[Screenshot 2026-07-13 at 3.40.51 PM.jpg]]

But unlike load, the offset immediate is not at index `[11:0]` directly, but separated across the instruction.

If we were to support stores, we need a channel to transfer the value of register 2 to data memory directly, and then a choice bit to select between the ALU's outputs or register 2's outputs.

![[Screenshot 2026-07-13 at 3.48.21 PM.jpg|500]]