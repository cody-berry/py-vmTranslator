// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 333
@333
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 888
@888
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 3
@static.3
D=M
@SP
M=M+1
A=M-1
M=D
// push constant 1
@static.1
D=M
@SP
M=M+1
A=M-1
M=D
// sub 
@SP
AM=M-1
D=M
A=A-1
D=D-M
M=D
// push constant 8
@static.8
D=M
@SP
M=M+1
A=M-1
M=D
// add
@SP
AM=M-1
D=M
A=A-1
D=D+M
M=D
