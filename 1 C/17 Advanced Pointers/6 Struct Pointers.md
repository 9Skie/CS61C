This is just explaining a bit about struct pointers, and making a simple linked list to explain struct pointers + memory allocation.

This would be a simple node in a linked list using a struct:

```c
struct node {
    int value;
    struct node *next;  // pointer to another Node
};
```

If p points to a struct Node, then
- `*p.value` accesses the value field
- `p->value` is the exact same thing

The `->` operator is a combination of the `*` and `.` operators; it performs indirection on `p` to locate the structure that it points to, then selects the `value` member of the structure.

This is an example of setting a node with a value of 3, and a next node of `NULL`.

```c
struct node *p;
p->value = 3;
p->next = NULL;     // same as (*p).next = NULL;
```

---
## Creating a Linked List

In C, a linked list is not a built-in data structure. Instead, it must be explicitly implemented by defining a node structure and dynamically allocating memory in the heap memory for each node at runtime.

This code initializes a `first` pointer, and creates a node in the heap memory.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 17.jpg|500]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=456&rect=191,125,536,255|C Programming A Modern Approach (K. N. King) (Z-Library), p.427]]

Then, we inserted all the values and pointers to their correct place.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 18.jpg|500]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=457&rect=181,269,533,677|C Programming A Modern Approach (K. N. King) (Z-Library), p.428]]

If you are wondering how `sizeof(struct node)` works... it returns:
- The total number of bytes required to store one struct Node in memory (which, is made up of the primitive data types), including any padding added for alignment.

As for the size of `sizeof(struct node next)`, it is just the size of a pointer on that machine. 

So:
- On a **64-bit system** → pointer = **8 bytes**
- On a **32-bit system** → pointer = **4 bytes**

(Padding is like just an engineer's bandaid fix bro...)
- A detailed explanation of it exists in https://www.songho.ca/misc/alignment/dataalign.html

![[Screenshot 2026-02-09 at 2.07.50 PM.png]]