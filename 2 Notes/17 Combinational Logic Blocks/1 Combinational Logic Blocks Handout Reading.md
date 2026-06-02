Now, we are coming to (a close) to these circuits, and in this note, we'll discuss about data multiplexors, an arithmetic/logic unit, and a adder/subtractor circuit.

## MUX

The simple idea of a mux is just... select between 2 bits, through the toggle of 1 bit.
- when s=0, C=A when s=1, C=B

This particular mux example is a called a 2-to-1 multiplexor. It is 2-to-1 because it takes two data inputs and outputs one of them, and so we only need 1 selector bit.

![[Screenshot 2026-06-02 at 11.36.20 AM.png|300]]

You could use the sum of products to derive this, and that's kinda boring! I personally like to think it through first:
- Think s as like an index toggle, if it's 0, we toggle A's index, if it's 1, we toggle B's index
- Then, if s is 0 we should select A, right? so it must be `not s` for A to be selected, if s is 1 we should select B.

So the final gates should look like this:

![[Screenshot 2026-06-02 at 2.34.42 PM.png|300]]

Now, this intuition can carry over for more complicated mux inputs, what if we have 4 inputs and we need to select 1? Well, we would need 2 selector bits s, and... use these bits to perform somewhat of a binary search?

![[Screenshot 2026-06-02 at 2.44.44 PM.png|300]]

The first layer of muxes uses the s0 input to narrow the four inputs down to two, then the second layer uses s1 to choose the final output.

## ALU

We are going to consider the design of a simpler version of the ALU, one that only includes only for basic functions, ADD, SUB, bitwise AND, and bitwise OR.

So at it's heart, we can re-use the mux logic we saw above, as the output are simply picking from 4 independent results:
- when S=00, R=A+B 
- when S=01, R=A-B 
- when S=10, R=A AND B 
- when S=11, R=A OR B

![[Screenshot 2026-06-02 at 4.34.58 PM.png|300]]

Now, this is a bit counter-intuitive, since previously in programming, we usually thought that it's the wiring logic that goes first, then computation, like if statements, we usually think the process is:

```python
if something_happens:
	print("I Go!")
else:
	print("I Go Instead!")
```

But in hardware logic, we first calculate all the operations, then choose which operation's result we will use.

There's still however, the add/subtract which we do not know how to implement.

## Full Adder

So a 1-bit adder needs to consider:

![[Screenshot 2026-06-02 at 5.23.43 PM.png|300]]

```
inputs:
	a
	b
	c(i) - carry_in

outputs:
	c(i+1) - carry_out
	s(i) - sum
```

By careful inspection of the truth table, we can come to these conclusions for what each output requires for the minimal input.

![[Screenshot 2026-06-02 at 5.28.01 PM.png|300]]

Now, we can wire these 1 bit adders together to create an n-bit adder. All we need to do is to wire the carry-out output of one stage into the carry-in input of the next, from least significant to most:

![[Screenshot 2026-06-02 at 6.10.23 PM.png|400]]

This does create latency, however, as the 1st bit's output goes into the 2nd bit, and then into the 3rd bit... and so on, there will be 32 units of delay in this case for the naive adder.

For subtraction, we really just need to invert B into negative B through a not gate, then have some way to select between them, which we can use XOR. 

So we stick an XOR on each bit of B, wire the other input to SUB, and boom: SUB=0 adds, SUB=1 subtracts.

![[Screenshot 2026-06-02 at 7.40.42 PM.png|400]]

Uh... this image did leak an answer for overflow, which, is to determine if the carry into the MSB differs from the carry out of the MSB.

## Overflow

Overflow means the result of signed arithmetic doesn't fit, and from such, your first instinct might be "overflow = final carry-out is 1", but that isn't true.

- `0111 + 0001 = 1000` (7+1=-8): overflow, carry-out is **0**
- `1111 + 1111 = 1110` (-1+-1=-2): no overflow, carry-out is **1**

Trace `0111 + 0001`:

```
  0 1 1 1   (7)
+ 0 0 0 1   (1)
-----------
c:  1 1 1    ← carries between bits
  1 0 0 0   (-8, wrong!)
```

Carry into MSB = 1, carry out = 0. They differ → overflow.

Trace `1111 + 1111`:

```
  1 1 1 1   (-1)
+ 1 1 1 1   (-1)
-----------
c:1 1 1 1    ← carries
1 1 1 1 0   (drop extra → 1110 = -2 ✓)
```

Carry into MSB = 1, carry out = 1. They match → no overflow.

If the lower bits push a carry *into* the MSB but the MSB doesn't push one *out*, the sign flipped unexpectedly. 

If both happen or neither happen, the sign is fine. XOR is literally "are these two bits different?" So one XOR gate on the leftmost full adder gives you overflow.