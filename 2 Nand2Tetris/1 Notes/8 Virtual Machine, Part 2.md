In this chapter, we will be continuing developing the virtual machine, seeing how it can support functions, the calling of functions, passing parameters into functions, recursion of functions... so this will be a rather difficult task.

Take a mathematical expression for example:

$x = -b + \sqrt{b^2 - 4ac}$

From a programmer's perspective, this can be rewritten as:

```
x = -b + sqrt(power(b, 2) - 4*a*c)
```

Which means calling in functions like `sqrt` and `power`, and passing in parameters to these functions, you can tie it together with conditionals or whatever too, and they can be layered on top of one another however much we like.

In general, functions work like such:

- the calling function (*caller*) passes arguments to the called function (*callee*)
- the caller is suspended until the callee finishes execution
- the caller takes the returned values from the callee and finishes execution

Anddd this is super duper annoying at the low level:

- Temporarily save the address which the caller's execution will return to after the callee is finished (*return address*)
- Temporarily save the current memory resources the caller uses
- Allocate needed resources, and pass in arguments to the callee
- When callee is finished, go back to caller's code through return address

The TDLR is, the caller "freezes" and lets the callee runs, and when the callee is done it "unfreezes" the caller, and the caller continues running, which is done in the following steps.

- Make the callee's return value available to the caller's code
- Remove the callee’s stack and register usage (known as recycling)
- Retrieve the saved memory resources of the caller
- Retrieve the saved return address of the caller
- Resume executing caller's code from return address

## Branching

Normally, we usually define functions at the top of a file and call them when needed in our main program, and so for functions to exist, a program must support branching, since a computer executes instructions sequentially by default from the first instruction to the last.

We saw branching in assembly code already, with labels and pointers we can achieve effects like if statements and for loops.

In the VM, branching is done with these 2 commands:

- `goto symbol` - unconditional branching, jump to the command after `symbol` in stack and keep execution
- `if-goto symbol` -conditional branching, pop off top value from stack, if it's not false, jump to the command after `symbol` and keep execution, else continue next command in stack

This is an example of a while loop in VM branching:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 53.jpg|400]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=209&rect=120,168,510,509|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.209]]

## Functions

Just like how $x + y$ can be written as this on the stack:

```
push x
push y
add
```

A custom function, power, acts similarly on the stack too, say $(x + y)^2$:

```
push x
push y
add
call power
```

The only real difference is that a `call` needs to be made to the function, and the function must be defined in the VM byte code before it can be called, as the following example of calculating $\sqrt{x^2 + y^2}$ :

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 54.jpg|300]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=212&rect=256,467,451,736|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.212]]

As a program runs, function calls form a calling chain.

Initially, the chain contains a single function (for example, main). When main calls another function, and that function calls another, the chain grows. Each function in the chain waits for the function it called to return, so only the last function in the chain, the current function, is actively executing.

Although all functions share a single global stack, each function call creates its own stack frame, a dedicated region of the stack used to store that function’s local variables and temporary values. When a function calls another function, a new stack frame is pushed on top of the stack. When the function returns, its frame is removed, and execution resumes in the caller.

It's best to understand this through an example.

We start with the main function.

```
| main's locals |
| main's temps  |
+---------------+
```

Now, main calls another function foo, and a new frame is pushed on top.

```
| foo's locals |
| foo's temps  |
|--------------|
| main's locals|
| main's temps |
+--------------+
```

Say foo calls another function, bar, a new frame is again added.

```
| bar's locals |
| bar's temps  |
|--------------|
| foo's locals |
| foo's temps  |
|--------------|
| main's locals|
| main's temps |
+--------------+
```

And now bar finishes operation, it's frame will be deleted.

```
|     DONE     |
|--------------|
| foo's locals |
| foo's temps  |
|--------------|
| main's locals|
| main's temps |
+--------------+
```

Because each function accesses locals relative to its own frame, different functions can safely store values on the same stack without interfering with one another.

So, we have like... a stack of stacks? Where each function is allowed to operate on it's own local stack on our global stack.

## WARNING! THE BELOW NOTES ARE NOT SORTED CORRECTLY!

In order to properly create a *frame* for a function (local stack), this is where the set of pointers: `LCL`, `ARG`, `THIS`, `THAT` comes into play, this image shows the details:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 55.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=214&rect=126,134,492,437|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.214]]

We can see a direct example of how stack frames are used with this recursive example of a factorial function.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 56.jpg|400]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=217&rect=138,482,496,732|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.217]]

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 57.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=217&rect=111,299,502,476|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.217]]

With the idea of frames, we can see how values of functions are stored while waiting for deeper calls to return. Each frame stores the function’s local variables and state, allowing multiple active calls to coexist safely on the same global stack. As calls return, their frames are removed in reverse order, and the saved values are restored.

### VM Specifications

Again, that was a load dump of theory without explicit saying stuff about syntax, and so here is the syntax for branching and load.

### Branching

- `label`: labels the current location in the function's code, only labeled locations can be jumped to, and is only accessible inside the function
- `goto label`: uncoditionally jump to the label inside the function
- `if goto label`: conditionally jump to the label inside the function, by popping the top value of the stack and checking if it is 0

### Functions

Ah, the actual syntax in the nand2tetris vm differs from the examples of functions we've seen above, for some reason, follow this syntax please.

- `function functionName nVars`, basically a function's name and how many variables are allowed in the function.
	- like `function Recursion 1`, would mean the name of the function is `Recursion`, and it takes in `1` variables.
- `call functionName nArgs`, similar idea, calling a function by it's name and indicating that there are `nArgs` pushed onto the stack ready to be used as arguments for input.
- `return`, this... doesn't actually return anything by itself! What usually happens is the values that are needed to be returned are sitting at the top of the stack, waiting to be operated on.
	- The TLDR is just that this terminates the function being run right now

The book has pointed out the responsibility of the VM implementation needed for the caller function, and callee function.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 58.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=222&rect=70,251,547,600|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.222]]

And the book, right after gave the details of how a function's calling, definition, and return is (logically) translated in assembly code.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 59.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=223&rect=130,355,484,662|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.223]]

### Compilation for Multiple Files

This is a pretty wild part, but the book wants us to extend the capabilities of our VM translator from 1 file to multiple files.

Well, in real-world software development, programs are usually split across multiple source files. Each file groups related functionality, and functions defined in one file can be called from another. This modular structure exists mainly to help humans organize and maintain code.

During compilation, however, these files do not execute independently. Each source file is compiled into an intermediate form, and all of them are then linked together into a single executable program. At runtime, the computer runs only this one executable, with all functions sharing the same address space.

The book asks us to reproduce this idea in a simplified way, the VM translator will directly merge all VM files in a folder into one assembly file, skipping the separate compilation and linking.

Because all VM files are merged, the resulting assembly program has a single global namespace. At the assembly level, function abstractions no longer exist—there are only labels and jump instructions, and every label must be unique.

## Design Suggestions

As we recall in chapter 7, we've designed the VMTranslator, Parser, and CodeWriter, this part will lay out some suggestions to add the functionalities needed to support translating functions.

### VMTranslator

For a single file's translation, it should look similar to the one we built in chapter 7.

For a folders' file's translation, it should create a Parser for each individual vm file, and 1 Codewriter to writing to the final asm file, the VMTranslator needs to inform the CodeWriter for each new vm file being processed.

### Parser

Implementation doesn't change

### Code Writer

Welp, now we need to do allllllll the additional work with functions! Here's the full table of what it should be capable of doing.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 60.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=228&rect=62,159,559,740|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.228]]
