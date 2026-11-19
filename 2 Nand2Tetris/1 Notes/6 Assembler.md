Remember about how we said we need a tool to help us convert from assembly language to machine language? That's the assembler's job.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 38.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=151&rect=137,438,480,726|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.151]]

## The Hack Machine Language Specification

We know how the binary commands work for every line, as we looked into the details of that in Chapter 4.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 39.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=153&rect=125,424,486,730|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.153]]

And in building the CPU in chapter 5, we understood the logic that the assembly programs follow.

A single assembly line can include:

- An A-instruction or C-instruction
- Declaring a label (xxx)
- A comment

Symbols are also pretty complicated in the hack assembly program, it could be:

- predefined, like R0 - R15 corresponding to 0-15 respectively
- labels, like (xxx), refers to the address of an instruction in the program, mainly for implementing loops and conditional jumps.

```
(Love)
```

- variable, refers to RAM addresses used to store values, if (xxx) is not a predefined symbol or a label, the assembler treats it as a variable and assigns it a RAM address when the program is loaded.

```
@Love
```

A symbol does not begin with a digit.

Now, with that little review of the Hack binary code and assembly code, we will talk about the general idea of translating from assembly to binary.

## Assembly to Binary Translation

So, as we recall, there are lines in assembly where it's instructions, also other lines of purely symbols.

For handling instructions:

> [!PDF|yellow] [[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=155&selection=4,0,19,47&color=yellow|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.155]]
> > For each assembly instruction, the assembler
> > \- parses the instruction into its underlying fields;
> > \- for each field, generates the corresponding bit-code, as specified in figure 6.2;
> > \- if the instruction contains a symbolic reference, resolves the symbol into its numeric value;
> > \- assembles the resulting binary codes into a string of sixteen 0 and 1 characters; and
> > \- writes the assembled string to the output file.

Symbols are much more trickier, as each assembly file is a case by case basis for how symbols are used for the specific purpose, and it's not as straightforward as just referring to a big table to match an instruction in assembly to binary.

There are 3 stages:

- Initialization:
	- The assembler creates a symbol tables to store all the predefined symbols, alongside their pre-allocated values
	- Like mapping R0: 0, R1: 1...
- First pass:
	- The assembler goes through the entire assembly file line by line, whenever it encounters a label declaration, it adds a new entry to the symbol table, and associates the symbol with a the current line number +1, (line number is the number of A-instruction/C-instruction the assembler has went through so far in the file)
	- Note this doesn't include variable declarations, that is in pass 2
- Second pass:
	- Now we start parsing each line and follow the logic of the CPU, like start by checking if it's an A instruction or C instruction, if there is a symbolic reference or not etc.
	- If there is a variable declaration, and it's not included in the symbol table yet, we assign it the next available RAM address.

Honestly, don't be scared! The Hack computer follows the RISC paradigm for designing the CPU processor, so all binary commands are of fixed length, it's just a matter of what this does + where things go for every fixed line.

## Implementation

The books gives an overview of theoretically what the assembler needs to do, and describes a basic assembler with a complete assembler afterwards.

The basic assembler will have no symbolic references, so nothing like `@variable`, just `@1234`.

It will be divided into 2 parts

- a *parser* that goes through each line, and divides each line into fields that needs translation
- a *code* module that looks at the fields and does direct translation into binary codes

### Parser

The book listed out a big sheet of functionalities that the parser should have.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 40.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=159&rect=62,193,555,734|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.159]]

In human words, it needs to open the file, go through it line by line, skip over white space and comments, see what instruction type is the current line, and then depending on the instruction type return fields accordingly.

### Code

The code module is a lot simpler, as it's just looking at a big table to find the corresponding bits to return for translation.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 41.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=160&rect=65,563,553,668|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.160]]

### Complete Assembler

The complete assembler adds on top the symbol table, which, really is just a mapping of variable names to addresses, they could be variables predefined in the language itself, or variables that you added in the assembly code.

To implement it... well, you can directly utilize key value pairs, like a *hash map* in a high level language, this is mostly built in, and we just need these functionaries from it.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 42.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=161&rect=67,142,544,301|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.161]]
