The control logic of instructions could be basically be viewed as a lookup table, where certain instructions correspond to certain control bits, but how/where do we implement this lookup table?

We can implement this lookup table using a small ROM. The purpose of the ROM is to store the correct control-bit pattern for each instruction type.

For example, the ROM might receive parts of the instruction such as the `opcode`, `funct3`, and sometimes `funct7`:

$(\text{opcode}, \text{funct3}, \text{funct7}) \rightarrow \text{control ROM}$

These bits act like an address into the ROM. 

![[Screenshot 2026-07-16 at 5.25.11 PM.jpg|500]]

The diagram shows how this ROM-style controller can be built from two main parts: an **address decoder** and a bank of stored **control words**.

The inputs on the left are the instruction-identifying bits. These bits form the input to the controller. The address decoder examines that input and activates exactly one row corresponding to the current instruction.


At that address, the ROM stores one row containing all the control signals needed for that instruction:

$(ImmSel,\ RegWEn,\ BrUn,\ ASel,\ BSel,\ ALUSel,\ MemRW,\ WBSel,\ldots)$

So conceptually, the ROM performs:

$(\text{instruction bits}) \rightarrow (\text{all control bits})$

![[Screenshot 2026-07-16 at 5.24.39 PM.jpg|500]]

It is called a ROM because the mapping is fixed by the processor design. The CPU does not need to change these control patterns while running; it only reads the row corresponding to the current instruction.

Physically, this does not always have to be built as a literal memory chip. The same behavior can be implemented using combinational logic gates, such as decoders, AND gates, and OR gates. 

From the programmer’s perspective, though, it is useful to think of it as a ROM lookup table: instruction in, control signals out.




