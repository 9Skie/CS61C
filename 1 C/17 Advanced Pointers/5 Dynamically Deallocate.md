It is possible for memory to remain allocated even after it is no longer needed by the program. If the program loses all references to that memory without freeing it, the memory becomes inaccessible and cannot be reused, yet it continues to occupy space until the program terminates.

We call those 'memory leaks'.

> You'll feel it if you are playing a game with poor optimization, as the game goes on, it will become slower and slower

Well, how do we have these memory leaks? Take this example.

```c
p = malloc(whatever_1);
q = malloc(whatever_2); 
p = q;
```

Originally, after the execution of the first 2 statements, p points to a memory block, and q points to another.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 15.jpg|200]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=452&rect=315,574,416,638|C Programming A Modern Approach (K. N. King) (Z-Library), p.423]]

But, when we set `p = q`, both variables point to the memory block `q` points to, and there are no variables that point to the original memory block for `p`.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 16.jpg|200]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=452&rect=316,492,416,551|C Programming A Modern Approach (K. N. King) (Z-Library), p.423]]

We can't access it, and so we can't change/get values inside of it, and it's just sitting there lost in memory, taking up space.

Some languages provide a garbage collector that automatically locates 'garbage' like this memory block, and frees it up for use, but C doesn't have that, and you must manually `free` the memory.

---
## The free Function

Say we had the same example:

```c
p = malloc(whatever_1);
q = malloc(whatever_2); 
free(p); // The memory block at p is freed, it can now be used by other memory allocations
p = q;
```

Now, the original memory block at p has been freed, but we also must beware of another problem that exists, 'dangling pointers'.

The call to `free` simply deallocates the memory block that the pointer points to, but it doesn't change the pointer itself. After the call, the pointer still holds the same address, even though that address no longer refers to valid, owned memory.

Such a pointer is called a _dangling pointer_, and any attempt to read from or write to it results in undefined behavior.

So it's best practice to give that deallocated pointer a `NULL`, to indicate it is no longer being used.
- If it is being used elsewhere... give it a new address!

```c
free(p);
p = NULL;
```