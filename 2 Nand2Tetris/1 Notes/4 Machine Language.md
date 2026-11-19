Now that we've built so many circuits, from basic gates to the ALU, the memory... how does any of that connect with what the humans write up in their fancy high-level language?

The common explanation is that high-level code is first translated into **assembly language**, which is then converted into **machine language** and finally executed on the hardware. But what exactly is machine language, and how does it control the hardware directly?

The book says:

> [!PDF|yellow] [[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=96&selection=65,0,91,9&color=yellow|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.96]]
> > A machine language is an agreed-upon formalism designed to code machine instructions. Using these instructions, we can instruct the computer’s processor to perform arithmetic and logical operations, read and write values from and to the computer’s memory, test Boolean conditions, and decide which instruction to fetch and execute next. Unlike high-level languages, whose design goals are cross-platform compatibility and power of expression, machine languages are designed to effect direct execution in, and total control of, a specific hardware platform. Of course, generality, elegance, and power of expression are still desired, but only to the extent that they support the basic requirement of direct and efficient execution in hardware.

Now, as you can see, machine language is pretty tied to the hardware, as it describes how to operate on a specific set of hardware, so different machines clearly have different machine languages. There’s no universal machine language that works across all computers, unlike the universal nature of the gates and silicon in our systems.

So, the book will teach about the *Hack Machine Language*, a machine language designed for this class, this chapter focuses less on the machine, but rather how to control it.

## Machine Code

### The Hardware

Before the code, let's quickly go over how the hardware interacts with each other.

Memory is used to store data and instructions; each memory location is accessed by specifying its address.

The processor (CPU) is capable of performing arithmetic and logical operations, memory access, and branching operations (we will get to this later).

In transferring data between the memory and the CPU, we will need other registers to temporarily store the data & addresses; they will be categorized in 2 types: *data registers* and *address registers*.

- Data registers combined is *RAM*
- Instruction registers combined is *ROM*

Here's a diagram showing the connections visually between the hardware.

![[4 Machine Language 1.png|500]]

### The Code

> [!PDF|yellow] [[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=99&selection=0,0,25,8&color=yellow|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.99]]
> > Machine language programs can be written in two alternative, but equivalent, ways: binary and symbolic.

It would make sense for programmers to think symbolically something like: "3 + 12".

But obviously, as we remember from making the ALU, that's not something that the machine can understand, and we would have to give that instruction in binary.

We would have to interpret the notion of "adding" as `101011` (by the ALU we have written in chapter 2), 3 (in 16 bits) as `0000000000000011`, and 12 as `0000000000001100` to finally give the instruction of `101011|0000000000000011|0000000000001100` to the computer's memory/

- The `|` does't exist in the real command, I am writing it for your understanding

Clearly, people recognized the need for a **translator** that could systematically convert the *symbolic* programs into *binary* programs. This led to the creation of the tools and terminology we use today:

- binary programs -> machine language = `0100001101...`
- symbolic programs -> assembly language = `R1 + R2...`
- symbolic programs -> **assembler (translator)** -> machine language

We will make the assembler in [[6 Assembler]].

## Instructions

For every machine language, there are:

- Arithmetic and logical operations
- Memory access
- Flow control (loops)

We will presume there are registers denoted as R0, R1, R2, R3... and on.

What we will introduce here is the assembly language (that's understandable to humans) which will be translated to the machine language.

### Arithmetic and logical operations

Basically, all the stuff we've talked about up to this point! Adding, subtracting, And, Or, Xor... you know.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 24.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=100&rect=63,326,392,479|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.100]]

### Memory Access

This just corresponds to accessing and manipulating memory addresses.

An example could look something like this:

```
load A, 200        ; Set address register to 200
load M, 1          ; Set memory registor (at address A) to 1
```

### Flow Control (Loop)

The ability to loop is also included in machine language, except they call it branching, which denoted by the `goto` instructions, which can be conditional or unconditional.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 25.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=101&rect=122,342,493,525|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.101]]

### Variables

Uh... a bit confusing, but the general gist is that variable data & address definitions are better than literal values, since that has more potential to be transferred to other machines.

Now that we understand a machine language's capabilities, we will go look at the Hack Machine Language.

## Hack Machine Language

As we know that machine language is specific to the hardware, we will first look at the Hack computer's hardware.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 26.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=103&rect=129,393,496,613|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.103]]

Ok, I wanna throw you first some examples before going into the syntax formally, or else it's going to be super boring.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 27.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=106&rect=126,116,490,325|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.106]]

Confused? Now let's look at the syntax.

Memory:

- The entire instruction memory is ROM, but only 1 instruction will be accessed at a time.
	- The value of the address of the currently accessed instruction register is called the *current instruction*.
- The entire data memory is RAM, but also, only 1 data will be accessed at a time.
	- The value of the address of the currently accessed data register is called *M*

Register:

- There are 3 registers which we can manipulate: D (data), A (address), and M (current data memory)
- Their values (except the address register, A) could be set through the syntax `=`, like `D = M`

Addressing:

- The address register's values could be set through the syntax `@`, like `@17` will set A to be 17.

Branching:

- Unconditionally, the syntax is `0;JMP`, which jumps to the *current instruction* at address register A's value, the 0 is a placeholder for conditionals, which currently there isn't.
- Conditionally, there is greater than `conditional;JGT`, equal to `conditional;JEQ`... we'll see more later.

Variables:

- Variables in Hack are **symbols** that represent **memory addresses**, not direct values.
	- For example, `x = 17` means “store 17 in the memory location named `x`”.
- The instruction `@x` sets the **address register A** to the **memory address** assigned to `x` by the assembler, **not** to the value stored in `x`.
- If you haven’t assigned a value to `x` yet, `@x` still loads its address into A. You can then store into or load from that memory location using `M`.
- Hack provides 16 built-in symbols `R0` through `R15`, which are pre-assigned to memory addresses 0 through 15.

The entire language specification is as follows:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 28.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=109&rect=118,304,488,590|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.109]]

There are also some things regarding the screen and keyboard; they interact with the system through memory-mapped addresses.

The screen starts at **RAM address 16384** (or @SCREEN) and consists of 256 rows, each with 512 pixels. This is represented as **8192 16-bit words**, with each word controlling 16 pixels. Each pixel can be set to **black** (1) or **white** (0). To manipulate a specific pixel, you fetch the corresponding 16-bit word, modify the appropriate bit(s), and write the word back into memory.

The **keyboard** is mapped to **RAM address 24576** (or @KBD). When a key is pressed, the **16-bit character code** for that key appears at @KBD. If no key is pressed, the code 0 is stored in that memory location. The Hack character set maps the keyboard’s input to these codes.

## Hack Programming

I get it! It's overwhelming to suddenly be thrown with such an arbitrary amount of syntax in your face, so there are 3 examples here to help you digest hack programming.

Program 1:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 29.jpg|250]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=117&rect=128,376,485,727|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.117]]

Program 2:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 30.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=108&rect=102,296,509,732|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.108]]

Program 3:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 31.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=119&rect=128,272,485,576|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.119]]
