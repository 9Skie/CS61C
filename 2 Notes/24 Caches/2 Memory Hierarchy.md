As we know,**memory hierarchy** is a fundamental idea in computer architecture.

The CPU works closely with small, fast storage such as registers, while relying on larger but slower storage such as main memory for storing large amounts of data.

However, accessing main memory is rather slow, and we might not need 100% of the entire program's memory available to us at all times, as programs usually do not access all of their data uniformly, we really just need to access memory that is recently accessed a lot by the program.

Therefore, we can place recently or frequently accessed data into a smaller, faster memory closer to the CPU, but not as close as registers, in a place called cache, which is a small subset copy of the main memory.

![[Pasted image 20260804222408.png|500]]