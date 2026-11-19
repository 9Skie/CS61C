
> [!PDF|yellow] [[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=33&selection=7,0,12,11&color=yellow|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.33]]
> > Every digital device—be it a personal computer, a cell phone, or a network router—is based on a set of chips designed to store and process binary information. Although these chips come in different shapes and forms, they are all made of the same building blocks: elementary logic gates.

As we know, computers fundamentally operate with 1's and 0's, true and false, we call these binary values.

The job of boolean algebra is to take in binary inputs and return binary outputs, they are represented like any other math with operators, called boolean operators.

These are the 3 fundamental ones.

| Name | Bool Notation | Logic Notation |
| --- | --- | --- |
| And | $x \cdot y$ | $x \land y$ |
| Or | $x + y$ | $x \lor y$ |
| Not | $\bar{x}$ | $\neg x$ |

![[1 Boolean Algebra 1.png|300]]

Boolean functions are just combinations of these operators, all boolean functions can be defined using a *truth table*, a table that shows all possible outcomes for a boolean function.

For example, here is the truth table for $(x + y) \cdot \overline{z}$:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 1.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=36&rect=126,280,497,511|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.36]]

## Logic Gates

A *gate* is a physical device that implements a simple boolean function. Today, gates are made up by transistors in silicon conducting electricity.

> It's the physicist's job to make gates possible in the real world, we might even move on from electricity to photonics (light) some day

And, Or, Not gates are represented in these diagrams:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 2.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=38&rect=117,77,490,136|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.38]]

And since the input/output of gates are all the same, they can be combined.

For example, $x \cdot y \cdot z$ can be represented with $(x \cdot y) \cdot z$

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 3.jpg|646]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=39&rect=122,385,488,485|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.39]]

All combinational logic functions can be expressed as a combination of And, Or, and Not operations.

However, And, Or, and Not can all be expressed using Nand, and thus all combinational logic can be implemented using Nand, which is how we will be implementing all of these boolean algebra combinations.

> But let us first understand the idea of logic gate combinations

A boolean function/gate interface (what the gate is suppose to do) can be expressed in many ways, some more efficient, some less efficient, we'll come back later as to how to design them efficiently.

## Hardware Description Language

So, are we going to buy transistors, breadboards, and start soldering away to make electrical circuits?

Well… hardware designers don’t do that anymore. Instead, they first simulate and test the circuit designs virtually before building anything physical. This is where **Hardware Description Languages (HDLs)** come in.

HDLs are specialized programming languages used to describe the behavior and structure of electronic circuits. They allow us to describe how a circuit behaves over time, how it responds to inputs, and how it produces outputs all in a way that can be synthesized into real hardware.

The usual process goes somewhat like:

1. The designer specifies the chip logic by writing an HDL program
2. The chip is virtually created using a tool called *hardware simulator*
3. The chip logic is tested by various sets of input output pairs
4. The chip is also tested for it's speed, energy consumption, cost etc
5. The designer goes back to step 1 to optimize the chip

This is a diagram showing the HDL program, test script, and output file of a Nand gate.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 4.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=43&rect=120,468,478,730|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.43]]

An HDL definition of a chip has two sections: a header and a parts section.

- The header specifies the chip’s name and its input/output pins.
- The parts section describes the components that make up the chip, with each component listed by name and its connections to other parts in the design.

HDLs are not so different from high level programming languages, it's just the difference of using a hardware simulator compared to a compiler.

A hardware simulator looks something like this, we will be using a virtual one provided by the course.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 5.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=45&rect=132,345,482,611|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.45]]

### API Style

Before actually going in to the hardware simulator and playing with building chips, we'll first look at the API for each chip, to see how they carry out a common Boolean operation.

Here is the API for the Nand Chip:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 6.jpg|646]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=46&rect=75,414,537,480|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.46]]

An API (Application Programming Interface) is a set of rules that allows two different software programs to communicate with each other, in this case:

