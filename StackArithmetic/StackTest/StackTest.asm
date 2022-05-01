// push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
// eq
@SP
AM=M-1
D=M
A=A-1
D=D-M
@TRUE1
D;JEQ
@SP
A=M-1
M=0
@STOP1
D;JMP
(TRUE1)
@SP
A=M-1
M=-1
(STOP1)
// push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// eq
@SP
AM=M-1
D=M
A=A-1
D=D-M
@TRUE2
D;JEQ
@SP
A=M-1
M=0
@STOP2
D;JMP
(TRUE2)
@SP
A=M-1
M=-1
(STOP2)
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
// eq
@SP
AM=M-1
D=M
A=A-1
D=D-M
@TRUE3
D;JEQ
@SP
A=M-1
M=0
@STOP3
D;JMP
(TRUE3)
@SP
A=M-1
M=-1
(STOP3)
// push constant 892
@892
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 891
@891
D=A
@SP
M=M+1
A=M-1
M=D
// lt
@SP
AM=M-1
D=M
A=A-1
D=D-M
@TRUE4
D;JLT
@SP
A=M-1
M=0
@STOP4
D;JMP
(TRUE4)
@SP
A=M-1
M=-1
(STOP4)
// push constant 891
@891
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 892
@892
D=A
@SP
M=M+1
A=M-1
M=D
// lt
@SP
AM=M-1
D=M
A=A-1
D=D-M
@TRUE5
D;JLT
@SP
A=M-1
M=0
@STOP5
D;JMP
(TRUE5)
@SP
A=M-1
M=-1
(STOP5)
// push constant 891
@891
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 891
@891
D=A
@SP
M=M+1
A=M-1
M=D
// lt
@SP
AM=M-1
D=M
A=A-1
D=D-M
@TRUE6
D;JLT
@SP
A=M-1
M=0
@STOP6
D;JMP
(TRUE6)
@SP
A=M-1
M=-1
(STOP6)
// push constant 32767
@32767
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D
// gt
@SP
AM=M-1
D=M
A=A-1
D=D-M
@TRUE7
D;JGT
@SP
A=M-1
M=0
@STOP7
D;JMP
(TRUE7)
@SP
A=M-1
M=-1
(STOP7)
// push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 32767
@32767
D=A
@SP
M=M+1
A=M-1
M=D
// gt
@SP
AM=M-1
D=M
A=A-1
D=D-M
@TRUE8
D;JGT
@SP
A=M-1
M=0
@STOP8
D;JMP
(TRUE8)
@SP
A=M-1
M=-1
(STOP8)
// push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D
// gt
@SP
AM=M-1
D=M
A=A-1
D=D-M
@TRUE9
D;JGT
@SP
A=M-1
M=0
@STOP9
D;JMP
(TRUE9)
@SP
A=M-1
M=-1
(STOP9)
// push constant 57
@57
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 53
@53
D=A
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
// push constant 112
@112
D=A
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
// neg 
@SP
A=M-1
M=-M
// and
@SP
AM=M-1
D=M
A=A-1
D=D&M
M=D
// push constant 82
@82
D=A
@SP
M=M+1
A=M-1
M=D
// or 
@SP
AM=M-1
D=M
A=A-1
D=D|M
M=D
// not 
@SP
A=M-1
M=!M
