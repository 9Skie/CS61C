// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

// Bruh since there is no multiply implemented we are doing this instead
// R2 = R1 * R0 = R0(1) + R0(2) + R0(3) + ... R0(R1)
// So we need some loop instead
@count
M=0
@sum
M=0

// Check if count = R1, then we stop looping
(Loop)
@count
D=M
@R1
D=D-M
@End
D;JEQ

// If not, we add R0 to sum, count = count + 1
@sum
D=M
@R0
D=D+M
@sum
M=D
@count
M=M+1

// Loop back to loop
@Loop
0;JMP

// End, put value in R2
(End)
@sum
D=M
@R2
M=D


