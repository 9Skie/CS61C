A little note about CALL, the name of this chapter, it means (Compiling, Assembling, Linking, and Loading), back to the class.

We've probably heard of this before, how Python is pretty easy to program, pretty slow to run, or how C is harder to program, and how it's faster to run, in fact, there's a big spectrum of this tradeoff with different languages.

![[Screenshot 2026-03-03 at 2.53.57 PM.png|500]]

There are two ways to run a program:
- **Interpreter**: directly executes the program without translating it into native machine code ahead of time.
- **Translator**: converts the program into another language (typically machine code) and then executes the translated version.

An **interpreter** executes a program directly, instruction by instruction, at runtime. It reads the source (or bytecode), decodes it, and performs the operations on the fly. No separate machine-code executable is produced ahead of time.
- they are pretty easy to implement, and students even did this in CS61A (really)?
- they produce more understandable error messages

A **translator (compiler)** converts the entire program into another form—typically native machine code—before execution. The output is a standalone executable that the CPU can run directly.
 - it helps 'hide' program source code from the users
 - and faster, faster, faster!