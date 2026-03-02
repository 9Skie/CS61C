
## The If

In C, an if statement looks something like this:

```c
if (expression) statement:
```

There must be parentheses around the expression.

But usually... you won't just simply simply run 1 statement, right? It would be multiple/compound statements.

In python, we use indentation to indicate what code falls under the statements, like:

```python
if x > 5:
	print("Hi!")
```

In C, indentation doesn't matter in terms of the syntax, you need a `{}` around the code that is under the `if` statement (and other statements).

```c
int x = 3;

if (x > 5) {
	printf("Hello!")
	}
```

---
## The Else

And the else statement looks basically exactly like in python, except no `:` behind it.

```c
# include <stdio.h>

int x = 3;

if (x > 5) {
	printf("Hello!");
}
else {
	printf("Hi, the above didn't happen!");
}
```

We can continue nesting if's and else's, just MAKE SURE you have `{}` around every statement! Or else it's very easy to mix up which if goes with which else.

```c
int x = 3;

if (x > 5) {
	printf("It's larger than 5!");
	if (x > 4) {
		printf("It's larger than 4!");
	}
	else {
		printf("Can you tell which else this belongs to?");
	}
}
else {
	printf("And that's why you should format your code!")
}
```
