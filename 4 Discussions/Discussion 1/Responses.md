1. Depending on the context, the same sets of bits may represent different things.

Obviously yes, it can represent audio, images, text... whatever. But fundamentally, bits store representations of numbers, but it could represent various codexes.
- An integer follows the codex of 2's complement
- A floating point number follows the floating point arithmetic standard. 
- A unsigned integer follows basic binary addition


2. It is possible to get an overflow error in Two’s Complement when adding numbers of opposite signs.

That's... how we get 0, no? Take the case of 1 + (-1) under a 8 bit representation, `00000001` + `11111111` would result in a 9 bit number in binary arithmetic, but the computer can't store that and we get `00000000`, which arithmetically correctly is 0.


3. If you interpret a N bit Two’s complement number as an unsigned number, negative numbers would be smaller than positive numbers.

No, in fact it would be much larger, since the LSB is used to store the biggest possible value, it originally used to be a negative value in 2's complement, but now it's positive when we turn it unsigned.

For example, `10000000` is -128, while the biggest possible representation of a positive number is `01111111`, 127. If we treat `10000000` unsigned, it would be larger than the biggest possible 2's complement positive number.


4. If you interpret an N bit Bias notation number as an unsigned number (assume there are negative numbers for the given bias), negative numbers would be smaller than positive numbers.

No idea about bias notation

---
## Unsigned Numbers

![[disc01.jpg|500]]

[[disc01.pdf#page=1&rect=66,71,443,132|disc01, p.1]]

It's indeed basically a summation of $r^i * d_i$, given r is the base of choice, but d must range from [0, r] as a value.

![[disc01 1.jpg|500]]

[[disc01.pdf#page=2&rect=66,467,443,647|disc01, p.2]]

1. hex = 0x93, denary = 147
2. binary = 0b00111111, hex = 0x3F
3. hex = 0x24, denary = 36
4. hex = 0x00, binary = 0b00000000
5. hex = 0x27, binary = 0b00100111
6. binary = 0b000110110101, hex = 0x1B5
7. binary = 0b0000000100100011, denary = 291


![[disc01 2.jpg|500]]

[[disc01.pdf#page=2&rect=94,236,383,284|disc01, p.2]]

- 2 Ki = 2^10


---
## Signed Integers

a. What is the largest integer? What is the result of adding one to that number?

1. largest: 255, adding 1: overflow, 0
2. idk
3. largest: 127, adding 1: -128


b. How would you represent the numbers 0, 1, and -1?

1. 0b00000000, 0b00000001, cannot
2. 0b00000000, idk
3. 0b00000000, 0b00000001, 0b11111111


c. How would you represent 17 and -17?

1. 0b00010001, cannt
2. idk
3. 0b00010001, 0b11101111


d. What is the largest integer that can be represented by any encoding scheme that only uses 8 bits?

it would be $n^8$, as each bit can only represent a binary choice of yes or no, the problem is we can choose any arbitrary base of n, so there is no upper limit


e. Prove that the two’s complement inversion trick is valid (i.e. that x and (not x) + 1 sum to 0).

How would I prove this? For all cases?


f. Explain where each of the three radices shines and why it is preferred over other bases in a given context.

Decimal is what normal math and humans base their understanding of everything is on, it's what all of our math is based upon.

Binary is what the computer uses for everything, it's the fundamental state which electricity can be for a computer's transistors.

Hexadecimal is not really used, it's just binary disguised but more easily readable to the eyes of someone dealing with binary.