I think the book doesn't really explain this in a universal way that I like it would, so, I've turned to other sources.

First, C has 2 types of memory, static memory, and dynamic memory.
- static memory:  memory that is reserved for variables **before** the program runs, and remains allocated for the entire lifetime of the program.
	- This includes global variables, static variables, and arrays whose size is known at compile time.
- dynamic memory: memory that is allocated **after** the program starts running. Allocation of dynamic memory can also be referred to as _runtime_ memory allocation.
	- This is the memory which we have control with allocation

How memory looks like on the computer when a C file is compiled.

![code_section](https://media.geeksforgeeks.org/wp-content/uploads/20251106114528441034/code_section.webp "Click to enlarge")

- Code Section: Stores compiled instructions of the program.
- Stack Memory: Stores local variables and function call data. 
- Heap Memory: Used for dynamic allocation. Memory is manually managed using pointers.
- Data Segment: Holds global and static variables.

To be clear again, the heap, the dynamic memory is where all of our memory control happens.

---

To allocate dynamic memory, you can use the `malloc()` or `calloc()` functions. It is necessary to include the `<stdlib.h>` header to use them.

```c
int *ptr1 = malloc(size);  
int *ptr2 = calloc(amount, size);
```

- The `malloc()` function has one parameter, _size_, which specifies how much memory to allocate, measured in bytes.

- The `calloc()` function has two parameters:
	- _amount_ - Specifies the amount of items to allocate
	- _size_ - Specifies the size of each item measured in bytes

## A bit more about Malloc 

Malloc essentially 'gives' you a continuous piece of memory (in bytes) which you are free to put values in, read out from, etc.

It returns you a pointer to the beginning of the memory address which you've allocated, very much similar to like how a list essentially is just a pointer to it's first element.

In fact, you can even use the same syntax to get values back from that pointer and onwards (this works in other times were we use pointers too).

```c
int val_from_ptr = *ptr1
int val_from_list = ptr[0]
// These return the same values!
```

Malloc, however, doesn't initialize any values in the memory it just allocated, and if you directly read from the memory address, it will return garbage values.

The amount of byte Malloc allocates is related to 2 things.
- the data type which you want to store
- how many of that data type which you want to store

So what programmers would normally instead write is:

```c
int *ptr1;
int n;
ptr1 = malloc(n * sizeof(*ptr1))
```

This allocates enough memory to store `n` contiguous objects, with the size of each element determined automatically by `sizeof(*ptr1)` (which is just the size of int in this case, as the data type for which ptr1 is pointing to is int).

---
## A bit more about Calloc 

Calloc simplifies the process we've described above with those 2 parameters.

```c
int *ptr1;
int n;
ptr1 = malloc(n * sizeof(*ptr1))

ptr1 = callac(n, sizeof(*prt1)) // Same idea with 1 difference
```

- amount - Specifies the amount of items to allocate
- size - Specifies the size of each item measured in bytes

 Internally, calloc allocates a contiguous block of memory large enough to hold count × size bytes and **initializes every byte to zero**.

 Unlike malloc, which leaves the allocated memory uninitialized, calloc guarantees that the allocated memory starts in a known zero state (basically, all the bits in that memory is 0)

