We actually know a bit of this through Nand2Tetris! 

C compilers map C programs directly into the architecture-specific machine code.

Java, and python instead first map into an architecture-independent virtual machine byte code, which then gets compiled into machine code by the architecture-specific compiler.

The C program goes through a process that looks like this into an exe file:

![[Pasted image 20260206200002.png|500]]

We can see why this could be a good thing? If it's machine-architecture specific code, it's definetly optimized for that architecture.
- But these days, you could achieve similar level performance in python with the calling of libraries like Cython
- It's like why scientific computation and machine learning is done in python instead of C, despite it being important to optimize performance 
- I mean... who doesn't like simple syntax brushing away all the nitty gritty bottom bits while being optimized?

But, we can also see a downside with C. If you made an executable in 1 machine, you'll need to recompile the code in a new architecture.

This change, compile, run iteration could also be slow during development for testing code.

(There were some things discussing about the pre-processor here, but I think I'll go learn about that in the book readings.)