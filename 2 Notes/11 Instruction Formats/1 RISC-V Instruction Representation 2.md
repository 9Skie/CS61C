ENIAC (Electronic Numerical Integrator and Computer), completed in 1945 at the University of Pennsylvania by J. Presper Eckert and John Mauchly, was built primarily to compute artillery firing tables for the U.S. Army. 

These tables required solving differential equations numerically to predict projectile trajectories under varying conditions.

![[Pasted image 20260224124208.png|500]]

Its programming model worked like this:
- The machine consisted of accumulators, function tables, and arithmetic units.
- To “program” it, operators manually connected cables between units and set switches to configure data paths and control flow.
- The sequence of operations was determined by physical wiring, not by a stored instruction stream in memory.

If you wanted ENIAC to solve a different problem, you would have to literally rewire the physical wires on the computer, flip some switches... and this could take hours or even days.

The crucial limitation was that ENIAC did not store instructions in memory as encoded data. It stored numbers, but the logic of execution lived in hardware interconnections.

So... then came the idea of a 'stored program computer'.

---
## Stored Program Computer

Well, what if  instead of having wires define control flow, we get memory contents defining control flow? 

Instead of physically rewiring components to determine which units talk to which, the stored-program idea fixes the hardware wiring once and for all and lets binary instructions in memory dynamically select which internal data paths and operations are activated at each clock cycle. 

Each instruction is just a bit pattern that the control unit decodes into electrical control signals—choosing ALU operations, register sources, memory access, and even the next instruction address via the program counter—so control flow is no longer embodied in cables but in the sequence of bits fetched from memory.

This idea was formalized in the EDVAC design and later machines like EDSAC and IAS, it made connivence, but it also gave certain responsibility and consequences.

---
## Everything Has a Memory Address?

Since all instructions and data are stored in memory, everything has a memory address, like EVERYTHING! Go open your task manager (windows) or activity monitor (Mac), you'll be able to see that instructions for ALL the apps that you open taking up certain portions of your memory.

## What is the Program?

And, as we remember that as all program instructions are fundamentally in a binary representation, we have the burden of keeping instructions 'backward compatible'.

Once programs are distributed as binary machine code, those binaries are tied to a specific instruction set architecture (ISA). If a future processor interprets those bit patterns differently, the program breaks.

So hardware vendors face a constraint: new CPUs must continue to understand old binary encodings if they want old software to run unchanged. That is backward compatibility at the ISA level.

This is why x86 today still recognizes instruction encodings from the original 8086/8088 era. Modern Intel and AMD CPUs internally translate those instructions into micro-operations, but architecturally they still honor the original binary contract.

---
## Instructions as Numbers

Regardless of how many bits is used for registers and addresses (32 bits for RV32, 64 bits for RV64), RISC-V has fixed length instructions of 32 bits, and assembly string like `add x10, x11, x0` must be converted to a binary format for the hardware to understand.

So, how would we even access addresses or registers? An instruction probably looks like:

```
do something + to somewhere
```

If the `somewhere` is already 32 bits (or 64 bits), what's even left for the instruction at all?

A 32-bit RISC-V instruction is not trying to _contain_ a full address. Instead, we divide instruction words into fields, and each field tells the processor information about the instruction:
- what it's doing
- where is it doing on

And so, we could define difference fields for different instructions, and in RISC-V, instructions are divided into 6 different types:

![[Screenshot 2026-02-24 at 1.20.40 PM.png|500]]

Let’s use a clean R-format example, since that shows fields most clearly.
  
```
add x10, x11, x12
```

Now in RISC-V, R-format instructions are 32 bits divided into fixed fields:

```
[ funct7 | rs2 | rs1 | funct3 | rd | opcode ]
```

Bit widths:
- funct7 = 7 bits
- rs2  = 5 bits
- rs1 = 5 bits
- funct3 = 3 bits
- rd = 5 bits
- opcode  = 7 bits

Now let’s fill them in for this instruction, you don't need to understand the whole thing right now:

- For add:
	- opcode  = 0110011
	- funct3  = 000
	- funct7  = 0000000

- Register numbers:
	- x10 = 10 → 01010
	- x11 = 11 → 01011
	- x12 = 12 → 01100

Now place them into the format:

```
funct7  rs2    rs1    funct3 rd     opcode
0000000 01100  01011  000    01010  0110011
```

That 32-bit number is the machine instruction, and how does the CPU understand it?

When this 32-bit word is fetched from memory:
1. The instruction register holds those 32 bits.
2. The decoder looks at the opcode (last 7 bits).
    - 0110011 tells the control unit: “This is an R-type arithmetic instruction.”
3. The control logic then examines funct3 and funct7.
    - funct3 = 000 and funct7 = 0000000 together specify ADD.
4. The rs1 and rs2 fields tell the register file which registers to read (x11 and x12).
5. The rd field tells the register file where to write the result (x10).

Nothing magical happens. The CPU is built so that certain bit positions are wired into specific decoder logic. The instruction format defines that wiring contract.

So fields solve the representation problem because the 32-bit word is not a “number” in the arithmetic sense — it is a structured control packet. Each slice of bits activates a different part of the datapath.