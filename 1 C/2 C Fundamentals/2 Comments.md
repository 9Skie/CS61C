### Single Line Comments

Single line comments begin with `//`, the compiler's not gonna care about it.

You can use it to disable some code:

```c
printf("This will run");  
// printf("This will NOT run");
```

Or maybe give some reference to what the code is doing:

```c
// This prints "Hello World!"
printf("Hello World!");
```

---
### Multi-line comments 

This is the way the books teaches it, but `/*` used to be the old way of writing comments in C, it is still used these days for writing multi-line comments.

Basically, before C99 (released in 1999), you could only use multi-line comments in C.

```c
/* The code below will print the words Hello World!  
to the screen, and it is amazing */  
printf("Hello World!");
```

