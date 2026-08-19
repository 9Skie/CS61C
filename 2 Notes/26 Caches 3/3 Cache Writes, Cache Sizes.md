All of what previously we've been looking at is reading from cache, and how that makes access faster compared to main memory.

Now instead we'll look at 'writing' into cache, as it's also faster than writing into main memory, but we encounter new issues, which is keeping the cache and main memory consistent.

Originally, we said the cache is just a copy of main memory, which works fine for reads, but no longer for writes. But suppose the processor changes a value and writes the new value only into the cache. The cache now contains the updated value, while main memory still contains the old value. The two copies are no longer consistent.

We could solve this by updating both the cache and main memory every time a write happens, but then we discard the fact that a cache write is much faster than main memory write.


There are two main solutions to this problem: **write-through** and **write-back**.

- write-through**: every cache write is also immediately written to the next level of memory. This keeps the cache and memory consistent, but generates more memory traffic and can make writes slower.

- **write-back**: the processor initially writes only to the cache. The cache marks that block as **dirty**, meaning it has been modified and no longer matches main memory. Main memory is updated only later, when that dirty block is about to be removed from the cache.

---

## Block Sizes

We are now invesitgating another problem (that's quite unrelated), that is, how big should block sizes be? We previously in Cache 2 used a block size of 16 bytes, but is it optimal?

With a larger block size, it gives better spatial locality, as a wider range of access to nearby memory data is granted.

But at the same time, it has a larger miss penalty, as when a miss happens, it takes longer time to load a new block from the next level of memory.


It's probably best to understand this from an example:

```text
Cache lines:  4
Block size:   16 bytes
Word size:    8 bits
Address size: 32 bits
```

Suppose we access memory address `64`, and the corresponding block is not currently in the cache. Since each cache block contains 16 bytes, the cache does not load only address `64`; it loads the entire block containing it:

```text
Memory block 4:

addresses 64–79
```

Block `4` maps to cache line:

$(4 \bmod 4)=0$

so the entire block is copied into cache line `0`:

```text
Cache line 0:

[64][65][66] ... [79]
```

Now, if we access any address from `64` through `79`, such as `65`, `70`, or `78`, the required data is already inside that cache block, so we can get a quick **cache hit**.

However, suppose we next access address `80`. Address `80` belongs to the next memory block:

```text
Memory block 5:

addresses 80–95
```

That block is not part of the block we just loaded. If it is not already elsewhere in the cache, we get another cache miss and must fetch addresses `80–95` from main memory. Block `5` maps to cache line `1`.

```text
64–79  → block 4 → cache line 0
80–95  → block 5 → cache line 1
```

This suggests one way we could potentially reduce cache misses: **increase the block size**.

For example, suppose each cache block contained `64 bytes` instead of `16 bytes`. Then accessing address `64` would bring in:

```text
addresses 64–127
```

rather than only:

```text
addresses 64–79
```

Now, if the program later accesses addresses `80`, `90`, `100`, and so on, those addresses are already in the cache. This takes advantage of **spatial locality**: programs often access memory locations near locations they recently accessed.

However, larger blocks also have a cost. On a cache miss, the cache now has to transfer much more data from main memory:

```text
16-byte block → fetch 16 bytes on a miss
64-byte block → fetch 64 bytes on a miss
```

So increasing the block size can reduce the number of misses when nearby memory is frequently accessed, but each individual miss becomes more expensive because more data must be transferred.

One important distinction: this is increasing the **cache block size**, not necessarily just increasing the total cache size. With 4 lines:

```
4 lines × 16 bytes = 64-byte cache
4 lines × 64 bytes = 256-byte cache
```

So if we keep the same number of lines while making each block larger, the total cache also becomes larger, if we are trying to increase the size of a line without changing the total cache size, we would have to decrease the number of lines instead.


In conclusion:

Miss penalty and block size have a linear relationship, the larger the block size, the longer it takes to recover from a cache miss.

![[Screenshot 2026-08-07 at 10.50.53 AM.jpg|300]]

Miss rate decreases as block size increases, but without changing the total cache size, miss rate would bounce back as we decrease the number of lines due to increase line size.

![[Screenshot 2026-08-07 at 10.51.03 AM.jpg|300]]

A similar relationship happens with average access time, the larger the block size, the average access time decreases, but it bounces back due to increased miss penalty & miss rate

![[Screenshot 2026-08-07 at 10.51.11 AM.jpg|300]]