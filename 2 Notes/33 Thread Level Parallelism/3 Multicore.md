Uh... we sort of explained this in parallel computing, but hopefully there's a different perspective.

In the early days of computing, all computational resources just kept growing, frequency of chips where doubling, the number of transistors were doubling, the power draw of them were doubling... and everyone was happy, gamers, scientists, cooperations.

But till a certain point we stopped, the power draw got to a point that the chips became hard to cool down, their frequencies couldn't go any higher, and the sequential app performance also halted.

![[Screenshot 2026-08-17 at 10.46.34 AM.jpg|500]]


And entered 2005, this is when multicore became an idea, the intel core 2 Duo was the first production level CPU that had more than 1 core.

We see that while sequential app performance halted, parallel app performance continued to improve, and the number of transistors continued to increase (as we can just increase the number of cores).

![[Screenshot 2026-08-17 at 10.46.52 AM.jpg|500]]

---

So, now that we are in a multicore world, what's shared and what's not shared?

The most common model is **shared memory**.

 In a shared memory system, each core has access to the entire memory space of the processor. This means multiple cores can communicate easily by reading and writing to shared variables.

However, each core usually has its own cache to improve performance. Since multiple caches may contain copies of the same data, special hardware is needed to keep these caches consistent. This is called **cache coherence**.

---

There are two main ways to use a multiprocessor

- Job-level parallelism: Multiple processors run completely separate tasks.
	- For example, one core may run a web browser while another core runs a compiler.

The processors are working on unrelated problems, so there is no communication required between programs.


- Partitioning a single task across multiple cores :Instead of running separate programs, we divide one large task into smaller pieces and assign each piece to a different core.

This approach can achieve large speedups, but it requires communication and synchronization between cores because the different parts of the task may depend on each other.


This is all hard! But as we can see, it's the only way to improve performance from this point onwards, as we are hitting limitations in speed, energy consumption and heat dissipation in single cores.

This shift toward parallel computing appears everywhere, from small mobile devices to large-scale data centers.


In **mobile systems** such as smartphones and tablets, we use multiple cores and specialized processors to improve both performance and energy efficiency.

At the other extreme, we have **warehouse-scale computers**, such as large cloud data centers. Instead of a single computer with multiple cores, we combine many computers together into a larger system.

Each individual computer is called a **node**, and each node may contain:
- Multiple CPUs
- Large amounts of memory
- Storage devices such as disks or SSDs

A warehouse-scale computer consists of many of these nodes working together. Inside each node, we can use different forms of parallelism, like MIMD and SIMD.


Look at the past 12 years, the number of MIMD cores have grown by 2.5 times, and the number of SIMD cores have grown by 8 times.

![[Screenshot 2026-08-17 at 11.06.16 AM.jpg|500]]