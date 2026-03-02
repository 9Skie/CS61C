Function pointers allows you to pass functions as arguments to other functions in C.

Why would you do that? Well, because sometimes you want to pass behavior, not data.

Like if you wanted to iterate through an array and manipulate each element, we can write a function that takes in an array, and a function, which will be operated on every single element.

You write the loop **once**:

```c
void map_ints(int A[], int n, int (*f)(int)) {
    for (int i = 0; i < n; i++) {
        A[i] = f(A[i]);
    }
}
```

And decide the behavior later:
- double
- scale
- clamp
- hash
- transform
- etc...

This is how you avoid copy-pasting logic like an amateur.