> [!PDF|yellow] [[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=59&selection=7,0,12,10&color=yellow|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.59]]
> > In this chapter we build a family of chips designed to represent numbers and perform arithmetic operations. Our starting point is the set of logic gates built in chapter 1, and our ending point is a fully functional Arithmetic Logic Unit.

The ALU is something essential to the CPU. It is the circuit that performs all arithmetic on bits, like addition and multiplication. It can also perform boolean algebra on bits, like And, Or comparisons.

But first, we need to understand how numbers are represented in the binary sense.

## Binary Numbers

Normally, we describe numbers in a **base-10 system**. It is based on powers of 10, where each place value represents a power of 10.

However, computers use a **base-2 system**. It is based on powers of 2, where each place value represents a power of 2.

![[2 Boolean Arithmetic 1.png|646]]

Because fundamentally as we know, computers are built by transistors, which can be either 1 of 2 states, on or of, corresponding to 0 and 1 respectively. And these binary states are the basis of all higher-level processes, from a gate to a CPU, which is called *digital logic*.

However, as computers are fixed machines, there is an upper and lower limit which we allow the number of bits to represent a number, typically this is by $2^n$, like $8, 16, 32, 64$
and onwards.

That's how we have Windows 64 or Linux 64, meaning they use 64 bits to represent a single number on the computer, here's a little [FAQ](https://support.microsoft.com/en-us/windows/32-bit-and-64-bit-windows-frequently-asked-questions-c6ca9541-8dce-4d48-0415-94a3faa2e13d)from Microsoft.

### Binary Addition

Binary addition happens from right to left, similar to how normal addition would go, we call the right most bit the *least significant bit* (LSB) and the left most bit the *most significant bit* (MSB).

A *carry* is just the resulting value of the bitwise addition carried over to the next bit, however, if the MSB addition generates a carry of 1, we have an overflow, meaning we store numbers with $n$ bits, but the number in result of calculation requires $> n$ bits to store.

![[2 Boolean Arithmetic 2.png|500]]

### Two's Complement

But, how do we represent positive and negative numbers? All that we shown above was positive numbers.

Today the used system is called *two's complement*, basically where if we have a word size of $n$ bits, the representation for $-x$ is $2^x - x$.

(I'm using the book's example here)

In a 4 bit system, $-7$ would be $2^4 - 7 = 9$, and it would take place in 9's original binary representation, `1001`.

There's 2 clever things about this system:

1. the positive binary representation of 7 is `0111`, if you did $-7 + 7$ in the binary sense, `0111 + 1111 = 0000` , which would result in 0 (if overflow bit ignored).
2. it basically "mapped" the negative numbers from behind the positive numbers on the number line, to in front of them.

| Binary | Decimal (Positive) | Decimal (Two's Complement) |
| --- | --- | --- |
| 0000 | 0 | 0 |
| 0001 | 1 | 1 |
| 0010 | 2 | 2 |
| 0011 | 3 | 3 |
| 0100 | 4 | 4 |
| 0101 | 5 | 5 |
| 0110 | 6 | 6 |
| 0111 | 7 | 7 |
| 1000 | 8 | -8 (16 - 8) |
| 1001 | 9 | -7 (16 - 7) |
| 1010 | 10 | -6 (16 - 6) |
| 1011 | 11 | -5 (16 - 5) |
| 1100 | 12 | -4 (16 - 4) |
| 1101 | 13 | -3 (16 - 3) |
| 1110 | 14 | -2 (16 - 2) |
| 1111 | 15 | -1 (16 - 1) |

So, this also made the range of numbers change:

- Positive: $0$ to $2^n - 1$
- Two's complement: $-(2^{n-1})$ to $2^{n-1} - 1$

A simple way to understand two’s complement is to think of the most significant bit (MSB) as representing a negative value. For example, in the binary number 1000, we can treat the 1 as representing $-8$, and 1001 as $-8 + 1 = 7$.

> It's not wrong, right?

# Arithmetic Chips

Now that we understand how numbers are represented in a binary fashion, and how binary addition works, we'll now turn to how this is implemented with logic gates and circuits.

To build an ALU, we will start with the half-adder, then move on to the full-adder, followed by the adder, and then the incrementer, ultimately leading us to the ALU.

- Half-adder: add 2 bits
- Full-adder: add 3 bits
- Adder: add 2 $n$ bit numbers
- Incrementer: add 1 to any number

I'll simply give the diagram for all of them here.

Half Adder:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 13.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=66&rect=128,258,497,493|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.66]]

Full Adder:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 14.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=67&rect=127,466,496,730|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.67]]

Adder:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 15.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=67&rect=122,138,502,357|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.67]]

The incrementer chip will be ignored for now.

## The ALU

This ALU does not have multiplication, division, or floating-point operations, which will be implemented through software. It is worth noting that in practice, ALUs typically handle these basic arithmetic functions with hardware.

![[2 Boolean Arithmetic 3.png|500]]

The HACK ALU has two 16-bit inputs, representing the operands x and y. It also has a 16-bit output, which represents the computation result, along with a zero flag (zr) and a negative flag (ng), indicating whether the output is all zeros and whether it is negative.

Here's an example of it working in action with $x - 1$, with $x = 2$.

> Yes this is just the book's example

1. The control bits of the ALU will be set to 001110
2. 0 - zx, so we are not setting x to 0
3. 0 - nx, so we are not inverting x to it's two's complement
4. 1 - zy, so we are setting y to 0
5. 1 - ny, so we are inverting y to it's two's complement
6. 1 - f, so we are adding values, not doing bitwise and
7. 0 - no, the output is not negated

There is a whole big table of all the functions that this ALU should have.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 16.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=70&rect=107,294,506,736|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.70]]

## Implementation

This, is, really, confusing!

While the authors have said that they just used "backward reasoning" to come to make the ALU...

> [!PDF|yellow] [[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=72&selection=4,0,40,35&color=yellow|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.72]]
> > It may be instructive to describe the thought process that led to the design of our ALU. First, we made a tentative list of the primitive operations that we wanted our computer to perform (right column of figure 2.5b). Next, we used backward reasoning to figure out how x, y, and out can be manipulated in binary fashion in order to carry out the desired operations. These processing requirements, along with our objective to keep the ALU logic as simple as possible, have led to the design decision to use six control bits, each associated with a straightforward operation that can be easily implemented with basic logic gates.

It doesn't click with me as a systematic way to develop any type of circuits! Last time I was just scrambling left and right hoping the combinations I made worked, and I don't think that will get me far this time around.

They gave us a bit of steps to follow, like figure out the logic, write the HDL code, test and debug...

> [!PDF|yellow] [[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=73&selection=0,0,4,9&color=yellow|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.73]]
> > Throughout this section, when we say “build/implement a logic design that …,” we expect you to (i) figure out the logic design (e.g., by sketching a gate diagram), (ii) write the HDL code that realizes the design, and (iii) test and debug your design using the supplied test scripts and hardware simulator

But how is that enough? I gotta figure out a way how people make circuits in the first place, what's the thinking process?

This is a pretty good video discussing about it: https://www.youtube.com/watch?v=CwnfYzYnsuA
