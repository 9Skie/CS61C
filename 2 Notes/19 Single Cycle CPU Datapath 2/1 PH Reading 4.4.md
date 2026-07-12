Recalling from 4.1 and 4.3, we made a simplified single-cycle datapath that covers:
- R-type ALU instructions: `add`, `sub`, `and`, `or`, `slt`
- 64-bit memory instructions: `ld`, `sd`
- Equality branch: `beq`

Now, how does the  CPU know which path to use for this particular instruction? The answer is we need a control unit, which reads the instruction’s opcode and outputs a small set of control bits.

Different instructions have different control bits, lets start with the ALU.

---
## ALU Control Bits

According to the rules of RISC-V, these are the associated control bits to our functions.

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 11.jpg|300]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=500&rect=64,335,220,415|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.500]]

> [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=500&selection=91,0,100,5&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.500]]
> > We can generate the 4-bit ALU control input using a small control unit that has as inputs the funct7 and funct3 fields of the instruction and a 2-bit control field, which we call ALUOp. ALUOp indicates whether the operation to be performed should be add (00) for loads and stores, subtract and test if zero (01) for beq, or be determined by the operation encoded in the funct7 and funct3 fields (10).

So, the ALU does not directly figure out every instruction by itself but instead uses a two-step decision.
1. The main control unit looks at the instruction’s opcode and produces `ALUOp`.
2. A smaller “ALU control” unit uses `ALUOp` plus `funct3`/`funct7` to tell the ALU exactly what to do.

| `ALUOp` | Meaning                                           | Example                                      |
| ------- | ------------------------------------------------- | -------------------------------------------- |
| `00`    | ALU must add                                      | `ld`, `sd`: calculate `base + offset`        |
| `01`    | ALU must subtract and test for zero               | `beq`: calculate `x1 - x2`; zero means equal |
| `10`    | Look at `funct3`/`funct7` to choose the operation | R-type `add`, `sub`, `and`, `or`, etc.       |

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 12.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=501&rect=103,398,522,526&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.501]]

We can see a lot of `x`'s in this table because those are `don't care terms`, represented by an X in an input column.

---
## General Control Bits

As we recall, there are 4 simple instruction classes: arithmetic, load, store, and conditional branch, all of which use four different instruction formats.

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 13.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=504&rect=97,541,531,681&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.504]]

RISC-V deliberately puts the important fields in the same bit positions whenever possible:

- `opcode`: always bits `6:0`
- `rs1`: always bits `19:15`
- `rs2`: always bits `24:20` when needed
- `rd`: always bits `11:7` when there is a destination

Using this information, we can add instruction labels to the simple data path to know which bits are routed exactly where to.

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 14.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=506&rect=93,499,541,788&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.506]]

This is what each control bit's on/off mean for the instruction.

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 15.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=507&rect=104,559,527,771&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.507]]

These control signals are set based on the input signals to the control unit, which corresponds to the opcode bits of `[6:0]`.

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 16.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=508&rect=91,430,545,787&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.508]]

So, now you can actually understand the opcode for every type of instruction by inferring what control logic they need! Do they need to branch? Do they need to read or write? And onwards.

It's probably best to see these control bits in action within an instruction to instantly see how they work.

Take the instruction `add x1, x2, x3`:

1. The instruction is fetched, and the PC is incremented.
2. Two registers, x2 and x3, are read from the register file.
	- the main control unit computes the setting of the control lines during this step. 
3. The ALU operates on the data read from the register file, using portions of the opcode to generate the ALU function. 
4. The result from the ALU is written into the destination register (x1) in the register file.

If we recall from the R-instruction format, the opcode + ALUop looks like [001000] and [10] respectively, meaning we only have `reg-write` for the entire data path and `add` for the ALU.

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 17.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=511&rect=81,430,553,795|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.511]]

---
## Why Single Cycles Aren't Used Today

A single-cycle CPU means every instruction must completely finish before the next instruction can begin, and this isn't usually very efficient.

Why? Because the clock cycle must be long enough for the slowest instruction, usually a load `ld`. 
- A load has to fetch the instruction, read a register, calculate an address, access data memory, and write the loaded value into a register.
- Simpler instructions, like `add`, never accesses data memory, for example, but it still waits for a clock period sized for a load.

We'll look at optimizing the data path down the road (basically for the rest of this course), through ideas like pipelining, so we can execute different stages of multiple instructions at once, or cache, so we can access memory less frequently, and thread level parallelism, so we can run multiple independent instructions at the same time.