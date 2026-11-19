The general idea for this class, and the 2 onwards is about having different cores working on different threads.

Now, what do multiple cores mean? If we have 2 cores, it means each cores has it's own control, data path, program counter, registers, ALU. The memory and third level cache is often shared.

![[110 Learning/112 CS/112.2 SWE/2 What is a Computer/1 UCB CS61C/3 Notes/33 Thread Level Parallelism/attachments/Screenshot 2026-08-17 at 10.29.51 AM.jpg|500]]

We'll look more into multicore in the next note