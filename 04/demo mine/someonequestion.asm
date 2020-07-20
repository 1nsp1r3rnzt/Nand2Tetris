@SCREEN
D=A

@screen
M=D

@8192
D=A

@n         //n=8192
M=D

@i     //i=0
M=0

(LOOP)   
@i     //i=0
M=0

@KBD   //Load keyboard bit
D=M
@BLACK  // Jump to BLACK label when key is pressed.
D;JNE

@WHITE // Jump to WHITE label when key is not pressed.
D;JEQ
@LOOP
0;JMP

(BLACK)
@i            //Read i
D=M
@n           
D=D-M        //i-n


@LOOP     // Jump if i-n=0
D;JEQ

@screen   //read screen variable

D=M

@i
A=D+M   // A = screen + i

M =-1  // Write -1

@i     

M=M+1     //i = i+1

@BLACK
0;JMP

(WHITE)

@i        //Read i  
D=M

@n           //Read n
D=D-M             //i-n
 
@LOOP        //JUMP BACK TO LOOP WHEN WRITTEN      

D;JEQ

@screen

D=M

@i

A=D+M

M=0

@i

M=M+1

@WHITE

0;JMP

