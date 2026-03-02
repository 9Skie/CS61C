This looks pretty much the same in python.

![[Pasted image 20260128215024.png|500]]

The only difference I can see is the `++`/`--`, this is directly for increment/decrement a variable.

```c
int x = 5;

++x; // Increment x by 1 (x becomes 6)
--x; // Decrement x by 1 (x becomes 5 again)

printf("%d\n", x); // 5
```

There is actually 2 versions of doing this:

```c
x++;   // post-increment
++x;   // pre-increment
```

They... do the same thing? Main difference being HOW this operation works:

```c
arr[i++]   // use i, then increment
arr[++i]   // increment, then use i
```

(I prefer `x++`)