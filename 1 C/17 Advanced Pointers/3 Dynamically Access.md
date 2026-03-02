Dynamic memory behaves like an array, with its data type specified by the type of the pointer.

As with arrays, to access an element in dynamic memory, refer to its index number:

```c
ptr[0] = 12;
```

Of course, you can still do the typical pointer arithmetic, instead of changing the mindset to be an array-like notation.

```c
*ptr = 12;
```

Dynamic memory does not have its own data type, it is just a sequence of bytes. The data in the memory can be interpreted as a type based on the data type of the pointer.

Just do remind yourself that when you do access to memory addresses in dynamic memory.

```c
// Allocate memory  
int *ptr;  
ptr = calloc(4, sizeof(*ptr));  
  
// Write to the memory  
ptr[0] = 2;  
ptr[1] = 4;  
ptr[2] = 6;  
  
// Read from the memory  
printf("%d\n", *ptr);  
printf("%d %d %d", ptr[0], ptr[1], ptr[2]);
```
