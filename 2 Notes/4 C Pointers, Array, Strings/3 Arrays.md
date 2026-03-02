Arrays are really identical to pointers, like `char *string` and `char string[]` is almost nearly identical, they both point to a memory address, except an array variable points to the 1st element.

Declaration:

```c
int ar[2]; // 2 is it's length
```

Declaration & Initialization:

```c
int ar[2] = {795, 635}
```

Accessing numbers:

```c
ar[val]
```

---
## Pointers with Arrays

You can access an array through a pointer as well.

![[Screenshot 2026-02-07 at 11.17.14 AM.png|500]]

C does not know an array's length, or bounds, you could accidentally go out of bounds of an array and C would be fine with that.

---
## Pointer Arithmetic

pointers can add/subtract integers to move locations in where it's pointing , but it actually depends on the data type the pointer holds.

![[Screenshot 2026-02-07 at 11.24.01 AM.png|500]]

---
## Functions and Pointers

When you pass arguments to a function, it just gets a copy of those arguments, and so changing the copy doesn't changed the original.

![[Screenshot 2026-02-07 at 11.33.27 AM.png|500]]

However with pointers, you can directly change the value which the pointer is pointing to, and that changes the value.

![[Screenshot 2026-02-07 at 11.33.58 AM.png|500]]

You can even change a pointer's value with a function, through pointer to pointers.

![[Screenshot 2026-02-07 at 11.34.35 AM.png|500]]