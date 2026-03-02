The idea behind two's complement is to try to solve the problems that one's complement has left behind, by making the largest bit represent a negative value.
- this forces 00000000 to be 0, no duplicates
- and makes the addition/subtraction of the values circular

![[Screenshot 2026-02-06 at 3.17.59 PM.png|500]]

How should we interpret the circular understanding of this number line? Well, look below.
- If you move clockwise on this wheel, you will `add 1` to the representation.
- If you move anti-clockwise on this wheel, you will `subtract 1` to the representation.

![[Pasted image 20260206150914.png|500]]

Some people might interprit it as 'pulling' the unsigned representation of the number line from [0, 255] to [-128, 127] using the same bits.
- It's like having the numbers [0, 1, 2, 3, 4... 255] all being -128 ($2^8$) from them!