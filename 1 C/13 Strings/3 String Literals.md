A string literal is just a sequence of characters, enclosed in double quotes in C.

We first encountered string literals in Chapter 2; they often appear as format strings in calls of `printf` and `scanf`.

But they by default actually don't exist in C! Isn't that crazy? You have to make a string from a *list of chars*.

```c
char greetings[] = "Hello World!";
```

The length of the list is automatically determined based on the number of characters you inputted, you don't have to specify it's length by defalut.

And as you expect, the string input must be wrapped around in `"`, and outputting the string in it's entirety isn't like iterating through a list, but rather with another special format specifier `%s`, short for string.
- If they already included this, why cant they make a string data type...?

```c
char greetings[] = "Hello World!";  
printf("%s", greetings);
```

But if you try to access an individual character in it, we go back to printing in `%c`.

```c
char greetings[] = "Hello World!";  
printf("%c", greetings[0])
```

---
## How String Literals Are Stored

As we just saw, string literals are a list of chars, to distinguish a string literal from another in memory, a special character, the _null character_ marks the end of a string, `\0`.

For example, this is the string literal 'abc' in memory.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 9.jpg|300]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=308&rect=319,343,409,380|C Programming A Modern Approach (K. N. King) (Z-Library), p.279]]

---
## Operating on String Literals

And as a string literal is just a list, we know how to go through them, open up elements in them, get pointers in them... it's all the same.

