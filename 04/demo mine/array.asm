//for (i=0;i=n;i++)
//{
//	arr[i]=-1
//}


//Assign space for array
//Assign array a beginning space address
//assign n as total items
//Assign i to 0
//goto Endloop if i = n
//assign arr[i] = -1
//increment i to i+1
//Go to beginning of loop
//Endloop

@100
D=A
@arr
M=D


@10
D=A
@n
M=D

@i
M=0

(LOOP)
@i
D=M
@n
D=D-M
@END
D;JEQ


//Get right address

@arr
D=M              //D= Arr address
@i
A=D+M
M=-1

@i
M = M+1 


@LOOP
0;JMP


(END)
@END
0;JMP


