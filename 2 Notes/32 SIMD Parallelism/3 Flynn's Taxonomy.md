Flynn's taxonomy is a classification system for computer architectures proposed by Michael J. Flynn in 1966. It categorizes systems based on the number of concurrent instruction streams and data streams (single or multiple), dividing them into four core types: SISD, SIMD, MISD, and MIMD.

![[Pasted image 20260814212809.png|500]]

|Type|Instruction streams|Data streams|Basic idea|
|---|---|---|---|
|SISD|1|1|One instruction operates on one piece of data|
|SIMD|1|Many|Same instruction operates on many pieces of data|
|MISD|Many|1|Different instructions operate on the same data|
|MIMD|Many|Many|Different processors execute different instructions on different data|

However, most modern programs aren't directly fitting under 1 specific category, it's usually a combination together such called SPMD (single program multiple data).


SISD is simple: there is a sequential processor that goes through the instruction stream and processes data from memory one operation at a time.

- This is roughly what we've learned so far in CS61C.

![[Screenshot 2026-08-14 at 9.32.45 PM.jpg|300]]

SIMD is where a single instruction stream is applied to multiple data streams at the same time.

![[Screenshot 2026-08-14 at 9.33.03 PM.jpg|300]]

MIMD generally does not happen on a single CPU core. Instead, multiple processors or cores simultaneously execute different instructions on different data.

- This is common in multicore CPUs and large-scale systems such as data centers.

![[Screenshot 2026-08-14 at 9.35.57 PM.jpg|300]]

MISD is where multiple instruction streams operate on the same data stream.
- This is very rare in general-purpose computing and mostly appears in specialized or fault-tolerant systems.

![[Screenshot 2026-08-14 at 9.35.19 PM.jpg|300]]