> [!PDF|yellow] [[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=46&selection=11,7,13,18&color=yellow|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.46]]
> > For each chip, the API specifies the chip name, the names of its input and output pins, the chip’s intended function or operation, and optional comments.

The rest of them you'll understand by logic inferring from the API of Nand, here is what they should do (already in book):

- Not: outputs the opposite value of it's input value
- And: returns 1 when both inputs are 1, 0 otherwise
- Or: returns 1 when at least one of its inputs is 1, 0 otherwise
- Xor: returns 1 when only one of its inputs is 1, 0 otherwise

There are 2 more complicated ones called the Mux (Multiplexer) and DMux (Demultiplexer), the idea goes as such:

Mux (Multiplexer):

- Inputs: Two data bits (a and b) and one selection bit (sel).
- Outputs: The selected input (either a or b) based on the value of sel.
- Logic: The multiplexer outputs the value of a when $sel = 0$, and the value of b when $sel = 1$

So, in TDLR:

- If $sel = 0$, $out = a$.
- If $sel = 1$, $out = b$.

This is the diagram, truth table, and API of Mux:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 7.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=48&rect=136,445,478,721|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.48]]

DMux (Demultiplexer):

- Inputs: One data bit (input), and a selection bit (sel).
- Outputs: Two output bits (a and b), the data bit sent to one of them based on the value of sel.
- Logic: The demultiplexer sends the input to a when $sel = 0$, and to b when $sel = 1$

This is the diagram, truth table, and API of DMux:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 8.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=48&rect=136,90,476,300|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.48]]

### Multi-Bit Gates

However, computers are often handling multiple bits at the same time, and right now all these gates we know handle single/double bit operations.

In scaling up these gates to process $n$ bits at the same time, the logic is exactly the same. The only difference being that individual bits will be indexed, so that we can access them individually. Like if we want the 3rd bit in the input bits, it would simply be denoted as `in[3]`.

Here is the Multi-bit Not API:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 9.jpg|646]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=49&rect=75,316,538,377|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.49]]

### Multi-Way Gates

But who said in the $n$ bits being processed, each of them needs to have the exact same operation? In multi-way gates, we can extend the logic to allow for different operations on each of the individual bits or groups of bits.

Like the **multi-way Or**, allowing $m$ inputs and returning 1 if at least one of the inputs is 1.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 10.jpg|646]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=50&rect=75,239,537,301|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.50]]

Or the **multi-way multiplexer**, where it selects from one of its $m$ inputs using $k$ selection bits, where $k = \log_2 m$.

Here is it's gate:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 11.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=51&rect=78,602,415,719|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.51]]

The sel bits act as a binary index for selecting one of the $m$ input bits. For example, $sel = 00$ selects in[0], $sel = 01$ selects in[1], $sel = 10$ selects in[2], and so on.

And this is it's API:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 12.jpg|646]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=51&rect=74,418,539,511|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.51]]

(You can infer how the **Multi-bit demultiplexer** works, right?)

## Implementation

> [!PDF|yellow] [[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=52&selection=14,3,23,74&color=yellow|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.52]]
> > n particular, we’ll focus on two general approaches to implementing logic gates: behavioral simulation and hardware implementation. Both approaches play important roles in all our hardware construction projects.

Behavioral simulation is writing out the logic gate's **interface** with a high level programming language. Like using OOP (object oriented programming) to create a class for a chip, and define its attributes & methods.

But... that kinda defeats the purpose of diving deep down here, no?

So that's where Hardware implementation comes in. Instead of using a high level programming language, we write it out using HDL, this would be rather cumbersome to set up on your computer, and so the class just happens to have a website that you can simulate HDL programs.

[https://nand2tetris.github.io/web-ide/chip/](https://nand2tetris.github.io/web-ide/chip/)

Get building.

Implementing the chips were hard... I got stuck on quite a few of them.
