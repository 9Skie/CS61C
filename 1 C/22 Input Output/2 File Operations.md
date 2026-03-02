## Opening Files

In C, you can create, open, read, and write to files by declaring a [pointer](https://www.w3schools.com/c/c_pointers.php) of type `FILE`, and use the `fopen()` function:

```c
FILE *fptr;  
fptr = fopen(filename, mode);
```

| Parameter  | Description                                                                                                                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| _filename_ | The name of the actual file you want to open (or create), like `filename.txt`                                                                                                                    |
| _mode_     | A single character, which represents what you want to do with the file (read, write or append):<br><br>`w` - Writes to a file  <br>`a` - Appends new data to a file  <br>`r` - Reads from a file |

The filename isn't really a filename... it's where the file is relative to the computer (or absolute path if you wish)

```c
FILE *fptr;  
fptr = fopen("C:\\directoryname\\filename.txt", "r");
```

Modes matter for opening the file, for text files, we can pick these modes to operate the file on.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 23.jpg|500]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=573&rect=234,225,479,312&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.544]]


For binary files, we have to explicitly tell C the file is in a binary format with the `b` character on top of all these modes.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 24.jpg|500]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=574&rect=218,579,508,670&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.545]]

---
## Closing Files

The `fclose` function allows a program to close a file that it’s no longer using.

```c
FILE *fptr;  
  
// Open a file  
fptr = fopen("filename.txt", "r");  
  
// Close the file  
fclose(fptr);
```

---
## Creating & Writing Files

To create a file, you can use the `w` mode inside the `fopen()` function.

The `w` mode is used to write to a file. **However**, if the file does not exist, it will create one for you:

```c
FILE *fptr;  
  
// Create a file  
fptr = fopen("filename.txt", "w");  
  
// Close the file  
fclose(fptr);
```

As you can see as well, if the file exists, we can write to it instead.

Let's use the `w` mode from the previous chapter again, and write something to the file we just created.

The `w` mode means that the file is opened for **writing**. To insert content to it, you can use the `fprintf()` function and add the pointer variable (`fptr` in our example) and some text:

```c
FILE *fptr;  
  
// Open a file in writing mode  
fptr = fopen("filename.txt", "w");  
  
// Write some text to the file  
fprintf(fptr, "Some text");  
  
// Close the file  
fclose(fptr);
```

However, if there was a file with contents in it, doing the above operation would just overwrite it.

---
## Append to File

If you want to add content to a file without deleting the old content, you can use the `a` mode.

The `a` mode appends content at the end of the file:

```c
FILE *fptr;  
  
// Open a file in append mode  
fptr = fopen("filename.txt", "a");  
  
// Append some text to the file  
fprintf(fptr, "\nHi everybody!");  
  
// Close the file  
fclose(fptr);
```

As you can see, we had to add the `\n` (new line character) at the front so the test actually goes to a new line.

---
## So... What is a File?

A `FILE` data type in C actually is just a struct.

```c
typedef struct {
    int cnt;       // characters left in buffer
    char *ptr;     // next character in the buffer
    char *base;    // location of buffer
    int mode;      // mode of file access
    int fileno;    // file descriptor
} FILE;
```

This is essentially a simplified version of what <stdio.h> internally uses to implement file streams.