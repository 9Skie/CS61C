## H files

Previously, we've mostly been working with singular files in C, but usually a program is divided among many number of source files.

By convention, source files have the extension .c. Each source file contains part of the program, primarily definitions of functions and variables. 

But, when you divide a program into several source files, we have to answer to the question of How can a function in 1 file call a function defined in another file?

We've seen header files when talking about the pre-processor through the `#include` directive with `.h` files, called header files.

We can include either built in C libraries, or our own files (we need file paths if it's our own files).

![[C Programming A Modern Approach (K. N. King) (Z-Library) 25.jpg|500]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=380&rect=194,344,534,470|C Programming A Modern Approach (K. N. King) (Z-Library), p.351]]

This can share functions, macros & type definitions, and even variables? Wait what variables?

Like, if I define a global variable in one file:

```c
/* file1.c */
int counter = 0;   // definition
```

I can directly use it in another file, no imports needed!

```c
/* file2.c */
extern int counter;   // declaration only
```