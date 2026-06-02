> [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=254&selection=36,0,39,1&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.254]]
> > This section describes the four steps in transforming a C program in a file from storage (disk or flash memory) into a program running on a computer.


If we recall the stage of compilation, it goes as such:

1. A C program gets compiled by a compiler and turns into assembly
2. The assembly program gets assembled into machine language (binary)
3. The linker takes the machine language, and other imported code (like from libraries of other files) and combines it into an executable
4. The loader is used for loading the executable actually onto memory.

![[110 Learning/112 CS/122 Basics/2 What is a Computer?/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy) 16.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=255&rect=89,449,536,786|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.255]]

But... I think it's not explained very well in it's details, it goes through a bit of history, saying how programs before usually written in assembly as compilers were inefficient in using the limited memory at the time.

In the assembler, there are possible 'non' real instructions, like pseudo instructions that the assembler will convert to RISC-V instructions, there was a little dip talking about the 'symbol table', but no details were explaiend.

The linker is bout determining the exact addresses of data and instruction labels (where jumps are etc),  all absolute references, that is, memory addresses that are not relative to a register, must be relocated to reflect its true location.

However, the book doesn't go into details about the implementation of any of the above, it's just a high-level gloss over.

---

## Why Linker Exists

If a program were treated as a single unit, then changing even one line of code would require recompiling the entire program. This would be inefficient and wasteful, especially for large software systems. 

The linker solves this problem by allowing programs to be divided into separately compiled and assembled modules. Each source file can be compiled independently into an object file, and the linker then combines these object files, resolving symbol references and stitching them into a single executable.

As a result, when you modify part of the program, only the affected source files need to be recompiled, and the linker can reuse the previously compiled object files for the rest of the program.

Beyond modular compilation, the linker also plays a role in library usage. Instead of copying all library code into every executable (static linking), the linker can record dependencies on shared libraries (dynamic linking). In this case, the executable contains references to external library symbols, and the actual library code is loaded and finalized at runtime by the loader. This allows multiple programs to share the same library code in memory and reduces executable size while still preserving modularity.

- It's what we call the DLLs over just copying file code over and over...

## What Loader Does

> [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=263&selection=95,0,111,12&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.263]]
> > 1. Reads the executable file header to determine size of the text and data segments. 
> > 2. Creates an address space large enough for the text and data. 
> > 3. Copies the instructions and data from the executable file into memory. 
> > 4. Copies the parameters (if any) to the main program onto the stack. 
> > 5. Initializes the processor registers and sets the stack pointer to the first free location. 
> > 6. Branches to a start-up routine that copies the parameters into the argument registers and calls the main routine of the program. When the main routine returns, the start-up routine terminates the program with an exit system call.
> 

---

## Virtual Machine Intermediates

As we saw earlier with C programs, the resulting executable depends heavily on the target hardware architecture and operating system. Different platforms use different compilers, object formats, and instruction sets. For example, macOS commonly uses Clang, Windows uses MSVC, and Linux often uses GCC. A program compiled for one architecture (e.g., x86-64) cannot run directly on another (e.g., ARM) because the generated machine code is architecture-specific.

Java addressed this portability problem with the idea of “write once, run anywhere.” 

Instead of compiling directly to native machine code, Java source code is compiled into an intermediate representation called Java bytecode. This bytecode is designed to run on a Java Virtual Machine (JVM), which acts as an abstraction layer between the program and the underlying hardware. Each platform implements its own JVM, translating bytecode into native instructions for that specific architecture at runtime. As a result, the same compiled Java program can run on different hardware platforms without recompilation, as long as a compatible JVM exists.

![[110 Learning/112 CS/122 Basics/2 What is a Computer?/2 UCB CS61C/2 Notes/attachments/PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy) 17.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=268&rect=76,524,537,723|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.268]]