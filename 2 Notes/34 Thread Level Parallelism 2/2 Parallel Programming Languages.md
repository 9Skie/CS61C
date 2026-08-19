So... multicore, multithreading... we understand the big concepts, but how are these ideas actually translated into code?

Apparently, there are many different approaches, for example:

- Go has built-in support for concurrency through goroutines.
- CUDA provides a programming model specifically designed for GPU parallelism.

But why so many different approaches? Well, there are many parallel programming languages and frameworks because there is no universal solution. Parallel programming is highly dependent on the problem being solved.

- Scientific computing and machine learning often involve large matrix operations, where many identical computations can be performed simultaneously.
- A web server needs to handle many unrelated requests at the same time.

These problems all require different styles of parallelism, so specialized programming models have emerged for different situations, and automatically converting normal sequential code into efficient parallel code is extremely difficult.

For sequential programming, it took decades of compiler research before compilers could reliably translate C code into efficient assembly code. However, automatically translating C code into efficient parallel code is a much harder problem.

A compiler would need to understand:
- Which operations are independent?
- Which data can be safely shared?
- How should the workload be divided between cores?
- How should communication and synchronization be handled?

These problems are much more complicated than simply generating sequential machine instructions. Therefore, today we mostly have specialized solutions for specific cases rather than one perfect parallel compiler.

This area is still an active field of research, and solving general automatic parallelization remains an open problem. Whoever creates a system that can automatically transform ordinary programs into highly efficient parallel programs could make a significant impact.