Pointers can be used to access arrays as well, as an array in C is just a collection of values sitting one after another in memory.

```c
int myNumbers[4] = {25, 50, 75, 100};  
int i;  
  
for (i = 0; i < 4; i++) {  
  printf("%p\n", &myNumbers[i]);  
}
```

This would result in something alike:

```c
0x7ffe70f9d8f0  
0x7ffe70f9d8f4  
0x7ffe70f9d8f8  
0x7ffe70f9d8fc
```

The last number of each of the elements' memory address is different, with an addition of 4. It is because the size of an `int` type is typically 4 bytes.

![[Pasted image 20260208102540.png|500]]

---
## Pointer Arithmetic Under The hood

So, as we saw that as array elements are stored next to each other in memory, and fundamentally pointers are still just a value, like an integer.

So we can increment pointers to also change the element which it is pointing to in an array.

And C is not stupid to the point which, if you increment the pointer by 1, it doesn't know that you want to access the next element in the array.

```c
int myNumbers[4] = {25, 50, 75, 100};  
int *p = myNumbers;  // points to myNumbers[0]  
  
printf("%d\n", *p);       // 25  
printf("%d\n", *(p + 1)); // 50  
printf("%d\n", *(p + 2)); // 75  
printf("%d\n", *(p + 3)); // 100
```

And so, this means we can loop through arrays through pointers as well.

```c
int myNumbers[4] = {25, 50, 75, 100};  
int *p = myNumbers;    // start of array  
  
for (int i = 0; i < 4; i++) {  
  printf("%d\n", *p);  
  p++; // move to next element by changing the pointer's value
}
```

Did you think you had to increment the point by the literal number of bytes a value takes up in the array? 

C's smart enough for that, but do remind yourself that the pointer does move forward by that many bytes.

For example:
- An `int*` pointer moves by the size of an integer (usually 4 bytes).
- A `char*` pointer moves by the size of a character (1 byte).

So if both pointers start at memory address `1000`:
- `int*` → `p + 1` would move to address `1004`
- `char*` → `p + 1` would move to address `1001`

```c
int myNumbers[2] = {1, 2};  
char letters[] = "Hi"; // 'H', 'i', '\0'  
  
int *pi = myNumbers; // int pointer  
char *pc = letters; // char pointer  
  
printf("%p\n", (void*)pi);  
printf("%p\n", (void*)(pi + 1)); // moves by sizeof(int) (4 bytes)   
  
printf("%p\n", (void*)pc);  
printf("%p\n", (void*)(pc + 1)); // moves by 1 byte
```
