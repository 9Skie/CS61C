Pointers can be pointed to any data type, and if you are unsure what data type to point to, you can set the pointer to be type `void` at first.

You can even have pointers to functions? Unsure purpose of this.

---
## Struct Pointers

Pointers can also be pointing to structures, like here, using pointers to access data from a struct.

![[Screenshot 2026-02-07 at 10.26.39 AM.png|500]]

You could directly use the dot notation and access the values of the struct like a class's properties.

But with pointers, you can use the `->` to access the property of a struct from the pointer.

---
## Null Pointers

A **null pointer** in C is a pointer that is **guaranteed to point to nothing valid**.

It’s the language’s way of saying: “this pointer intentionally does not refer to an object."

It's a way to explicitly point to nothing.

So instead of a garbage pointer:

```c
int *p;        // garbage pointer (dangerous)
```

We can make sure to say it's not currently in use:

```c
int *p = NULL; // safe, explicit
```

---
## Pointing to Different Sized Objects

As we know, modern hardware has 8-bits (byte) cells, and a C pointer just points to an address.

The reason we need data types is to tell the compiler how many bytes to fetch to the computer.

![[Screenshot 2026-02-07 at 10.41.11 AM.png|500]]

However, there's this additional thing that we would like called 'word alignment' for data types, it's that:
- Word alignment means data is stored at memory addresses that are multiples of its size (or the CPU’s preferred word size).
- Like for a 8-bit (byte) computer, all data types should be multiples of 8 bits, for performance.

This reading is taken from https://www.songho.ca/misc/alignment/dataalign.html for a more detailed explanation.

In programming language, a data object (variable) has 2 properties; its value and the storage location (address). Data alignment means that the address of a data can be evenly divisible by 1, 2, 4, or 8. In other words, data object can have 1-byte, 2-byte, 4-byte, 8-byte alignment or any power of 2. 

For instance, if the address of a data is 12FEECh (1244908 in decimal), then it is 4-byte alignment because the address can be evenly divisible by 4. (You can divide it by 2 or 1, but 4 is the highest number that is divisible evenly.)

CPU does not read from or write to memory one byte at a time. Instead, CPU accesses memory in 2, 4, 8, 16, or 32 byte chunks at a time. The reason for doing this is the performance - accessing an address on 4-byte or 16-byte boundary is a lot faster than accessing an address on 1-byte boundary.

The following diagram illustrates how CPU accesses a 4-byte chuck of data with 4-byte memory access granularity.

![[Pasted image 20260207104929.png|500]]

If the data is misaligned of 4-byte boundary, CPU has to perform extra work to access the data: load 2 chucks of data, shift out unwanted bytes then combine them together. This process definitely slows down the performance and wastes CPU cycle just to get right data from memory.

![[Pasted image 20260207105014.png|500]]

---
# Size of

You can know the size of a data type, in bytes of a data type. You can even use this in structs!