A **function pointer** is like a normal pointer, but instead of pointing to a variable, it points to a **function**.

This means it stores the _address of a function_, allowing you to call that function using the pointer.

Function pointers let you decide which function to run while the program is running, or when you want to pass a function as an argument to another function.

Say this is our function:

```c
int add(int a, int b) {
    return a + b;
}
```

This is a function pointer:

```c
int (*fp)(int, int);
```

 - fp is a pointer to a function that takes (int, int) and returns int.

For assignment, these 2 are the same:

```c
fp = add;
fp = &add;
```

And this goes for calling similarly, you can use it like a normal function, or use the pointer notation.

```c
int result = fp(2, 3);
int result = (*fp)(2, 3);
```

---
## Why Do This?

Why have pointers to functions? Well, this allows us to pass functions as arguments to other functions.

Like this function here, which takes in two integers, and a possible function that is applied to them.

```c
int apply(int x, int y, int (*op)(int, int)) {
    return op(x, y);
}
```

And here are some common operations, serving as examples.

```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int sub(int a, int b) {
    return a - b;
}

int mul(int a, int b) {
    return a * b;
}

int divi(int a, int b) {   // avoid name clash with stdlib
    return a / b;
}
```

This allows us to pass these different operations (functions) to the apply function, increasing the modularity of our code.

```c

int (*op_add)(int, int) = add;
int (*op_sub)(int, int) = sub;
int (*op_mul)(int, int) = mul;
int (*op_div)(int, int) = divi;

int main(void) {
    printf("%d\n", apply(6, 3, op_add));  // 9
    printf("%d\n", apply(6, 3, op_sub));  // 3
    printf("%d\n", apply(6, 3, op_mul));  // 18
    printf("%d\n", apply(6, 3, op_div));  // 2
}
```

|Normal Function|Function Pointer|
|---|---|
|Called directly by its name|Called using a pointer|
|The function is decided before the program runs|You can choose which function to call while the program is running|
|Good for simple code|Good for flexible and reusable code|
