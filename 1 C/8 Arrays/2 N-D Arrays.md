You first start by declaring row, then column.

```c
int matrix[2][3] = { {1, 4, 2}, {3, 6, 8} };
```

Accessing elements goes that way too, first row, then column.

```c
int matrix[2][3] = { {1,2,3}, {4,5,6}};

printf("%d", matrix[1][2]) // Outputs 4
```

And looping through here would require us multiple for loops! (I so wish you can just loop through arrays directly).

```c
int matrix[2][3] = { {1, 4, 2}, {3, 6, 8} };  
  
int i, j;  
for (i = 0; i < 2; i++) {  
  for (j = 0; j < 3; j++) {  
    printf("%d\n", matrix[i][j]);  
  }  
}
```

You can go above 2D, into 3D and 4D.

---
## N-D Arrays in Memory

Though, how are these arrays actually stored in memory? Because there is no dimensional space in memory.

For 2D arrays, they just get broken down into a 1D list in memory, first by row, then by col.

![[Screenshot 2026-02-07 at 10.46.53 PM.png|500]]

This idea extends to 3D arrays, which is broken down first by stacks, and onwards etc.

![[Screenshot 2026-02-07 at 10.47.13 PM.png]]