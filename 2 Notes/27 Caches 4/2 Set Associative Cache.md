A **set-associative cache** is a compromise between a direct-mapped cache and a fully associative cache.

Recall the two sides, starting with direct mapped cache, each memory block has exactly **one possible location**.

```text
Memory block 0  → Cache line 0
Memory block 4  → Cache line 0
Memory block 8  → Cache line 0
```

This is very fast because we immediately know where to look, but many blocks can conflict.


On the other hand for fully associative cache, a memory block can go anywhere.

```text
Memory block 0  → Any cache line
Memory block 4  → Any cache line
Memory block 8  → Any cache line
```

There are no conflict misses, but the cache has to search every line.


A **N-way set associative cache** sits in the middle. Instead of one huge collection of cache lines, we divide the cache into **sets**. Each set contains multiple cache lines.

For example, a **2-way set associative cache**:

```text
Cache

Set 0:
+-----------+
| Line 0    |
| Line 1    |
+-----------+

Set 1:
+-----------+
| Line 2    |
| Line 3    |
+-----------+
```

Each memory block maps to exactly one **set**, but inside that set it can be placed in any of the lines.

For example:

```text
Block 0 → Set 0 → Line 0 or Line 1
Block 4 → Set 0 → Line 0 or Line 1
Block 1 → Set 1 → Line 2 or Line 3
```


The address format also becomes a middle ground.

Direct-mapped:

```text
+------------+---------+---------+
| Tag        | Index   | Offset  |
+------------+---------+---------+
```

The index directly selects one cache line.


Fully associative:

```text
+------------+---------+
| Tag        | Offset  |
+------------+---------+
```

There is no index because the block can be anywhere.


N-way set associative:

```text
+------------+---------+---------+
| Tag        | Set     | Offset  |
+------------+---------+---------+
```

The set index selects a group of possible locations, then the tag is compared against every line inside that set.

Example for a 4-way set associative cache:

```text
Address arrives

        |
        v

Set index selects Set 3

        |
        v

Compare tag with all 4 lines in Set 3


Set 3:

+-------+------+------+
| Valid | Tag  | Data |
+-------+------+------+
|   1   |  A   | ...  |
+-------+------+------+
|   1   |  B   | ...  |
+-------+------+------+
|   1   |  C   | ...  |
+-------+------+------+
|   1   |  D   | ...  |
+-------+------+------+
```

If any tag matches, it is a hit. The "N-way" means the number of cache lines per set.

The reason modern CPUs usually use set associative caches is that it gives most of the benefit of fully associative caches while avoiding the huge hardware cost of comparing every cache line.