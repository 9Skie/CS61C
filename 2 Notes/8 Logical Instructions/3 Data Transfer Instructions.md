Jim Gray gave a physical latency analogy between the speed of transferring data.

Say, if you wanted to retrieve some data from your head, by analogy that takes about 1 minute. But if you needed to retrieve some data from Sarcramento, driving from UCB, it would take about 1.5 hours.

This is the same ratio in memory, a register takes about 1 nano second to access, while memory takes about 100 nano seconds to access.
- so... you know, it's probably a good idea to not do so much loading from assembly to memory back and fourth

---
## Load from Memory to Register

Assume this is the C code:

```c
int A[100];
g = h + A[3];
```

The assembly would would be this:

```
la   x15, A          # x15 = &A[0] (base address of array)

lw   x10, 12(x15)    # x10 = A[3]  (12 bytes offset)
lw   x12, h          # x12 = h

add  x11, x12, x10   # x11 = h + A[3]

sw   x11, g          # g = x11
```

We want to focus on this line:

![[Screenshot 2026-02-12 at 4.07.12 PM.png|500]]

`lw` is the command that loads memory to register, in this case, we loaded the value from `12(x15)` to `x10`.

But what is `12(x15)`? Let us explain, it's an 'offset'.

1. A is an integer array, and each integer occupies 4 bytes in memory.
2. When we load the base address of A into x15, that register holds the memory address of A[0]
3. When we refer to 12(x15), it means: take the address stored in x15 and add an offset of 12 bytes. 
4. Since each integer is 4 bytes, an offset of 12 bytes corresponds to 3 × 4 bytes, which is exactly the location of A[3].

Offset just means '+'

---
## Store from Register to Memory

The same syntax and idea applies, so just read this code.

```c
int A[100];
A[10] = h + A[3];
```

The assembly would would be this:

```
la   x15, A          # x15 = base address of A[0]

lw   x10, 12(x15)    # x10 = A[3]   (3 * 4 bytes = 12)
lw   x12, h          # x12 = h

add  x11, x12, x10   # x11 = h + A[3]

sw   x11, 40(x15)    # A[10] = result  (10 * 4 bytes = 40)
```

We want to focus on this line:

![[Screenshot 2026-02-12 at 4.15.52 PM.png|500]]

Essentially, this is the inverse logic of lw, so I don't need to explain it again.

---
## Loading and Storing Bytes

Instead of transferring entire words (the entire content of a register), you can also transfer data in single bytes.

![[Screenshot 2026-02-12 at 4.18.26 PM.png|500]]

This operates only on the least significant byte in x10, and doesn't affect the rest of the bytes.

![[Screenshot 2026-02-12 at 4.20.20 PM.png|500]]