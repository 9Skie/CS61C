When the processor reads data, it first checks whether the required memory block is already available in the cache. From there, several outcomes are possible.

A **cache hit** occurs when the required memory block is already stored in the cache line selected by the address index, in that case, the cache can return the requested data immediately.

Suppose cache line `0` currently contains memory block `4`:

```text
Cache line 0:

[tag: block 4] [addresses 64–79]
```

The CPU requests address `64`.

```text
CPU requests address 64
        ↓
Address 64 belongs to block 4
        ↓
Block 4 maps to cache line 0
        ↓
Cache line 0 contains block 4
        ↓
Cache hit
```

The CPU reads the requested value directly from the cache.


A **cache miss** occurs when the selected cache line does not contain the required memory block. The cache must then request the required block from the next lower level of the memory hierarchy, such as another cache level or main memory.

Suppose cache line `0` currently contains memory block `0`:

```text
Cache line 0:

[tag: block 0] [addresses 0–15]
```

However, the CPU requests address `64`, which belongs to block `4`.

```text
CPU requests address 64
        ↓
Address 64 belongs to block 4
        ↓
Block 4 maps to cache line 0
        ↓
Cache line 0 contains block 0
        ↓
Cache miss
```

The computer retrieves the entire block from main memory:

```text
Main memory block 4:

[64][65][66] ... [79]
```

It then copies that block into cache line `0`, replacing block `0`. The CPU can then read address `64` from the newly loaded cache block.


After a miss, **block replacement** may occur. The existing block in the selected cache line is discarded and replaced with the newly retrieved block.

The overall process is therefore:

```text
Processor requests an address
        ↓
Index selects one cache line
        ↓
Tag is compared
        ↓
Cache hit or cache miss
        ↓
If miss, fetch block and replace current line
```

Cache behavior is also sometimes described using the informal idea of **cache temperature**. It describes how useful the cache contents currently are.
- A **cold cache** has just started or has recently been cleared. Its lines are empty or invalid, so the first accesses to memory blocks will usually miss.
- A **warming cache** has begun to fill with recently accessed blocks. Some repeated accesses may now hit, but many new accesses will still miss.
- A **warm cache** contains a useful working set of recently accessed blocks. The program is now reusing cached data, so the hit rate becomes reasonably high.
- A **hot cache** contains data that closely matches the program’s current access pattern. Most accesses hit, so the cache is providing a substantial performance benefit.

This temperature language is informal. A cache may be full but still perform poorly if the program keeps accessing blocks that replace each other.


There are several measurements are used to describe cache performance.

The **hit rate** is the fraction of memory accesses that are cache hits:

$(\text{hit rate})=\frac{\text{number of cache hits}}{\text{total memory accesses}}$


The **miss rate** is the fraction of memory accesses that are cache misses:

$(\text{miss rate})=\frac{\text{number of cache misses}}{\text{total memory accesses}}$

Since every access is either a hit or a miss:

$(\text{miss rate})=1-\text{hit rate}$


The **hit time** is the time required to access the cache and determine whether the requested data is present. 

The **miss penalty** is the additional time required when a cache miss occurs, it's generally much larger than the hit time, which is why even a relatively small miss rate can significantly affect performance.