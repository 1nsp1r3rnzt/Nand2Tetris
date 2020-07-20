// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.


@i
M=0

//Final Result = Clear memory
@R2
M=0

(LOOP)
@R0
D=M                   //Load R0
@ENDLOOP
D;JEQ                 //R0=0,Result = 0

@R1      // R1 times
D=M
@i
D = D - M         // I-R2
@ENDLOOP
D;JEQ                 //I-R2=0

//Read R0 to data
@R0
D=M
@R2
D=D+M
M=D       //R2 = M+D(R0)

@i
M=M+1         ///increment i

@LOOP
0;JMP



(ENDLOOP)
@ENDLOOP
0;JMP