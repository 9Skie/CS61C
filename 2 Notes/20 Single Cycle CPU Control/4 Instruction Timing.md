As we walk through the data path of an instruction, we find many concurrent things, like when we are generating the immediate, we are retrieving an operand from the register file as well.

Lets go over another one, shall we? The add instruction.

- instruction fetch
	1. update program counter
	2. concurrently:
		1. add 4 to pc
		2. fetch instruction from instruction memory
- instruction decode
	1. concurrently:
		1. retrieve value of rs1 and rs2 from registers
		2. set all control bits accordingly
- instruction execute
	1. rs1 & rs2 go through Bsel & Asel (both set to 0)
	2. ALU adds both values
- memory access
	- none, skipping
- memory write back
	- through WBSel, we know the data we are writing back into a register

![[Screenshot 2026-07-16 at 4.41.48 PM.jpg|500]]

So the approximate delay path for `add` is: 
$(PC \rightarrow \text{instruction memory} \rightarrow \text{register file} \rightarrow \text{input muxes} \rightarrow \text{ALU} \rightarrow \text{write-back mux} \rightarrow \text{register file})$

---
## Generalization

We can see a more generalized instruction timing of the 5 cycles and link that with the data path that we've been discussing.

![[Screenshot 2026-07-16 at 5.05.33 PM.jpg]]