 
@j       //j=0
M=0  
 
@i         //i=0
M=0 


@8192   
D=A
@n
M=D

(LOOP1)
@SCREEN         //load screen to addr1
D=A
@addr1
M=D 


(LOOP)           //Read keyboard
  @KBD
  D=M
  @END1
  D,JEQ        //if no input then jump to end loop


 @addr2         //
 A=M              //A = M[addr2]
M=-1           //M=-1 
@i             
M=M+1       //Increment m[i] = m[i]+1
@1              
D=A        // D = 1


  @addr2        //Jump to register[addr2]  
  M=M+D         //M[addr2] =M[addr2]+1(From data) 
  @LOOP         
0;JMP            //Jump to loop

(END1)       
@SCREEN              
D=A        
@addr1           
M=D           //M[addr1] = SCREEN


(END)     
@KBD 
  D=M             //D = M[KBD]
  @LOOP1 
  D,JNE          //JUMP TO LOOP1 IF KEY IS PRESSED
 
 @addr1              
 A=M           //A = M[ADDR1]              
M=0            //M=0
@j              //load j
M=M+1          //J=J+1
@1              
D=A            //D=1
  @addr1       //@Screen
  M=M+D        //M[addr1] = m[addr1]+1
  @END         //jump to end
0,JMP
 
 @ENDALL
 0,JMP
