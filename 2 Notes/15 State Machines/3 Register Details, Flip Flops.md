Last lecture, we saw the 'register', which is suppose to temporarily store some values, but what makes it up? 

A register has an input D (data), and output Q (quiescent), and a clock, and it's essentially made up of a series of flip flops in parallel.

The flip-flop is a circuit that maintains a state until directed by input to change the state. A basic flip-flop can be constructed using four-NAND or four-NOR gates. A flip-flop is popularly known as the basic digital memory circuit, [here](https://www.geeksforgeeks.org/digital-logic/flip-flop-types-their-conversion-and-applications)|.

There are multiple types of flip flops, but in this class (and what is commonly used) is the D-flip flop, it consists a single data input(D), a clock input(CLK),and two outputs: Q and Q' (the complement of Q).

![[Pasted image 20260308163035.png|300]]

This is the internal circuit and truth table of it.

![[Pasted image 20260308163148.png]]

![[Pasted image 20260308163153.png]]

---
## Timing on a Flip Flop

This is super important! Previously we've been rather 'vague' about what the clock does on a computer, just that it 'keeps things in unison' without really understanding what that unison means, now'll we'll truly understand that.

Assume we are on a 'rising edge triggered' flip flop, basically this means when the clock is 'rising' from 0 to 1, this is the time when the value of input `d` is sampled and transferred to the output `q`, and other times, d's value is ignored, even though it might be changing between the clock cycle.

![[Screenshot 2026-03-08 at 4.42.10 PM.png|500]]

As we can see, d's value is only sampled during the rising edge trigger of the clock.

But this raises a question, what if it just happens that when we want to sample d to q, d's changing itself? Like it's going through the process of becoming a 1 signal from 0, or a 0 signal from 1? 

We can't accept that! If we read a changing value of d into q, q's going to store something very weird, this would be called unstable in terms of a value, like being 0.7, or 0.3 in terms of voltage.

So, we say that the input data must be stable in the period of the sampling, meaning that d must 'hold' it's value during the 'rising edge' of the clock signal.
- d must already be stable for a short time before the rising edge.
- d must remain stable for a very small time after the clock edge.
- it takes time for d to transfer the value to q, but during this delay, d's value is already free to change

So long story short, D must not change during  $[t_{edge}-t_{setup},\; t_{edge}+t_{hold}]$

![[Screenshot 2026-03-08 at 4.48.12 PM.png|500]]
