Sometimes this will just "happen" out of nowhere in the code! Like $5/2$, this will get you $2.5$, but... isn't 5 and 2 integers in C? So our answer will be wrong.

```c
int x = 5;  
int y = 2;  
int sum = 5 / 2;  
  
printf("%d", sum); // Outputs 2, not 2.5
```

There's 2 types of conversions in C:
- implicit - happens automatically
- explicit - done by you!

---
## Implicit Conversion

This happens automatically in C, like assigning 9 a type `float`.

```c
// Automatic conversion: int to float  
float myFloat = 9;  
  
printf("%f", myFloat); // 9.000000
```

But this can't work correctly the other way around, like assigning 9.99 into type `int`.

---
## Explicit Conversion

This is done manually by placing a type in `()` in front of the value, and this is the way to get the correct answer from the $5/2$ problem.

This is also sometimes called 'casting' in C.

```c
// Manual conversion: int to float  
float sum = (float) 5 / 2;  
  
printf("%f", sum); // 2.500000
```

This can be done in front of a variable:

```c
int num1 = 5;  
int num2 = 2;  
float sum = (float) num1 / num2;  
  
printf("%f", sum); // 2.500000
```

Also, by default, all numerical vales are stored as doubles in C.