We also have branching instructions in assembly.

Branching instructions are like conditionals, like the if statement.

![[110 Learning/112 CS/112.2 SWE/2 What is a Computer/1 UCB CS61C/3 Notes/8 Logical Instructions/attachments/Screenshot 2026-02-12 at 9.59.50 PM.png|500]]

There's other types of branching like `bne` (branch if not equal), or `blt` (branch if less than), basically just if statements? But not all branching is conditional, there is unconditional branching `j` (jump).

Here's an example of C if statements translated in assembly.

![[110 Learning/112 CS/112.2 SWE/2 What is a Computer/1 UCB CS61C/3 Notes/8 Logical Instructions/attachments/Screenshot 2026-02-12 at 10.06.02 PM.png|500]]

And loops like: while, for, switch also reduces to:

- a comparison
- a conditional branch
- sometimes an unconditional jump

Here's an example of a for loop:

![[110 Learning/112 CS/112.2 SWE/2 What is a Computer/1 UCB CS61C/3 Notes/8 Logical Instructions/attachments/Screenshot 2026-02-12 at 10.12.09 PM.png|500]]

