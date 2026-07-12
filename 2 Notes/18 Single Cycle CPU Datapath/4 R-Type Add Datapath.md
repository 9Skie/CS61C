For simplicity, lets start with just a data path that just supports one instruction type, and just one instruction under that one instruction type.

They were simple instructions, register to register instructions.

![[Screenshot 2026-07-07 at 9.03.47 PM.png|500]]

There are only 2 changes to the machine state, as we can see, 1 is the register which we write the ALU add result to, and the other is the incrementation of the program counter.

At the simplest, we will have a program counter that is able to increment itself by 4.

![[Screenshot 2026-07-07 at 9.08.19 PM.png|200]]

Then, we just have to decode the instruction accordingly, which is the 1st register? which is the 2nd register? where is the data being written? That's this later part.
- program counter points to address in instruction memory, say at `x`
- instruction is loaded from `[x:x+32]` bits
- instruction is divided into:
	- opcode
	- rd
	- functiont3
	- rs1
	- rs2
	- funct7

| Field  |  Bits | Width | Span          |
| ------ | ----: | ----: | ------------- |
| opcode |   6:0 |     7 | [x : x+7)     |
| rd     |  11:7 |     5 | [x+7 : x+12)  |
| funct3 | 14:12 |     3 | [x+12 : x+15) |
| rs1    | 19:15 |     5 | [x+15 : x+20) |
| rs2    | 24:20 |     5 | [x+20 : x+25) |
| funct7 | 31:25 |     7 | [x+25 : x+32) |

Recall from instruction formats that the format of instructions are fixed, different bits at different indexes must correspond to different parts of the instruction.

![[Screenshot 2026-07-08 at 10.51.24 AM.png|500]]

Then after this division, we are able to know the registers we need to read from, and the register we need to write to.

So then the ALU produces the result based on the data stored at the registers we need to read from, and then puts the computed value at the register we need to write to.

Simultaneously, this program counter by default gets incremented by 4 bytes, but only updates the program counter at the next tick.

In summary, this is the data path.

![[Screenshot 2026-07-07 at 9.11.14 PM.png|500]]

However, we still haven't added control into this diagram, there's only 1 simple control in this instruction type, that is controlling whether we are enabling register write or not.

![[Screenshot 2026-07-08 at 11.04.50 AM.png|500]]


Why don't we also see the timing diagram for add? We already said the flow of the logic above, so honestly... just take a look at the diagram and come to conclusions yourself.
- X is a boundary of the 'time' of the value being stored in the register

![[Screenshot 2026-07-08 at 11.10.08 AM.png|500]]

