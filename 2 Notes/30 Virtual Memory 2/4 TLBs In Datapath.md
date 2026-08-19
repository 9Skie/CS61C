Now, how does this actually come into the 5 pipeline? It's not complicated really, the TLB only comes into play when we need to access memory, that is, when we are fetching instruction from memory, or accessing memory for read/write later on.

![[Screenshot 2026-08-10 at 11.04.47 PM.jpg|500]]

In finality, the TLB look up process is where it all begins, if the translation is found in the TLB, this is called a **TLB hit**. The CPU immediately gets the physical address and then performs a protection check. The protection check verifies whether the operation is allowed, if the access is permitted, the CPU continues normally.

However, if the TLB does not contain the translation, this is called a **TLB miss**. The CPU must now perform a **page table walk**, where the hardware page table walker searches the page table to find the virtual page's corresponding physical frame.

During the page table walk, there are two possibilities. 
- If the page exists in physical memory (DRAM), the hardware obtains the physical frame number, updates the TLB with this new translation, and continues the memory access.
- If the page table shows that the page is not currently in DRAM, a **page fault** occurs. This means the virtual page exists, but its data has been moved to disk. The operating system must load the page from disk into DRAM, then update the page table and TLB.

![[Screenshot 2026-08-10 at 11.09.45 PM.jpg|500]]
