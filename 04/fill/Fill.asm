// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.


(LOOP)
@i    //initialize i
M=0

@8192                 // we have 512 rows and 256 cols, total cell = 512*256 but each register has 16 cells. so 512*256/16
D=A
@n
M=D


@KBD
D=M
@WHITESCREEN
D;JEQ   //D=0;JMP TO WHITE SCREEN


(BLACKSCREEN)
@i
D=M
@n
D=M-D
@LOOP
D;JEQ        //VERIFY WHOLE SCREEN IS WRITTEN

@i
D=M

@SCREEN
A=A+D
M=-1


@i
M=M+1

@BLACKSCREEN
0;JMP

//LOOP TO WRITE THE SCREEN
//OUTER LOOP
//i=512



(WHITESCREEN)
@i
D=M
@n
D=M-D
@LOOP
D;JEQ        //VERIFY WHOLE SCREEN IS WRITTEN


@i
D=M

@SCREEN
A=A+D
M=0


@i
M=M+1

@WHITESCREEN
0;JMP
//JUMP BACK TO LOOP
@LOOP
0;JMP



