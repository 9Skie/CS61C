## `#define` - Create a Macro

```c
#define PI 3.14  
  
int main() {  
  printf("Value of PI: %.2f\n", PI);  
  return 0;  
}
```

A macro is a name that represents a value (like PI), or a piece of code, defined using the `#define` directive.

In the example below, `PI` is replaced with `3.14` before the program is compiled.

This means that every time `PI` appears in the code, it will be replaced with `3.14`:


Macros can also take parameters, like a function:

```c
#define SQUARE(x) ((x) * (x))  
  
int main() {  
  printf("Square of 4: %d\n", SQUARE(4));  
  return 0;  
}
```

---

## `#ifdef` and `#ifndef` - Conditional Compilation

The `#ifdef` and `#ifndef` directives let you include or skip parts of the code depending on whether a macro is defined.

This is called **conditional compilation**, and it's useful for debugging or creating different versions of a program.

```c
#define DEBUG  
  
int main() {  
  #ifdef DEBUG  
    printf("Debug mode is ON\n");  
  #endif  
  return 0;  
}
```

In this case, as we have the line `#define DEBUG`, `DEBUG` is defined, and so we execute out the line ` printf("Debug mode is ON\n");`.

It basically is like an if statement.