Ah, this is just repeating what the book has already said mostly.

Basically, as there's no way possibly to have all the data put in registers, we have to temporarily store some of it in the memory, which we call a stack.
- there's only 1 variable the registers need to keep track of to operate the stack, the `sp` register, stack pointer (x2)

And, for some reason in RISC-V, it is defined that push 'decrements' the stack pointer, and pop vice versa.

Now, there are 'stack frames', the chunk of stack memory reserved for one single function call.
- Inside a stack frame, there are return instruction addresses, parameters, and other local variables.
- Stack frames can 'jump' to one another depending on function calls

![[Screenshot 2026-02-20 at 7.36.44 PM.png|200]]

Again, they discussed about what's already written in the book... having the leaf function, and turning it into the RISC-V code.