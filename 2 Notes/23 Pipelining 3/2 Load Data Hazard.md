Let's look at a series of instructions:

```
lw   s2, 20(s1)
and  s4, s2, s5
or   s8, s2, s6
add  s9, s4, s2
slt  s1, s6, s7
```

We can instantly see an issue between the first `lw` and the first `and`, as:

-  `lw s2, 20(s1)` loads a word from memory address `s1 + 20` into register `s2`.
- `and s4, s2, s5` computes a bitwise AND between `s2` and `s5`, storing the result in `s4`.


The data from memory is only written back at the end of the 4th cycle of the first load instruction, but the bitwise and needs that data to be used for the ALU, and such, a 1 cycle stall would be unavoidable.

![[Screenshot 2026-08-04 at 9.26.47 PM.jpg|500]]

The instruction immediately after a load is called the **load delay slot**.

If that instruction needs the loaded value, the processor must stall for one cycle. This is equivalent to inserting a `nop`, except an actual `nop` also takes up code space.

To avoid the stall, we can place an unrelated instruction after the load. The unrelated instruction fills the delay slot, giving the load enough time to finish without wasting a cycle.

![[Screenshot 2026-08-04 at 9.29.21 PM.jpg|500]]