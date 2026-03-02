C gives programmers direct control over memory. By understanding how memory is allocated and freed, you can release resources when they are no longer needed and use only the amount of memory required for a task.

Most of the functions related to memory allocation is under the `<stdlib.h>` header.

- malloc—Allocates a block of memory but doesn’t initialize it. 
- calloc—Allocates a block of memory and clears it.  
- realloc—Resizes a previously allocated block of memory

We will explain how they come into play 1 by 1.