Now, we have multiple cores, but how do we actually use them?

One simple observation is that modern computers are already doing many things at the same time.

On a Unix-based system, we can run:

```
ps -x
```

`ps` stands for **process status**. It displays information about the processes currently running on the system.

The `-x` option tells `ps` to include processes that do not have an associated terminal. This allows us to see background processes and system services as well.

It would display something like this:

```
PID     TTY      TIME     CMD
1234    pts/0    0:01     bash
5678    ?        0:10     chrome
9012    ?        0:05     python
```

Each row represents a **process**, which is an independent program currently being executed.


If we run this on our own computer, we will usually see hundreds of processes running at the same time, but how? Threads.


A thread stands for "thread of execution". It is a single stream of instructions being executed by a processor.
- A program or process can split (fork) itself into multiple threads. These separate threads can, in theory, execute simultaneously on different CPU cores.

With a single core, a single CPU can execute many threads through time sharing, The CPU rapidly switches between different threads:

![[Screenshot 2026-08-17 at 11.22.05 AM.jpg|500]]


Each thread has it's dedicated program counter, separate registers, but has access to the shared memory.

A physical CPU core provides one or more **hardware threads**. A hardware thread is an actual execution slot in the CPU that can actively execute instructions.

A program can create multiple software threads. Across the entire system, the total number of runnable software threads from all programs may exceed the number of available hardware threads provided by the CPU. 
- Therefore, the operating system must schedule and multiplex software threads onto hardware threads, that's... not for this entire class of CS61C, that's CS162.

The operating system creates the illusion that many software threads are running simultaneously, even when there are fewer hardware threads available through context switching, but again, that's for an OS class.