As arrays in C are just a collection of values sitting consecutively in memory, referencing the array will just return the `pointer` to the first element of the array.

```c
int myNumbers[4] = {25, 50, 75, 100};  
  
// Get the memory address of the myNumbers array  
printf("%p\n", myNumbers);  
  
// Get the memory address of the first array element  
printf("%p\n", &myNumbers[0]);

// They are the same!!!
```

So you can access an array with a pointer operator, by de-referencing the pointer.

```c
int myNumbers[4] = {25, 50, 75, 100};  
  
// Get the value of the first element in myNumbers  
printf("%d", *myNumbers);
```
