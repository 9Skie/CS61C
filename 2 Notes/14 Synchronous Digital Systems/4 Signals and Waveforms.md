Is this becoming a signals and system class? Sort of... at least this class is.

We've talked about clocks at first already, and we've seen from the handout, but just looking at the signal in this adder circuit, we'll realize that signals in the circuits are noisy, and that they can be delayed.

![[Screenshot 2026-03-05 at 9.38.56 PM.png|500]]

Usually we group waveforms together into 'words', essentially meaning some bit of data gets interpreted together.

![[Screenshot 2026-03-05 at 9.42.50 PM.png|500]]

Like in this case, 4 bits in interpreted as 1 byte, nothing crazy.

---

There are two main types of circuits. One type behaves like a pure function in mathematics: it receives inputs and immediately produces outputs based only on those inputs. These are called **combinational circuits**.

The other type depends not only on the current inputs but also on its previous state. These circuits retain information over time, and are therefore called **sequential circuits**.

![[Pasted image 20260305215432.png|500]]