But why pointers? Why give this xtra layer of confusion to ourselves in coding? One of the examples is changing the values of variables passed to a function.

> [!PDF|yellow] [[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=276&selection=24,0,72,16&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.247]]
> > Pointers offer a solution to this problem: instead of passing a variable x as the argument to a function, we’ll supply &x, a pointer to x. We’ll declare the corresponding parameter p to be a pointer. When the function is called, p will have the value &x, hence *p (the object that p points to) will be an alias for x. Each appearance of *p in the body of the function will be an indirect reference to x, allowing the function both to read x and to modify it

## Without Pointers

You want a function to change a variable, when you use it, the value in main doesn't change.

```c
void increment(int x)
{
    x = x + 1;
}

int main(void)
{
    int a = 5;
    increment(a);
    printf("%d\n", a);  // still 5
}
```

**Why this fails:**
- x is a **copy** of a
- You changed the copy
- The original stays untouched

---
## The solution (with pointers)

  Instead of passing the value, pass where the value lives*

```c
void increment(int *p)
{
    *p = *p + 1;
}

int main(void)
{
    int a = 5;
    increment(&a);
    printf("%d\n", a);  // now 6
}
```

So, you can see how it's being handled differently with pointers.

|**Without pointer**|**With pointer**|
|---|---|
|“Here’s the number”|“Here’s the address”|
|Modify copy|Modify original|
|No side effects|Intentional side effects|
