This is a very quick run, so... yeah, and as most of the syntax of C is similar to Java, the professor only decided to go through some of the stuff that is C-specific.

## True or False

In C, there is no boolean data type by default, so it becomes common practice to use `0` as false.

For pointers (discussed later on), it's false is `NULL`.

Booleans only come in when `stdbool.h` came around.

And true... (hm, not well described here)

---
## Data Types

Data types matter in C for their size in bits, and there's not a lot of these compared to other programming languages.

![[Screenshot 2026-02-06 at 10.14.53 PM.png|500]]

---
## Constants 

There are 'constants', which are values that can't be changed during the execution of a program, or Enums, a group of contants.

Constants:

![[Screenshot 2026-02-06 at 10.26.59 PM.png|500]]

Enums:

![[Screenshot 2026-02-06 at 10.27.59 PM.png|500]]

---
## Types in Functions

In C, functions need to have a datatype of return, which is any C data type. 

---
## Structs

typedef allows you to define new, custom data types.

structs, are a special type of typedef that allows multiple variables to be grouped under the same name.

---
## Flow Control

Standard good old statements!
- if-else, while, for, switch case...

We aren't spending much time 'in class' for these, go read the K&R book.