A **direct-mapped cache** is a cache in which every block of main memory can be stored in exactly one specific cache line.
- A **cache line** is one storage location inside the cache.
- A **memory block** is a fixed-size group of consecutive bytes transferred between main memory and the cache.

The cache line is selected using:

$(\text{cache line index}) = (\text{memory block number}) \bmod (\text{number of cache lines})$


Suppose we have:
- Cache lines: 4
- Block size: 16 bytes

Because each block contains 16 bytes, main memory is divided as follows:

```text
Memory block 0: addresses 0–15
Memory block 1: addresses 16–31
Memory block 2: addresses 32–47
Memory block 3: addresses 48–63
...
```

To determine which block contains a particular address, we calculate:

$(\text{memory block number}) = \left\lfloor \frac{\text{address}}{16} \right\rfloor$

$(\text{cache line index}) = (\text{memory block number}) \bmod 4$

So:

```text
Memory blocks 0, 4, 8, 12, ... → Cache line 0
Memory blocks 1, 5, 9, 13, ... → Cache line 1
Memory blocks 2, 6, 10, 14, ... → Cache line 2
Memory blocks 3, 7, 11, 15, ... → Cache line 3
```


For a direct-mapped cache, the CPU divides each binary memory address into three fields:

```text
Memory address

+---------------+---------+--------+
|      Tag      |  Index  | Offset |
+---------------+---------+--------+
```

- **Index:** selects which cache line to inspect.
- **Tag:** identifies which memory block is currently stored in that cache line.
- **Offset:** selects the specific byte within the cache block.


