We know why people turn to parallelism, because there's a dead cap for increasing the performance of processors by simply increasing their clock speeds.

And we see a lot of newer general applications of parallelism, ones that I like a lot as well, and it all ties down to linear algebra and it's applications:

One of such is machine learning:
- ![[Screenshot 2026-08-14 at 9.12.27 PM.jpg|500]]

Another of such is computer graphics:
- ![[Pasted image 20260814211325.png|500]]


Speaking of which, we can quickly review matrix multiplication here:

![[Screenshot 2026-08-14 at 9.15.54 PM.jpg|500]]

$C=A\times B$

each element in $C$ is calculated by taking the dot product between a row of $A$ and a column of $B$:

$C_{ij}=\sum_k(A_{ik}B_{kj})$

In the image, the highlighted row from $A$ and highlighted column from $B$ are multiplied together and summed to produce one value in $C$.

The important idea for parallelism is that each value in the output matrix $C$ can be calculated independently. Therefore, different workers can calculate different elements of $C$ at the same time, making matrix multiplication a very parallelizable operation.