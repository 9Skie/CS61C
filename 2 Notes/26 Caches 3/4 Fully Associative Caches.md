Before, with a direct-mapped cache, there was a fixed relationship between main-memory blocks and cache lines. For example, with 4 cache lines:

```text
Memory blocks 0, 4, 8, 12, ... → cache line 0
Memory blocks 1, 5, 9, 13, ... → cache line 1
Memory blocks 2, 6, 10, 14, ... → cache line 2
Memory blocks 3, 7, 11, 15, ... → cache line 3
```

This means different memory blocks can be forced to compete for the same cache line, even if other cache lines are currently unused. These are **conflict misses**.

But what if we removed this fixed mapping entirely? With a **fully associative cache**, any memory block can be placed in any cache line.

So if we have 4 cache lines, we might access memory block `0` and place it in line `0`, then access memory block `3` and place it in line `1`, then access memory block `17` and place it in line `2`:

```text
Cache line 0 → memory block 0
Cache line 1 → memory block 3
Cache line 2 → memory block 17
Cache line 3 → empty
```

The important part is that memory block `17` is not forced into some predetermined line. It can use any available cache line.

Because there is no fixed mapping, there is also no longer an **index field** in the address. The address only needs:

```text
+----------------------------+-------------+
| Tag                        | Offset      |
+----------------------------+-------------+
```

The **tag** identifies which memory block we are looking for, while the **offset** selects the specific byte within that block.

The tradeoff is that the cache can no longer use an index to jump directly to one line. Since the requested block could be in any cache line, its tag has to be compared against the tags of all cache lines.

Also, fully associative caches eliminate **conflict misses caused by fixed mapping**, but misses can still happen if the cache is full or if the block has never been loaded before.


