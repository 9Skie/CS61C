Previously, we've seen comparison statements in C return 0's and 1's, not true's and false's.

But C does have `bool`! So I find that a bit weird, but it's not included in C directly, we must import a header file for it.

```c
# include <stdbool.h>
```

And then you can start declaring `bool` type variables

```c
# include <stdbool.h>

bool isProgrammingFun = true;  
bool isFishTasty = false;
```

To print them however, C doesn't treat them uniquely as their own data types, C still treats them as 0 and 1, so you can still work with them just as you work with 0 and 1.

```c
// Create boolean variables  
bool isProgrammingFun = true;  
bool isFishTasty = false;  
  
// Return boolean values  
printf("%d", isProgrammingFun);   // Returns 1 (true)  
printf("%d", isFishTasty);        // Returns 0 (false)
```