The executable still sits inside your disk, and it's the Loader's job to fire it up into memory.
- Technically this goes a lot, lot deeper in the OS... 

In the big idea, the loader:

1. Reads the executable file's header to determine size of text and data segments
2. creates new address space for program large enough to hold text and data segments, along with a stack segment
3. Copies instructions + data for executable file into the new address space
4. Copies arguments passed to the program onto the stack

5. Initializes machine registers
	- this means clearing most registers, but stack pointer assigned addresses of 1st free stack location

6. Jumps to start up routine that copies program's arguments from stack to registers & sets the PC
	- If main routine returns, start-up routine terminates program with exit system call

