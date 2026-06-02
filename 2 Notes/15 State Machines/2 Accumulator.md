Before, we've been mostly talking about combinational circuits, now it's time to start looking into sequential circuits.

A very simple example of where a sequential circuit is used is for example in the registers (in the CPU) and the memory, storing our intermediate calculation values and instructions/data.

Let's think about a simple one, accumulator, how do we achieve this C code through some circuit?

```c
int s = 0;
int i;

for (i=0, i<5, i++){
	s += x // assume x is some input at every loop
}
```

A first guess might look something like this:

![[Screenshot 2026-03-08 at 3.39.43 PM.png|300]]

Where the output of S is repeatedly sent to the input of the adder, alongside with future information, but this raises 2 concerns:
1. how to initialize the value of s?
2. how do we know when to exist the for loop?

So, we need to introduce a register to this circuit to temporarily store the computation, another input to give S an initial value, and another input to indicate to 'clear' the stored computation values.

![[Screenshot 2026-03-08 at 3.48.07 PM.png|300]]



