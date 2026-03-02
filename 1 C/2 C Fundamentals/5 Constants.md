There are variables which you can explicitly state that their values should never be changed in C, this is with the `const` keyword.
- that makes the variable unchangeable... as the program runs

```c
const int myNum = 15;  // myNum will always be 15  
myNum = 10;  // error: assignment of read-only variable 'myNum'
```

Also, you must assign a value to a `const` variable, you can't declare it and then assign a value to it later.

```c
const int minutesPerHour;  
minutesPerHour = 60; // error
```