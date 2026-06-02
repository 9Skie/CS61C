Honestly, the assembler was a heck ton of stuff, and the goal of a linker is just to take all the O files (object code) and turn them into a single executable.

Each O file is divided into 3 parts, it's text, it's data, and it's info (symbol table, relocation table)

![[Screenshot 2026-03-03 at 4.40.23 PM.png|500]]

The big idea is that:

1. all the text segments from each .o file gets put together
2. all the data segment from each .o file gets put goether with other text segments
3. resolve references by going through all relocation tables and filling in absolute addresses

There are **four common ways instructions refer to addresses**, and the key question is: _does the linker need to fix them later?_

- **PC-Relative Addressing** _(beq, bne, jal; auipc/addi)_
    - Never need to relocate (PIC: Position-Independent Code)

- **Absolute Function Address** _(auipc/jalr)_
    - Always relocate

- **External Function Reference** _(auipc/jalr)_
    - Always relocate

- **Static Data Reference** _(often lui/addi)_
    - Always relocate

---

## Solving References

The linker knows the **length and ordering of all text and data segments** from every object file. Using this information, it can determine the **final memory layout of the program**. Once the layout is known, the linker can compute the **absolute addresses of all labels and data** that instructions reference.

To resolve references, the linker first searches for the symbol (a label or piece of data) in the **symbol tables of the user’s object files**. If the symbol is not found there, it then searches **library files** (for example, when resolving a call to printf). 

Once the correct address of the symbol is determined, the linker **updates the machine code using the relocation table** so that each instruction points to the correct location. Finally, the linker outputs a **single executable file** containing the combined text and data segments (along with a header).


Let’s walk through a **very small concrete example** of what the linker is doing.


File 1:  main.c

```
int add(int a, int b);

int main() {
    return add(2, 3);
}
```


File 2: add.c

```
int add(int a, int b) {
    return a + b;
}
```


**Step 1 — Compilation / Assembly**

Each file becomes its **own object file**.

```
main.c  →  main.o
add.c   →  add.o
```

Inside **main.o**, there will be something like:

```
call add
```

But the assembler **does not know where add lives yet**, because it is defined in another file.

So the assembler:
- leaves a **placeholder** for the address
- records an entry in the **relocation table**


**Step 2 — Linking**

The linker now receives:

```
main.o
add.o
```

From their symbol tables it learns:

```
add → defined in add.o
main → defined in main.o
```

The linker also knows:
- how long each .text section is
- where each one will be placed in memory

Example layout:

```
0x10000  main code
0x10040  add code
```

Now the linker can determine:

```
add = 0x10040
```


**Step 3 — Resolving the reference**

The linker goes to the relocation entry that said:

```
Instruction in main.o needs address of add
```

It replaces the placeholder with:

```
0x10040
```

Now the instruction in the final executable correctly jumps to add.

---

## Static vs Dynamic Linking

Everything described so far corresponds to **static linking**, where all code and data from the program and any libraries it uses are copied together into a single executable file.

In this model, the linker resolves all symbol references at build time, producing a self-contained program. If any part of the program changes, the affected source files must be recompiled and the program must be relinked to produce a new executable.

One consequence of static linking is that the executable can grow very large, since every library used by the program is copied directly into the binary. If many programs use the same libraries, each program will contain its own separate copy of that library code.

To address this, **dynamic linking** allows programs to reference shared libraries instead of embedding them directly into the executable. The executable records its dependency on these libraries, and the actual library code is loaded at runtime by the system’s loader.


Now, there are tradeoffs to DLL.

When programs use **shared libraries** (for example libxyz.so), the library code is **not copied into every executable**. Instead, the executable only records that it depends on that library. At runtime, the loader loads the shared library once and multiple programs can use it.

This leads to three advantages:
- **Less disk space**: executables are smaller because they do not contain the library code.
- **Less RAM usage**: if two programs both use the same library, the operating system can load **one copy of the library into memory** and both programs share it.


The downside is the line on the slide: “At runtime, there’s time overhead to do link.”

This means that when the program starts, the system must:
1. Locate the shared libraries
2. Load them into memory
3. Resolve symbol references (like printf)

This takes a small amount of extra time compared to a statically linked executable that already contains everything.