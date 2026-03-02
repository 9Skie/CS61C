We can not only pass pointers to functions but also write functions that return pointers. 

The following function, when given pointers to two integers, returns a pointer to whichever integer is larger:

```c
int *max(int *a, int *b)
{
    if (*a > *b)
        return a;
    else
        return b;
}
```

Example usage:

```c
int x = 10, y = 20;
int *p = max(&x, &y);

printf("%d\n", *p);  // 20
```

