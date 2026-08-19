So in software, we can avoid race conditions with synchronization by using user routines. When we are aware of possible race conditions, we can use locks to prevent multiple threads from accessing the same shared resource at the same time.

However, at the lower hardware level, there are also hardware synchronization instructions built into the CPU to help prevent race conditions from happening.

This is done through something called atomic read/write operations, where a read and write happen as a single indivisible instruction. No other thread is allowed to access or modify that shared resource in between the read and write.

In RISC-V, these instructions are called **AMOs, or Atomic Memory Operations**. An AMO atomically performs an operation on a value in memory, writes the new result back to memory, and places the **original memory value** into the destination register.

For example:

```
amoadd.w rd, rs2, (rs1)
```

Conceptually, this does:

```
t = M[x[rs1]]
x[rd] = t
M[x[rs1]] = t + x[rs2]
```

So `rs1` contains the address of the shared memory location, `rs2` contains the value we want to add, and `rd` receives the old value that was stored in memory.


Of course, we normally would not write the low-level RISC-V synchronization code ourselves. OpenMP provides higher-level synchronization functionality, including an abstract data type called a **lock**.

```C
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main(void) {
    omp_lock_t lock;
    omp_init_lock(&lock);

    #pragma omp parallel
    {
        int id = omp_get_thread_num();

        // parallel section
        // ...

        omp_set_lock(&lock);

        // sequential / critical section
        printf("id = %d\n", id);

        omp_unset_lock(&lock);

        // parallel section
        // ...
    }

    omp_destroy_lock(&lock);
}
```

The overall program creates multiple OpenMP threads. Most of the code inside the parallel region can execute concurrently, but there is one section protected by a lock. Only one thread can execute that protected section at a time; the other threads have to wait until the lock is released.

The structure of the OpenMP locking mechanism works like this:

1. `omp_lock_t lock;` — creates a lock variable.
2. `omp_init_lock(&lock);` — initializes the lock before any thread uses it.
3. `omp_set_lock(&lock);` — a thread tries to acquire the lock. If another thread already has it, this thread waits.
4. The thread executes the protected section while holding the lock.
5. `omp_unset_lock(&lock);` — releases the lock so another thread can acquire it.
6. `omp_destroy_lock(&lock);` — destroys the lock after the parallel work is finished.


But locks can introduce a new problem called a **deadlock**. A deadlock happens when multiple threads are each waiting for another thread to release a resource, so none of them can continue.
- For example, Thread 1 holds Lock A and waits for Lock B, while Thread 2 holds Lock B and waits for Lock A. Neither thread can move forward, so the program becomes stuck indefinitely.

![[Pasted image 20260819095814.png|400]]

So, how to solve a deadlock?  The main goal is to make sure threads cannot form a circular chain of waiting. 

In the earlier example, Thread 1 holds Lock A and waits for Lock B, while Thread 2 holds Lock B and waits for Lock A. Because each thread is waiting for the other to release something, neither can continue.

A common solution is to enforce a consistent lock ordering. For example, if every thread is required to acquire Lock A before Lock B, then one thread may have to wait for Lock A, but it cannot already be holding Lock B while doing so. That removes the circular dependency that causes the deadlock.

Another approach is to avoid waiting forever. A thread can try to acquire a lock, and if it fails, it can release the locks it already holds and try again later. The big idea is that deadlocks are prevented by designing the synchronization so that threads cannot end up permanently waiting on each other.