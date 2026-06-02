Now that we are down at the machine language level, we know the instructions formats, we know how all the linking happens... where do those binary 0's and 1's actually go? How do those actually get understood by the computer?

![[Screenshot 2026-06-01 at 2.31.56 PM.png|400]]

We gotta move to the hardware of the computer! The actual chips that run the electricity through and processes those signals into whatever you are doing.

But, there must be an agreement between the software and hardware... we've seen these guys, ISAs, stuff like:

-  x86 – used by most desktop and laptop CPUs (Intel and AMD processors).
- ARM architecture – dominant in phones, tablets, and many embedded systems.
- RISC-V – a newer open standard used in research, embedded devices, and increasingly in commercial chips.

![[Pasted image 20260305190432.png|500]]

The ISA is an abstraction and doesn’t specify in detail how the instruction execution should be implemented. Consequently their are many different ways to design the processor.

A microprocessor might look like this:

![[Screenshot 2026-03-05 at 7.17.57 PM.png|300]]

Looks kinda scary, but the details will be discussed later in this class, as you zoom into any of them, you'll realize they look exactly the same with just transistors and copper wires.

We as computer scientists don't really care about the copper wires and transistors, can you imagine a Nand gate looking something like this?

![[Screenshot 2026-03-05 at 7.23.50 PM.png|200]]

I can't, we abstract it to something like this as computer scientists, you could be an computer engineer if you cared about the above diagram.

![[Screenshot 2026-03-05 at 7.24.12 PM.png|200]]

To make all the parts of a processor work together, computers use a **clock signal**. This is a repeating electrical signal that switches between 0 and 1 at a constant frequency. Each switch defines a **clock cycle**.

The clock acts as a global timing reference for the processor. Instead of circuits changing state at random times, most components update only at specific moments, usually at the rising or falling edge of the clock.

Do realize that, due to physical constraints, digital circuits cannot produce a result instantly. Even electricity has a velocity limit, and the delay between inputs being turned into outputs in hardware is called the **propagation delay**.

![[Screenshot 2026-03-05 at 7.47.58 PM.png|500]]

 However, the propagation delay of a circuit should always be smaller than the clock period, as in the photo shown.

And, we usually don't just send bits 1 at a time, we group them together to transmit words of data.

![[Screenshot 2026-03-05 at 7.38.21 PM.png|300]]

The drawing shows a collection of 4 wires used to transmit a 4-bit word. The waveforms show how the signals on the wires might change over time.

