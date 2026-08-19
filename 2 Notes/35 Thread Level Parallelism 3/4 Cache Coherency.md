As we discussed in the last note, the problem is that cached copies of the same memory location can become inconsistent. Cache coherence solves this through a communication mechanism between processors over the interconnection network.

Whenever a processor has a cache miss or wants to write to a cache line, it communicates with the other processors so they can coordinate what happens to their copies.

If a processor is only reading a value, multiple processors are allowed to keep cached copies of that same value, that's fine, but it's not the case for writes.

If one processor modifies a cached value, the other processors' copies are now stale. So those other copies must be invalidated before the write proceeds. 
- After that, if another processor wants the value again, it has to fetch the updated version instead of continuing to use its old cached copy.


Each cache block keeps a few state bits that describe the status of that block.

- A block can be in the **Shared** state, meaning the data is up to date and other caches are also allowed to have their own copy of the same block. This is fine as long as everyone is only reading.
    
- A block can be in the **Modified** state, meaning this cache has changed the data. In this state, this cache has the only valid up-to-date copy, other caches must not have a usable copy, and main memory may still contain the old value because the modified block has not been written back yet.
    
- A block can be in the **Exclusive** state, meaning this cache has the only cached copy of the block, but the value is still identical to main memory. Since no other cache has a copy, this processor can write to it directly, after which the block typically becomes Modified.
    
- A block can be in the **Owner** state, meaning multiple caches may have copies of the block, but this cache owns the newest version. The other caches can keep Shared copies, while main memory may still be outdated. If another processor requests the block, the Owner cache is responsible for supplying the up-to-date data.

Uh... I get it, it's suddenly a lot to take in, it's ok.

---

Lets go back to our example, where processor 1 and 2 reads `memory[1000]` first (where it contains 20), and where processor 0 writes `memory[1000]` with 40.

We first have the 2 reads happen:

![[Screenshot 2026-08-19 at 11.03.58 AM.jpg|500]]


Then we have the write happen, but as it's not in processor 0's cache, it goes into the interconnected network and invalidate other copies in other caches, and writes the value 0 into it's own cache.

![[Screenshot 2026-08-19 at 11.05.02 AM.jpg|500]]


But... we can encounter a new problem, suppose we have a block size of 32 bytes, and processor 0 is reading and writing variable X at `memory[4000]` and processor 1 is reading and writing variable Y at `memory[4012]` what happens? 

![[Screenshot 2026-08-19 at 11.08.44 AM.jpg|500]]

Because `X` at `4000` and `Y` at `4012` are inside the same 32-byte cache block, the coherence protocol cannot track them independently. It tracks the state of the entire block.

Suppose both processors initially have this block in the **Shared** state. If Processor 0 writes to `X`, it must obtain exclusive ownership of the whole block, so Processor 0’s copy becomes **Modified** and Processor 1’s copy becomes **Invalid**.

Then if Processor 1 wants to write to `Y`, even though `Y` is a different variable, its cache line is currently invalid. It must request the whole block again, causing Processor 0’s copy to be invalidated and Processor 1’s copy to become Modified.

So the state may keep bouncing back and forth:

```
P0 writes X:
P0 → Modified
P1 → Invalid

P1 writes Y:
P0 → Invalid
P1 → Modified
```

This is **false sharing**: the processors are not actually sharing the same variable, but because the variables occupy the same cache block, the coherence protocol treats them as if they are interfering with each other.


We prevent false sharing by making sure variables that are frequently written by different processors do not live in the same cache line.

The common solution is **padding or alignment**. For example, instead of placing `X` and `Y` close together:

```
[ X ... Y ... ]   ← same 32-byte cache block
```

we deliberately separate them so they occupy different cache blocks:

```
[ X ............... ] [ Y ............... ]
   cache block 1       cache block 2
```

Now Processor 0 can modify `X` without invalidating Processor 1’s cache line containing `Y`, and vice versa.

So the general rule is: if different threads frequently write different variables, try to place those variables on **different cache lines**. In practice this is done with padding, alignment, or data-structure layout changes.