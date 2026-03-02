As we know, there's just 32 registers in a RISC-V cpu, but we definitely will work with more than 32 values.

So, that's why we need to load from and store to memory.

![[Screenshot 2026-02-12 at 3.33.53 PM.png|500]]

In CS61C, they use 32 bit registers, while the book from Patterson uses a 64 bit register, I will follow the convention of 64 bits.
- and, for some reason, we introduce the notation that 1 word = 4 bytes, 

Registers in RV64 are 64 bits wide, but the values we store in them are often much smaller, like 8-bit characters or 32-bit integers. 

The hardware still uses the full 64-bit register, so there needs to be an efficient way to place smaller values into a register without wasting the rest of the register's space.

(WHICH HE DOESNT FUCKING ACTUALLY ANSWER WITH SMALL ENDIAN)

(WE JUST WASTE THE SPACE BRUH IN THE REGISTORS)

---
## Small Endian

This is just a way to store bytes in memory, not addresses, so fuck this order of teaching.

Suppose we have the 32-bit number:

```
0x12345678
```

Break it into bytes:

```
12, 34, 56, 78
^MSB        ^LSB
```

In little endian memory, it is stored like this:

|**Address**|**Value**|
|---|---|
|100|78|
|101|56|
|102|34|
|103|12|

Smallest address → least significant byte.

![[Screenshot 2026-02-12 at 3.52.12 PM.png|500]]

