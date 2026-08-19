Think about this simple loop:

```c
for (int i = 0; i < 100; i++) {
    ...
}
```

In the serial version, a single worker executes every iteration one after another, each iteration performs some computation on one element of the data.

However, if each iteration is independent of the others, then there is no reason they must execute sequentially.

For example, if we have 4 workers, we can divide the work into 4 separate chunks:

```c
Worker 0:
for (int i = 0; i < 25; i++) {
    ...
}

Worker 1:
for (int i = 25; i < 50; i++) {
    ...
}

Worker 2:
for (int i = 50; i < 75; i++) {
    ...
}

Worker 3:
for (int i = 75; i < 100; i++) {
    ...
}
```

Now each worker processes a different portion of the data. All four workers can execute these sections at the same time, reducing the total execution time.


If we are using OpenMP, this could be done in 4 lines simply:

```C
#include <omp.h>

#pragma omp parallel for
for (int i = 0; i < 100; i++) {
    ...
}
```

The OpenMP runtime will automatically create multiple threads and divide the loop iterations between them.

OpenMP (Open Multi-Processing) is a framework for writing shared-memory parallel programs. It allows programmers to add simple compiler directives to existing C/C++ code to tell the compiler which parts of the code can be executed in parallel.

As we saw in that example, OpenMP will automatically create threads and distribute the loop iterations among them. Instead of manually creating threads and assigning work, the programmer only needs to specify where parallelism exists, and where it ends in the program.

![[Screenshot 2026-08-17 at 3.36.25 PM.jpg|500]]
