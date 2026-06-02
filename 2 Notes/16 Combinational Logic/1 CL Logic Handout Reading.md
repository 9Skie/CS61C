While we've fiddled around with the literal circuits and then simplified them down into abstract boxes, what should be the combinational logic in those circuits? 

Look at this adder, it takes 2 different 2 bit inputs A and B, and outputs a 3 bit output C.

![[Screenshot 2026-06-01 at 11.36.40 AM.png|200]]

How would we be able to use the simple combinational circuits that we learnt: AND, OR, XOR, NOT... etc to actually construct this adder?

![[Screenshot 2026-06-01 at 11.41.58 AM.png|200]]

We could treat this process as a black box for now, and just take a look at the  functional relationship between input values and output values. As for each input pattern of 1’s and 0’s applied to the CL block, there exists a single output pattern, it's a 1 to 1 relationship.

We could list that entire input/output relationship out, and it's called a truth table.

![[Screenshot 2026-06-01 at 11.42.49 AM.png|150]]

Ok, what to do with this now? Well, we turn to boolean algebra. Invented by George Boole, it was a mathematical algebra system where the variables could only be true or false. 

Later, Claude Shannon (the father of information theory) showed (for his Master’s thesis) how to map Boolean algebra to digital circuits, and so, we can express all of our circuits in boolean algebra.

![[Screenshot 2026-06-01 at 12.00.33 PM.png]]

Ok, but how does this tie to a truth table? If we can somehow reverse engineer a boolean algebra expression from a truth table, we can then reverse engineer the circuit.

We can use this method called **sum of products**.

1. We start with a  truth table that lists every possible input combination and the corresponding output.
2. To construct a circuit from the truth table, we look at every row where the output is `1`.
3. For each row where the output is `1`, we create an AND expression that exactly matches that input combination.

![[Screenshot 2026-06-01 at 2.35.39 PM.png|400]]

Following that, through algebraic manipulation by boolean algebra rules, the expression can be simplified then translated to a circuit of logic gates.
- I'm not so interested in memorizing all the rules to boolean algebra

![[Screenshot 2026-06-01 at 3.03.47 PM.png|400]]

The point of simplifying a circuit down is... well, many, For one, you save literal silicon because you require fewer transistors for your chips. And from a computer science perspective, you also make the latency of your circuits go down because there's less parts in it.
![[Screenshot 2026-06-01 at 3.06.26 PM.png|400]]

In conclusion, when we just have a truth table, we have to derive the sum of products boolean expression from it, then simplify it down using boolean algebra rules to create an efficient circuit of logic gates.

![[Screenshot 2026-06-01 at 3.08.14 PM.png|400]]