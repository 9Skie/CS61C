Hm, this is about pipelining.

Previously in the book, we talked about how the single cycle CPU is rather inefficient, as every instruction must completely finish before the next instruction can begin, and this isn't usually very efficient.

But if we consider the stages of an instruction:
- **Fetch:** Get the instruction from memory.
2. **Decode:** Determine what it means.
3. **Execute:** Perform the operation.
4. **Memory:** Access memory if needed.
5. **Write-back:** Store the result.

Each stage seems independent from each other? Hm... how can we use this property?

> [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=519&selection=22,0,34,64&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.519]]
> > Anyone who has done a lot of laundry has intuitively used pipelining. The non-pipelined approach to laundry would be as follows: 
> > 1. Place one dirty load of clothes in the washer. 
> > 2. When the washer is finished, place the wet load in the dryer. 
> > 3. When the dryer is finished, place the dry load on a table and fold. 
> > 4. When folding is finished, ask your roommate to put the clothes away. 
> > 5. When your roommate is done, start over with the next dirty load.
> 

![[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 18.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=521&rect=86,610,531,781&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.521]]

But say, while the dryer is drying clothe set 1, why cant we have clothe set 2 be going into the washer? 

> [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=519&selection=43,7,46,68&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.519]]
> > As soon as the washer is finished with the first load and placed in the dryer, you load the washer with the second dirty load. When the first load is dry, you place it on the table to start folding, move the wet load to the dryer, and put the next dirty load into the washer.

![[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 19.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=521&rect=86,419,533,612&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.521]]

Pipelining is an implementation technique in which multiple instructions are overlapped in execution, and in this case, we have shrunk the execution time from 8 hours to 3.5 hours in total to wash the dirt clothes for all 4 people, RISC-V uses a similar philosophy as well.

> [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=522&selection=19,0,28,55&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.522]]
> > The same principles apply to processors where we pipeline instruction execution. RISC-V instructions classically take five steps: 
> > 1. Fetch instruction from memory. 
> > 2. Read registers and decode the instruction. 
> > 3. Execute the operation or calculate an address. 
> > 4. Access an operand in data memory (if necessary). 
> > 5. Write the result into a register (if necessary). Hence, the RISC-V pipeline we explore in this chapter has five stages.
> > The following example shows that pipelining speeds up instruction execution just as it speeds up the laundry.

![[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 20.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=524&rect=99,474,530,776&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.524]]

This does not necessarily make one individual instruction faster. A single instruction still has to pass through all five stages, it may even take slightly longer because pipeline registers are added between stages. 
- The benefit is higher throughput: the CPU can finish more instructions over the same amount of time.

But there are many, many complexities that come with trying to pipeline instructions this way.... there are 3 situations that prevent starting the next instruction directly in the next cycle.

---
## Structure Hazard

A structural hazard happens when two instructions need the same hardware resource at the same time. 

For example, if instruction fetch and data memory access share one memory unit, then a load/store instruction can conflict with the next instruction being fetched. Since the CPU cannot use the same memory for both at once, one instruction must stall, creating a bubble. 

The usual fix is to use separate instruction memory and data memory, as we are already doing.

---
## Data Hazard

A **data hazard** happens when an instruction needs a value that a previous instruction has not written back yet. 

For example, `add x19, x0, x1` produces a new value for `x19`, and the next instruction `sub x2, x19, x3` needs that value. But in the pipeline, `sub` may read `x19` before `add` reaches the write-back stage.

This means `sub` reads the old value of `x19`, causing the wrong result.

![[Screenshot 2026-05-01 at 9.20.35 AM.png|500]]

- notice how we are simplifiying read/write operations with right shaded and left shaded blocks
	- right shaded is read
	- left shaded is write
	- no shade is no memory access

To avoid a data hazard, the CPU can insert a **bubble**, meaning a fake “do nothing” instruction, usually called a **NOP** just to wait it out.

In this case, the `sub` needs the new value of `x19`, but the `add` has not written it back yet. So the pipeline can stall the `sub` for a few cycles and insert empty work in between.

![[Screenshot 2026-05-01 at 9.22.12 AM.png|500]]

---
## Control Hazard

A **control hazard** happens when a branch or jump makes the CPU unsure which instruction should come next. 

For example, with `beq`, the CPU must first compare two registers before it knows whether to continue to `PC + 4` or jump to the branch target. But the pipeline wants to fetch the next instruction before that decision is ready.

![[Screenshot 2026-05-01 at 9.25.37 AM.png|500]]

A basic solution is to wait until branch outcome is determined before fetching the next instruction.

![[Screenshot 2026-05-01 at 9.27.06 AM.png|500]]

But like... that's really dumb! A smarter way would be to predict whether the branch will be taken or not, but uh... this is a whole complication on it's own. 

A very simple strategy of this type of prediction is:
- Always predict `not taken`:Assume the branch will not jump, so immediately fetch the instruction at PC + 4.

For example:

```
beq x1, x0, target
add x5, x6, x7
```

The CPU predicts that `beq` is not taken and begins executing `add`. If the prediction is correct: the pipeline continues normally.

If the prediction is wrong: the CPU discards the incorrectly fetched instructions, jumps to `target`, and restarts the pipeline there.
- $\text{guess next PC} \rightarrow \text{keep working} \rightarrow \text{flush if wrong}$

This is called **static branch prediction** because the prediction does not change based on past behavior.