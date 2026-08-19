The **Translation Lookaside Buffer (TLB)** is a hardware cache that stores recent virtual address to physical address translations.

Every time the CPU accesses memory, it first needs to translate the virtual address into a physical address.

However, the page table itself is stored in DRAM. This creates a problem: before accessing the actual data, we need to access memory once just to find the translation. Without a TLB, one memory access becomes:

```text
CPU wants data
      |
      ↓
Look up page table in DRAM
      |
      ↓
Get physical frame number
      |
      ↓
Access actual data in DRAM
```

So one memory access becomes two memory accesses, this drastically slows down our memory access speeds. The TLB solves this by keeping a small cache of recent page table entries inside the CPU, basically cache but only exclusively for page tables.

The TLB stores entries like:

```text
+----------------+----------------+
| Virtual Page   | Physical Frame |
+----------------+----------------+
| Page 5         | Frame 12       |
| Page 8         | Frame 20       |
| Page 10        | Frame 3        |
+----------------+----------------+
```

When the CPU receives a virtual address, it first checks the TLB. 

If the virtual page is already in the TLB, we immediately know the physical frame, this is called a **TLB hit**. If the translation is not in the TLB, this is a **TLB miss**. The CPU then has to walk the page table and do that double memory access thing, very similar to a cache miss.

So in conclusion, CPU first requests virtual addresses to the TLB, which if it's a hit, the physical address is then checked with the cache to see if there's a hit, if the TLB has a miss, we then go to main memory's page table to get the mapping.

![[Screenshot 2026-08-10 at 4.12.25 PM.jpg]]


