 With our new understanding the flip flop and the clock, we can fully understand how the timings of the accumulator works.

Assume that there is this much (as shown in diagram) delay for the addition, and for the period of sampling after clk change.

![[Screenshot 2026-03-08 at 5.11.42 PM.png|300]]

The values in our circuit will be as such:

![[Screenshot 2026-03-08 at 5.12.19 PM.png|500]]

And I'll explain every step:

1. the reset is set to 1, this overwrites any value in the register into 0
2. when the clock ticks (the 1st time), it samples that reset value, and overwrites s(i-1) as 0
	- as you can see, there is a delay between the clock tick and the s(i-1) value change, that's the clk-to-q delay
3. the value of x(0) is loaded into x(i), the adder adds them
4. the resulting value is placed at s(i)
	- again notice the delay from adding
5. the second clock ticks, and we load the value of s(i) into s(i-1), there is delay (loading)
6. x(1) is loaded, and then again x(i) adds with s(i-1), there is delay (adding)
7. the value is stored at s(i)
8. we repeat this similar cycle from step 3, except no longer with x(0) but whatever x value is loaded