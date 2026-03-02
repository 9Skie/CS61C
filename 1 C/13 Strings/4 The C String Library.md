C has a lot of built in functions that operate on strings.

## Common string functions (<string.h>)

### **Length**

```c
strlen(s);
```

- Returns number of characters **excluding** '\0'

### **Copy**

```c
strncpy(dest, src, n);
```

### **Concatenate**

```
strncat(dest, src, n);
```

### **Compare**

```c
strcmp(a, b);     // returns the number of differences between the strings
strncmp(a, b, n); // return the number of differences in the first n characters of the string
```

---

## Character functions (<ctype.h>)

These operate on **single characters**, not strings.

### **To upper / lower**

```c
toupper(c); // 'a' -> 'A'
tolower(c); // 'A' -> 'a'
```

Example:

```c
char c = 'a';
c = toupper(c);   // 'A'
```

### **Apply to a whole string**

```c
for (int i = 0; s[i] != '\0'; i++)
    s[i] = toupper(s[i]);
```

---
## Converting a char to an int

### **If the char is a digit**

```c
char c = '7';
int x = c - '0';   // x == 7
```

This works because digits are contiguous in ASCII.

### **If you have a string number**

```c
int x = atoi("123");      // simple, no error checking
```