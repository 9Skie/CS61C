As we discussed how to perform algebraic operations using logic gates in [[2 Boolean Arithmetic]], we now must turn to how the values we've been operating on are stored on a computer, which turns us to look at *circuits that can store memory*.

All the chips we've previously studied were *combinational*.

> Meaning, their outputs depended *solely* on their inputs.

This doesn't allow them to have a memory of anything, so we need to look at *sequential* circuits.

> Meaning, their outputs depend on both their current inputs and their previous state (history).

But the difference between "current" and "previous" invokes the idea of "time" on a computer, which we first need to explain how "time" works for a computer, before discussing memory.

## How Time Works To A Computer

> [!PDF|yellow] [[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=78&selection=11,0,20,6&color=yellow|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.78]]
> > Computer programs use variables, arrays, and objects—abstractions that persist data over time. Hardware platforms support this ability by offering memory devices that know how to maintain state. Because evolution gave humans a phenomenal electro-chemical memory system, we tend to take for granted the ability to remember things over time. However, this ability is hard to implement in classical logic, which is aware of neither time nor state.

Even before we can represent time on a computer, we need to understand that signals do not run instantly on a computer.

1. Fundamentally, electricity travels through the silicon in the gates’ inputs and outputs, and this takes time.
2. Performing calculations involves many gates, inputs, and outputs, which adds to the time it takes.
3. The more calculations the computer needs to perform, the longer it takes for the final output to appear.

Time in the real world is continuous, but computers operate on discrete logic—0’s and 1’s, or on’s and off’s—within their circuits. As a result, time is divided into fixed intervals called *cycles* (in synchronous circuits), determined by a clock. Just as we have 60 seconds in a minute, a computer has $n$ cycles within a second.

So when we say a CPU is **2.4 GHz**, it means the CPU can complete **2.4 billion cycles per second**. Let's turn to an example of how time is visualized on a computer with a Not gate.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 17.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=80&rect=120,258,494,452|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.80]]

Let's start by looking at cycle 1.

When we provide an input of 1 to the gate, there is a delay before the gate fully recognizes it as 1. This delay means the gate's output doesn’t immediately go to 0; it responds accordingly only after the input has fully propagated.

This process repeats in cycle 2, when `in` turns into 0, and `out` changes to 1.

Now, there are 2 observations to be made here:

1. A clock cycle should be *longer* than any possible time delay in the circuits
2. A clock cycle is achieved by a *ticktock*, a tick (when the clock signal goes from 0 to 1), and a tock (when the clock signal goes from 1 to 0).

In many systems, the input changes occur during the tick, and the state is read and stabilized during the tock, ensuring synchronization. In synchronous circuits, signal propagation and state changes are synchronized to the clock, ensuring that all parts of the circuit update their states in unison.

And this name gave rise to one of the most evil developments in human history.

![[3 Memory 1.png|200]]

## Memory Circuits

Ok! Now, how does this time, 0, 1, 0, 1, tick, tock, tick, tock relate to building memory circuits?

We start with the DFF (data flip-flop), a time-dependent logic gate that can switch between representing 0 and 1. It can be used to create a 1-bit register to store 1 bit of data, which then can come together to make an $n$ bit register, all of which can come together to construct the RAM.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 18.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=79&rect=119,579,496,739|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.79]]

Data Flip Flop:

A data flip-flop (DFF) simply implements the behavior of $out(t) = in(t-1)$, essentially copying the value of `in(t-1)` into the next cycle.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 19.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=82&rect=126,236,485,432|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.82]]

1-Bit Register:

On top of the data flip-flop's functionality, the register adds the ability to control whether the stored information `out` is retained or overwritten with new incoming data `in` by a signal called `load`.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 20.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=86&rect=123,390,492,635|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.86]]

16-Bit Register:

Nothing new here, we simply scaled from 1 bit to 16 bits.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 21.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=86&rect=128,149,489,215|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.86]]

RAM:

The RAM really is just a stack of $n$ m-bit registers, and each register can be selected for read/write. So on top of an m-bit register's functionality, we now need an additional variable called `address` to know which register we are selecting for operation.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 22.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=87&rect=125,213,486,346|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.87]]

Counter (Program Counter):

A very similar chip to the register, except it also can increment its value by 1 every cycle with inc, and its value can be reset with `reset`.

It'll come in handy later...

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 23.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=88&rect=128,138,488,218|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.88]]

## Implementation

In the current simulator, it is impossible to write a data flip-flop, and so you won't be able to write anything after that... so they implemented it for us, and we can use it directly.
