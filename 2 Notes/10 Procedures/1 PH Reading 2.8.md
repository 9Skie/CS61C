As we've already saw the steps required for calling a function in assembly, we won't repeat ourselves here again.

The TLDR is, you need to prepare all the arguments the function needs, jump to the function's code and execute it, them jump back to where you came from before the jump.

To jump to the function's code, and keep a copy of where to return, we use the `jal` (jump and link) instruction

```
jal x1, ProcedureAddress
```

This means to: jump to ProcedureAddress and write return address to x1.
- recall x1 is also ra, short for 'return address'
- return address is the address of this instruction + 4, in other words program counter + 4

To return from the function's code to the stored address of where to returns is through the `jalr` (jump and link register) instruction.

```
jalr x0, 0(x1)
```

This means to: jump to the address stored inside register x1.
- the processor sets the program counter (PC) to the value inside x1
- since the destination register is x0, no new return address is saved, as x0 is always 0

---

Let's see how this jumping would work in a function calling series of steps:

```
main -> A -> main
```

In this case, jumping is simple.

```
main:
	# load arguments
    jal  ra, A              # call A
    # continue execution after return
```

```
A
	# do something
	jalr x0, 0(ra)          # return
```

And then main resumes execution.



If we made this process a bit more complex...

```
main -> A -> B -> A -> main
```

The logic of jumping is still the same, just remember, a callee function can only return to it's caller function.
`
```
main:
    # load arguments for A
    jal  ra, A              # call A
    # execution resumes here after A returns
```

```
A:
    addi sp, sp, -8         # allocate stack space (8 bytes for ra)
    sw   ra, 0(sp)          # save return address (back to main)
    
    # do something
    # load arguments for B
    jal  ra, B              # call B
    
    # there's more code below

```

```
B:
    # do something
    jalr x0, 0(ra)          # return to A
```

```
A:
	# following the code above
	lw   ra, 0(sp)          # restore return address (back to main)
    addi sp, sp, 8          # deallocate stack space

    jalr x0, 0(ra)          # return to main
```

As you can see from this more complicated example, we had to introduce a few more concepts:
- callers and calleees
- a stack


What's a caller & callee? Well...

A caller is the program that provides necessary parameter values and 'calls' another program

A callee is the program that got 'called', and it executes a series of stored instructions based on the parameters provided by the caller, then returns back to the caller


What's a stack? Well...

Because RISC-V only has 32 registers, and because:
- a function may need many intermediate values
- nested function calls require saving multiple return addresses

There's no way there's enough space to store all those numbers, so we need a structured way to store additional data in memory, the stack.

Each function call creates a **stack frame**, which is just a chunk of memory reserved by subtracting from sp. When the function finishes, that memory is released by adding back to sp.

It's still a bit abstract, and the book gave 2 really good examples of this in the book.


---
## Compiling a C Procedure That Doesn’t Call Another Procedure

```c
long long int leaf_example(long long int g,
                           long long int h,
                           long long int i,
                           long long int j)
{
    long long int f;
    f = (g + h) - (i + j);
    return f;
}
```

The parameter variables g, h, i, and j correspond to the argument registers x10, x11, x12, and x13, and f corresponds to x20.

And then after calculation, we can need to store the intermediate calculation values in other registers, x5, x6, and x20.

However, as x5, x6, x20 are callee-saved registers (an s register), according to the RISC-V calling convention, if a function modifies a callee-saved register, it must restore it before returning. 

That means before writing into x20, the function must first save its old value somewhere, which is in the stack.

So at the beginning of the function, space is created on the stack to put those values, then after the execution of the function, the values are put back, and the stack pointer returns to it's original position.

As you can see, we had to make space in the stack to store those values.

![[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy) 3.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy).pdf#page=223&rect=99,367,522,602|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface (David A. Patterson, John L. Hennessy), p.223]]


This is the assembly code:

```
leaf_example:

	// allocate space in stack, save registor values
    addi sp, sp, -24        # allocate 3 * 8 bytes
    sd   x5, 16(sp)         # save t0 (x5)   [not strictly required]
    sd   x6,  8(sp)         # save t1 (x6)   [not strictly required]
    sd   x20, 0(sp)         # save s4 (x20)  [required if we modify x20]

    add  x5, x10, x11       # x5 = g + h
    add  x6, x12, x13       # x6 = i + j
    sub  x20, x5, x6        # f  = (g+h) - (i+j)

    addi x10, x20, 0        # return value in a0

	// restore values in stack, increment stack pointer
    ld   x20, 0(sp)         # restore s4
    ld   x6,  8(sp)         # restore t1 (optional)
    ld   x5, 16(sp)         # restore t0 (optional)
    addi sp, sp, 24         # pop stack frame

    jalr x0, 0(x1)          # return
```

---
## Compiling a Recursive C Procedure, Showing Nested Procedure Linking

Here we have a function that recursively calls itself:

```c
long long fact(long long n) {
    if (n < 1) return 1;
    else return n * fact(n-1);
}
```

We will put the value of n at register x10, and save the return address in x1 (ra). And then we will subtract 1 from n and put in in x5, and then have a conditional branching logic to see if n is bigger 0 or not.

If n is less then 1, `fact` returns 1 and goes back to the return address. If not, we should jump to the recursive function in L1, decrement x10 by 1, and perform the recursive case, where `fact` is called again.

```
fact:

	// allocating space in stack and having return addresses
    addi sp, sp, -16      # allocate stack space
    sd   x1, 8(sp)        # save return address (ra)
    sd   x10, 0(sp)       # save n

    addi x5, x10, -1      # x5 = n - 1
    bge  x5, x0, L1       # if n >= 1, go do recursion

    addi x10, x0, 1       # base case: return 1
    addi sp, sp, 16       # pop stack frame
    jalr x0, 0(x1)        # return

L1:
    addi x10, x10, -1     # a0 = n-1
    jal  x1, fact         # call fact(n-1), RECURSION

    addi x6, x10, 0       # x6 = result of fact(n-1)

	// again restoring values in stack and incrementing stack pointer
    ld   x10, 0(sp)       # restore original n
    ld   x1, 8(sp)        # restore original return address
    addi sp, sp, 16       # pop stack frame

    mul  x10, x10, x6     # a0 = n * fact(n-1)
    jalr x0, 0(x1)        # return
```

---

How come there's still more in this chapter...? I don't think I understand the stack.