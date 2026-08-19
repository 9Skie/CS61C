By default as we said, hardware threads have a 1 to 1 mapping with cores, and each hardware thread executes one software thread at a time.

However, we can encounter a problem. Suppose a hardware thread encounters a slow operation, such as an I/O request or a cache miss. During this waiting period, the execution resources of that hardware thread may not be fully utilized.

One solution is hyper-threading (SMT), where a single physical core provides multiple hardware threads. 
- This means the core maintains multiple execution contexts, including separate program counters, registers, and thread states.

![[Screenshot 2026-08-17 at 2.55.08 PM.jpg|500]]

Now, if Hardware Thread 0 is waiting for data, the core can continue making progress by executing instructions from Hardware Thread 1, instead of leaving some execution resources idle.

However, do be careful in understanding this model, this is concurrency, not parallelism, as 1 core can still only run 1 active hardware thread at a time, there's still only 1 ALU in 1 core.