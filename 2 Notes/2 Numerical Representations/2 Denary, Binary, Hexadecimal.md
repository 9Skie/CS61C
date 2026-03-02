Denary is usually how humans think of numbers, in base 10.

![[Screenshot 2026-02-04 at 1.03.43 PM.png|500]]

Binary is how computers think about numbers, in base 2, this is because fundamentally the computer relies on a transistor, which can be either on (1) or off (0).

![[Screenshot 2026-02-04 at 1.05.06 PM.png|500]]

Hexadecimal is in base 16, which is also used on computers! It's only purpose is to make the programmer reading long binary digits less painful.

![[Screenshot 2026-02-04 at 1.07.30 PM.png|500]]

---
## Conversion Between Denary and Binary

It's not hard, just think about going left to right, how many of (col n) can you fit inside that column?

If it's 1, we put that down, and subtract the value from our original value. If it's 0, we put that down and move to the next column.
> This is because in binary, you can only choose to put in 1, or 0.

![[Pasted image 20260204131644.png|300]]

A mathematical way is to just keep dividing the number by 2, and it's remainder will make up the binary bits.

![[Pasted image 20260204131848.png|200]]


---
## Conversion Between Denary and Hex

It's the exact sam idea as binary, except now instead of only being able to fill in 1 or 0 to the question 'how many of (col n) can you fit inside that column?' We can fill in 0-16.

![[Screenshot 2026-02-04 at 1.22.02 PM.png|500]]

The division trick works still.

![[Pasted image 20260204132346.png|300]]

---
## Conversion Between Binary and Hex

There's just a big table of how binary converts to hex.

![[Pasted image 20260204130719.png|300]]

And every time when you want to convert binary to hex, you just go 4 bits at a time and recall back to this table of how binary maps to hex.

![[Pasted image 20260204141513.png|400]]

Which just means working this process backwards when you convert hex into binary.

![[Pasted image 20260204141902.png|400]]

---
## When to use What Base?

Well, denary is great for our use, right? All of our maths is based on this anyways.

Hex is... well, it doesn't really exist, it's just for looking at a string of binary digits for the ease of your eyes.

Binary is what your computer uses anyways!