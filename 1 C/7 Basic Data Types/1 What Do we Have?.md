As we saw in explaining variables, a variable must specify it's data type in C, and printing out different data types require different keywords.

```c
// Create variables  
int myNum = 5;             // Integer (whole number)  
float myFloatNum = 5.99;   // Floating point number  
char myLetter = 'D';       // Character  
  
// Print variables  
printf("%d\n", myNum);  
printf("%f\n", myFloatNum);  
printf("%c\n", myLetter);
```

So, why specify data type? This is because data type directly matters in C for their size in bits, here are some basic examples.

![[Pasted image 20260128203045.png|500]]

