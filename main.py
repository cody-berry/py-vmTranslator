from CodeWriter import CodeWriter
from Parser import Parser


parser = Parser('StackArithmetic/SimpleAdd/SimpleAdd.vm')
code_writer = CodeWriter('StackArithmetic/SimpleAdd/SimpleAdd.asm')


for code in parser.file:
    if parser.hasMoreLines():
        command = parser.advance()
        print(command)
        if len(command) == 1:
            code_writer.writeArithmetic(command[0])
        if len(command) == 3:
            code_writer.writePushPop(command[0], command[1], command[2])

        print('----------------')




