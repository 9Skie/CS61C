It's easiest to understand C by directly throwing you it's "hello world".

```c
#include <stdio.h>

int main(void){
	printf("Hello World");
	return 0;
}
```

As you can see, the general form of a program can be divided as such:

```c
directives

int main(void){
	functions
	statements
}

```

---
### Directives

In simple, these tell C what to include before the program is being compiled, in this case, `#include <stdio.h>`, which contains information about C's standard I/O library.

They are alike importing libraries in python... except every time, you'll need to import the standard I/O library for C.

---
### Functions

The name "function" got it's name in C just like functions in mathematics, f(x), g(x, y) and so on, they take inputs, and usually return outputs.

Functions fall into 1 of 2 types in C:
- User defined
- C provided (library functions)

For every C file, the `main` function is mandatory, we'll talk about how to make other functions a long time later.

The main function is a bit special. It doesn't take in anything, so it has the input of `void`, and the value that it returns is a status code, `return 0`.

`return` causes the function to terminate, `0` indicates the program went normal.

---
### Statements

A statement is a command that's executed when the program runs... we'll get in detail of them later down the line, in this program, we've only used the `printf` statement and the `return` statement.

Also, you must end a statement with a `;`, this is C syntax.

`printf` doesn't automatically print in a new line in C, unlike python, you must manually add `\n` to it to print on a new line.

```c
printf("This won't print a new line!")
printf("This one will!\n")
```