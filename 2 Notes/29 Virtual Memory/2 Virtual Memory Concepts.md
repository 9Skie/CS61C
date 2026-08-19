The core idea of virtual memory is: a program uses **virtual addresses**, and those addresses are mapped to physical RAM by the OS and hardware. Each process operates in its own **virtual address space**, and the OS together with hardware translates these virtual addresses into actual **physical memory addresses**.

- **Virtual memory** refers to the addresses that a process sees and uses. These addresses are relative to that process's own address space. 
    
- **Physical memory** refers to the actual addresses in the computer's hardware, specifically the locations in RAM. These are the real memory locations where data is stored.

As we know from operating systems, a computer is not running only one program. Multiple processes exist at the same time, and the OS manages switching between them while keeping them isolated from each other.

The OS maintains a mapping between the two:

```text
Process A:
Virtual address 0x1000
        ↓
Physical address 0x5000


Process B:
Virtual address 0x1000
        ↓
Physical address 0x9000
```

Both processes believe they are accessing address `0x1000`, but the OS maps them to different physical locations, providing memory isolation and allowing multiple programs to safely share the same machine

![[Screenshot 2026-08-10 at 11.58.08 AM.jpg|500]]