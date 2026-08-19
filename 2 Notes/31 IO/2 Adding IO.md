A computer uses IO devices to interact with the outside world, or else we humans also can't interact with the computer.

But right now we have the question, how are IO devices added to a computer under a unified connection? How can we consider a mouse, a keyboard, a screen all IO devices when clearly the computer interacts with them differently?

Fundamentally think about it this way, we call them all IO devices because they are either input or output (or both) devices, which means it must input a sequence of bytes to the computer, whether it be instructions or data, or output a sequence of bytes from the computer.

So, what happens is we make device communication look exactly like reading and writing memory.


In MMIO, a portion of the physical address space is reserved for devices. When the CPU writes to an address in that range, the data doesn't go to memory, the memory controller routes it to the device instead. When the CPU reads from that address, it gets bytes from the device.

The beauty is that the CPU needs no special I/O instructions. The same `load` and `store` instructions that work on RAM work on devices.

![[Screenshot 2026-08-11 at 8.31.42 AM.jpg|500]]


But this has a question, the speed of IO is very different from the speed of processors, like, look at this diagram here:

![[Screenshot 2026-08-11 at 9.32.26 AM.jpg|500]]

The speed of IO is generally very much slower compared to processors! So how to solve this problem? Next note.