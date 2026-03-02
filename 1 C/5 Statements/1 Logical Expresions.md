C doesn't have a lot of statements, and most of them fall under 3 categories (except return and expressions, which was already looked at).

- Selection statements: `if`, `switch`
- Iteration statements: `while`, `do`, `for`
- Jump statements: `break`, `continue`, `goto`

And the rest are just compounded statements of the ones above.

---
## Comparisons

> [!PDF|yellow] [[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=103&selection=10,0,51,1&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.74]]
> > Several of C’s statements, including the if statement, must test the value of an expression to see if it is “true” or “false.” For example, an if statement might need to test the expression i < j; a true value would indicate that i is less than j. In many programming languages, an expression such as i < j would have a special “Boolean” or “logical” type. Such a type would have only two values, false and true.

In python, if you do a comparison, it will return a type `bool`, which can either be true or false.

In C... comparisons are a bit weirder, since the return value of a comparison is either `1` or `0`, which symbolically represents true (1) and false (0).
- It's weird that C does this... since it does have a class of `bool`.

Like, this comparison will return 1:

```c
int x = 5;  
int y = 3;  
printf("%d", x > y); // returns 1 (true) because 5 is greater than 3
```

But else than that, it's basically the same as python.

![[Pasted image 20260128221451.png|500]]

ut outside of numerical comparisons, we also have Logical comparisons, which, do not look like python.

In python, we'd actually have keywords for them, like `and`, `or`, `not`, in C those doesn't exist, and we have these weird abstract symbols.

![[Pasted image 20260128230140.png|500]]
