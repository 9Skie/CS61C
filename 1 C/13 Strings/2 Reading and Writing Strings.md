We've already seen a lot in reading and writing strings with `printf` and `scanf`.

But... today we'll introduce 2 more helpful buddies for strings! `puts` and `gets` (This is dead! Do not use)

---
## printf

- Formatted output
- Can print numbers, strings, mixed data
- You control formatting

```c
printf("Hello %s, you are %d\n", name, age);
```

## puts

- String-only output
- Automatically adds a newline
- Simpler, less error-prone

```c
puts("Hello world");
```

Use when:
- You just want to print a string + newline
- No formatting needed

## Quick comparison

|**Feature**|printf|puts|
|---|---|---|
|Formatting|Yes|No|
|Prints non-strings|Yes|No|
|Adds newline|Only if you ask|Always|
|Simplicity|More complex|Very simple|

---
## scanf

- **Formatted input**
- Can read ints, floats, strings, etc.
- Stops reading strings at whitespace

```c
scanf("%d", &x);
scanf("%s", name);
```

**Problems:**
- Easy to misuse
- %s can overflow if you’re careless
- Leaves newlines behind


### fgets

- Reads **an entire line**
- **Keeps spaces**
- Stops at newline or when buffer is full
- **Prevents buffer overflow**
- Stores the newline (\n) if there’s room

```c
char s[50];
fgets(s, sizeof(s), stdin);
```


## Quick Comparison

| **Feature**       | scanf("%s") | fgets  |
| ----------------- | ----------- | ------ |
| Reads spaces      | ❌ No       | ✅ Yes |
| Reads full line   | ❌ No       | ✅ Yes |
| Buffer size known | ❌ No       | ✅ Yes |
| Newline kept      | ❌ No       | ✅ Yes |
| Safe by default   | ❌ Risky    | ✅ Yes |