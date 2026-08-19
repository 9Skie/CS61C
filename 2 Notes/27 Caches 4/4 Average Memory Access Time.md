The goal of cache design is to minimize **Average Memory Access Time (AMAT)**:

$(\text{AMAT})=\text{Hit Time}+(\text{Miss Rate}\times\text{Miss Penalty})$

This means we want a cache that is fast to access, has few misses, and can recover quickly when misses happen.

The whole point of any cache design is just 'we want less misses, and for each miss we want less penalty'

To reduce **miss penalty**, modern systems use multiple levels of cache. Instead of going directly from the L1 cache to slow main memory, a miss in L1 can check larger but slower L2 and L3 caches first.

```text
CPU
 ↓
L1 Cache
 ↓
L2 Cache
 ↓
Maybe more cache levels
 ↓
Main Memory
```

The closer a cache is to the CPU, the smaller and faster it is. L1 cache is extremely fast but has limited capacity, so it cannot hold much data. L2 is larger but slower, and L3 is even larger but slower. Finally, DRAM is much larger than all caches but has a much higher access latency.

When the processor requests data, it first checks the L1 cache. If the data is there, we have an L1 hit and the processor receives the data quickly. However, if the data is not in L1, the processor checks L2 and so on.

Assume we just have 2 layers of cache, then the formula of AMAT expands from the normal AMAT equation:

$(\text{AMAT})=\text{L1 hit time}+\text{L1 miss rate}\times\text{L1 miss penalty}$

However, the L1 miss penalty is no longer simply the DRAM access time. Instead, an L1 miss first causes an L2 lookup:

$(\text{L1 miss penalty})=\text{L2 hit time}+\text{L2 miss rate}\times\text{L2 miss penalty}$

So the full equation becomes:

$(\text{AMAT})=\text{L1 hit time}+\text{L1 miss rate}\times(\text{L2 hit time}+\text{L2 miss rate}\times\text{L2 miss penalty})$


Typically, an **L1 cache** is very small, usually only tens of KB, because it is designed to be extremely fast. It can be accessed within about one clock cycle and has a very low miss rate, usually around 1–5%. 

An **L2 cache** is larger, usually hundreds of KB, but it is slower, taking several clock cycles to access. Because it stores more data, it has a lower chance of missing, but its miss rate is still higher, typically around 10–20% of L1 misses.