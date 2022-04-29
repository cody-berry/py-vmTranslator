from CodeWriter import CodeWriter
from Parser import Parser


parser = Parser('StackArithmetic/StackTest/StackTest.vm')
code_writer = CodeWriter('StackArithmetic/StackTest/StackTest.asm')


for code in parser.file:
    if parser.hasMoreLines():
        command = parser.advance()
        print(command)
        if len(command) == 1:
            code_writer.writeArithmetic(command[0])

        print('----------------')




