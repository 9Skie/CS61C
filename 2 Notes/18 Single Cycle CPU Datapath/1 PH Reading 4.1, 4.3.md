## 4.1 Introduction

> [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=476&selection=77,31,85,2&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.476]] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=477&selection=0,0,10,44&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.477]]
> >
> >  For every instruction, the first two steps are identical:
> >  ...
> > 	1. Send the program counter (PC) to the memory that contains the code and fetch the instruction from that memory. 
> > 	2. Read one or two registers, using fields of the instruction to select the registers to read. For the ld instruction, we need to read only one register, but most other instructions require reading two registers. 
> >  ...
> > After these two steps, the actions required to complete the instruction depend on the instruction class.

So now, we are actually thinking about how to implement a physical CPU that can take in some RISC-V instructions (not everything, just some things).

Lets take review of the simple ALU instructions in how it would physically work:

- **ALU**: Address calculation (memory-reference), operation execution (arithmetic-logical), or equality test (branch).
- **Memory access**: Read data for a load, or write data for a store.
- **Register write-back**: Write the ALU result or loaded data into a register.
- **PC update**: Branch to a new address if the comparison succeeds; otherwise PC + 4.

Down here, they make an abstraction of the flow of data through the simplified ALU only processor.

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 2.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=478&rect=95,538,536,774&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.478]]

Biggggg chart, but if we break it down, it's not a lot:

- We start at the program counter, we go to this address, and find the corresponding instruction there, and we fetch it.
- The register operands used by an instruction are specified by fields of that instruction, like which register are we loading data from, what instruction are we performing at the ALU etc.
- Now, the result from the ALU could be an arithmetic result (just for arithmetic, like adding numbers), branching (checking if branching is gonna happen), or a memory result (going to a memory address for some reason)
- Then accordingly 'things' happen! The ALU's output could be a memory address, which means load reads there, store writes there, or it could be data written back to a register, or a branch condition.

But like... we didn't really show 'how' this decision is made, we have just said 'its possible to have these different instructions to be executed', well, a Multiplexer can do the routing for us on which exact instruction variant gets executed.

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 3.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=480&rect=90,445,539,780&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.480]]

Chill out! We just added some control lines & Mux switches, lets first look at the Muxes.

The top mux (when given the control bit of `branch` from all control bits) controls what value goes into the PC, is it a branch or just the next line?

The middle mux controls whether the output from the ALU or  the value at the address that the ALU has computed that goes for writing into the register file.

The lowest mux determines whether the second input is either from a register or an immediate value.

> [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=480&selection=19,35,24,36&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.480]]
> > The added control lines are straightforward and determine the operation performed at the ALU, whether the data memory should read or write, and whether the registers should perform a write operation. The control lines are shown in color to make them easier to see.

---
## 4.3 Building a Datapath

While the above demonstrated an example of a simple ALU-operation-ready CPU, how would we get here?

We start at a program counter, to which we use this program counter's address to get an instruction, and then the program counter is incremented by 4 bytes (the length of a RISC V instruction) by default.

So we need:
- a program counter
- instruction addresses -> instructions
- addition

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 4.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=488&rect=89,547,534,685&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.488]]

And they combine this way in the logic that we just described above, this is universal to any instruction:

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 5.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=489&rect=85,354,540,789&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.489]]


Now, consider the R-format instructions, which:
- reads 2 registers
- performs an ALU operation
- writes the result to a register (maybe)

So now, we need the given R-format instruction to determine which register is read by register number, it needs to output written register data from those registers, we need to determine which ALU operation needs to be done, if a write operation is happening or not, and which register is to be written to.
- As there are 32 registers in RISC-V, each register number is 5 bits ($32 = 2^5$)

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 6.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=490&rect=96,158,535,347&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.490]]


We'll wait a little before we turn this into a data path, as we have load & store register instructions that use these tools as well, but need a bit more.

A **load** (`ld x1, offset(x2)`) needs to:
- read one register (the base, x2)
- sign-extend the 12-bit offset immediate to 64 bits
- add base + offset in the ALU to form the memory address
- read the data word at that address from data memory
- write that value into the register file (x1)

A **store** (`sd x1, offset(x2)`) needs to:
- read two registers, the base (x2) _and_ the value to be stored (x1)
- sign-extend the offset and add it to the base in the ALU, same as load
- write the value from x1 into data memory at that address
- write nothing back to the register file

So, we need 2 more components, an address first which we access to write data to or read data from, and the ability to generate an immediate.

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 7.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=492&rect=91,245,536,470&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.492]]


Combine these parts tog ether first, we have the data path for memory instructions and R-type instructions.

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 8.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=497&rect=100,561,526,768&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.497]]


Of course we can keep going! Say, branching instructions, what do they need (`beq x1, x2, offset`)? It needs to:

- Compare the two registers for equality, by letting the ALU subtract them and see if the zero flag is raised 
- Then compute the branch target address: PC + sign-extended offset, shifted left 1 bit
- Lastly select the next PC based on the comparison:
    - equal → branch taken → PC = branch target address
    - not equal → branch not taken → PC = PC + 4 as usual

So beyond our existing data path, this adds a second adder for PC + offset, a shift-left-1 on the sign-extended offset, and a mux to choose between PC + 4 and the branch target.

The logic looks like this:

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 9.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=495&rect=99,462,532,774&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.495]]


Combine everything together for the biggg data path, and we have completed the simple data path for a simple CPU!

![[110 Learning/112 CS/112.2 SWE/1 Working With Computers/2 What is a Computer/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 10.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=499&rect=88,484,537,781&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.499]]