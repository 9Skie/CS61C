When a program is in execution, the program and data will live separately in memory.

![[Screenshot 2026-02-13 at 9.47.35 PM.png|500]]

Now, with the program in the memory, what does the processor do with it? We start going through it line by line.

By default, we read the code incrementally line by line through the program counter, it's a register that holds the byte address of the next instruction to be executed, and increments at every clock cycle.
- Remember, RISC-V instructions are 4 bytes, so the program counter increments 4 bytes by default

![[Screenshot 2026-02-13 at 9.46.11 PM.png|500]]

---
## A little more About the Registers

There are 32 registers in RISC-V, as we known, and they are named from x0 - x31

But since that says very little about their functionalities, we can also access them through alternative names.

Here’s the same table, but now explicitly showing the **ABI alternative names** (the human-readable ones you’ll actually see in assembly):

| **Group**              | **x# Range** | **ABI Names** | **Who Saves?**     | **Purpose**                     |
| ---------------------- | ------------ | ------------- | ------------------ | ------------------------------- |
| **zero**               | x0           | zero          | —                  | Constant 0                      |
| **Return Address**     | x1           | ra            | Caller (if needed) | Stores return address after jal |
| **Stack Pointer**      | x2           | sp            | —                  | Stack pointer                   |
| **Arguments / Return** | x10–x17      | a0–a7         | Caller             | Function args + return values   |
| **Temporaries**        | x5–x7        | t0–t2         | Caller             | Scratch                         |
|                        | x28–x31      | t3–t6         | Caller             | Scratch                         |
| **Saved Registers**    | x8           | s0 (also fp)  | Callee             | Saved register / frame pointer  |
|                        | x9           | s1            | Callee             | Saved register                  |
|                        | x18–x27      | s2–s11        | Callee             | Saved registers                 |

- s0 is also called **fp** **(frame pointer)** when used that way.
- a0 and a1 are also used for return values.
- t registers and a registers are both caller-saved.
- s registers are callee-saved.