The do statement is closely related to the while statement.

It's just a variant of the while loop that executes at least 1 time, and has the while condition at the end of the loop.

```c
int i = 10;  
  
do {  
  printf("i is %d\n", i);  
  i++;  
} while (i < 5); // condition false! But the above code under do will at least run once
```