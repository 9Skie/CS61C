2.6

> [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=206&selection=35,0,42,3&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.206]]
> > Although the first computers operated on full words, it soon became clear that it was useful to operate on fields of bits within a word or even on individual bits. Examining characters within a word, each of which is stored as 8 bits, is one example of such an operation (see Section 2.9). 

1 word = 8 bytes, the book uses registers that store 64 bits.

These guys already existed in C, so it's just a matter of translation between them and RISC-V syntax.

![[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy) 1.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=207&rect=99,538,530,669&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.207]]

And, that weird syntax of `slli` is _shift right logical immediate_, it's just how RISC-V decided to name these bit shifts.

Like shifting right by 4 bits

```
slli x11, x19, 4 // reg x11 = reg x19 << 4 bits
```

Then the rest you've seen, like OR, AND, XOR... just refer to them up in the table


---
2.7

For some weird reason, the class decided now is a good time to talk about branching when clearly it has been used when we were reading from 2.9.

But anyways, branching is how all conditionals and looping is reduced to in assembly.

It's comprised of:

- a comparison
- a conditional branch
- sometimes an unconditional jump

Like this instruction:

```
beq rs1, rs2, L1
```

> [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=211&selection=26,0,42,1&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.211]]
> > This instruction means go to the statement labeled L1 if the value in register rs1 equals the value in register rs2. The mnemonic beq stands for branch if equal.

We can see how this branching is basically a if statement, also, here's an example of how it can be used in a while loop.

```c
while (save[i] == k) 
	i += 1;
```

This is very complicated in assembly! Because we need to load `save[i]` into a register, which requires us to know the address of `save[i]`, which comes from offsetting `save[0]`.

Assume we already have these things in the registers:

-  x22 = i
-  x24 = k
-  x25 = &save[0]

```
Loop:
    slli x10, x22, 3        # x10 = i * 8  (byte offset)
    add  x10, x10, x25      # x10 = address of save[i]
    ld   x9, 0(x10)         # Temp reg x9 = save[i]
    bne  x9, x24, Exit      # if save[i] != k, go to Exit
    addi x22, x22, 1        # i = i + 1
    beq  x0, x0, Loop       # jump back to Loop (always taken)

Exit:
```

Then the branch address table thing is... I'm confused about it, so lets understand it later through the lectures.

---
3.2

Suddenly, we are talking about binary addition.

And we are talking about how overflow can be detected on a computer, with the following operations in addition and subtraction.

![[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy) 2.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=373&rect=103,308,528,425&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.373]]

