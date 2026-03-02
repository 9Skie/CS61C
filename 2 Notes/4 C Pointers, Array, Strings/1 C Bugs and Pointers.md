A lot of C has 'Undefined Bahavior', meaning it will run one way on one computer, but another way on another.

They happen very easily in pointers! So... be careful while playing with them.

---
## Address and Values

Memory is simply a huge array, going from 0 up to the limitations of how much memory your computer has.

And with that addressing comes values, just like a list, we can have access o where something is (address), and what something is (value at address).

![[Screenshot 2026-02-07 at 9.23.47 AM.png|500]]

---
## Pointers

As an address refers to a particular memory location, a pointer stores that address of a variable.

![[Screenshot 2026-02-07 at 9.24.48 AM.png|500]]

Here's the basic syntax for pointers.

![[Screenshot 2026-02-07 at 9.31.43 AM.png|500]]

- you start by declaring a variable that is a data type to pointers, then give it an address of an integer, and you can access the address through `p`, and the value through `*p`

They gave a simple example through for creating a pointer.

![[Screenshot 2026-02-07 at 9.37.30 AM.png|400]]

They gave another example of how to change the value of a pointer.

![[Screenshot 2026-02-07 at 9.38.12 AM.png|400]]

---
## Why Pointers?

It helps us move data around... without moving them! Say we have a huge list of data that we would like to pass to a function, normally, the function would create a big copy of that data locally and run from there.

But with pointers, we could just ask the function to run on the original data by pointing to it.

However, his also comes with drawbacks, pointers can cause problem with dynamic memory management, and dangling references with memory leaks.

- Dynamic memory management: Manually allocating and freeing heap memory at runtime; mess it up and you get crashes, corruption, or leaks.
    
- Dangling reference: A pointer that still points to memory after it’s been freed; using it is undefined behavior.
    
- Memory leak: Allocated memory that’s never freed; you lose access to it and your program slowly eats RAM.