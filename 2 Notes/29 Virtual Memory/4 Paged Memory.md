As we said, every page in virtual memory goes through a memory map to physical memory, or by extension the disk storage.

![[Pasted image 20260810121243.png|500]]

But how does this work in theory? Lets start by looking at a virtual address, it's divided into 2 parts:

Virtual Address (32 bits)

```text
+----------------------+----------------+
|     Page Number      |    Offset      |
|       20 bits        |    12 bits     |
+----------------------+----------------+
```

Virtual memory is divided into fixed-size pieces called **pages**.
- The **page number** tells us **which virtual page** we are accessing.
- The **offset** tells us **where inside that page** the data is located.

In this case, there are 20 page bits, so in total possible $2^20$ pages, and there's 12 offset bits, so each page is $2^12$ bytes.

The virtual address is essentially saying:
> "Go to virtual page X, and then go to byte Y inside that page."

This happens for every process on the computer, and every process has a dedicated page table.

![[Screenshot 2026-08-10 at 12.38.37 PM.jpg|500]]


Now, how does this virtual address get translated into physical address? Physical memory (RAM) is also divided into **physical pages**, usually called **page frames**:

For the basic idea of virtual memory translation, you only need to map the **virtual page number** to the **physical frame number**. The offset does not need to be translated, and is kept over across the translation.


But with this new intermediate step of accessing a page table before being able to access a physical memory address, overhead is added, to speed the process up, we can use cache to store frequently used page table entries.

The entire page table itself is stored in memory, and whenever we are trying to reference any address in the physical memory, we first reference to the page table, then to the actual physical frame.