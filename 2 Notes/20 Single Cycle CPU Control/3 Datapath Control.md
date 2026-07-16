This class is just showing how data path control bits are actually used.

![[Screenshot 2026-07-16 at 4.19.56 PM.jpg|500]]

For a `beq` instruction, the control logic primarily looks at the instruction’s `opcode` and `funct3` fields.

For example:

```assembly
beq x1, x2, target
```

This instruction tells the CPU to read `x1` and `x2`, compare them, and then decide which instruction address should come next. If the two registers are equal, the CPU jumps to the branch target. Otherwise, it continues normally to $(PC + 4)$.

The control signals are inferred as follows:

|**Control signal**|**Value for** `beq`|**Why**|
|---|---|---|
|`ImmSel`|`B`|`beq` uses a B-type immediate|
|`RegWEn`|`0`|A branch does not write to a register|
|`BrUn`|don’t care|Equality does not depend on signedness|
|`BrEq`|used|Determines whether $(R[rs1] = R[rs2])$|
|`BrLT`|ignored|`beq` does not test whether one value is less than another|
|`ASel`|`1`|Sends the current $PC$ to the ALU|
|`BSel`|`1`|Sends the branch immediate to the ALU|
|`ALUSel`|`add`|Calculates $(PC + \text{immediate})$|
|`MemRW`|no write|A branch does not modify data memory|
|`WBSel`|don’t care|Nothing is written back to a register|
|`PCSel`|`BrEq`|Selects the branch target only when the registers are equal|

## **Which data paths are active**

The current $PC$ is sent to instruction memory to fetch the `beq` instruction. At the same time, the upper adder computes $(PC + 4)$, which is used if the branch is not taken.

The instruction fields select $(rs1 = \text{Inst}[19:15])$ and $(rs2 = \text{Inst}[24:20])$. The register file reads $(R[rs1])$ and $(R[rs2])$ and sends them to the branch comparator.

For `beq`, the comparator checks whether the values are equal. It sets $(BrEq = 1)$ when $(R[rs1] = R[rs2])$ and $(BrEq = 0)$ otherwise. `BrLT` is not used.

The immediate generator extracts and sign-extends the B-type immediate. The ALU then computes the branch target as $(PC + \text{immediate})$.

The $PC$ multiplexer chooses between $(PC + 4)$ and $(PC + \text{immediate})$. Since $(PCSel = BrEq)$, the branch target is selected when the registers are equal; otherwise, the processor continues to $(PC + 4)$.

## **Paths that are not meaningfully used**

`beq` does not write to data memory or to a destination register. Therefore, the memory-write path, write-back path, write-back multiplexer, and destination-register input are unused.

The main active paths are $(PC \rightarrow \text{IMEM} \rightarrow \text{register file} \rightarrow \text{branch comparator})$ and $(PC + \text{B-type immediate} \rightarrow \text{PC multiplexer} \rightarrow PC)$.

The control unit decodes the `opcode` and `funct3`, recognizes `beq`, and generates the required mux selections, ALU operation, and control signals.