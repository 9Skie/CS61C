> [!PDF|yellow] [[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=222&selection=64,1,71,74&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.193]]
> > In C, arguments are passed by value: when a function is called, each argument is evaluated and its value assigned to the corresponding parameter. Since the parameter contains a copy of the argument’s value, any changes made to the parameter during the execution of the function don’t affect the argument. 

Like in this example:

```c
int power(int x, int n)
{
    int result = 1;
    while (n > 0) {
        result *= x;
        n--;
    }
    return result;
}
```

Modifying n does **not** affect the original variable, so it can safely be used as the loop counter, eliminating the need for a separate variable i.

---
## Array Arguments

Arrays are often used as arguments. When a function parameter is a one-dimensional array, the length of the array can be (and is normally) left unspecified:

```c
int f(int a[]){ /* no length specified */ 

} 
```

You could also explicitly state it too, but why would you?