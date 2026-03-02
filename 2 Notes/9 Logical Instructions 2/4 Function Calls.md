There are 6 steps in calling a function.

![[Screenshot 2026-02-16 at 5.05.29 PM.png|500]]

And as we remembered from [[3 Machine Program]], there are certain registers in our 32 registers for this purpose.

![[Screenshot 2026-02-16 at 5.16.25 PM.png|500]]

Take this function for example:

```c
int sum(int x, int y) {
	return x + y;
}
```

And we called it in main, with some certain values

```c
int main() {
  int a = 7, b = 5;
  int c = sum(a, b);
  ...
}
```

In following the above idea of how we call a function, it would look something like this in assembly.

```
-------------------------
Caller code (in this case, main)
-------------------------

1000:  li   s0, 7          # a = 7        (pretend a stored in s0)
1004:  li   s1, 5          # b = 5        (pretend b stored in s1)

1008:  mv   a0, s0         # a0 = a       (1st arg x)
1012:  mv   a1, s1         # a1 = b       (2nd arg y)

1016:  jal  ra, 2000       # call sum: ra = 1020, PC = 2000

1020:  mv   s2, a0         # c = return value (save result in s2)
1024:  ...                 # continue main


-------------------------
Function: sum(x, y)
-------------------------

2000:  add  a0, a0, a1     # a0 = x + y   (return value goes in a0)
2004:  jalr x0, 0(ra)      # return       (PC = ra)
```

As you can see, the order of operations went like:

1. Put arguments in a place where functions can access them
	- store the value of a and b in saved registers
	- `1000:  li   s0, 7`
	- `1004:  li   s1, 5 `
	- load the value of a and b in function argument registers
	- `1008:  mv   a0, s0 `
	- `1012:  mv   a1, s1 `

2. transfer control to function
	- jump the program counter to where the function's code is located
	- `1016:  jal  ra, 2000 `

3. Acquire local storage resources needed for function

4. Perform desired task of the function
	- the function executes it's code based on the given values
	- `2000:  add  a0, a0, a1 `

5. Put return value in a place where calling code can access it and restore any registers you used, release local storage

6. the functions jumps the program counter to the return address after it finishes execution
	- `2004:  jalr x0, 0(ra) `


Now, you might be confused why steps 3 and 6 don't have corresponding assembly code in our example, because:

- step 3: no stack is created because the function does not call other functions, use callee-saved registers, or require local storage beyond the argument registers.

- step 5: no stack cleanup or register restoration is needed because the function did not allocate a stack 

