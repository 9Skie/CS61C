Recall what we talked about last class, of how a function call works in RISC-V.

- function gets called by main (through a jump command)
- the return address to main is saved in `ra` (x1)
- values in registers get moved to function's stack frame, `sp` increments (decrements, fuck, RISC-V...)
- pc jumps to the function's instructions and executes it
- return all values in stack to their respective registers, free up stack frame, return pc to return address.


This class is going to talk about what we should do when we have multiple functions. Again! The book already talked about this.

Here's the example the class uses:

![[Screenshot 2026-02-20 at 8.00.07 PM.png|500]]

And they said the question, if we store the return address in `ra` for `sumSquare`, it's just going to be overwritten by `mult`, and all the values in registers that say, sumSquare used might be changed by `mult`

The solution is through the stack, obviously!

- CalleR: the calling function
- CalleE: the called function

When the CalleE is done playing with it's execution, the CalleR must know what register's values have been changed, and which one's have not, this is done in convention in RISC-V, certain registers are susceptible to be changed, while others are not.

![[Screenshot 2026-02-20 at 8.09.29 PM.png|500]]

This is a more detailed table to the RISC-V calling convention of which registers must be saved by the callee and which may be freely modified (caller saved).

![[Screenshot 2026-02-20 at 8.12.03 PM.png|500]]

