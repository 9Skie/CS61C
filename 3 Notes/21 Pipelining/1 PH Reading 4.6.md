We saw the concept of pipelining, but how do we actually enable it in our current CPU design?

We can first roughly divide our CPU into 5 parts:
- instruction fetch
- instruction decode/register file read
- execute
- memory access
- write back

![[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 21.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=545&rect=97,462,532,777|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.545]]

Generally, we can see that instructions go from left to right in this diagram, except the 2 blue lines:
- write back stage, writing back the result back to register file
- execute stage, selecting the next PC value

But due to this general division, we are able to add 'registers' between these different stages of execution to temporarily store the result of a stage to send to the next stage.

![[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 22.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=548&rect=96,571,542,778|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.548]]

> [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=548&selection=9,7,20,30&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.548]]
> > They are labeled by the stages that they separate; for example, the first is labeled IF/ID because it separates the instruction fetch and instruction decode stages. The registers must be wide enough to store all the data corresponding to the lines that go through them. For example, the IF/ID register must be 96 bits wide, because it must hold both the 32-bit instruction fetched from memory and the incremented 64-bit PC address.

There's also a long description of a bug of the current design to which we have to change the data path for the write register. 
- I'm not going into that

![[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 23.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=559&rect=98,571,534,774&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.559]]

---
## Pipeline Control


![[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 24.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=565&rect=90,528,541,784&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.565]]

> [!PDF|yellow] [[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=565&selection=23,0,27,15&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.565]]
> > To specify control for the pipeline, we need only set the control values during each pipeline stage. Because each control line is associated with a component active in only a single pipeline stage, we can divide the control lines into five groups according to the pipeline stage.

The idea is exactly the same as the non-pipelined version of the CPU, but instead of all control signals given at once, the control line needs to be set for each stage for each instruction.

![[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface 25.jpg|500]]

[[PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface.pdf#page=569&rect=86,467,542,786&color=yellow|PH - Computer Organization and Design RISC-V Edition The Hardware Software Interface, p.569]]

