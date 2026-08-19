Now that we have multiple workers running at the same time, we encounter a new problem: multiple workers may need to access the same shared resource.

For example, imagine multiple workers editing the same document. If two workers try to modify the same part of the document at the same time, their changes may conflict and the final result may become incorrect.

This is called a race condition. A race condition happens when the correctness of a program depends on the timing or ordering of multiple threads. Since threads can execute in different orders each time, the program may produce inconsistent or unexpected results.

To solve this, we needsynchronization. Synchronization is the process of controlling how multiple workers access shared resources so that they do not interfere with each other.

The most common approach is using a lock. A lock ensures that only one worker can access a critical section of code or a shared resource at a time. When one worker is modifying shared data, other workers must wait until the resource becomes available.

```C
// wait for lock released
while (lock != 0)
    ;

// lock == 0 now (unlocked)

// set lock
lock = 1;

// access shared resource ...
// e.g. pi
// sequential execution! (Amdahl ...)


// release lock
lock = 0;
```
