Going deeper, a page table isn't just a mapping of virtual page to physical frames, the OS also needs additional information about the current state and permissions of that page.

A typical page table entry (PTE) looks more like:

```
+----------------+--------------------------------+
| Physical Frame | Flags                          |
+----------------+--------------------------------+
| Frame Number   | Valid, Read, Write, Execute... |
+----------------+--------------------------------+
```

The physical frame number tells the CPU where the page is currently located in RAM. The flags provide additional information about that page.

For example:

- **Valid bit (present bit):** tells whether this virtual page currently has a mapping to physical memory.
- **Read/Write permissions:** tells whether the program is allowed to modify this page.
- **Execute permission:** tells whether the page can contain executable code.
- **Dirty bit:** tells whether the page has been modified since it was loaded into memory.
- **Reference bit:** tells whether the page has recently been accessed.

A page table entry might look like:

```
Virtual Page 5:

+-----------+-------+----------+
| Frame     | Valid | Flags    |
+-----------+-------+----------+
| Frame 12  |   1   | RW       |
+-----------+-------+----------+
```

This means:
> Virtual page 5 is currently stored in physical frame 12 in RAM, it is readable and writable.


## Page Faults

 When we access memory, we start with a virtual address. The virtual address contains a virtual page number and an offset:

```text
Virtual Address

+----------------+----------+
| Virtual Page   | Offset   |
+----------------+----------+
```

The virtual page number is used to search the page table. The page table contains the corresponding physical frame number and additional flags that describe the state and permissions of that page.

```text
Page Table Entry

+----------------+--------+----------------+
| Physical Frame | Valid  | Permissions    |
+----------------+--------+----------------+
```

At this point, two main things can happen.


First, the page table contains a mapping, and the valid bit is `1`. This means the virtual page is currently loaded into DRAM.

The CPU can now use the physical frame number together with the offset to access the data in memory. The permission flags are checked to make sure the operation is allowed.


The second case is that the page table entry exists, but the valid bit is `0`. This means the virtual page exists, but it is not currently in DRAM. Instead, its contents have been moved to disk.

Since there is no physical frame currently assigned, the CPU cannot continue the memory access. This causes a **page fault**, and the OS takes over. 

The OS then needs to bring the page back into DRAM and allocate a physical frame to it. If DRAM has no free space, the OS must first evict another page from DRAM. It chooses a page based on some replacement policy, writes it back to disk if necessary, and then loads the required page into the newly freed frame.