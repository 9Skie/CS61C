So... we got add, now we are gonna go to subtraction! Subtraction looks very identical to addition in terms of it's instruction format (as well as data path), so we are just going to tweak our data path by a tiny bit.

![[Screenshot 2026-07-08 at 11.13.05 AM.png|500]]

If you take a look, only `inst[30]` (the 30th bit of the instruction) is different for add and sub, where sub is a 1, and add is a 0.

So... we just need to add a little control bit at the ALU to toggle it's operation between addition and subtraction! Let's call it `ALU Sel`.

![[Screenshot 2026-07-08 at 11.19.11 AM.png|500]]

But as smart as you, you can go, wait a minute, if we can use 1 bit to toggle between addition and subtraction, we can use 2 bits to toggle between addition, subtraction, multiplication, and division! By extension, we can use 3 bits for 8 different operations!

These are all implemented in RISC-V already by decoding funct3 and funct7 fields, to select the appropriate ALU function.

![[Screenshot 2026-07-08 at 11.23.03 AM.png|500]]