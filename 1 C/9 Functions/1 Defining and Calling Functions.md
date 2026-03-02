We've been dealing with functions this entire time, actually... `main()` is a function which is called at every time of execution, `printf()` is another function.

C is revolved around in functions, as there are no objects in this programming language, this is a function that sums up an array's values.

```c
int sum_array(int *arr, int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += arr[i];
    return sum;
}
```

Here are the parts of that function:

```c
int                 // return type
sum_array           // function name
(int *arr, int n)   // parameters
{
    int sum = 0;    // local variable

    for (...)       // loop (control flow)
        ...;

    return sum;     // return value
}
```

And such, this is the general syntax to any function.

```c
return_type name(parameters)
{
	declarations
    statements;
    return value;   // omitted if return_type is void
}
```
---

## Calling Functions

to call a function and run it's code, it's as simple as writing it's name out in the main program.

```c
// Create a function  
void myFunction() {  
  printf("I just got executed!");  
}  
  
int main() {  
  **myFunction();** // call the function  
  return 0;  
}  
  
// Outputs "I just got executed!"
```

(Though right now, our functions do not have any 'arguments')