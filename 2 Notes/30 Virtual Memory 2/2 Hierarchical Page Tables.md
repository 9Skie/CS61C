Now that we understand how a basic page table works, we are now at another concern: size.

Assume we have:
- 20 bits for the virtual page size -> $2^20$ possible pages
- 4 bytes per address (32 bit computer)

Then, for 1 process, it will maximumly have a page table size of:

 $\text{Page Table Size} = (\text{number of entries}) \times (\text{size of each entry})$
 $= 2^{20} \times 4 \text{ bytes}$
$= 4 \times 2^{20} \text{ bytes}$
$= 4 \text{ MiB}$

Now consider a number of processes, like 100, we will realize the page table size quickly grows out of hand.

$\text{Total Page Table Size} = (\text{number of processes}) \times (\text{page table size per process})$
$= 100 \times 4 \text{ MiB}$
$= 400 \text{ MiB}$

The problem with a single-level page table is that the virtual address space is usually much larger than the memory a process actually uses.

This clearly isn't very reasonable for our processes, as keeping track of memory addresses is filling up our memory, that's ridiculous! So what solutions do we have for this?

We instead take a Hierarchical Page Table approach, basically splitting the table as a tree like data structure, so nstead of having one giant page table:

```text
Virtual Page Number
        |
        ↓
+----------------+
| Single Page    |
| Table          |
+----------------+
        |
        ↓
Physical Frames
```

we split the page table into multiple levels. The virtual page number is divided into smaller pieces:

```text
Virtual Address

+----------+----------+----------+
|    P1    |    P2    | Offset   |
+----------+----------+----------+
| Level 1  | Level 2  |          |
| Index    | Index    |          |
+----------+----------+----------+
```

The first part (`P1`) indexes into the first-level page table. The entry in this table does not directly point to a physical page. Instead, it points to a second-level page table.

The second part (`P2`) then indexes into that second-level page table, which finally contains the mapping to the physical frame.

There is 4 parts in 64 bit address spaces.

![[Pasted image 20260810154014.png|500]]

In our case, the p1 address is 10 bit long, and the p2 address is also 10 bit long.

![[Screenshot 2026-08-10 at 3.45.37 PM.jpg|500]]

A hierarchical page table saves memory by only creating page table structures for the parts of the virtual address space that a process actually uses. It trades slightly more complex translation for much lower memory overhead.






You're right. The explanation should be written as a continuous concept. Let me rewrite it closer to your style.

---

The problem with a single-level page table is that the **virtual address space is usually much larger than the memory a process actually uses**.

For example, with a 32-bit virtual address:

```text
Virtual Address

+----------------------+------------+
| Page Number          | Offset     |
| 20 bits              | 12 bits    |
+----------------------+------------+
```

The page number has 20 bits, meaning there are:

$2^{20}$

possible virtual pages.

If each page table entry is 4 bytes, then the page table needs:

$2^{20} \times 4 \text{ bytes}=4\text{ MiB}$

for a single process.

The issue is that a process usually does not use all $2^{20}$ pages. For example, a small program might only use a few thousand pages, but the single-level page table still needs to reserve an entry for every possible virtual page.

So the idea of a **hierarchical page table** is to avoid creating page table entries for unused parts of the virtual address space.






```text
Virtual Address

        P1          P2        Offset
         |           |            |
         ↓           |            |

+--------------+    |            |
| Level 1      |    |            |
| Page Table   |    |            |
+--------------+    |            |
         |          |            |
         ↓          |            |
+--------------+ ←--             |
| Level 2      |                 |
| Page Table   |                 |
+--------------+                 |
         |                       |
         ↓                       ↓

Physical Frame + Offset
```

The important advantage is that the OS only creates level 2 page tables for regions of memory that are actually being used.

For example, suppose a program only uses two small areas of its virtual address space:

```text
Virtual Address Space

0x00000000
     |
     |  used
     |
0x00100000


0x80000000
     |
     |  used
     |
0x80100000
```

A single-level page table would need entries covering the entire address space.

A hierarchical page table only creates the necessary pieces:

```text
Level 1 Page Table

+---------+
| Entry 0 | ----> Level 2 Table ----> Actual pages
+---------+
| Empty   |
+---------+
| Empty   |
+---------+
| Entry 2 | ----> Level 2 Table ----> Actual pages
+---------+
```

The unused regions do not require page tables at all.

The tradeoff is that address translation requires more steps. A single-level page table needs one lookup, while a hierarchical page table needs multiple lookups:

```text
Single-level:

Virtual Address
       ↓
Page Table
       ↓
Physical Frame


Hierarchical:

Virtual Address
       ↓
Level 1 Page Table
       ↓
Level 2 Page Table
       ↓
Physical Frame
```

However, modern systems use a **TLB (Translation Lookaside Buffer)** to cache recent translations, so most memory accesses do not require walking the entire page table.

The key idea is:

> A hierarchical page table saves memory by only creating page table structures for the parts of the virtual address space that a process actually uses. It trades slightly more complex translation for much lower memory overhead.
