// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

// The screen should be cleared... as in returned to the default white?
// How do we deal with IO operations? I dunno
// Oh it was there... @Screen & @KBD

// Screen Size (In 16 Bits) = 8192 = 256 x 512 / 16 
@8192
D=A
@ScreenSize
M=D

// Keyboard input receive
(Loop)
@KBD
D=M

// Is it pressed? If it is 0 nothing is pressed, elsewise something is
@NoPress
D;JEQ

// Turn screen black
@count
M=0
(LoopBlack)
@count
D=M

// Turn 1 pixel registor (16 bits) black, move to next pixel registor
@SCREEN
A=D+A
M=-1
@count
M=M+1
D=M

// Check if we are done with 8192 pixel registors
@ScreenSize
D=D-M

// Loop back to beginning
@Loop
D;JEQ

// Continue black loop
@LoopBlack
0;JMP

// Turn screen white
(NoPress)
@count
M=0
(LoopWhite)
@count
D=M

// Turn 1 pixel registor (16 bits) white, move to next pixel registor
@SCREEN
A=D+A
M=0
@count
M=M+1
D=M

// Check if we are done with 8192 pixel registors
@ScreenSize
D=M-D

// Loop back to beginning if conditional met
@Loop
D;JEQ

// Or we continue white loop
@LoopWhite
0;JMP
