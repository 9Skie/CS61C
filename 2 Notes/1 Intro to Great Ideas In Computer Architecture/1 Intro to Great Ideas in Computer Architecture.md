This is apparently the biggest computer architecture class taught anywhere... darn!

The professor teaching it was a gradate at UC Berkeley, who fell in love with computer graphics, and became a PHD later. He fell in love with teaching and everything! You can feel the enthusiasm of him through the screen!

---
## CS61C is not about C Programming

Why? C is just a tool, it's high level enough that all the knowledge that you've learnt up to this point about programming still applies in this language, but it's low level enough such that it exposes you to the internal workings of the machine.

This class, alike Nand2tetris, goes all the way from the hardware level up to the software and know everything that is going on inside a computer. But it's going to go much more deeer than Nand2Tetris! 

The original idea for how computer architecture works is alike this diagram:

![[Screenshot 2026-02-03 at 8.14.21 PM.png|500]]

But as you know, today we don't just work with "1 computer with 1 core" simplicity anymore, there's parallelism at so many levels, hardware, data, instructions, threads, cores...

![[Screenshot 2026-02-03 at 8.16.35 PM.png|500]]

There are 6 great ideas that are in computer architecture, for our computers to get where we are today.
- Abstraction
	- The idea that we can manage system complexity by hiding intricate, low-level hardware details (like logic gates or circuits) behind simplified, high-level interfaces (such as instruction sets or operating systems)
	- So every time you write some C code... you don't have to think about how the logic gates are being flipped
	- ![[Pasted image 20260204100628.png|400]]
- Moore's Law
	- Moore's Law is the observation by Intel co-founder Gordon Moore)that the number of transistors on a microchip doubles roughly every two years, leading to exponential increases in computing power, smaller devices, and lower costs.
	- He predicted this back in 1965, and it held up all the way till 2010
	- ![[Screenshot 2026-02-04 at 10.08.22 AM.png|400]]
- Memory Hierarchy
	- A memory hierarchy is the structured organization of computer storage into levels (registers, cache, RAM, disk), where faster memory is smaller and more expensive, and slower memory is larger and cheaper.
	- This organization places small, fast memory closest to the CPU to minimize access time for frequently used data, while larger, slower storage (such as RAM and disks) is used for less frequently accessed data.
	- ![[Pasted image 20260204102020.png|400]]
- Parallelism
	- Parallelism in computer architecture is the design approach of using multiple processors or functional units to execute tasks simultaneously, breaking down complex problems into smaller parts for faster, more efficient computation.
	- There's instruction level parallelism, a processor's ability to execute multiple instructions simultaneously by overlapping their execution
	- ![[Pasted image 20260204102711.png|300]]
	- Core level parallelism is by executing multiple threads of a program simultaneously, typically on multi-core processors
	- ![[Pasted image 20260204103017.png|400]]
- Performance Measurement & Improvement
	- With all those 'ways' to make computers faster, we would like to have **quantitative metrics** to evaluate the performance of these computer systems.
	- Performance is primarily measured using **latency** (how long a task takes to complete) and **throughput** (how much work is completed per unit time). These metrics are evaluated using **benchmarks** and workload analysis.
- Dependability via Redundancy
	- This means improving the reliability and correctness of a computer system by duplicating critical components or operations, so that if one part fails, another can take over or detect the error.
		- Like, if a youtube server got on fire, the youtube website would still be up, and there would be copies of videos on that server in other servers
	- This goes from data centers, to hardware disks, to memory... everywhere

---

 And they'll be using this book from Patterson & Hennessy
 
 John L. Hennessy and David A. Patterson won the 2017 [ACM A.M. Turing Award](https://amturing.acm.org/) for revolutionizing computer architecture through a systematic, quantitative approach to designing Reduced Instruction Set Computer (RISC) processors. Their work, which enables faster, more energy-efficient, and ubiquitous microprocessors in 99% of modern devices, is considered the "Nobel Prize of computing".

So... go read their book! It's amazing.