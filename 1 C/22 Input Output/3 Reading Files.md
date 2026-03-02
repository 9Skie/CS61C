In the previous chapter, we wrote to a file using `w` and `a` modes inside the `fopen()` function.

To **read** from a file, you can use the `r` mode:

```c
FILE *fptr;  
  
// Open a file in read mode  
fptr = fopen("filename.txt", "r");
```

This will make the `filename.txt` opened for reading, but we still need a few steps before we read something out from the file:
-  we need a string that's big enough to store the content of the file in memory
- we need to call a function that actually can go through the file's content


So, let us:

- create a string that can store up to 100 characters (for example)

```c
FILE *fptr;  
  
// Open a file in read mode  
fptr = fopen("filename.txt", "r");  
  
// Store the content of the file  
char myString[100];
```

- use the `fgets()` function to read the file

The `fgets()` function takes three parameters:

```c
fgets(myString, 100, fptr);
```

1. The first parameter specifies where to store the file content, which will be in the `myString` array we just created.
2. The second parameter specifies the maximum size of data to read, which should match the size of `myString` (`100`).
3. The third parameter requires a file pointer that is used to read the file (`fptr` in our example).


So in completion, we can open a file, get an array to store the file's content in memory, read the file's content, and print it out.

```c
FILE *fptr;  
  
// Open a file in read mode  
fptr = fopen("filename.txt", "r");  
  
// Store the content of the file  
char myString[100];  
  
// Read the content and store it inside myString  
fgets(myString, 100, fptr);  
  
// Print the file content  
printf("%s", myString);  
  
// Close the file  
fclose(fptr);
```

---
## Improved Implementation

However, we have the problem that we don't know file sizes, and probably won't be able to load entire files into memory. 

So, what we can do instead is first have a thing called 'buffer', a fixed size array, that temporarily stores data read from the file.

We then repeatedly call `fgets()` inside a loop, each call attempts to fill the buffer with the next portion of the file.

After each read:
- The contents of the buffer are processed (in this case, printed).
- The same buffer is reused for the next read.
- This continues until fgets() returns NULL, indicating the end of the file.

This approach allows us to process files of any size while using only a constant amount of memory.

If a line in the file is longer than the buffer size, it will not fit in a single call to `fgets()`, Instead, that line will be delivered in multiple chunks across multiple iterations of the loop.

Suppose our file looks like this:

```txt
Hello
World
This is a very very long line...
```

To read every line of the file, you can use a while loop:

```c
#include <stdio.h>
#define BUFSZ 8

int main() {
	// Open a file in read mode  
    FILE *fptr = fopen("filename.txt", "r");

	// Store the content of the file  
    char myString[BUFSZ];

	// Read the content and print it  
    while (fgets(myString, BUFSZ, fptr)) {
        printf("Chunk: %s", myString);
    }

	// Close the file  
    fclose(fptr);
    return 0;
}
```

Output will look like:

```
Chunk: Hello\n
Chunk: World\n
Chunk: This is
Chunk:  a very
Chunk:  very l
Chunk: ong lin
Chunk: e...\n
```

---
## Malloc Version

So far, we've used an array as the buffer, but that means that array is allocated automatically when the function begins, and not determined at runtime.

So, instead of asking the compiler to reserve memory automatically, we can ask the operating system for memory while the program is running using `malloc()`

Using malloc here does **not** make the file reading more powerful, it only changes:
- where the buffer is stored
- how long it lives
- who is responsible for freeing it

The logic is exactly the same as above, except we are using `malloc` instead of `array`.

```c
#include <stdio.h>
#include <stdlib.h>

#define BUFSZ 8

int main() {
	// Open file
    FILE *fptr = fopen("filename.txt", "r");

    // Allocate buffer on the heap
    char *myString = malloc(BUFSZ);

    // Read the file chunk by chunk
    while (fgets(myString, BUFSZ, fptr)) {
        printf("Chunk: %s", myString);
    }

    // Free heap memory
    free(myString);

    // Close file
    fclose(fptr);
    return 0;
}
```