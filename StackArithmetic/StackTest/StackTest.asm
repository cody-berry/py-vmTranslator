// add
@SP
AM=M-1
D=M
A=A-1
D=D+M
M=D
// sub 
@SP
AM=M-1
D=M
A=A-1
D=D-M
M=D
// neg 
@SP
A=M-1
M=-M
// not 
@SP
A=M-1
M=!M
