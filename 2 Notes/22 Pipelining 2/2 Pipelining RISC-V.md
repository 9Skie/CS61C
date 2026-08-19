This is uh... very similar to PH reading 4.5, I'll just place a table here for a comparison for pipeline vs non pipeline.

- The delay for individual instruction gotten worse for trading throughput

![[Screenshot 2026-07-27 at 9.53.54 PM.jpg|500]]


## Better Understand The Diagram

The 'blue boxes' abstractly represent a part in the data path that relates to a part in the cycle, like fetch (from instruction memory), decode (into registers) etc.

If there's a read operation going on, the box is blue on the right.

If there's a write operation going on , the box is blue on the left.

If the box is dim, that means this part is not accessed for this instruction.

![[Screenshot 2026-07-27 at 9.58.49 PM.jpg|500]]