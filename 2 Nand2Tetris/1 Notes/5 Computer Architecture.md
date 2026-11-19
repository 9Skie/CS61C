> [!PDF|yellow] [[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=124&selection=7,0,10,44&color=yellow|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.124]]
> > This chapter is the pinnacle of the hardware part of our journey. We are now ready to take the chips that we built in chapters 1–3 and integrate them into a general-purpose computer system, capable of running programs written in the machine language presented in chapter 4.

So it's finally all coming together! It's going to be time to build a computer!

However, before going into how the hardware all wires and fires, we should first understand a fundamental design principle that almost all modern computers follow, the *von Neumann architecture*, as our computer will follow it too.

## The von Neumann Architecture

How do computers seem to perform infinitely complex tasks, despite being limited to a fixed set of simple operations? This stems from the stored-program concept.

The idea is simple: the computer’s hardware only needs to support a small number of basic operations, and more complex instructions can be broken down into combinations of these fundamental operations.

When a more complex instruction is needed, it is temporarily loaded into memory and executed by the computer based on its predefined set of simple instructions. This allows the computer to perform a wide variety of tasks, depending on the instructions loaded into memory.

This distinction, where the hardware handles basic instructions and more abstract, complicated instructions are loaded in memory when needed, became the foundation of the concept of *software*.

> And fun thing is, software written in high-level languages would be translated into machine code and stored in the computer's storage as an .exe file (executable)

And this is the basis of the *von Neumann Architecture*.

> [!PDF|yellow] [[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=126&selection=18,0,51,60&color=yellow|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.126]]
> > The von Neumann architecture, shown in figure 5.1, is based on a Central Processing Unit (CPU), interacting with a memory device, receiving data from some input device, and emitting data to some output device. At the heart of this architecture lies the stored program concept: the computer’s memory stores not only the data that the computer manipulates but also the instructions that tell the computer what to do.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 32.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=126&rect=129,258,484,415|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.126]]

Now, we will dive deeper into what each part is doing in a computer.

### Memory

The course says programs are serialized into .exe files and then loaded into the instruction memory, but that is ROM in this case, more generally, programs are also loaded into RAM,

## CPU

We've seen most of the things that make up the CPU, the ALU, the registers that store intermediate values.

The repetitive cycle of fetching an instruction, decoding the instruction, executing the instruction, fetching a new instruction... is referred to as the *fetch-decode-execute cycle*.

## IO (Input/Output)

Every IO actually looks the same to the computer, as for each device is allocated a set amount of memory, called its *memory map*, and that's what the computer sees a device as.

For example, as we knew from [[4 Machine Language]], the keyboard is mapped to @24576 in the Hack Computer, the screen, being a resolution of 512 x 256, is mapped from @16384 - @24575 (16 bits each at a time of manipulation).

We can receive inputs from the keyboard by getting the value stored at the keyboard's memory map, and direct outputs to the screen by changing the values stored at the screen's memory map.

## The Hack Computer

A lot of this is redundant descriptions of things we've already created, so we will put the diagrams here of the new stuff.

CPU:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 33.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=132&rect=112,109,514,446|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.132]]

Instruction Memory:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 34.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=133&rect=116,94,492,296|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.133]]

Data Memory:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 35.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=137&rect=88,296,539,740|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.137]]

## Implementation

They've already given you the circuits for everything! You just need to put them together.

CPU:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 36.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=139&rect=131,90,496,315|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.139]]

The idea of the CPU goes as follows:

1. Instruction Decoding
	- The left-most bit decides whether it's an instruction for the A register (if it's 0, A-instruction) or the ALU for computation (if it's 1, C-instruction)
2. Instruction Execution
	- If it's an A instruction, the 15 bits remaining contain the value to be stored in the A register
	- If it's a C instruction, then the instruction is treated as a series of control bits in the format: `1xxaccccccdddjjj`
		- xx (filler): They don’t affect the operation and are simply there to fill out the instruction format.
		- a (address): determines which input is fed to the ALU
		  \- If a = 0, the ALU gets its input from the A register.
		  \- If a = 1, the ALU gets its input from M, the value stored in the RAM at the address specified by the A register.
			- cccccc (computation): define the computation performed by the ALU.
			- ddd (destination): specify which registers should store the result of the ALU computation.
			- jjj (jump): determine whether and where the program counter should jump to after executing the instruction.

You can recall from this place for the details of the syntax of an instruction:

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=109|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.109]]

3. Instruction Fetching
	- By default, the CPU fetches the next instruction by incrementing the program counter by 1 and going to the address stored at the program counter, which initially starts at 0.
	- If a jump is encountered, the CPU prioritizes the jump and fetches the instruction from the address specified by the jump, instead of simply incrementing the program counter.
	- Honestly... jumping is a bit weird, I don't remember reading about this in the textbook, but the idea is that we must use the zero flag (zr) and negative flag (ng)
		- (no jump) 000 -> load = 0
		- (if result > 0) 001 -> ng = 0 and zr = 0 -> load = 1
		- (if result = 0) 010 -> zr = 1 -> load = 1
		- (if result >= 0) 011 -> zr = 1 or (ng = 0 and zr = 0) -> load = 1
		- (if result < 0) 100 -> ng = 1 -> load = 1
		- (if result != 0) 101 -> zr = 0 -> load = 1
		- (if result <= 0) 110 -> ng = 1 or zr = 1 -> load = 1
		- (just jump) 111 -> load = 1
		- 001 -> **Jump if the zero flag is set** (PC should update if the result was zero).
		- 010 -> **Jump if the negative flag is set** (PC should update if the result was negative).
		- 011 -> **Jump if the zero or negative flag is set**
		- 100 -> **Jump if the positive flag is set**
		- 101 -> **Jump if the zero or positive flag is set**
		- 110 -> **Jump if the negative or positive flag is set**
		- 111 -> **Unconditional jump** (PC should always update).

Computer:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 37.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=142&rect=122,214,498,457|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.142]]
