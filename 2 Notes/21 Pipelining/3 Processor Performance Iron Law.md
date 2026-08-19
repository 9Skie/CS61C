There is an 'iron law' for processor performance that tells how long it takes to execute a program, the formula looks as such:

![[Screenshot 2026-07-25 at 11.23.35 AM.jpg|400]]

- **Instructions/Program**: the number of dynamic instructions the program actually executes at runtime. It's determined by:
	- Task
	- Algorithm efficiency
	- programming language
	- compiler
	- instruction set architecture

- **Cycles/Instruction (CPI)**: how many clock cycles each instruction takes on average, given the microarchitecture.
	- Task
	- processor implementation (microarchitecture)
	- complex instructions (?)
	- superscalar processors (?)

- **Time/Cycle**:  the clock period (1/clock frequency). Set by the critical path delay through the slowest pipeline stage.
	- processor implementation (microarchitecture)
	- manufacturing size (14nm, 7nm, 3nm...)
	- voltage


Like compare these 2 CPUs: 

![[Screenshot 2026-07-25 at 11.37.53 AM.jpg|400]]

- **Processor A**: fewer instructions (1M) and a faster clock (2.5 GHz), but a much higher CPI (2.5)
- **Processor B**: more instructions (1.5M) and a slower clock (2 GHz), but a much lower CPI (1)


Despite A's advantages on two of the three terms, its CPI is so much worse that it loses overall:

- A: 1,000,000 × 2.5 / 2.5×10⁹ = 1 ms
- B: 1,500,000 × 1 / 2×10⁹ = 0.75 ms