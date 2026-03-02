> [!PDF|yellow] [[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=568&selection=9,0,15,57&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.539]]
> > C’s input/output library is the biggest and most important part of the standard library. As befits its lofty status, we’ll devote an entire chapter (the longest in the book) to the <stdio.h> header, the primary repository of input/output functions.

Most of what C's input output is about dealing with 'streams', a flow of bytes between a program and an input/output (I/O) device, like a keyboard or screen.

For example, the input device you are usually most familiar with is the keyboard, it gives input 'streams' of bits to the program, and we receive that input using functions like `scanf`

Where with the output, we are usually familiar with the screen, whenever we use thing like `printf`, we are outputting the program's contents to the screen.

By default, `<stdio.h>` provides three standard streams ready to use.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 20.jpg|500]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=570&rect=257,610,471,671&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.541]]

But right now, we will concentrate on how streams connect with files in C.

---
## File Pointers

Accessing a stream in a C program is done through a _file pointer_, which has type `FILE*`, with this type only declarable using `<stdio.h>`.

```c
#include <stdio.h>
FILE *fp // declare a file pointer
```

---
## File Types

`<stdio.h>` supports two kinds of files: text and binary. 

- The bytes in a _text file_ represent characters, making it possible for a human to examine the file or edit it. 
- The bytes in a _binary file_ is just... binary, an executable C program is stored in these

Text files are divided into lines, and may contain a special end of file character.

Binary files aren’t divided into lines, and there are no end-of-line or end-of-file markers, all bytes are treated equally.


Take for example when we want to store the number 32767 into a file.


- in a text file it would look like:

 ![[C Programming A Modern Approach (K. N. King) (Z-Library) 21.jpg|500]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=571&rect=231,271,489,312&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.542]]


- in a binary file it would look like:

![[C Programming A Modern Approach (K. N. King) (Z-Library) 22.jpg|200]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=571&rect=305,204,411,236&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.542]]


Keep that in mind when we do any file operations.