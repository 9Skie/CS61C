## Unsigned Integers

Addition in binary works just as similar it is in denary.

![[Pasted image 20260206103859.png|300]]

Binary overflow happens your final answer requires more bits to represent the number than the computer allows.

Like in the above image, it needs 5 bits to represent the number, but if you were only given 4, the computer would only store `0100` and the `1` on the left would be discarded.
-  the bits are stored inclemently from the LSB (least significant bit) all the way to the maximum length.

This is what we call an 'unsigned integer', it only stores values incremental from 0 upwards, 1, 2, 3, 4... it cannot store negative numbers.

![[Screenshot 2026-02-06 at 10.46.34 AM.png|400]]

---
## Signed Numbers

One simple solution to this idea is just make the left most bit to represent a sign instead, either positive `0` or negative `1`.

![[Screenshot 2026-02-06 at 10.52.03 AM.png|500]]

And through this representation, we can just flip the bits of a positive number, to get it's corresponding representation of the negative value.

![[Pasted image 20260206145510.png|500]]

But there are shortcomings of this representation:
- it's arithmetic is not straight forward
	- like (-1) + (-1) = 10000000 + 10000000, that creates overflow
- there are duplicate representations with ambiguity
	- 0 can be 00000000, or 10000000

So there was a better solution to all of this called two's complement.