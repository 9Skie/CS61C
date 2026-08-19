Caches work because programs usually do not access memory randomly. Instead, memory accesses tend to follow patterns called **locality**.

There are two main types of locality:
- temporal locality
- spatial locality

---

## Temporal Locality

**Temporal locality** means that if a memory location is accessed, it is likely to be accessed again soon.

Because recently used data is likely to be needed again, the cache keeps recently accessed data close to the CPU.

Example situations:
- A variable inside a loop is repeatedly accessed.
- A function is called multiple times.


## Spatial Locality

**Spatial locality** means that if a memory location is accessed, nearby memory locations are likely to be accessed soon.

Because of this, caches usually load a block of nearby memory rather than a single value.

Example situations:
- Iterating through an array from beginning to end.
- Accessing consecutive instructions in a program.