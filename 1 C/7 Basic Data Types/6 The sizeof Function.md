You can get the size of the memory (in bytes) of the variable by using a function called `sizeof`.

```c
int myInt;  
float myFloat;  
double myDouble;  
char myChar;  
  
printf("%zu\n", sizeof(myInt)); // outputs 4
printf("%zu\n", sizeof(myFloat)); // outputs 4
printf("%zu\n", sizeof(myDouble)); // outputs 8
printf("%zu\n", sizeof(myChar)); // outputs 1
```

As you can see, we are not using the original ways of printing them out, we are using this `%zu` format specifier instead of their respective originals.

This is because `sizeof` returns a value of type `size_t` instead of a int or something else.

(Knowing the size of data types will help us a lot when we go into memory management later in C, saving memory and improving performance)
