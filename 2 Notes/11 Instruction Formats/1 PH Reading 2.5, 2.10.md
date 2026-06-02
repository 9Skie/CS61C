2.5

> [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=195&selection=6,0,9,62&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.195]]
> > Instructions are kept in the computer as a series of high and low electronic signals and may be represented as numbers. In fact, each piece of an instruction can be considered as an individual number, and placing these numbers side by side forms the instruction. 

Isn't it amazing sometimes what comes out from a computer? All these 0s and 1s making up some the greatest stuff in the world.

But how does assembly translate into those 0s and 1s? Do they serve any special purpose? Well, yes, there are `instruction formats` in RISC-V, take this instruction for example:

```
add x9, x20, x21
```

In binary, it looks something like this:

![[110 Learning/112 CS/112.2 Basics/112.2.3 What is a Computer?/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy) 4.jpg|300]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=196&rect=87,608,508,691&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.196]]

Each of these segments is a _field_:
- the 1st, 4th, 6th field tells the RISC-V CPU it's an addition instruction
- the 2nd field tells you where we are storing the data (at x21)
- the 3rd field is one of the operands where we are getting data from at (x20)
- the 5rd field is one of the operands where we are getting data from at (x21)

More generally, a RISC-V instruction of R-type looks like such.

![[110 Learning/112 CS/112.2 Basics/112.2.3 What is a Computer?/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy) 5.jpg|300]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=198&rect=45,598,551,750&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.198]]

However... you can sort of already see the downside of a instruction type like this, how would you do offsets? You can't, as there's just not enough bits to store informations about offsets, and therefore are forced to turn to another type of instruction.

I-Insructions have a general look like this:

![[110 Learning/112 CS/112.2 Basics/112.2.3 What is a Computer?/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy) 6.jpg|300]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=199&rect=62,534,536,640&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.199]]

And they allow those 12 bits entirely to be used as 'offsets', which means we can have a range of `address +- 2048 bytes` of distance, like this instruction here:

```
ld x9, 64(x22)
```

Here, 22 (for x22) is placed in the rs1 field, 64 is placed in the immediate field, and 9 (for x9) is placed in the rd field.

There's a lot of these instruction types... we'll go over them in the class, but they all only have 4 bytes in length.


2.10

> [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=239&selection=3,0,5,38&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.239]]
> > Although keeping all RISC-V instructions 32 bits long simplifies the hardware, there are times where it would be convenient to have 32bit or larger constants or addresses. 

So, to overcome this problem, RISC-V would break down loading into an 'upper' and 'lower' part.

To load a 32-bit value:
1. Use lui to load the upper 20 bits.
2. Use addi to add the lower 12 bits.

Say, we wanted to load a big value into `x19`

```
lui   x19, upper20
addi  x19, x19, lower12
```

What happens is lui sets `x19 = upper20 << 12`, and then addi adds the lower 12 bits through `x19 = (upper20 << 12) + lower12`.

---
## Branching Close Relatively

Next, we talk about branching instructions in the binary format, and you can only branch to even addresses.

The unconditional jump uses its own special format, the UJ-Format, 7 bit opcode, 5 bit destination, and a 20 bit literal address.

![[110 Learning/112 CS/112.2 Basics/112.2.3 What is a Computer?/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy) 8.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=241&rect=61,366,534,445&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.241]]

But, this raises a problem, a conditional branch in RISC-V does not have enough bits to encode a full memory address — even 20 bits would only allow $2^{20}$ possible byte addresses, which is far too small compared to a 64-bit address space.

However, most branches in real programs do not jump arbitrarily far; they typically go to nearby instructions, such as the beginning of a loop or the end of an if block. Since these targets are usually close to the current instruction, it is more efficient to encode the branch as an **offset** rather than an absolute address.

With PC-relative addressing, the branch instruction stores a signed offset, and the processor computes the target as:

$\text{new PC} = \text{current PC} + \text{offset}$

This allows the program to reside anywhere in memory while keeping branch instructions compact, since they only need to describe how far to jump relative to the current instruction rather than specifying a full 64-bit address.

This philosophy also carries over to other conditional jump comparisons.


## Branching Far Away

Ok, but what if we really have the need to branch far far away, what do we do?

```
beq x10, x0, L1
```

Like right now, beq has a limited branch range (≈ ±4 KB), if L1 is too far away, this instruction cannot reach it.

So we rewrite it as:

```
bne x10, x0, L2
jal x0, L1
L2:
```

Simply, the idea is that we branch to L2 on the inverse conditional of what we had before, which is if x10 != 0 it branches. 

If 10 == 0, we fall through to the next instruction which is an unconditional jump, which can get us pretty far away, $2^{20}$ possible byte addresses away!

Outside of what we've already talked about, there's still other addressing modes.

 > [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=244&selection=50,0,73,37&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.244]]
> > 1. Immediate addressing, where the operand is a constant within the instruction itself. 
> > 2. Register addressing, where the operand is a register. 
> > 3. Base or displacement addressing, where the operand is at the memory location whose address is the sum of a register and a constant in the instruction. 
> > 4. PC-relative addressing, where the branch address is the sum of the PC and a constant in the instruction.


![[110 Learning/112 CS/112.2 Basics/112.2.3 What is a Computer?/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy) 9.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=246&rect=72,481,556,797&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.246]]

Hm... I guess we'll see these along as we go through the class