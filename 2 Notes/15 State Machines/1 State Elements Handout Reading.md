Basically, we already talked about combinational circuits, and need to know about state circuits now.

Say we wanted to achieve this circuit:

![[Screenshot 2026-03-09 at 10.08.08 AM.png|300]]

An adder that adds into itself is simply not enough, as there's no understanding of S's initial value, and how to reset the values at the end of the for loop.

![[Screenshot 2026-03-09 at 10.09.53 AM.png|300]]

(And we've already explained how this digital circuit worked, I'll not explain it again)

![[Screenshot 2026-03-09 at 10.11.06 AM.png|300]]

---
## Pipelining

We saw how a register is needed to make an adder possible, and now we'll see how it is able to speed up also combinational circuits.

Take this circuit for example:

![[Screenshot 2026-03-09 at 10.18.35 AM.png|300]]

The clock cycle rate is severely limited, as we want to simultaneously capture values into the input register on clock tick and also capture values into the output register.

Because you would have to wait for the value to propagate through the entire **combinational path**, the adder and shifter between the two registers before the next clock edge.

If the clock period becomes too short, then we won't even wait for the adder and shifter to finish it's calculation before we capture the next value, which would be wrong.

![[Screenshot 2026-03-09 at 10.23.15 AM.png|400]]

So we can improve upon this idea through using additional registers in the process.

![[Screenshot 2026-03-09 at 10.24.04 AM.png|300]]

You might wonder how this speeds things up, aren't we just adding more delays in between the adder and register? We'd have to write to the second register, then the third register.

Well, the idea is that instead of waiting for an adder and shifter delay for 1 clock cycle, we just have to wait for an adder/shifter + value copy delay, which is much shorter than the 2 gates combined.

So, yes, this approach would make the inputs more delayed in clock cycles, as in 1 clock cycle the data would be going from the inputs to the adder and the intermediate register, and the next clock cycle to the shifter and the final register. But, as we can directly increase our clock speed because of each shorter cycle, it actually is faster than the previous approach.

![[Screenshot 2026-03-09 at 10.28.06 AM.png|400]]

It does feel incredibly counter intuitive that adding more overhead to a circuit makes it faster.

---
## Finite State Machines

Adding on top of the idea of registers and state circuits, we come to finite state machines.

![[Screenshot 2026-03-09 at 10.42.51 AM.png|300]]

It... basically looks like markov chains, but instead of describing transition states with probabilities, it's a fixed, guaranteed interaction based on the previous states.

```
next_state = f(current_state, input)
```

Why do we do this? Well, FSMs are needed whenever a system’s behavior depends on **what happened before**.

The PDF gave an example of a circuit that is used to detect the occurrence of three 1’s in a row in an input sequence of bits, which, the circuit must remember previous bits somehow to detect three 1's in a row.

The diagram for s0, s1, s2 simply means 'seen 0 1s, seen 1 1s, seen 2 1s'.

![[Screenshot 2026-03-09 at 10.45.15 AM.png|300]]

The number of possible states we can store depends on the number of bits inside the register, if you have **2 flip-flops**, you can represent 4 states:

```
00
01
10
11
```

Now, then the circuit for such a thing shouldn't be hard to understand, we have a combinational logic circuit (to determine state transitions), a register that just keeps feeding itself into the input and is part of the output (to keep/update state transitions), and new coming inputs/outputs.

![[Screenshot 2026-03-09 at 10.53.21 AM.png|300]]

In a way... this is sort of a generalized version of the adder's sequential logic.