Again we are here, the idea is simple, make a circuit that when it sees 3 consecutive 1's it returns a 1, else return 0.

![[Screenshot 2026-03-09 at 11.17.48 AM.png|400]]

As we've already seen the the adder, which, itself is a form of a finite state machine:
- a combinational logic which can take in some new input with a previous state, to make a next state and some output
- a register that stores the current state (next state)

![[Screenshot 2026-03-09 at 11.25.14 AM.png|500]]

And such, we can combine multiple finite state machines together to form more complex sequential circuits. 

The output of one finite state machine can become the input of another, and similarly the output of that second machine can feed back as input to the first.

By connecting them in this way, larger systems can be built where different state machines interact with each other to control the overall behavior.

![[Screenshot 2026-03-09 at 11.32.26 AM.png|400]]

