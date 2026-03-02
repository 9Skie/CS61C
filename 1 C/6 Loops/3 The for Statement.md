The for loop looks a lot more complicated...

```c
for (expression_1; expression_2; expression_3) {  
  // code block to be executed
}
```

- **Expression 1** is executed (one time) before the execution of the code block.
- **Expression 2** defines the condition for executing the code block.
- **Expression 3** is executed (every time) after the code block has been executed.

Like, this is printing 1 to 5.

```c
int i;  
  
for (i = 0; i < 5; i++) {  
  printf("%d\n", i);  
}
```

Loops inside loops also work.

```c
int i, j;  
  
for (i = 1; i <= 3; i++) {  
  for (j = 1; j <= 3; j++) {  
    printf("%d ", i * j);  
  }  
  printf("\n");  
}
```


If the idea of a for loop is confusing in C, you can understand the for as a while loop.

```c
expression_1;
while (expression_2) {
    // some code
    expression_3;
}
```
