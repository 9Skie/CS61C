If the amount of memory you reserved is not enough, you can _reallocate_ it to make it larger through `realloc()`.

The `realloc()` function takes two parameters:

```c
int *ptr2 = realloc(_ptr1_, _size_);
```

- The first parameter is a pointer to the memory that is being resized.
- The second parameter specifies the new size of allocated memory, measured in bytes.

The `realloc()` function tries to resize the memory at _ptr1_ and return the same memory address. If it cannot resize the memory at the current address then it will allocate memory at a different address and return the new address instead.

## A bit more about Realloc

Realloc is similar to malloc, in these sense that regardless if the memory got larger or smaller after reallocation, the original values at those memory addresses will not be changed.
- Assuming we are still at the original memory address

If we jumped to a new memory address after realloc, the original memory block is automatically freed and must no longer be accessed. Its contents are no longer owned by the program and may be reused or overwritten by the allocator at any time.

We will talk about 'freeing memory' in the next note.

Also, if realloc didn't find a new address, nor was it able to just extend the current memory, it would return a `NULL` pointer.