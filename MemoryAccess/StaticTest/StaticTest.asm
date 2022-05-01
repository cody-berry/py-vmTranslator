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
// pop static 8
@SP
AM=M-1
D=M
@static.8
M=D
// pop static 3
@SP
AM=M-1
D=M
@static.3
M=D
// pop static 1
@SP
AM=M-1
D=M
@static.1
M=D
// push static 3
@static.3
D=M
@SP
M=M+1
A=M-1
M=D
// push static 1
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
D=M-D
M=D
// push static 8
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
