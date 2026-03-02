As we know, anything on the computer fundamentally is represented by numbers, and all numbers are represented by bits.

Here are clean, concrete examples you can drop straight into notes. No fluff.

1. **Characters (text)**
	- Characters are **numbers mapped by a lookup table**.
		- Example: ASCII / Unicode
		    - 'A' → 65
		    - 'a' → 97
		    - '0' → 48
	- So text is just a sequence of integers, stored in bytes (or multiple bytes for Unicode).

2. **Audio**
	- Audio is stored as **discrete samples of amplitude over time**.
	- The interval between sampling is the **sample rate**
	- The interval which sound vibrations are recorded is the **Amplitude range 

So audio is literally:

```
[120, 132, 128, 140, ...]
```

Each number = air pressure at that instant.

3. **Images**
	- Images are **2D grids of pixels**, each pixel is a number (or set of numbers).
	- Common format: **RGB**
		- Each channel usually 8 bits
		- Range per channel: **0–255**
  
Example pixel:

```
[R, G, B] = [255, 0, 0]   // red
```

So an image is:

```
height × width × 3 numbers
```

 4. **Programs**
	- Programs are **numbers interpreted as instructions**.

Example:

```
10110000 01100001
```

Might mean:
> “Move the number 97 into a register”

Source code is text → numbers → instructions → electrical signals.

---

### TLDR

Everything on a computer—text, sound, images, video, programs—is just **numbers**, and those numbers are stored as **bits**, interpreted differently depending on context.