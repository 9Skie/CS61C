> [!PDF|yellow] [[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=128&selection=18,0,36,5&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.99]]
> > A loop is a statement whose job is to repeatedly execute some other statement (the loop body). In C, every loop has a controlling expression. Each time the loop body is executed (an iteration of the loop), the controlling expression is evaluated; if the expression is true—has a value that’s not zero—the loop continues to execute.

It's part of the good old standard!

```c
while (condition) {  
  // code block to be executed
}
```

the syntax looks really similar to a if statement, no?

```c
int i = 0;  
  
while (i < 5) {  
  printf("%d\n", i);  
  i++;  
}
```
