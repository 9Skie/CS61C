When you start with an assembly file (e.g., file.s), the **assembler** translates it into an **object file** (e.g., file.o). Each assembly file gets converted into their own object files respectively. An object file **does contain machine code**, but it is **not yet a complete executable program**.

There are 4 steps in this process:
1. reading and using directives
2. replacing psudo-instructions
3. producing machine language
4. creating object files


## Directives

There are two kinds of lines in an assembly file:
1. Real instructions → translated into machine code
2. Directives → tell the assembler how to build the object file

An object file is organized by directives, and there are 5 of them:
- **.text** — indicates that subsequent items belong to the text (code) section. Any instructions following this directive will be placed in the machine-code portion of the object file.
- **.data** — indicates that subsequent items belong to the data section. Values declared here are stored as initialized data in memory.
- **.globl sym** — declares a symbol as global, meaning it can be referenced by other object files during linking. This affects the symbol table of the object file.
- **.string "str"** — stores a null-terminated string in the data section. This does not generate executable instructions; it emits raw bytes.
- **.word w1, w2, ...** — stores one or more 32-bit values in successive memory locations in the data section.


## Pseudo Instruction Replacement

This is just converting convenient variations of machine language instructions as if real instructions

Like the instruction `mv t0, t1` is not a real instruction, the real instruction is `addi t0, t1, 0`


## Producing Machine Language

1 - Simple instructions

Most simple instructions, where all necessary information is in the instruction itself can be directly translated into machine code.


2 - Incomplete information 

As for ones which we don't have direct knowledge of all the information, like, a branch or jump instruction may reference a label whose final memory address has not yet been determined.

In such cases, the assembler cannot finalize the instruction completely. Instead, it generates a **partial machine instruction** and records a **relocation entry** describing what part of the instruction must be fixed later (for the linker)

This is part of a bigger list of items called the relocation table.


3 - forward reference problem

Now, one problem that can occur when assembling branch instructions is the **forward reference problem**. This happens when an instruction jumps to a label that appears later in the program, which the assembler has not yet read.

At that moment, the assembler does not know the position of that label relative to the current instruction, so it cannot compute the correct offset for the branch.

```
addi t2, zero, 9        # t2 = 9

L1: 
	slt  t1, zero, t2       
    beq  t1, zero, L2       
    addi t2, t2, -1         
    j    L1                 

L2:
```

Like at the line `beq  t1, zero, L2`, the assembler doesn't know where L2 is.

To solve this problem, we have to make 2 passes of all the assembly code:
1. remember the position of all labels
2. use those label positions to generate code


## Symbol Tables

A **symbol table** is a data structure created by the assembler that records the names and locations of symbols defined in the program. A symbol can be a label, a variable, or a function name. For each symbol, the table stores information such as the symbol’s name, the section it belongs to (for example .text or .data), and its offset within that section.

![[Pasted image 20260303162025.png|500]]

The symbol table allows symbols to be referenced **across different object files**. If a symbol is declared global (for example using .globl), its name and location are exported in the object file’s symbol table. During linking, the linker reads the symbol tables of all object files and matches references to the corresponding definitions.


## Relocation Table

A **relocation table** records places in the object file where the final address is not yet known.

When the assembler generates machine code, some instructions reference symbols whose exact addresses will only be determined later during linking. 

A very common example is a **function call to a function defined in another file**, like here with 2 files:

file1.c

```c
void foo() {
    bar();
}
```

file2.c

```c
void bar() {
}
```

When file1.c is compiled to assembly and then assembled, the assembler sees a call to bar, but **bar is not defined in this file**. Its final address will only be known after the linker combines all object files.

In those cases, the assembler inserts a placeholder value and adds an entry to the relocation table. Later, the **linker** uses the relocation table to update those instructions with the correct addresses once the final program layout is known.