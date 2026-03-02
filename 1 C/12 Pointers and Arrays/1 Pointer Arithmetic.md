Say we declared an array, and a pointer that points to the first element of the array.

```c
int arr[10];
int *arr_p;

p = &a[0];
```

Graphically, this is what happens in memory.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 4.jpg|500]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=287&rect=274,525,443,591|C Programming A Modern Approach (K. N. King) (Z-Library), p.258]]

We can now access `arr[0]` through `arr_p`, or just `arr[0]`.

```c
*arr_p = 5;
```

This updates the 1st element in our array.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 5.jpg|500]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=287&rect=273,385,444,452|C Programming A Modern Approach (K. N. King) (Z-Library), p.258]]

---
## Pointer Arithmatic

You can then perform addition & subtraction on these pointers, just like moving indexes in an array, we will see them in more detail next note.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 6.jpg|500]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=288&rect=184,465,543,675|C Programming A Modern Approach (K. N. King) (Z-Library), p.259]]

![[C Programming A Modern Approach (K. N. King) (Z-Library) 7.jpg|500]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=288&rect=185,212,544,420|C Programming A Modern Approach (K. N. King) (Z-Library), p.259]]

