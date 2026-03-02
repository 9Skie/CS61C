If you recall somewhat from Nand2Tetris, a typical program's memory looks something like this:

```
-------------------
Stack              ← local variables, stack frames
-------------------
Heap               ← malloc/free
-------------------
Static Data        ← globals, static variables
-------------------
Text               ← program instructions
```

In C, the lifetime of a variable depends on where it lives in this memory:

| **Variable Type**      | **Lifetime**      | **Memory Region** |
| ---------------------- | ----------------- | ----------------- |
| Local (int y)          | Function duration | Stack             |
| Global (int x)         | Entire program    | Data segment      |
| static inside function | Entire program    | Data segment      |
| malloc memory          | Until freed       | Heap              |

And we can see a perfect example of that in our function of:

```c
int sumSquare(int x, int y) {
	return mult(x,x) + y
	}
```

Assume we currently have x living in a0, and y living in a1.

```
addi sp, sp, -8   # make space for values on stack
sw ra, 4(sp)      # save the return address on stack
sw a1, 0(sp)      # save y on stack

mv a1, a0         # copy value of x to a1
jal mult          # call jal over to the mult function


# at this point, we've returned from mult, so sp is at y in memory
lw a1, 0(sp)      # get the value of y from the stack
add a0, a0, a1
lw ra, 4(sp)      # get the return address from stack
addi sp, sp, 8    # return the stack pointer to before
```

Now, where is this stack in memory usually? The stack starts near the highest addresses of the process’s address space and grows downward toward lower addresses (that's just RISC-V...)

I'll just bring out the image again:

```
-------------------
Stack              ← 0xfffffff0
-------------------
Heap               ← not fixed as amount of static data varies
-------------------
Static Data        ← 0x10000000
-------------------
Text               ← 0x00010000
-------------------
Reserved           ← 0x00000000
```

![[Screenshot 2026-02-20 at 9.30.16 PM.png|500]]